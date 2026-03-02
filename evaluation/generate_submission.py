# import pandas as pd
# import os 
# import sys
# import csv
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


# from backend.rag_engine import RAGEngine

# rag = RAGEngine()
# excel_path = os.path.join(os.path.dirname(__file__), "..", "Gen_AI Dataset.xlsx")

# # Load the Excel file
# df = pd.read_excel(excel_path, sheet_name=1)

# # df = pd.read_excel("Gen_AI Dataset.xlsx", sheet_name=1)

# with open("sushma_akula.csv", "w", newline="") as f:
#     writer = csv.writer(f)
#     writer.writerow(["Query", "Assessment_url"])

#     for _, row in df.iterrows():
#         query = row["Query"]

#         results = rag.search(query, top_k=65)

#         for r in results:
#             writer.writerow([query, r["url"]])
            
# print("✅ CSV Generated!")
import pandas as pd
import os
import sys
import csv

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from backend.rag_engine import RAGEngine

rag = RAGEngine()
excel_path = os.path.join(os.path.dirname(__file__), "..", "Gen_AI Dataset.xlsx")

# Load the Excel file
df = pd.read_excel(excel_path, sheet_name=1)

with open("sushma_akula.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Query", "Assessment_url"])

    for _, row in df.iterrows():
        query = row["Query"]

        results = rag.search(query, top_k=10)

        for r in results:
            writer.writerow([query, r.get("url", "")])  

print(" CSV Generated!")