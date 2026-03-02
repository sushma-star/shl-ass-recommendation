import sys
import os
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from backend.rag_engine import RAGEngine

rag = RAGEngine()
excel_path = os.path.join(os.path.dirname(__file__), "..", "Gen_AI Dataset.xlsx")

df = pd.read_excel(excel_path)


recalls = []

for _, row in df.iterrows():
    query = row["Query"]  
    true_urls = [row["Assessment_url"]]  

    results = rag.search(query, top_k=65)
    predicted_urls = [r.get("url", "") for r in results]

    match = len(set(predicted_urls) & set(true_urls))
    recall = match / len(true_urls) if len(true_urls) > 0 else 0

    recalls.append(recall)

mean_recall = sum(recalls) / len(recalls)
print(" Mean Recall@10:", mean_recall)