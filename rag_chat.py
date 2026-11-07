"""
Minimal RAG FAQ chatbot — pgvector + Ollama (open-source, fully local).

Pipeline:

  INGESTION (at startup):
    docs/*.md -> split into chunks -> embed each chunk -> pgvector table

  QUERY (per question):
    question -> embed -> pgvector similarity search -> top 3 chunks
             -> prompt = question + chunks + chat history -> Llama 3.2 -> answer

Run everything with Docker (see README):
    docker compose up -d db ollama
    docker compose run --rm app
"""

import os
from pathlib import Path

import psycopg
import requests
from pgvector.psycopg import register_vector
from sentence_transformers import SentenceTransformer

DOCS_DIR = Path(__file__).parent / "docs"
TOP_K = 3  # how many chunks to retrieve per question

# These default to the docker-compose service names; override via env for
# local (non-Docker) runs.
DATABASE_URL = os.environ.get(
    "DATABASE_URL", "postgresql://rag:rag@db:5432/rag"
)
OLLAMA_URL = os.environ.get("OLLAMA_URL", "http://ollama:11434")
OLLAMA_MODEL = os.environ.get("OLLAMA_MODEL", "llama3.2:3b")


# ---------------------------------------------------------------------------
# Embedding model — turns text into a vector of 384 numbers that captures
# its *meaning*. Similar meaning => nearby vectors. Runs locally, no API.
# ---------------------------------------------------------------------------
print("Loading embedding model (first run downloads ~90MB)...")
embedder = SentenceTransformer("all-MiniLM-L6-v2")
EMBED_DIM = 384  # output size of all-MiniLM-L6-v2


# ---------------------------------------------------------------------------
# Step 1: Chunking — split each doc into sections small enough to retrieve.
# We split on "## " headers so each chunk is one FAQ topic. In a real system
# you'd also cap chunk size (e.g. ~500 tokens) and maybe overlap chunks.
# ---------------------------------------------------------------------------
def load_chunks() -> list[dict]:
    chunks = []
    for doc in sorted(DOCS_DIR.glob("*.md")):
        text = doc.read_text()
        for section in text.split("\n## "):
            section = section.strip()
            if section:
                chunks.append({"source": doc.name, "text": section})
    return chunks


# ---------------------------------------------------------------------------
# Step 2: Ingestion — store chunks + their embeddings in Postgres/pgvector.
# The `vector(384)` column type and the `<=>` distance operator come from the
# pgvector extension. Docs are tiny, so we just re-ingest on every startup.
# ---------------------------------------------------------------------------
def ingest(conn: psycopg.Connection) -> int:
    # CREATE EXTENSION must happen before register_vector — the vector type
    # doesn't exist in a fresh database until the extension is installed.
    conn.execute("CREATE EXTENSION IF NOT EXISTS vector")
    conn.commit()
    register_vector(conn)
    conn.execute("DROP TABLE IF EXISTS chunks")
    conn.execute(
        f"""CREATE TABLE chunks (
                id serial PRIMARY KEY,
                source text NOT NULL,
                text text NOT NULL,
                embedding vector({EMBED_DIM}) NOT NULL
            )"""
    )
    chunks = load_chunks()
    vectors = embedder.encode([c["text"] for c in chunks], normalize_embeddings=True)
    with conn.cursor() as cur:
        for chunk, vec in zip(chunks, vectors):
            cur.execute(
                "INSERT INTO chunks (source, text, embedding) VALUES (%s, %s, %s)",
                (chunk["source"], chunk["text"], vec),
            )
    conn.commit()
    return len(chunks)


# ---------------------------------------------------------------------------
# Step 3: Retrieval — embed the question and let pgvector find the closest
# chunks. `<=>` is cosine distance (0 = identical meaning), so we convert to
# similarity (1 - distance) for readability.
# ---------------------------------------------------------------------------
def retrieve(conn: psycopg.Connection, question: str, k: int = TOP_K) -> list[dict]:
    q_vector = embedder.encode([question], normalize_embeddings=True)[0]
    rows = conn.execute(
        """SELECT source, text, 1 - (embedding <=> %s) AS score
           FROM chunks ORDER BY embedding <=> %s LIMIT %s""",
        (q_vector, q_vector, k),
    ).fetchall()
    return [{"source": r[0], "text": r[1], "score": r[2]} for r in rows]


# ---------------------------------------------------------------------------
# Step 4: Generation — give the LLM the question plus the retrieved chunks,
# and instruct it to answer ONLY from them (this is what "grounded" means —
# it prevents the model from making things up).
#
# The LLM is Llama 3.2 3B served by Ollama: open-source, free, runs locally.
# Ollama exposes a simple HTTP API, so no SDK is needed.
# ---------------------------------------------------------------------------
SYSTEM_PROMPT = """You are a support assistant. Answer the user's question
using ONLY the documentation excerpts provided in each message.
If the answer is not in the excerpts, say "I don't have information about
that" and suggest contacting support@example.com. Be concise."""


def ensure_model():
    """Pull the model into Ollama if it isn't there yet (first run only)."""
    tags = requests.get(f"{OLLAMA_URL}/api/tags", timeout=10).json()
    if not any(m["name"] == OLLAMA_MODEL for m in tags.get("models", [])):
        print(f"Pulling {OLLAMA_MODEL} into Ollama (one-time, ~2GB)...")
        requests.post(
            f"{OLLAMA_URL}/api/pull", json={"model": OLLAMA_MODEL}, timeout=1800
        ).raise_for_status()


def answer(
    conn: psycopg.Connection,
    question: str,
    history: list[dict],
    retrieved: list[dict] | None = None,
) -> str:
    if retrieved is None:
        retrieved = retrieve(conn, question)

    # Show what was retrieved — watching this teaches you more about RAG
    # than anything else. Bad answers are almost always retrieval problems.
    print("\n  [retrieved chunks]")
    for r in retrieved:
        preview = r["text"][:60].replace("\n", " ")
        print(f"    {r['score']:.2f}  {r['source']}: {preview}...")

    context = "\n\n---\n\n".join(
        f"[from {r['source']}]\n{r['text']}" for r in retrieved
    )
    user_message = f"Documentation excerpts:\n\n{context}\n\nQuestion: {question}"

    # history gives the bot memory, so follow-ups like "and on the Team
    # plan?" make sense. We keep the last 6 turns to bound prompt size.
    response = requests.post(
        f"{OLLAMA_URL}/api/chat",
        json={
            "model": OLLAMA_MODEL,
            "stream": False,
            "messages": [{"role": "system", "content": SYSTEM_PROMPT}]
            + history[-6:]
            + [{"role": "user", "content": user_message}],
        },
        timeout=300,
    )
    response.raise_for_status()
    return response.json()["message"]["content"]


# ---------------------------------------------------------------------------
# Chat loop with conversation memory.
# ---------------------------------------------------------------------------
def main():
    conn = psycopg.connect(DATABASE_URL)
    n = ingest(conn)
    print(f"Indexed {n} chunks into pgvector")
    ensure_model()

    history: list[dict] = []
    print("\nRAG FAQ bot ready. Ask about billing, accounts, or the product.")
    print("Type 'quit' to exit.\n")
    while True:
        try:
            question = input("you> ").strip()
        except EOFError:
            break
        if not question or question.lower() in ("quit", "exit"):
            break
        reply = answer(conn, question, history)
        print(f"\nbot> {reply}\n")
        # Store the plain question (not the big prompt with chunks) so
        # history stays small.
        history.append({"role": "user", "content": question})
        history.append({"role": "assistant", "content": reply})


if __name__ == "__main__":
    main()
