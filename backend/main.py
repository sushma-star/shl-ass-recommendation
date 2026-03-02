from fastapi import FastAPI
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from backend.rag_engine import RAGEngine

app = FastAPI()

rag = None

@app.on_event("startup")
def load_rag():
    global rag
    from rag_engine import RAGEngine
    rag = RAGEngine()

@app.get("/")
def home():
    return {"message": "API Running"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/recommend")
def recommend(q: str):
    results = rag.search(q)
    return {"Query": q, "recommendations": results}


