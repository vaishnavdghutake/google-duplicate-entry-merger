import pandas as pd
from difflib import SequenceMatcher

#csv read
df = pd.read_csv("/Users/msan/product-merger/products.csv")
df.columns = df.columns.str.strip().str.lower()

#refine text
def clean_text(text):
    text = str(text).lower()
    text = text.replace("(", "").replace(")", "")
    text = text.replace(",", "").replace("-", " ")
    text = " ".join(text.split())
    return text

df["clean_product"] = df["product name"].apply(clean_text)

#similar
def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

#grouping
groups = []
visited = set()

for i, row1 in df.iterrows():
    if i in visited:
        continue

    group = [i]
    for j, row2 in df.iterrows():
        if i != j and similar(row1["clean_product"], row2["clean_product"]) > 0.70:
            group.append(j)
            visited.add(j)
    visited.add(i)
    groups.append(group)

#merge results
merged = []
for group in groups:
    items = df.loc[group]
    items_sorted = items.sort_values("price")

    sellers = [{"Store": s, "Price": p} for s, p in zip(items_sorted["store"], items_sorted["price"])]
    min_price = items_sorted["price"].min()
    merged.append({
        "Product Name": items.iloc[0]["product name"],  # representative name
        "Price": min_price,
        "Store": sellers
    })

#display
for product in merged:
    print("=" * 75)
    print(product["Product Name"])
    print(f"Lowest Price: {product['Price']}")
    print("Available at:")
    for s in product["Store"]:
        if s["Price"] == product["Price"]:
            print(f"  - {s['Store']} : {s['Price']} <-- Lowest Price")
        else:
            print(f"  - {s['Store']} : {s['Price']}")

