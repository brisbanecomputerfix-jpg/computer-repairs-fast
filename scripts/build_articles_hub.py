"""
Generate the dedicated Blog & Articles Knowledge Hub:
- articles/index.html
- blog/index.html (mirrored alias so /blog/ works seamlessly)
"""

import os
import sys
import json
import re
from collections import Counter

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SCRIPT_DIR)
sys.path.insert(0, SCRIPT_DIR)

from data_articles import ARTICLES
from isometric_illustrations import get_svg_illustration, assign_illustration_theme

ARTICLES_DIR = os.path.join(ROOT_DIR, "articles")
BLOG_DIR = os.path.join(ROOT_DIR, "blog")
os.makedirs(ARTICLES_DIR, exist_ok=True)
os.makedirs(BLOG_DIR, exist_ok=True)


def get_article_groups(art):
    """Assign multi-group tags to articles for smooth category filtering."""
    groups = set()
    cat = art.get("category", "").lower()
    slug = art.get("slug", "").lower()
    title = art.get("h1", "").lower()
    text = f"{cat} {slug} {title}"

    if any(k in text for k in ["school", "byod", "touchscreen", "student", "laptop-guide"]):
        groups.add("school")
    if any(k in text for k in ["macbook", "apple", "imac", "retina", "flexgate", "olm"]):
        groups.add("macbook")
    if any(k in text for k in ["scam", "cyber", "torrent", "antivirus", "vpn", "security", "malware", "hack", "vibe"]):
        groups.add("security")
    if any(k in text for k in ["wfh", "business", "office", "printer", "myob", "reckon", "network", "vps", "coolify", "docking"]):
        groups.add("wfh")
    if any(k in text for k in ["senior", "elderly", "bigpond", "optus", "email", "gmail", "courses", "community", "lesson"]):
        groups.add("seniors")
    if any(k in text for k in ["screen", "battery", "spill", "liquid", "ssd", "hinge", "hardware", "motherboard", "overheating", "dust", "pc-to-new-pc", "photos", "quote", "dual-boot", "ai-lm-studio", "smart-tv", "browser"]):
        groups.add("hardware")
    if not groups:
        groups.add("hardware")
    return list(groups)


def generate_articles_hub():
    # Schema.org items
    items = []
    for idx, art in enumerate(ARTICLES, 1):
        items.append({
            "@type": "ListItem",
            "position": idx,
            "url": f"https://computerrepairsfast.com.au/articles/{art['slug']}.html",
            "name": art["h1"]
        })

    schema_json = json.dumps({
        "@context": "https://schema.org",
        "@type": "CollectionPage",
        "name": "Brisbane Computer Repair Guides & Blog",
        "description": "Expert Brisbane computer repair guides: school laptop touchscreen repairs, MacBook Retina fixes, WFH emergency setup, Wi-Fi & small business IT support.",
        "url": "https://computerrepairsfast.com.au/articles/",
        "isPartOf": {
            "@type": "WebSite",
            "name": "Computer Repairs Fast",
            "url": "https://computerrepairsfast.com.au/"
        },
        "mainEntity": {
            "@type": "ItemList",
            "itemListElement": items
        }
    }, indent=2)

    # Count category articles
    group_counts = Counter()
    for art in ARTICLES:
        for g in get_article_groups(art):
            group_counts[g] += 1

    cards_html = ""
    for art in ARTICLES:
        slug = art["slug"]
        h1 = art["h1"]
        category = art.get("category", "Hardware Guide")
        reading_time = art.get("reading_time", "6 min read")
        meta_desc = art.get("meta_desc", "")
        groups_list = get_article_groups(art)
        groups_attr = " ".join(groups_list)

        # Topic-specific isometric vector SVG illustration (strictly non-AI)
        theme = assign_illustration_theme(art)
        svg_markup = get_svg_illustration(theme)

        # Strictly clean snippet text with NO dangling HTML tags
        snippet = ""
        for b in art.get("content_blocks", []):
            if b.get("type") == "snippet":
                raw = b.get("text", "")
                clean_text = re.sub(r'<[^>]+>', '', raw).strip()
                clean_text = " ".join(clean_text.split())
                if len(clean_text) > 170:
                    clean_text = clean_text[:167] + "..."
                snippet = clean_text
                break
        if not snippet:
            raw = art.get("meta_desc", "")
            clean_text = re.sub(r'<[^>]+>', '', raw).strip()
            clean_text = " ".join(clean_text.split())
            if len(clean_text) > 170:
                clean_text = clean_text[:167] + "..."
            snippet = clean_text

        cards_html += f"""
        <article class="article-hub-card" data-group="{groups_attr}">
          <a href="/articles/{slug}.html" class="article-card-visual-link" tabindex="-1" aria-hidden="true">
            <div class="article-card-visual">
              {svg_markup}
            </div>
          </a>
          <div class="article-card-body">
            <div class="article-card-header">
              <span class="article-category-badge" title="{category}">{category}</span>
              <span class="article-reading-time">⏱️ {reading_time}</span>
            </div>
            <h2 class="article-card-title">
              <a href="/articles/{slug}.html">{h1}</a>
            </h2>
            <p class="article-card-snippet">
              {snippet}
            </p>
          </div>
          <div class="article-card-footer">
            <a href="/articles/{slug}.html" class="article-card-btn">
              <span>Read Full Guide</span>
              <span class="btn-arrow" aria-hidden="true">→</span>
            </a>
          </div>
        </article>
        """

    def build_page(canonical_url):
        return f"""<!DOCTYPE html>
<html lang="en-AU">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0, viewport-fit=cover" name="viewport"/>
<meta content="#dc2626" name="theme-color"/>
<title>Brisbane Computer Repair Guides & Blog | Computer Repairs Fast</title>
<meta content="Expert Brisbane computer repair guides: school laptop touchscreen repairs, MacBook Retina fixes, WFH emergency setup, Wi-Fi & small business IT support." name="description"/>
<link href="{canonical_url}" rel="canonical"/>

<!-- Open Graph / Social Meta -->
<meta content="website" property="og:type"/>
<meta content="Brisbane Computer Repair Guides & Blog | Computer Repairs Fast" property="og:title"/>
<meta content="Expert Brisbane computer repair guides: school laptop touchscreen repairs, MacBook Retina fixes, WFH emergency setup, Wi-Fi & small business IT support." property="og:description"/>
<meta content="{canonical_url}" property="og:url"/>
<meta content="Computer Repairs Fast" property="og:site_name"/>
<meta content="https://computerrepairsfast.com.au/images/crf-ambulance-banner.png" property="og:image"/>

<!-- Favicons -->
<link href="/favicon.svg" rel="icon" type="image/svg+xml"/>
<link href="/favicon.png" rel="icon" sizes="32x32" type="image/png"/>
<link href="/apple-touch-icon.png" rel="apple-touch-icon"/>

<!-- Core Stylesheet -->
<link href="/css/style.css?v=2.3" rel="stylesheet"/>

<!-- Schema JSON-LD -->
<script type="application/ld+json">
{schema_json}
</script>

<style>
/* Articles Hub Custom Styles */
.site-breadcrumbs {{
  background: #f8fafc;
  border-bottom: 1px solid #e2e8f0;
  padding: 12px 0;
  font-size: 0.88rem;
  width: 100%;
}}
.breadcrumbs-container {{
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
  color: #64748b;
  display: flex;
  align-items: center;
  gap: 8px;
  box-sizing: border-box;
  width: 100%;
}}
.breadcrumbs-container a {{
  color: #64748b;
  text-decoration: none;
  transition: color 0.15s;
}}
.breadcrumbs-container a:hover {{
  color: var(--red-600);
}}
.breadcrumbs-container .sep {{
  color: #cbd5e1;
}}
.breadcrumbs-container .current {{
  color: var(--red-600);
  font-weight: 700;
}}

/* Hero Section */
.articles-hub-hero {{
  background: linear-gradient(180deg, #fef2f2 0%, #ffffff 100%);
  padding: 48px 0 36px;
  border-bottom: 1px solid #fee2e2;
  width: 100%;
}}
.hub-hero-inner {{
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
  text-align: center;
  box-sizing: border-box;
  width: 100%;
}}
.hub-hero-badge {{
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background: #fee2e2;
  color: #b91c1c;
  font-size: 0.85rem;
  font-weight: 750;
  padding: 6px 14px;
  border-radius: 999px;
  margin-bottom: 16px;
  border: 1px solid #fecaca;
}}
.hub-hero-h1 {{
  color: #0f172a;
  font-size: clamp(1.85rem, 3.8vw, 2.45rem);
  line-height: 1.25;
  margin: 0 0 14px;
  font-weight: 850;
  letter-spacing: -0.02em;
}}
.hub-hero-sub {{
  color: #475569;
  font-size: clamp(1rem, 1.8vw, 1.12rem);
  max-width: 760px;
  margin: 0 auto 24px;
  line-height: 1.6;
}}
.articles-filter-nav {{
  display: flex;
  gap: 8px;
  justify-content: center;
  align-items: center;
  flex-wrap: wrap;
  max-width: 1080px;
  margin: 0 auto;
}}
.filter-btn {{
  background: #ffffff;
  color: #334155;
  padding: 8px 16px;
  border-radius: 999px;
  font-size: 0.88rem;
  font-weight: 650;
  border: 1.5px solid #e2e8f0;
  cursor: pointer;
  transition: all 0.2s ease;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  user-select: none;
}}
.filter-btn:hover {{
  background: #fef2f2;
  border-color: #fca5a5;
  color: var(--red-600);
  transform: translateY(-1px);
}}
.filter-btn.active {{
  background: var(--red-600);
  color: #ffffff;
  border-color: var(--red-600);
  box-shadow: 0 4px 12px rgba(220, 38, 38, 0.25);
}}
.filter-count {{
  font-size: 0.78rem;
  padding: 2px 7px;
  border-radius: 999px;
  background: #f1f5f9;
  color: #475569;
  font-weight: 700;
  transition: all 0.2s ease;
}}
.filter-btn.active .filter-count {{
  background: rgba(255, 255, 255, 0.25);
  color: #ffffff;
}}

/* Articles Section */
.articles-hub-section {{
  padding: 36px 0 60px;
  background: #f8fafc;
  width: 100%;
}}
.articles-hub-container {{
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
  box-sizing: border-box;
  width: 100%;
}}
.articles-hub-toolbar {{
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 12px;
  margin-bottom: 24px;
  padding: 12px 20px;
  background: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 12px;
  font-size: 0.92rem;
  color: #64748b;
  box-shadow: 0 1px 3px rgba(0,0,0,0.03);
  box-sizing: border-box;
  width: 100%;
}}
.hub-results-count strong {{
  color: #0f172a;
}}
.hub-quick-hint {{
  font-size: 0.85rem;
  color: #64748b;
}}
.articles-grid {{
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
  gap: 28px;
  width: 100%;
  align-items: stretch;
}}

/* Card Component */
.article-hub-card {{
  background: #ffffff;
  border: 1.5px solid #e2e8f0;
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(15, 23, 42, 0.04);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  transition: transform 0.25s ease, box-shadow 0.25s ease, border-color 0.25s ease;
  position: relative;
  box-sizing: border-box;
}}
.article-hub-card:hover {{
  transform: translateY(-4px);
  box-shadow: 0 14px 28px rgba(15, 23, 42, 0.09);
  border-color: #fca5a5;
}}
.article-card-visual-link {{
  display: block;
  text-decoration: none;
  background: #f8fafc;
  border-bottom: 1px solid #f1f5f9;
  overflow: hidden;
}}
.article-card-visual {{
  width: 100%;
  height: 140px;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  position: relative;
}}
.article-card-visual svg.iso-svg {{
  width: 100%;
  height: 100%;
  display: block;
  transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1);
}}
.article-hub-card:hover .article-card-visual svg.iso-svg {{
  transform: scale(1.03);
}}
.article-card-body {{
  padding: 20px 20px 0;
  display: flex;
  flex-direction: column;
  flex-grow: 1;
}}
.article-card-header {{
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 8px;
  margin-bottom: 12px;
}}
.article-category-badge {{
  background: #fee2e2;
  color: #b91c1c;
  font-size: 0.78rem;
  font-weight: 750;
  padding: 4px 10px;
  border-radius: 999px;
  letter-spacing: 0.02em;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  max-width: 65%;
}}
.article-reading-time {{
  font-size: 0.8rem;
  color: #64748b;
  font-weight: 600;
  white-space: nowrap;
}}
.article-card-title {{
  font-size: 1.08rem;
  font-weight: 800;
  line-height: 1.42;
  margin: 0 0 10px;
  color: #0f172a;
  min-height: 2.84em;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}}
.article-card-title a {{
  color: #0f172a;
  text-decoration: none;
  transition: color 0.15s ease;
}}
.article-card-title a:hover {{
  color: var(--red-600);
}}
.article-card-snippet {{
  font-size: 0.89rem;
  color: #475569;
  line-height: 1.55;
  margin: 0 0 16px;
  min-height: 4.65em;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}}
.article-card-footer {{
  margin-top: auto;
  padding: 14px 20px 20px;
  border-top: 1px solid #f1f5f9;
}}
.article-card-btn {{
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  width: 100%;
  padding: 10px 16px;
  background: #f8fafc;
  color: #0f172a;
  border: 1.5px solid #e2e8f0;
  border-radius: 10px;
  font-size: 0.92rem;
  font-weight: 700;
  text-decoration: none;
  transition: all 0.2s ease;
  box-sizing: border-box;
}}
.article-card-btn:hover {{
  background: var(--red-600);
  color: #ffffff;
  border-color: var(--red-600);
  box-shadow: 0 4px 12px rgba(220, 38, 38, 0.2);
}}
.btn-arrow {{
  transition: transform 0.2s ease;
}}
.article-card-btn:hover .btn-arrow {{
  transform: translateX(4px);
}}

/* Emergency Assistance CTA */
.hub-emergency-cta {{
  background: #fef2f2;
  border: 2px solid #fecaca;
  border-radius: 16px;
  padding: 36px 28px;
  margin-top: 48px;
  text-align: center;
  max-width: 1200px;
  width: 100%;
  box-sizing: border-box;
}}
.hub-cta-icon {{
  font-size: 2.2rem;
  display: block;
  margin-bottom: 10px;
}}
.hub-cta-title {{
  color: #b91c1c;
  font-size: 1.6rem;
  margin: 0 0 10px;
  font-weight: 800;
}}
.hub-cta-text {{
  color: #475569;
  font-size: 1.05rem;
  max-width: 650px;
  margin: 0 auto 24px;
  line-height: 1.6;
}}
.hub-cta-actions {{
  display: flex;
  gap: 14px;
  justify-content: center;
  flex-wrap: wrap;
}}

@media (max-width: 640px) {{
  .articles-grid {{
    grid-template-columns: 1fr;
    gap: 16px;
  }}
  .articles-hub-toolbar {{
    flex-direction: column;
    align-items: flex-start;
  }}
  .filter-btn {{
    font-size: 0.82rem;
    padding: 6px 12px;
  }}
}}
</style>
</head>
<body>

<!-- Announcement Bar -->
<div class="ambulance-bar">
<div class="ambulance-bar-inner">
<div>
<a href="/index.html" style="color: #fff; text-decoration: underline; margin-right: 10px;">← Main Home</a>
<span class="ambulance-badge"><span class="pulse-dot"></span> 🚑 Brisbane Emergency Computer Knowledge Base</span>
</div>
<div>
<span>$80 Diagnostic (Inside Repair Fee) • $0 Call-Out • Same-Day Repairs Across Brisbane</span>
</div>
</div>
</div>

<!-- Header Navigation -->
<header class="site-header">
<div class="header-container">
<a class="brand-block" href="/">
<div class="brand-cross">✚</div>
<div class="brand-text">
<div class="title">Computer Repairs <span>Fast</span></div>
<p>Brisbane Emergency Computer &amp; Laptop Service</p>
</div>
</a>
<nav aria-label="Main Navigation" class="site-nav" id="siteNav">
<ul class="nav-list">
<li class="nav-item"><a class="nav-link" href="/services/">Services</a></li>
<li class="nav-item"><a class="nav-link active" href="/articles/">Guides & Blog</a></li>
<li class="nav-item"><a class="nav-link" href="/#pricing">Pricing</a></li>
<li class="nav-item"><a class="nav-link" href="/#locations">Locations</a></li>
<li class="nav-item"><a class="nav-link" href="/#how-it-works">How It Works</a></li>
<li class="nav-item"><a class="nav-link" href="/#reviews"><span style="color: #f59e0b; margin-right: 4px;">★</span>Reviews (112+)</a></li>
<li class="nav-item"><a class="nav-link" href="/contact.html">Contact</a></li>
</ul>
</nav>
<div class="header-contacts">
<div class="call-box">
<span class="call-sub">Need urgent help?</span>
<a class="call-tel dynamic-phone" href="tel:0401148654" title="Call Technician Now">📞 <span class="header-call-num">0401 148 654</span></a>
</div>
<a class="header-sms-pill" href="sms:0401148654?body=Hi%20Computer%20Repairs%20Fast,%20I%20have%20a%20question" title="Text Technician">💬 Text</a>
<a class="btn btn-emergency header-book-btn" href="/#booking">Book Visit</a>
<!-- Mobile Menu Hamburger Toggle -->
<button aria-expanded="false" aria-label="Open Navigation Menu" class="mobile-menu-toggle" id="mobileMenuToggle">
<span class="toggle-bar top-bar"></span>
<span class="toggle-bar mid-bar"></span>
<span class="toggle-bar bot-bar"></span>
</button>
</div>
</div>
</header>

<main id="main-content">

<!-- Breadcrumbs Navigation -->
<nav class="site-breadcrumbs" aria-label="Breadcrumb">
  <div class="breadcrumbs-container">
    <a href="/">Home</a>
    <span class="sep" aria-hidden="true">/</span>
    <span class="current">Guides &amp; Blog</span>
  </div>
</nav>

<!-- Hero Section -->
<section class="articles-hub-hero">
  <div class="hub-hero-inner">
    <div class="hub-hero-badge">
      <span>🚑</span>
      <span>Brisbane Tech Knowledge Base</span>
    </div>
    <h1 class="hub-hero-h1">
      Brisbane Computer Repair Guides &amp; Tech Blog
    </h1>
    <p class="hub-hero-sub">
      In-depth hardware repair guides, school laptop screen replacement costs, Apple MacBook diagnostics, Work-From-Home emergency fixes, and cybersecurity advice across Greater Brisbane.
    </p>

    <!-- Category Filters with Real-Time Filtering -->
    <div class="articles-filter-nav" role="toolbar" aria-label="Article Category Filters">
      <button type="button" class="filter-btn active" data-group="all" data-label="All Guides">
        <span>All Guides</span>
        <span class="filter-count">{len(ARTICLES)}</span>
      </button>
      <button type="button" class="filter-btn" data-group="school" data-label="School &amp; BYOD">
        <span>🎒 School &amp; BYOD</span>
        <span class="filter-count">{group_counts['school']}</span>
      </button>
      <button type="button" class="filter-btn" data-group="macbook" data-label="Apple MacBooks">
        <span>🍏 Apple MacBooks</span>
        <span class="filter-count">{group_counts['macbook']}</span>
      </button>
      <button type="button" class="filter-btn" data-group="hardware" data-label="Hardware &amp; Repairs">
        <span>🔧 Hardware &amp; Repairs</span>
        <span class="filter-count">{group_counts['hardware']}</span>
      </button>
      <button type="button" class="filter-btn" data-group="security" data-label="Cyber &amp; Scams">
        <span>🛡️ Cyber &amp; Scams</span>
        <span class="filter-count">{group_counts['security']}</span>
      </button>
      <button type="button" class="filter-btn" data-group="wfh" data-label="WFH &amp; Business">
        <span>🏢 WFH &amp; Business</span>
        <span class="filter-count">{group_counts['wfh']}</span>
      </button>
      <button type="button" class="filter-btn" data-group="seniors" data-label="Seniors &amp; Email">
        <span>✉️ Seniors &amp; Email</span>
        <span class="filter-count">{group_counts['seniors']}</span>
      </button>
    </div>
  </div>
</section>

<!-- Articles Grid Section -->
<section class="articles-hub-section">
  <div class="articles-hub-container">
    <div class="articles-hub-toolbar">
      <div class="hub-results-count" id="hubResultsCount">
        Showing <strong>{len(ARTICLES)}</strong> of {len(ARTICLES)} repair guides &amp; articles
      </div>
      <div class="hub-quick-hint">
        💡 Tip: Filter by category above (Apple MacBooks, Hardware, Cyber Scams, WFH) or browse our guides below
      </div>
    </div>

    <div class="articles-grid" id="articlesGrid">
      {cards_html}
    </div>

    <!-- Urgent Emergency CTA -->
    <div class="hub-emergency-cta">
      <span class="hub-cta-icon" aria-hidden="true">🚑</span>
      <h3 class="hub-cta-title">Need Immediate Computer Help in Brisbane?</h3>
      <p class="hub-cta-text">
        We come directly to your home, office, or school across Greater Brisbane. Fixed $80 diagnostic (included in your repair), $0 call-out fee, and fast same-day repairs.
      </p>
      <div class="hub-cta-actions">
        <a class="btn btn-emergency dynamic-phone" href="tel:0401148654" style="font-size: 1.15rem; padding: 12px 24px;">📞 Call 0401 148 654</a>
        <a class="btn btn-white" href="/#booking" style="border: 1px solid #d1d5db; font-size: 1.15rem; padding: 12px 24px;">📋 Book Mobile Visit</a>
      </div>
    </div>
  </div>
</section>

</main>

<!-- Footer -->
<footer class="site-footer">
<div class="footer-inner">
<div class="footer-col">
<h4>Computer Repairs Fast</h4>
<p>Brisbane's rapid mobile tech ambulance. Same-day on-site repairs and workshop drop-offs across metro Brisbane.</p>
<p>📞 Phone: <a href="tel:0401148654" style="color: #fff; font-weight: 700;">0401 148 654</a><br/>
✉️ Email: info@computerrepairsfast.com.au</p>
</div>
<div class="footer-col">
<h4>Quick Links</h4>
<ul class="footer-links">
<li><a href="/services/">All Repair Services</a></li>
<li><a href="/articles/">Guides & Blog</a></li>
<li><a href="/#pricing">Pricing & Diagnostic</a></li>
<li><a href="/#locations">Brisbane Suburbs</a></li>
<li><a href="/faq.html">Frequently Asked Questions</a></li>
<li><a href="/contact.html">Contact Us</a></li>
</ul>
</div>
<div class="footer-col">
<h4>Popular Guides</h4>
<ul class="footer-links">
<li><a href="/articles/brisbane-school-laptop-cracked-touch-screen-repair-guide.html">School Laptop Screen Repairs</a></li>
<li><a href="/articles/macbook-air-pro-cracked-screen-replacement-cost-brisbane.html">MacBook Screen Replacement Cost</a></li>
<li><a href="/articles/lenovo-laptop-broken-hinge-casing-repair-guide.html">Lenovo Broken Hinge & Casing Guide</a></li>
<li><a href="/articles/printer-offline-troubleshooting-wifi-setup-brisbane.html">Printer Offline Troubleshooting</a></li>
<li><a href="/articles/telstra-bigpond-optus-email-migration-to-outlook-365-guide.html">BigPond & Optus Email Migration</a></li>
<li><a href="/articles/senior-computer-lessons-online-banking-safety-brisbane.html">Senior Lessons & Banking Safety</a></li>
</ul>
</div>
<div class="footer-col">
<h4>Workshop Labs</h4>
<p>📍 East Brisbane Hub QLD 4169 (By appointment)<br/>
📍 West End Hub QLD 4101 (By appointment)<br/>
🚐 Mobile Van: Same-Day Service All Brisbane</p>
</div>
</div>
<div class="footer-bottom">
<p>© 2026 Computer Repairs Fast. All rights reserved. ABN: 98 288 669 674. Servicing Greater Brisbane, Queensland.</p>
</div>
</footer>

<!-- Mobile Slide-Down Drawer with Accordion Sections -->
<div aria-hidden="true" class="mobile-nav-drawer" id="mobileNavDrawer">
<div class="drawer-inner">
<div class="drawer-top-bar">
<div class="drawer-title-block">
<span class="drawer-pulse-dot"></span>
<span class="drawer-title-text">Menu &amp; Services</span>
</div>
<button aria-label="Close navigation menu (Esc)" class="drawer-close-btn" id="drawerCloseBtn" type="button">
<span class="close-x">✕</span>
<span class="close-word">Close</span>
</button>
</div>
<div class="drawer-search-wrap">
<div class="drawer-search-box">
<span class="drawer-search-icon">🔍</span>
<input type="search" class="drawer-search-input" id="drawerSearchInput" placeholder="Search 160+ services, suburbs, FAQs..." autocomplete="off">
</div>
</div>
<div class="drawer-acc-item">
<button aria-expanded="false" class="drawer-acc-btn">
<span class="drawer-acc-title">🛠️ Services</span>
<svg class="drawer-acc-arrow" fill="currentColor" height="16" viewbox="0 0 20 20" width="16"><path clip-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" fill-rule="evenodd"></path></svg>
</button>
<div class="drawer-acc-content">
<a class="drawer-sublink" href="/services/laptop-screen-repairs.html">
<span class="sub-icon">💻</span>
<div class="sub-info">
<strong>Laptop Screen Replacement</strong>
<span>Cracked, lines or black screen? Fitted same-day</span>
</div>
</a>
<a class="drawer-sublink" href="/services/laptop-battery-replacement.html">
<span class="sub-icon">🔋</span>
<div class="sub-info">
<strong>Laptop Battery Replacement</strong>
<span>Swollen batteries, rapid drain &amp; charging fix</span>
</div>
</a>
<a class="drawer-sublink" href="/services/data-recovery.html">
<span class="sub-icon">💾</span>
<div class="sub-info">
<strong>Emergency Data Recovery</strong>
<span>Lost photos, clicking drives &amp; dead SSDs</span>
</div>
</a>
<a class="drawer-sublink" href="/services/scam-virus-removal.html">
<span class="sub-icon">🛡️</span>
<div class="sub-info">
<strong>Scam Cleanup &amp; Banking Safety</strong>
<span>Immediate scam lockout &amp; remote tool purge</span>
</div>
</a>
<a class="drawer-sublink" href="/services/slow-computer-speed-up.html">
<span class="sub-icon">🚀</span>
<div class="sub-info">
<strong>Slow PC to SSD Speed Up</strong>
<span>Clone drive to fast NVMe SSD with zero data loss</span>
</div>
</a>
</div>
</div>
<div class="drawer-acc-item">
<button aria-expanded="false" class="drawer-acc-btn">
<span class="drawer-acc-title">📍 Locations</span>
<svg class="drawer-acc-arrow" fill="currentColor" height="16" viewbox="0 0 20 20" width="16"><path clip-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" fill-rule="evenodd"></path></svg>
</button>
<div class="drawer-acc-content">
<a class="drawer-sublink" href="/#locations">
<span class="sub-icon">🚐</span>
<div class="sub-info">
<strong>Brisbane Mobile Call-Out</strong>
<span>We come directly to your door today</span>
</div>
</a>
<a class="drawer-sublink" href="/locations/east-brisbane.html">
<span class="sub-icon">📍</span>
<div class="sub-info">
<strong>East Brisbane Hub (4169)</strong>
<span>Inner East, Coorparoo, Woolloongabba</span>
</div>
</a>
<a class="drawer-sublink" href="/locations/west-end.html">
<span class="sub-icon">📍</span>
<div class="sub-info">
<strong>West End Hub (4101)</strong>
<span>South Brisbane, Highgate Hill, Dutton Park</span>
</div>
</a>
</div>
</div>
<div class="drawer-direct-link" style="margin-bottom: 8px;">
<a class="drawer-single-btn" href="/#reviews" style="background: #fef2f2; border-color: #fca5a5; color: #b91c1c;">
⭐ 112+ Verified Google Reviews (4.9★)
</a>
</div>
<div class="drawer-direct-link">
<a class="drawer-single-btn" href="/contact.html">📞 Contact Us Directly</a>
</div>
<div class="drawer-cta-row">
<a class="btn btn-emergency dynamic-phone" href="tel:0401148654">📞 Call 0401 148 654</a>
<a class="btn btn-white-glass" href="sms:0401148654?body=Hi%20Computer%20Repairs%20Fast,%20I%20need%20help%20with%20my%20computer">💬 Text / SMS</a>
</div>
</div>
</div>

<!-- Navigate to Top Arrow Button -->
<button aria-label="Scroll back to top" class="back-to-top" id="backToTopBtn" title="Scroll to top" type="button">
<svg aria-hidden="true" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.8" viewbox="0 0 24 24">
<path d="M18 15l-6-6-6 6"></path>
</svg>
</button>

<!-- Mobile Sticky Emergency Action Bar -->
<div class="mobile-sticky-bar">
<a class="btn btn-emergency dynamic-phone" href="tel:0401148654">📞 Call 0401 148 654</a>
<a class="btn btn-white-glass" href="sms:0401148654?body=Hi%20Computer%20Repairs%20Fast,%20I%20need%20help%20with%20my%20computer">💬 Text / SMS</a>
</div>

<!-- Core Site Scripts -->
<script defer src="/js/main.js?v=2.3"></script>

<!-- Real-Time Category Filter Script -->
<script>
document.addEventListener('DOMContentLoaded', function() {{
  const filterBtns = document.querySelectorAll('.filter-btn');
  const cards = document.querySelectorAll('.article-hub-card');
  const resultsCount = document.getElementById('hubResultsCount');

  filterBtns.forEach(btn => {{
    btn.addEventListener('click', function() {{
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const targetGroup = btn.getAttribute('data-group');
      const label = btn.getAttribute('data-label') || 'articles';
      let visibleCount = 0;

      cards.forEach(card => {{
        const groups = (card.getAttribute('data-group') || '').split(' ');
        if (targetGroup === 'all' || groups.includes(targetGroup)) {{
          card.style.display = 'flex';
          visibleCount++;
        }} else {{
          card.style.display = 'none';
        }}
      }});

      if (resultsCount) {{
        resultsCount.innerHTML = 'Showing <strong>' + visibleCount + '</strong> of ' + cards.length + ' guides in ' + label;
      }}
    }});
  }});
}});
</script>

</body>
</html>"""

    # Write articles/index.html
    articles_index_path = os.path.join(ARTICLES_DIR, "index.html")
    with open(articles_index_path, "w", encoding="utf-8") as f:
        f.write(build_page("https://computerrepairsfast.com.au/articles/"))
    print(f"Generated {articles_index_path}")

    # Write blog/index.html with matching canonical
    blog_index_path = os.path.join(BLOG_DIR, "index.html")
    with open(blog_index_path, "w", encoding="utf-8") as f:
        f.write(build_page("https://computerrepairsfast.com.au/blog/"))
    print(f"Generated {blog_index_path}")


if __name__ == "__main__":
    generate_articles_hub()
