from serpapi import GoogleSearch
import csv
import os
import requests
from PIL import Image
from io import BytesIO
import subprocess
import sys


API_KEY = "779d5f70e51650ff9b630f0650ba1e6b4068e54a2ae4daa10b9a30327b6d39ee"

def fetch_google_shopping_data(query):
    search = GoogleSearch({
        "q": query,
        "tbm": "shop",
        "hl": "en",
        "gl": "in",
        "api_key": API_KEY
    })
    results = search.get_dict()
    products = results.get("shopping_results", [])
    return products


def save_to_csv(products, filename="products.csv"):
    save_path = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(save_path, filename)

    with open(full_path, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Product Name", "Price", "Store", "Image URL"])
        for product in products:
            name = product.get("title")
            price = product.get("price")
            store = product.get("source")
            image_url = product.get("thumbnail")
            writer.writerow([name, price, store, image_url])

    print(f"✅ Saved {len(products)} products to {full_path}")
    return full_path


def download_image(url, path):
    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        img = Image.open(BytesIO(response.content))
        img.save(path)
        return True
    except Exception:
        return False  


if __name__ == "__main__":
    query = input("Enter the product name: ")
    print("You searched for:", query)

    
    products = fetch_google_shopping_data(query)

    
    img_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images")
    os.makedirs(img_dir, exist_ok=True)

    
    for i, product in enumerate(products):
        url = product.get("thumbnail")
        if url:
            img_path = os.path.join(img_dir, f"{i}.jpg")
            download_image(url, img_path)

    
    save_to_csv(products)

    
    merge_script = os.path.join(os.path.dirname(os.path.abspath(__file__)), "merge_products.py")
    subprocess.run([sys.executable, merge_script])  
