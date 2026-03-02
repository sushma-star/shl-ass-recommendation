import requests
from bs4 import BeautifulSoup
import json

BASE_URL = "https://www.shl.com"
URL = "https://www.shl.com/solutions/products/product-catalog/"

def scrape():
    res = requests.get(URL)
    soup = BeautifulSoup(res.text, "html.parser")

    data = []

    for a in soup.find_all("a", href=True):
        href = a["href"]

        if "/products/product-catalog/view/" in href:
            name = a.text.strip()

            if name:
                data.append({
                    "name": name,
                    "url": BASE_URL + href
                })

 
    print("Total:", len(data))

    with open("data/products.json", "w") as f:
        json.dump(data, f, indent=2)

if __name__ == "__main__":
    scrape()
    