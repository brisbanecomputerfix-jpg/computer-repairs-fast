"""
Update Australian Business Number (ABN) across Computer Repairs Fast.
Target ABN: ABN 98 288 669 674
"""

import os
import re

ROOT_DIR = r"C:\Users\PC\.gemini\antigravity-ide\scratch\computer-repairs-fast"
NEW_ABN = "ABN 98 288 669 674"
NEW_ABN_COLON = "ABN: 98 288 669 674"
OLD_ABN = "53 624 812 790"

# 1. Update scripts/build_articles_hub.py
hub_py = os.path.join(ROOT_DIR, "scripts", "build_articles_hub.py")
with open(hub_py, "r", encoding="utf-8") as f:
    hub_content = f.read()
if OLD_ABN in hub_content:
    hub_content = hub_content.replace(f"ABN: {OLD_ABN}", NEW_ABN_COLON)
    hub_content = hub_content.replace(OLD_ABN, "98 288 669 674")
    with open(hub_py, "w", encoding="utf-8") as f:
        f.write(hub_content)
    print("Updated scripts/build_articles_hub.py")

# 2. Update scripts/build_all_pages.py
all_pages_py = os.path.join(ROOT_DIR, "scripts", "build_all_pages.py")
with open(all_pages_py, "r", encoding="utf-8") as f:
    content = f.read()
content = content.replace("ABN Registered.", f"{NEW_ABN_COLON}.")
content = content.replace(f"ABN: {OLD_ABN}", NEW_ABN_COLON)
with open(all_pages_py, "w", encoding="utf-8") as f:
    f.write(content)
print("Updated scripts/build_all_pages.py")

# 3. Update root HTML files (index, terms, privacy, contact, faq, 404, what-is-the-most-expensive...)
root_htmls = [
    "index.html",
    "terms.html",
    "privacy.html",
    "contact.html",
    "faq.html",
    "404.html",
    "what-is-the-most-expensive-thing-to-repair-on-a-laptop.html"
]

for fn in root_htmls:
    p = os.path.join(ROOT_DIR, fn)
    if not os.path.exists(p):
        continue
    with open(p, "r", encoding="utf-8") as f:
        html = f.read()
    
    # Replace old ABN if present
    if OLD_ABN in html:
        html = html.replace(f"ABN: {OLD_ABN}", NEW_ABN_COLON)
        html = html.replace(OLD_ABN, "98 288 669 674")
    
    # Replace ABN Registered. or update footer bottom
    if "ABN Registered." in html:
        html = html.replace("ABN Registered.", f"{NEW_ABN_COLON}.")
    
    # Check footer copyright line
    old_cr = "© 2026 Computer Repairs Fast (computerrepairsfast.com.au). All Rights Reserved."
    if old_cr in html and NEW_ABN_COLON not in html:
        html = html.replace(old_cr, f"{old_cr} {NEW_ABN_COLON}.")
    
    # Special file updates
    if fn == "terms.html":
        # Ensure Section 6 has ABN
        if "<strong>Computer Repairs Fast</strong><br>" in html and NEW_ABN_COLON not in html:
            html = html.replace(
                "<strong>Computer Repairs Fast</strong><br>",
                f"<strong>Computer Repairs Fast</strong><br>\n          {NEW_ABN_COLON}<br>"
            )
    elif fn == "privacy.html":
        if "<strong>Computer Repairs Fast</strong><br>" in html and NEW_ABN_COLON not in html:
            html = html.replace(
                "<strong>Computer Repairs Fast</strong><br>",
                f"<strong>Computer Repairs Fast</strong><br>\n          {NEW_ABN_COLON}<br>"
            )
    elif fn == "index.html":
        # Add taxID to schema if not present
        if '"@type": "EmergencyService"' in html and '"taxID"' not in html:
            html = html.replace(
                '"telephone": "0401148654",',
                f'"telephone": "0401148654",\n      "taxID": "98 288 669 674",'
            )

    with open(p, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Updated {fn}")

# 4. Update services/insurance-damage-reports-brisbane.html
ins_p = os.path.join(ROOT_DIR, "services", "insurance-damage-reports-brisbane.html")
if os.path.exists(ins_p):
    with open(ins_p, "r", encoding="utf-8") as f:
        ins_html = f.read()
    ins_html = ins_html.replace(
        "registered Australian Business Number (ABN),",
        f"registered Australian Business Number ({NEW_ABN_COLON}),"
    )
    ins_html = ins_html.replace("ABN Registered.", f"{NEW_ABN_COLON}.")
    with open(ins_p, "w", encoding="utf-8") as f:
        f.write(ins_html)
    print("Updated services/insurance-damage-reports-brisbane.html")

print("All source and template files updated with ABN: 98 288 669 674.")
