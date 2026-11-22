import os
import json
import re
import sys

BASE_DIR = r"C:\Users\PC\.gemini\antigravity-ide\scratch\computer-repairs-fast"
sys.path.append(os.path.join(BASE_DIR, "scripts"))

import data_services
import data_suburbs
import data_articles

records = []

# 1. Core Pages
core_pages = [
    {
        "title": "Fast Computer Repairs Brisbane — Mobile & Workshop",
        "url": "/",
        "category": "Core Page",
        "type": "core",
        "badge": "🏠 Home",
        "desc": "Same-day mobile computer and laptop repairs across Greater Brisbane. $80 diagnostic inside repair, zero call-out fees.",
        "keywords": "computer repairs brisbane mobile technician laptop pc mac workshop drop-off same day fast home visit onsite"
    },
    {
        "title": "Contact Computer Repairs Fast Brisbane (0401 148 654)",
        "url": "/contact.html",
        "category": "Core Page",
        "type": "core",
        "badge": "📞 Contact",
        "desc": "Book a mobile technician or workshop drop-off in East Brisbane, West End, or Toowong. Call 0401 148 654 or send SMS.",
        "keywords": "contact phone email phone call sms booking workshop address brisbane east brisbane west end toowong appointment"
    },
    {
        "title": "How It Works & 5-Step Quote Guide",
        "url": "/#how-it-works",
        "category": "Core Page",
        "type": "core",
        "badge": "📋 Quote Guide",
        "desc": "How to get a fixed computer repair quote in Brisbane. 5-point checklist, cost breakdown of parts vs labour, and timeframe.",
        "keywords": "how it works quote estimate process checklist what to provide cost breakdown timeframe pricing fixed fee"
    },
    {
        "title": "Frequently Asked Questions (49+ Verified Answers)",
        "url": "/faq.html",
        "category": "Core Page",
        "type": "faq",
        "badge": "❓ FAQ Hub",
        "desc": "Comprehensive answers to 49 common computer repair questions regarding costs, mobile visits, screens, hinges, and data privacy.",
        "keywords": "faq questions answers pricing help warranties payment terms senior discounts turnaround"
    },
    {
        "title": "Guides, Articles & Tech Knowledge Hub",
        "url": "/articles/",
        "category": "Core Page",
        "type": "guide",
        "badge": "📖 Knowledge Base",
        "desc": "In-depth DIY guides, laptop buying guides, scam warnings, data recovery tutorials, and hardware repair explanations.",
        "keywords": "articles guides blog knowledge base tutorials reviews advice student laptop wfh macbook"
    }
]
records.extend(core_pages)

# 2. Services (29)
for s in data_services.SERVICES:
    models_val = s.get('models', '')
    models_str = models_val if isinstance(models_val, str) else " ".join(models_val)
    issues_list = s.get('common_issues', [])
    if isinstance(issues_list, list):
        issues_str = " ".join([i.get('title', str(i)) if isinstance(i, dict) else str(i) for i in issues_list])
    else:
        issues_str = str(issues_list)
    
    # Enrich with common problem keywords
    synonyms = "screen display cracked replacement battery swelling charging power keyboard hinge broken liquid spill water coffee ssd speed slow upgrade scam virus cleanup data recovery"
    keywords = f"{s['slug']} {s.get('category', '')} {s.get('title', '')} {models_str} {issues_str} {synonyms} repair fix cost price brisbane mobile onsite workshop"
    
    records.append({
        "title": s['title'],
        "url": f"/services/{s['slug']}.html",
        "category": "Service",
        "type": "service",
        "badge": "⚡ Service",
        "desc": s.get('meta_desc', s.get('h1_sub', '')),
        "keywords": keywords.lower()
    })

# 3. Suburbs & Locations (36)
for sub in data_suburbs.SUBURBS:
    surrounding_val = sub.get('surrounding', '')
    surrounding_str = surrounding_val if isinstance(surrounding_val, str) else " ".join(surrounding_val)
    landmarks_val = sub.get('landmarks', '')
    landmarks_str = landmarks_val if isinstance(landmarks_val, str) else " ".join(landmarks_val)
    keywords = f"{sub['name']} {sub['postcode']} {sub.get('region', '')} {sub.get('hub', '')} {surrounding_str} {landmarks_str} mobile computer repair home visit technician local onsite"
    records.append({
        "title": f"Computer Repairs {sub['name']} ({sub['postcode']}) — Mobile & Workshop",
        "url": f"/locations/{sub['slug']}.html",
        "category": "Location",
        "type": "location",
        "badge": "📍 Suburb Hub",
        "desc": f"Fast same-day computer repairs in {sub['name']} QLD {sub['postcode']}. Mobile dispatch to your home with $0 call-out fee.",
        "keywords": keywords.lower()
    })

# 4. Articles (48)
for a in data_articles.ARTICLES:
    keywords = f"{a['slug']} {a.get('category', '')} {a.get('h1', '')} {a.get('title', '')} guide tips brisbane school student touch touchscreen macbook hinge scam cyber security wfh printer email"
    records.append({
        "title": a['title'],
        "url": f"/articles/{a['slug']}.html",
        "category": "Guide",
        "type": "guide",
        "badge": "📖 Guide",
        "desc": a.get('meta_desc', ''),
        "keywords": keywords.lower()
    })

# 5. FAQs from faq.html (49)
faq_path = os.path.join(BASE_DIR, "faq.html")
if os.path.exists(faq_path):
    with open(faq_path, "r", encoding="utf-8") as f:
        faq_html = f.read()
    
    card_pattern = re.compile(r'<div class="faq-card">\s*<button[^>]*>\s*<span>(.*?)</span>\s*<span class="faq-toggle-icon">.*?</span>\s*</button>\s*<div class="faq-a"[^>]*>\s*<p>(.*?)</p>', re.DOTALL)
    faq_matches = card_pattern.findall(faq_html)
    
    for q, ans in faq_matches:
        q_clean = re.sub(r'<[^>]+>', '', q).strip()
        ans_clean = re.sub(r'<[^>]+>', '', ans).strip()
        desc_snippet = ans_clean[:140] + ("..." if len(ans_clean) > 140 else "")
        records.append({
            "title": q_clean,
            "url": f"/faq.html",
            "category": "FAQ",
            "type": "faq",
            "badge": "❓ FAQ",
            "desc": desc_snippet,
            "keywords": f"faq {q_clean.lower()} questions answers"
        })

output_path = os.path.join(BASE_DIR, "search-index.json")
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(records, f, separators=(',', ':'), ensure_ascii=False)

print(f"Generated search-index.json with {len(records)} searchable items.")
print(f"File size: {os.path.getsize(output_path)} bytes.")
