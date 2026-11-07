# RAG FAQ Chatbot

A minimal Retrieval-Augmented Generation (RAG) chatbot that answers questions
from a folder of markdown FAQ docs. Fully open-source and fully local: pgvector
for retrieval, Llama 3.2 via Ollama for generation, React for the UI — no API
keys, no cloud. Built as a learning project for AI system design; every step
of the pipeline is visible and commented.

## How it works

```
INGESTION (at startup)
  docs/*.md -> split into chunks -> embed each chunk -> pgvector table

QUERY (per question)
  question -> embed -> pgvector similarity search -> top 3 chunks
           -> prompt = question + chunks + chat history -> Llama 3.2 -> answer
```

| Component | Choice | Notes |
|-----------|--------|-------|
| Embeddings | `all-MiniLM-L6-v2` (sentence-transformers) | Free, runs locally, 384-dim vectors |
| Vector store | Postgres + pgvector | Real similarity search with the `<=>` operator |
| LLM | Llama 3.2 3B via Ollama | Open-source, runs on CPU in Docker |
| API | FastAPI (`api.py`) | `POST /api/chat`, serves the UI at `/` |
| UI | React (single file, via CDN) | Chat interface, shows retrieved chunks + scores |
| Memory | Conversation history sent with each request | So follow-up questions work |
| Grounding | System prompt restricts answers to retrieved excerpts | Prevents hallucination |

## Run it

```bash
docker compose up --build
```

First run downloads the Llama 3.2 3B model (~2GB) into the Ollama container;
it persists in a volume, so later runs are fast.

Then open **http://localhost:8080**

There's also a terminal version of the same pipeline:

```bash
docker compose run --rm app python rag_chat.py
```

## Files

- `rag_chat.py` — the whole RAG pipeline (chunk, embed, ingest, retrieve, generate) + CLI chat loop
- `api.py` — FastAPI wrapper exposing `POST /api/chat` and serving the UI
- `static/index.html` — React chat UI (no build step — React via CDN)
- `docs/` — the knowledge base (three sample FAQ files; add your own)
- `docker-compose.yml` — three services: `db` (pgvector), `ollama`, `app`

## Example

```
you> I want my money back

  [retrieved chunks]
    0.42  billing.md: Refunds — Refunds are available within 30 days...
    0.38  billing.md: Late payments — If payment fails, we retry...

bot> To request a refund, email billing@example.com with your account
     email and invoice number.
```

Note: the question says "money back" and the doc says "refunds" — no shared
keywords. That's semantic (embedding-based) retrieval doing its job.

## What to try

- Ask a question the docs don't answer — the bot should say it doesn't know
  (grounding) instead of making something up
- Ask a follow-up like "and on the Team plan?" — conversation memory in action
- Watch the retrieved chunks and scores shown under each answer: bad answers
  are almost always retrieval problems, not LLM problems
- Add your own `.md` files to `docs/` and restart the app
- Swap the model: set `OLLAMA_MODEL: mistral:7b` in `docker-compose.yml`
  (bigger = better answers, slower on CPU)

## Known limitations (by design — it's a demo)

- Docs are re-ingested on every startup (fine for 15 chunks, not for 15,000)
- A 3B model sometimes answers follow-ups too conservatively; `llama3.1:8b`
  or `mistral:7b` noticeably improve grounded reasoning
- No streaming, auth, rate limiting, or eval harness
