import pandas as pd
import json

df = pd.read_excel("Gen_AI Dataset.xlsx")

data = []

for _, row in df.iterrows():
    data.append({
        "name": row["Query"],
        "url": row["Assessment_url"]
    })

with open("backend/data/products.json", "w") as f:
    json.dump(data, f, indent=2)

print(" JSON created successfully!")