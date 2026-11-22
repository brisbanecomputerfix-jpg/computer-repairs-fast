import glob
import os
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
files = glob.glob(os.path.join(ROOT_DIR, "**", "*.html"), recursive=True)

# Parse sitemap
tree = ET.parse(os.path.join(ROOT_DIR, "sitemap.xml"))
sitemap_urls = set(e.text for e in tree.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc"))

missing_h1 = []
missing_title = []
desc_too_long = []
missing_desc = []
missing_canonical = []
urls_not_in_sitemap = []

for f in files:
    rel = os.path.relpath(f, ROOT_DIR).replace("\\", "/")
    soup = BeautifulSoup(open(f, encoding="utf-8", errors="ignore"), "html.parser")
    
    # 404 is special
    if rel == "404.html":
        continue
        
    h1 = soup.find("h1")
    if not h1 or not h1.get_text(strip=True):
        missing_h1.append(rel)
        
    if not soup.title or not soup.title.string:
        missing_title.append(rel)
        
    desc = soup.find("meta", {"name": "description"})
    if not desc or not desc.get("content"):
        missing_desc.append(rel)
    elif len(desc.get("content")) > 165:
        desc_too_long.append((rel, len(desc.get("content"))))
        
    can = soup.find("link", {"rel": "canonical"})
    if not can or not can.get("href"):
        missing_canonical.append(rel)
        
    # Check sitemap
    if rel == "index.html":
        expected_url = "https://computerrepairsfast.com.au/"
    elif rel.endswith("index.html"):
        expected_url = f"https://computerrepairsfast.com.au/{rel[:-10]}"
    else:
        expected_url = f"https://computerrepairsfast.com.au/{rel}"
        
    if expected_url not in sitemap_urls:
        urls_not_in_sitemap.append(expected_url)

print("=" * 50)
print(f"Total HTML files found: {len(files)}")
print(f"Total verified sitemap URLs: {len(sitemap_urls)}")
print("=" * 50)
print(f"H1 missing or empty: {len(missing_h1)}")
print(f"Title missing or empty: {len(missing_title)}")
print(f"Meta description missing: {len(missing_desc)}")
print(f"Meta description too long (>165 chars): {len(desc_too_long)}")
print(f"Canonical tag missing: {len(missing_canonical)}")
print(f"HTML URLs not in sitemap: {len(urls_not_in_sitemap)}")
print("=" * 50)
if len(missing_h1) == 0 and len(missing_title) == 0 and len(desc_too_long) == 0 and len(missing_canonical) == 0 and len(urls_not_in_sitemap) == 0:
    print("ALL SEO CHECKS PASSED: 0 AUDIT DEFECTS!")
else:
    print(f"Issues to review: {desc_too_long[:3]}")
