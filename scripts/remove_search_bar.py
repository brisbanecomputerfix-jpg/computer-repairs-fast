"""
Completely remove search bar from Computer Repairs Fast website:
- Removes sub-bar search HTML from templates and all HTML files
- Removes search engine IIFE from js/main.js
- Removes search sub-bar styles from css/style.css
- Updates articles hub quick hint
"""

import os
import re

ROOT_DIR = r"C:\Users\PC\.gemini\antigravity-ide\scratch\computer-repairs-fast"

# 1. Update scripts/build_all_pages.py
bap_path = os.path.join(ROOT_DIR, "scripts", "build_all_pages.py")
with open(bap_path, "r", encoding="utf-8") as f:
    bap_text = f.read()

# Pattern matching the subbar search strip in build_all_pages.py
subbar_pattern = re.compile(r'<!-- Sub-Bar Search Strip[\s\S]*?</div>\s*</div>\s*</div>\s*\n', re.MULTILINE)
bap_text_clean = subbar_pattern.sub('', bap_text)
with open(bap_path, "w", encoding="utf-8") as f:
    f.write(bap_text_clean)
print("Updated scripts/build_all_pages.py (removed search templates)")

# 2. Update scripts/build_articles_hub.py
hub_path = os.path.join(ROOT_DIR, "scripts", "build_articles_hub.py")
with open(hub_path, "r", encoding="utf-8") as f:
    hub_text = f.read()

hub_text_clean = subbar_pattern.sub('', hub_text)
# Update quick hint text
hub_text_clean = hub_text_clean.replace(
    "💡 Tip: Search by topic, brand (MacBook, HP, Lenovo) or use the search bar above",
    "💡 Tip: Filter by category above (Apple MacBooks, Hardware, Cyber Scams, WFH) or browse our guides below"
)
with open(hub_path, "w", encoding="utf-8") as f:
    f.write(hub_text_clean)
print("Updated scripts/build_articles_hub.py (removed search bar and updated hint)")

# 3. Clean root HTML files
root_htmls = [
    "index.html",
    "contact.html",
    "faq.html",
    "terms.html",
    "privacy.html",
    "404.html",
    "what-is-the-most-expensive-thing-to-repair-on-a-laptop.html"
]

for fn in root_htmls:
    p = os.path.join(ROOT_DIR, fn)
    if os.path.exists(p):
        with open(p, "r", encoding="utf-8") as f:
            html = f.read()
        cleaned = subbar_pattern.sub('', html)
        with open(p, "w", encoding="utf-8") as f:
            f.write(cleaned)
        print(f"Removed search bar from {fn}")

# 4. Clean css/style.css
css_path = os.path.join(ROOT_DIR, "css", "style.css")
with open(css_path, "r", encoding="utf-8") as f:
    css_text = f.read()

# Match from /* Simple & Sleek Search Sub-Bar down to the end of media query
css_search_pattern = re.compile(
    r'/\*\s*={10,}\s*Simple & Sleek Search Sub-Bar[\s\S]*?@media\s*\(max-width:\s*768px\)\s*\{[\s\S]*?\}\s*\}',
    re.MULTILINE
)
css_cleaned = css_search_pattern.sub('/* Search sub-bar removed */', css_text)
with open(css_path, "w", encoding="utf-8") as f:
    f.write(css_cleaned)
print("Removed search bar styles from css/style.css")

# 5. Clean js/main.js
js_path = os.path.join(ROOT_DIR, "js", "main.js")
with open(js_path, "r", encoding="utf-8") as f:
    js_text = f.read()

# Remove the standalone search IIFE starting with "Simple, Instant Local Search Engine"
js_search_pattern = re.compile(
    r'/\*\*\s*\*\s*Simple, Instant Local Search Engine[\s\S]*?\}\)\(\);?\s*$',
    re.MULTILINE
)
js_cleaned = js_search_pattern.sub('// Search bar removed', js_text)
with open(js_path, "w", encoding="utf-8") as f:
    f.write(js_cleaned)
print("Removed search engine script from js/main.js")

print("All search bar components cleanly excised!")
