import json
import faiss
import os
import numpy as np
from sentence_transformers import SentenceTransformer


class RAGEngine:
    def __init__(self):
        print("Loading model...")

        self.model = SentenceTransformer('all-MiniLM-L6-v2')

        print("Loading data...")
        data_path = os.path.join(os.path.dirname(__file__), "..", "data", "products.json")


        with open(data_path, "r") as f:
            self.products = json.load(f)

        
        self.texts = [
            p["name"]  for p in self.products
        ]

        print("Creating embeddings...")

        self.embeddings = self.model.encode(self.texts)

        dim = len(self.embeddings[0])

        print("Building FAISS index...")

        self.index = faiss.IndexFlatL2(dim)
        self.index.add(np.array(self.embeddings))

        print("RAG Ready!")

    def search(self, query, top_k=5):
        q_emb = self.model.encode([query])
        D, I = self.index.search(np.array(q_emb), top_k)

        return [self.products[i] for i in I[0]]