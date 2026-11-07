"""
FastAPI backend for the RAG FAQ chatbot.

Wraps the pipeline from rag_chat.py in an HTTP API and serves the React UI:

  GET  /            -> the chat UI (static/index.html)
  POST /api/chat    -> {"question": "...", "history": [...]}
                       returns {"answer": "...", "chunks": [...]}

Run via Docker: docker compose up --build
Then open http://localhost:8000
"""

from contextlib import asynccontextmanager

import psycopg
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

import rag_chat

state = {}


@asynccontextmanager
async def lifespan(app: FastAPI):
    conn = psycopg.connect(rag_chat.DATABASE_URL)
    n = rag_chat.ingest(conn)
    print(f"Indexed {n} chunks into pgvector")
    rag_chat.ensure_model()
    state["conn"] = conn
    yield
    conn.close()


app = FastAPI(lifespan=lifespan)


class ChatMessage(BaseModel):
    role: str  # "user" or "assistant"
    content: str


class ChatRequest(BaseModel):
    question: str
    history: list[ChatMessage] = []


@app.post("/api/chat")
def chat(req: ChatRequest):
    conn = state["conn"]
    # Return the retrieved chunks too, so the UI can show *why* the bot
    # answered the way it did — great for demos and debugging retrieval.
    chunks = rag_chat.retrieve(conn, req.question)
    history = [m.model_dump() for m in req.history]
    reply = rag_chat.answer(conn, req.question, history, retrieved=chunks)
    return {
        "answer": reply,
        "chunks": [
            {"source": c["source"], "score": round(c["score"], 2),
             "preview": c["text"][:100]}
            for c in chunks
        ],
    }


# Serve the React UI at / (must be mounted last so /api routes win).
app.mount("/", StaticFiles(directory="static", html=True), name="static")
