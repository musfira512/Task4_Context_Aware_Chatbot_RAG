import os
import fitz  # PyMuPDF
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
import numpy as np
import requests

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def load_pdf(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    return " ".join([page.get_text() for page in doc])

def chunk_text(text, chunk_size=500):
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

def embed_chunks(chunks):
    model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = model.encode(chunks)
    return embeddings, model

def query_vector_db(query, vector_db, chunks, embedder):
    query_vec = embedder.encode([query])
    scores = cosine_similarity(query_vec, vector_db)[0]
    top_k = np.argsort(scores)[-3:][::-1]
    context = "\n".join([chunks[i] for i in top_k])
    return call_groq_llm(query, context)

def call_groq_llm(query, context):
    if not GROQ_API_KEY:
        return "[❌ ERROR] GROQ_API_KEY not set in environment or .env file."

    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "gemma2-9b-it",
        "messages": [
            {"role": "system", "content": "Answer based only on the provided context."},
            {"role": "user", "content": f"Context: {context}\n\nQuestion: {query}"}
        ],
        "temperature": 0.2
    }

    try:
        r = requests.post(url, headers=headers, json=payload)
        r.raise_for_status()
        return r.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"[❌ HTTP Error] {e}"
