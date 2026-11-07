FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Bake the embedding model into the image so the container works offline
# and doesn't re-download ~90MB on every run.
RUN python -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('all-MiniLM-L6-v2')"

COPY rag_chat.py api.py ./
COPY docs/ docs/
COPY static/ static/

EXPOSE 8000
# Web UI by default; run the CLI instead with:
#   docker compose run --rm app python rag_chat.py
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
