# Google Duplicate Entry Merger

A Python project that scrapes Google Shopping data, merges duplicate product listings based on text and price similarity, and optionally filters visually similar products using AI.

This project helps consolidate duplicate entries from multiple sellers into a clean, unified list — similar to Amazon or Flipkart product pages.

---

## **Features**

- Scrapes Google Shopping product listings using **SerpAPI**.
- Saves product details to **CSV** including name, price, store, and image URL.
- Merges duplicates based on **text similarity** and **lowest price**.
- Downloads product images for AI-based **visual similarity filtering**.
- Groups visually similar products using **CLIP embeddings** and **FAISS** for fast similarity search.
- Ready for further automation, reporting, or e-commerce analysis.

---

## **INSTALLATION**

1. Clone the repository:
```bash
git clone https://github.com/ProMSan2305/google-duplicate-entry-merger.git
cd google-duplicate-entry-merger
```
2. Create a Python virtual environment and activate it: python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

3. Install dependencies: pip install -r requirements.txt

## **USAGE**
Run the main script: python main.py
Enter the product name when prompted.
The script will:
1. Fetch product listings from Google Shopping.
2. Download images to images/ folder inside the project.
3. Save product info to products.csv.
4. Run merge_products.py to merge duplicates.

## **REPOSITORT STRUCTURE**
├── main.py               # Main script
├── merge_products.py     # Script to merge duplicate products
├── requirements.txt
├── products.csv          # Output CSV (generated after running)
├── images/               # Downloaded images (generated after running)
└── utils/                # Helper modules (if any)

## **HOW IT WORKS** 
1. User enters a search query.
2. main.py uses SerpAPI to fetch Google Shopping results.
3. Product info (name, price, store, image) is saved in CSV.
4. Product images are downloaded locally.
5. merge_products.py processes the CSV to merge duplicates and provide a unified listing.

## **ACKNOWLEDGEMENTS**
SerpAPI for Google Shopping access.
Pillow for image handling.


## **CODE**
![image alt](https://github.com/ProMSan2305/google-duplicate-entry-merger/blob/8a89d054d0cea315a3840abe4833609df73935a4/1code.png)
## **LISTING**
![image alt](https://github.com/ProMSan2305/google-duplicate-entry-merger/blob/8a89d054d0cea315a3840abe4833609df73935a4/2listing.png)
## **BACKEND**
![image alt](https://github.com/ProMSan2305/google-duplicate-entry-merger/blob/8a89d054d0cea315a3840abe4833609df73935a4/3backend.png)
## **.CSV**
![image alt](https://github.com/ProMSan2305/google-duplicate-entry-merger/blob/8a89d054d0cea315a3840abe4833609df73935a4/4csv.png)
## **IMAGES**
![image alt](https://github.com/ProMSan2305/google-duplicate-entry-merger/blob/8a89d054d0cea315a3840abe4833609df73935a4/5images.png)
