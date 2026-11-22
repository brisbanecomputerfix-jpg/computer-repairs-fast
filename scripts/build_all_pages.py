import os
import sys
import json
import re
import glob
import xml.etree.ElementTree as ET
from datetime import datetime

# Import data modules
from data_suburbs import SUBURBS
from data_services import SERVICES
from data_articles import ARTICLES

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOCATIONS_DIR = os.path.join(ROOT_DIR, "locations")
SERVICES_DIR = os.path.join(ROOT_DIR, "services")
ARTICLES_DIR = os.path.join(ROOT_DIR, "articles")

os.makedirs(LOCATIONS_DIR, exist_ok=True)
os.makedirs(SERVICES_DIR, exist_ok=True)
os.makedirs(ARTICLES_DIR, exist_ok=True)

print(f"Project Root: {ROOT_DIR}")

# --- SUBURB TEMPLATE ---
def render_suburb_html(s):
    slug = s["slug"]
    name = s["name"]
    postcode = s["postcode"]
    region = s["region"]
    hub = s["hub"]
    hub_dist = s["hub_dist"]
    travel_time = s["travel_time"]
    landmarks = s["landmarks"]
    surrounding_str = ", ".join(s["surrounding"])
    
    reviews_html = ""
    for r in s["reviews"]:
        stars = "★" * r["rating"]
        reviews_html += f"""
        <div class="review-card" style="background: #fff; padding: 24px; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 2px 8px rgba(0,0,0,0.03);">
          <div style="color: #f59e0b; font-size: 1.15rem; margin-bottom: 8px;">{stars}</div>
          <p style="font-size: 1rem; line-height: 1.6; color: #334155; margin-bottom: 14px;">"{r['text']}"</p>
          <div style="font-weight: 700; color: #0f172a; font-size: 0.95rem;">{r['name']} <span style="font-weight: 400; color: #64748b;">— {r['suburb']} Resident</span></div>
        </div>
        """
        
    faqs_html = ""
    faq_schema_list = []
    for q, a in s["faqs"]:
        faqs_html += f"""
        <div class="faq-item" style="background: #fff; border: 1px solid #e2e8f0; border-radius: 8px; margin-bottom: 12px; padding: 18px 24px;">
          <h3 style="margin-top: 0; color: #0f172a; font-size: 1.1rem; display: flex; align-items: center; gap: 8px;">
            <span style="color: var(--red-600); font-weight: 800;">Q.</span> {q}
          </h3>
          <p style="margin-bottom: 0; color: #475569; line-height: 1.6;">{a}</p>
        </div>
        """
        faq_schema_list.append({
            "@type": "Question",
            "name": q,
            "acceptedAnswer": {
                "@type": "Answer",
                "text": a
            }
        })
        
    faq_schema_json = json.dumps({
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": faq_schema_list
    }, indent=2)

    local_biz_schema_json = json.dumps({
        "@context": "https://schema.org",
        "@type": ["ComputerStore", "EmergencyService", "LocalBusiness"],
        "name": f"Computer Repairs Fast - {name}",
        "url": f"https://computerrepairsfast.com.au/locations/{slug}.html",
        "telephone": "0401148654",
        "priceRange": "$$",
        "address": {
            "@type": "PostalAddress",
            "addressLocality": name,
            "addressRegion": "QLD",
            "postalCode": postcode,
            "addressCountry": "Australia"
        },
        "openingHoursSpecification": [
            {
                "@type": "OpeningHoursSpecification",
                "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
                "opens": "08:00",
                "closes": "18:30"
            },
            {
                "@type": "OpeningHoursSpecification",
                "dayOfWeek": ["Saturday", "Sunday"],
                "opens": "09:00",
                "closes": "17:00"
            }
        ],
        "areaServed": [name] + s["surrounding"]
    }, indent=2)

    breadcrumb_schema_json = json.dumps({
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {
                "@type": "ListItem",
                "position": 1,
                "name": "Home",
                "item": "https://computerrepairsfast.com.au/"
            },
            {
                "@type": "ListItem",
                "position": 2,
                "name": "Locations",
                "item": "https://computerrepairsfast.com.au/#locations"
            },
            {
                "@type": "ListItem",
                "position": 3,
                "name": f"{name} ({postcode})",
                "item": f"https://computerrepairsfast.com.au/locations/{slug}.html"
            }
        ]
    }, indent=2)

    return f"""<!DOCTYPE html>
<html lang="en-AU">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0, viewport-fit=cover" name="viewport"/>
<meta content="#dc2626" name="theme-color"/>
<title>Computer Repairs {name} | Same-Day PC & Laptop Service {postcode}</title>
<meta content="Fast computer repairs in {name} QLD {postcode}. Laptop screens, scam cleanup & SSD speed-ups. Fixed $80 diagnosis, $0 call-out fee. Call 0401 148 654." name="description"/>
<link href="https://computerrepairsfast.com.au/locations/{slug}.html" rel="canonical"/>

<!-- Open Graph & Social Meta -->
<meta content="Computer Repairs {name} | Same-Day PC & Laptop Service {postcode}" property="og:title"/>
<meta content="Fast computer repairs in {name} QLD {postcode}. Laptop screens, scam cleanup & SSD speed-ups. Fixed $80 diagnosis, $0 call-out fee. Call 0401 148 654." property="og:description"/>
<meta content="https://computerrepairsfast.com.au/images/Fast-Computer-Repairs-East-Brisbane-4169.png" property="og:image"/>
<meta content="https://computerrepairsfast.com.au/locations/{slug}.html" property="og:url"/>
<meta content="business.business" property="og:type"/>
<meta content="en_AU" property="og:locale"/>
<meta content="summary_large_image" name="twitter:card"/>
<meta content="Computer Repairs {name} | Same-Day PC & Laptop Service {postcode}" name="twitter:title"/>
<meta content="Fast computer repairs in {name} QLD {postcode}. Laptop screens, scam cleanup & SSD speed-ups. Fixed $80 diagnosis, $0 call-out fee. Call 0401 148 654." name="twitter:description"/>

<!-- Favicon & Styles -->
<link href="/favicon.svg" rel="icon" type="image/svg+xml"/>
<link href="/favicon.png" rel="icon" sizes="32x32" type="image/png"/>
<link href="/apple-touch-icon.png" rel="apple-touch-icon" sizes="180x180"/>
<link href="/css/style.css?v=2.3" rel="stylesheet"/>

<!-- Schema.org Structured Data -->
<script type="application/ld+json">
{local_biz_schema_json}
</script>
<script type="application/ld+json">
{faq_schema_json}
</script>
<script type="application/ld+json">
{breadcrumb_schema_json}
</script>
</head>
<body>

<!-- Top Emergency Announcement Bar -->
<div class="ambulance-bar">
<div class="ambulance-bar-inner">
<div>
<a href="/index.html" style="color: #fff; text-decoration: underline; margin-right: 10px;">← Main Home</a>
<span class="ambulance-badge">
<span class="pulse-dot"></span> 🚑 {name} Mobile Dispatch & Workshop Service (QLD {postcode})
</span>
</div>
<div>
<span>$80 Diagnostic (Inside Repair Fee) • Zero Call-Out Fee • Workshop Drop-Off or We Visit Your Home</span>
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
<li class="nav-item"><a class="nav-link" href="/articles/">Guides & Blog</a></li>
<li class="nav-item"><a class="nav-link" href="/#pricing">Pricing</a></li>
<li class="nav-item"><a class="nav-link" href="/#locations">Locations</a></li>
<li class="nav-item"><a class="nav-link" href="/#how-it-works">How It Works</a></li>
<li class="nav-item"><a class="nav-link" href="/#reviews"><span style="color: #f59e0b; margin-right: 4px;">★</span>Reviews (112+)</a></li>
<li class="nav-item"><a class="nav-link" href="/contact.html">Contact</a></li>
</ul>
</nav>
<div class="header-contacts">
<div class="call-box">
<span class="call-sub">Need urgent help in {name}?</span>
<a class="call-tel dynamic-phone" href="tel:0401148654" title="Call Technician Now">📞 <span class="header-call-num">0401 148 654</span></a>
</div>
<a class="header-sms-pill" href="sms:0401148654?body=Hi%20Computer%20Repairs%20Fast,%20I%20need%20help%20in%20{name}" title="Text Technician">💬 Text</a>
<a class="btn btn-emergency header-book-btn" href="#booking">Book Visit</a>
</div>
</div>
</header>
<main id="main-content">

<!-- Breadcrumbs -->
<div style="background: #f8fafc; border-bottom: 1px solid #e2e8f0; padding: 12px 0;">
  <div style="max-width: 1200px; margin: 0 auto; padding: 0 16px; font-size: 0.9rem; color: #64748b;">
    <a href="/" style="color: #64748b; text-decoration: none;">Home</a> &gt; 
    <a href="/#locations" style="color: #64748b; text-decoration: none;">Locations</a> &gt; 
    <span style="color: var(--red-600); font-weight: 700;">{name} ({postcode})</span>
  </div>
</div>

<!-- Hero Section with Booking Form -->
<section class="hero-wrapper">
<div class="hero-box">
<div>
<div class="hero-pill-row">
<span class="red-pill">📍 {name} Dispatch (QLD {postcode})</span>
<span class="red-pill">🚗 Free In-Home Visits Across {region}</span>
<span class="red-pill">⚡ Same-Day Repairs</span>
</div>
<h1 class="hero-heading">Computer Repairs {name} QLD {postcode}<br/><span>Mobile Call-Out &amp; Workshop Repairs</span></h1>
<p class="hero-plain-text">
Broken laptop screen, slow PC, or scary scam phone call? Don't stress. We service all residences, apartments, and small businesses throughout <strong>{name}</strong> and surrounding areas ({surrounding_str}). We come directly to you with <strong>zero travel or call-out fees</strong>, or you can drop your computer off at our local {hub} ({travel_time} away).
</p>
<div class="hero-btn-row">
<a class="btn btn-emergency" href="tel:0401148654" style="font-size: 1.25rem;">
📞 Call {name} Dispatch: <span class="dynamic-phone">0401 148 654</span>
</a>
<a class="btn btn-white" href="#booking">
📋 Instant On-Site Booking
</a>
</div>
<div class="guarantee-grid">
<div class="guarantee-item">
<div class="guarantee-icon">🩺</div>
<div class="guarantee-text">
<strong>Fixed $80 Diagnosis</strong>
<p>Full testing at your home or our workshop. Credited to your repair total.</p>
</div>
</div>
<div class="guarantee-item">
<div class="guarantee-icon">🚗</div>
<div class="guarantee-text">
<strong>No Call-Out Fee ($0)</strong>
<p>Travel across {name} and inner Brisbane is 100% free of charge.</p>
</div>
</div>
<div class="guarantee-item">
<div class="guarantee-icon">⚡</div>
<div class="guarantee-text">
<strong>Same-Day Fixes</strong>
<p>Standard screens, batteries, and malware cleanups done in hours.</p>
</div>
</div>
<div class="guarantee-item">
<div class="guarantee-icon">👵</div>
<div class="guarantee-text">
<strong>Patient &amp; Senior Friendly</strong>
<p>Clear, plain-English advice with zero confusing technical jargon.</p>
</div>
</div>
</div>
</div>

<!-- Dispatch Card & Booking Form -->
<div class="dispatch-card" id="booking">
<div class="dispatch-header">
<h2><span>📍</span> {name} Mobile Booking</h2>
<p>We visit your home or office in {name} today</p>
</div>
<div class="dispatch-price-badge">
<div class="badge-item-left">
<span class="badge-fee">$80 Fixed</span>
<span class="badge-desc">Full Diagnostic</span>
</div>
<div class="badge-item-right">
<span class="badge-pill">$0 Call-Out Fee</span>
</div>
</div>

<form action="/send-mail.php" class="ajax-booking-form" method="POST">
<div aria-hidden="true" style="position: absolute; left: -9999px; top: -9999px; height: 0; width: 0; opacity: 0; pointer-events: none;">
<input autocomplete="off" name="website_hp" tabindex="-1" type="text"/>
<input autocomplete="off" name="company_hp" tabindex="-1" type="text"/>
</div>
<input name="form_timestamp" type="hidden" value=""/>
<input name="source_page" type="hidden" value="{slug}.html"/>

<div class="form-row-2col">
<div class="form-group">
<label for="bookName">1. Name</label>
<input class="form-control" id="bookName" name="name" placeholder="Your Name" required="" type="text"/>
</div>
<div class="form-group">
<label for="bookPhone">2. Phone / Mobile</label>
<input class="form-control" id="bookPhone" name="phone" placeholder="0412 345 678" required="" type="tel"/>
</div>
</div>

<div class="form-row-2col">
<div class="form-group">
<label for="bookSuburb">3. Suburb</label>
<input class="form-control" id="bookSuburb" name="suburb" required="" type="text" value="{name}"/>
</div>
<div class="form-group">
<label for="bookEmail">4. Email</label>
<input class="form-control" id="bookEmail" name="email" placeholder="email@example.com" required="" type="email"/>
</div>
</div>

<div class="form-group form-group-full">
<label for="bookProblem">5. What is the computer problem?</label>
<select class="form-control" id="bookProblem" name="problem">
<option value="not_starting">Won't turn on / Black screen / Freezing</option>
<option value="scam_virus">Scam phone call / Remote access pop-up</option>
<option value="broken_screen">Broken or cracked laptop screen</option>
<option value="slow_computer">Extremely slow / Needs SSD upgrade</option>
<option value="lost_data">Lost photos, documents, or clicking drive</option>
<option value="other">Other issue</option>
</select>
</div>

<button class="btn btn-emergency" style="width: 100%; font-size: 1.15rem; padding: 14px;" type="submit">
Book {name} Technician
</button>
</form>

<div style="text-align: center; margin-top: 14px; font-size: 0.95rem; color: var(--gray-600);">
Urgent? Call directly: <a class="dynamic-phone" href="tel:0401148654" style="color: var(--red-600); font-weight: 800; text-decoration: underline;">0401 148 654</a>
</div>
</div>
</div>
</section>

<!-- Local Coverage & Landmarks -->
<section class="content-section">
<div class="section-title-wrap">
<span class="section-tag">{name} Service Footprint</span>
<h2 class="section-heading">Local In-Home Repairs &amp; Workshop Support</h2>
<p class="section-sub">Rapid mobile dispatch near {landmarks}. Free travel across {region} Brisbane.</p>
</div>

<div class="services-grid">
<div class="service-card">
<div class="service-card-icon">💻</div>
<h3>Laptop Screen Replacement</h3>
<p>Cracked or flickering display? We replace screens for HP, Dell, Lenovo, ASUS, Acer and MacBooks on-site in {name} within 1 to 2 hours.</p>
<div class="service-card-meta">
<span class="badge-price">From $230 (Standard FHD)</span>
<a class="service-link" href="/services/laptop-screen-repairs.html">View Screen Pricing →</a>
</div>
</div>

<div class="service-card">
<div class="service-card-icon">🛡️</div>
<h3>Scam Cleanup &amp; Banking Security</h3>
<p>Received a suspicious call claiming to be Telstra, NBN or your bank? We visit your {name} home immediately, remove remote tools, and secure your accounts.</p>
<div class="service-card-meta">
<span class="badge-price">From $150 (In-Home)</span>
<a class="service-link" href="/services/scam-virus-removal.html">Scam Recovery →</a>
</div>
</div>

<div class="service-card">
<div class="service-card-icon">🚀</div>
<h3>Slow PC to SSD Speed Up</h3>
<p>Make your sluggish computer 5x to 10x faster. We clone your old drive to a lightning-fast NVMe/SATA SSD with zero data or program loss.</p>
<div class="service-card-meta">
<span class="badge-price">From $230 (Drive + Clone)</span>
<a class="service-link" href="/services/slow-computer-speed-up.html">Speed Up Service →</a>
</div>
</div>

<div class="service-card">
<div class="service-card-icon">🔋</div>
<h3>Swollen Battery Replacement</h3>
<p>Trackpad stiff or casing lifting in {name}? Swollen lithium batteries are a severe fire hazard. We safely replace cells on-site.</p>
<div class="service-card-meta">
<span class="badge-price">From $190 (Fitted)</span>
<a class="service-link" href="/services/laptop-battery-replacement.html">Battery Pricing →</a>
</div>
</div>

<div class="service-card">
<div class="service-card-icon">☕</div>
<h3>Liquid &amp; Coffee Spill Rescue</h3>
<p>Spilled tea, wine, or water? Turn it off immediately! Our ultrasonic de-oxidation cleaning strips corrosion and revives motherboards.</p>
<div class="service-card-meta">
<span class="badge-price">From $170 (Ultrasonic)</span>
<a class="service-link" href="/services/liquid-damage-repairs.html">Liquid Protocol →</a>
</div>
</div>

<div class="service-card">
<div class="service-card-icon">💾</div>
<h3>Emergency Data Recovery</h3>
<p>Hard drive clicking or laptop won't turn on? We rescue precious family photos, tax records, and documents with a strict 'No Data, No Fee' guarantee.</p>
<div class="service-card-meta">
<span class="badge-price">No Data, No Fee</span>
<a class="service-link" href="/services/data-recovery.html">Data Recovery →</a>
</div>
</div>
</div>
</section>

<!-- Verified Local Customer Reviews -->
<section class="content-section" style="background: #f8fafc;">
<div class="section-title-wrap">
<span class="section-tag">{name} Customer Feedback</span>
<h2 class="section-heading">Verified Local Brisbane Reviews</h2>
<p class="section-sub">Real customers in {name} and neighboring suburbs.</p>
</div>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 24px; max-width: 1200px; margin: 0 auto;">
{reviews_html}
</div>
</section>

<!-- Suburb Specific FAQ -->
<section class="content-section">
<div class="section-title-wrap">
<span class="section-tag">Frequently Asked Questions</span>
<h2 class="section-heading">{name} Computer Repair FAQs</h2>
<p class="section-sub">Everything you need to know about our mobile call-out and workshop services.</p>
</div>
<div style="max-width: 860px; margin: 0 auto;">
{faqs_html}
</div>
</section>

</main>

<!-- Footer -->
<footer class="site-footer">
<div class="footer-container">
<div class="footer-col">
<h4>Computer Repairs Fast</h4>
<p>Brisbane's rapid mobile tech ambulance. Same-day on-site repairs and workshop drop-offs across {name} ({postcode}) and metro Brisbane.</p>
<p>📞 Phone: <a href="tel:0401148654" style="color: #fff; font-weight: 700;">0401 148 654</a><br/>
✉️ Email: info@computerrepairsfast.com.au</p>
</div>
<div class="footer-col">
<h4>Nearby Hubs &amp; Locations</h4>
<ul class="footer-links">
<li><a href="/locations/east-brisbane.html">East Brisbane Hub (4169)</a></li>
<li><a href="/locations/west-end.html">West End Hub (4101)</a></li>
<li><a href="/locations/toowong.html">Toowong Hub (4066)</a></li>
<li><a href="/locations/new-farm.html">New Farm Hub (4005)</a></li>
<li><a href="/locations/indooroopilly.html">Indooroopilly Hub (4068)</a></li>
</ul>
</div>
<div class="footer-col">
<h4>Key Repair Services</h4>
<ul class="footer-links">
<li><a href="/services/laptop-screen-repairs.html">Laptop Screen Replacement</a></li>
<li><a href="/services/scam-virus-removal.html">Scam &amp; Virus Cleanup</a></li>
<li><a href="/services/slow-computer-speed-up.html">Slow Computer SSD Upgrades</a></li>
<li><a href="/services/laptop-battery-replacement.html">Battery Replacement</a></li>
<li><a href="/services/data-recovery.html">Emergency Data Recovery</a></li>
</ul>
</div>
<div class="footer-col">
<h4>Company &amp; Legal</h4>
<ul class="footer-links">
<li><a href="/articles/">Guides & Blog</a></li>
<li><a href="/faq.html">FAQ Guide</a></li>
<li><a href="/contact.html">Contact Us</a></li>
<li><a href="/privacy.html">Privacy Policy</a></li>
<li><a href="/terms.html">Service Terms &amp; Warranty</a></li>
</ul>
</div>
</div>
<div class="footer-bottom">
<p>© 2026 Computer Repairs Fast. All Rights Reserved. ABN: 98 288 669 674. Fixed $80 Diagnostic • $0 Call-Out Fee across Brisbane.</p>
</div>
</footer>

<script src="/js/main.js"></script>
</body>
</html>
"""

# --- SERVICE TEMPLATE ---
def render_service_html(s):
    slug = s["slug"]
    title = s["title"]
    h1_main = s["h1_main"]
    h1_sub = s["h1_sub"]
    meta_desc = s["meta_desc"]
    icon = s["icon"]
    category = s["category"]
    price_from = s["price_from"]
    models = s["models"]
    
    # Common issues list
    issues_html = ""
    for issue in s["common_issues"]:
        issues_html += f"""
        <li style="margin-bottom: 10px; display: flex; align-items: flex-start; gap: 10px;">
          <span style="color: var(--red-600); font-weight: 800; font-size: 1.1rem;">✓</span>
          <span>{issue}</span>
        </li>
        """
        
    # Pricing table rows
    pricing_rows = ""
    for item, price, time in s["pricing_table"]:
        pricing_rows += f"""
        <tr style="border-bottom: 1px solid #e2e8f0;">
          <td style="padding: 14px 18px; font-weight: 600; color: #0f172a;">{item}</td>
          <td style="padding: 14px 18px; color: var(--red-600); font-weight: 700; font-size: 1.05rem;">{price}</td>
          <td style="padding: 14px 18px; color: #64748b;">{time}</td>
        </tr>
        """
        
    # FAQs
    faqs_html = ""
    faq_schema_list = []
    for q, a in s["faqs"]:
        faqs_html += f"""
        <div class="faq-item" style="background: #fff; border: 1px solid #e2e8f0; border-radius: 8px; margin-bottom: 12px; padding: 18px 24px;">
          <h3 style="margin-top: 0; color: #0f172a; font-size: 1.1rem; display: flex; align-items: center; gap: 8px;">
            <span style="color: var(--red-600); font-weight: 800;">Q.</span> {q}
          </h3>
          <p style="margin-bottom: 0; color: #475569; line-height: 1.6;">{a}</p>
        </div>
        """
        faq_schema_list.append({
            "@type": "Question",
            "name": q,
            "acceptedAnswer": {
                "@type": "Answer",
                "text": a
            }
        })
        
    faq_schema_json = json.dumps({
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": faq_schema_list
    }, indent=2)

    service_schema_json = json.dumps({
        "@context": "https://schema.org",
        "@type": "Service",
        "name": h1_main,
        "serviceType": slug.replace("-", " ").title(),
        "provider": {
            "@type": "LocalBusiness",
            "name": "Computer Repairs Fast",
            "telephone": "0401148654",
            "url": "https://computerrepairsfast.com.au/"
        },
        "description": meta_desc,
        "areaServed": {
            "@type": "City",
            "name": "Brisbane"
        },
        "offers": {
            "@type": "Offer",
            "price": price_from.replace("From $", ""),
            "priceCurrency": "AUD"
        }
    }, indent=2)

    breadcrumb_schema_json = json.dumps({
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {
                "@type": "ListItem",
                "position": 1,
                "name": "Home",
                "item": "https://computerrepairsfast.com.au/"
            },
            {
                "@type": "ListItem",
                "position": 2,
                "name": "Services",
                "item": "https://computerrepairsfast.com.au/services/"
            },
            {
                "@type": "ListItem",
                "position": 3,
                "name": h1_main,
                "item": f"https://computerrepairsfast.com.au/services/{slug}.html"
            }
        ]
    }, indent=2)

    return f"""<!DOCTYPE html>
<html lang="en-AU">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0, viewport-fit=cover" name="viewport"/>
<meta content="#dc2626" name="theme-color"/>
<title>{title}</title>
<meta content="{meta_desc}" name="description"/>
<link href="https://computerrepairsfast.com.au/services/{slug}.html" rel="canonical"/>

<!-- Open Graph & Social Meta -->
<meta content="{title}" property="og:title"/>
<meta content="{meta_desc}" property="og:description"/>
<meta content="https://computerrepairsfast.com.au/images/Fast-Computer-Repairs-East-Brisbane-4169.png" property="og:image"/>
<meta content="https://computerrepairsfast.com.au/services/{slug}.html" property="og:url"/>
<meta content="service" property="og:type"/>
<meta content="en_AU" property="og:locale"/>
<meta content="summary_large_image" name="twitter:card"/>
<meta content="{title}" name="twitter:title"/>
<meta content="{meta_desc}" name="twitter:description"/>

<!-- Favicon & Styles -->
<link href="/favicon.svg" rel="icon" type="image/svg+xml"/>
<link href="/favicon.png" rel="icon" sizes="32x32" type="image/png"/>
<link href="/apple-touch-icon.png" rel="apple-touch-icon" sizes="180x180"/>
<link href="/css/style.css?v=2.3" rel="stylesheet"/>

<!-- Schemas -->
<script type="application/ld+json">
{service_schema_json}
</script>
<script type="application/ld+json">
{faq_schema_json}
</script>
<script type="application/ld+json">
{breadcrumb_schema_json}
</script>
</head>
<body>

<!-- Announcement Bar -->
<div class="ambulance-bar">
<div class="ambulance-bar-inner">
<div>
<a href="/index.html" style="color: #fff; text-decoration: underline; margin-right: 10px;">← Main Home</a>
<span class="ambulance-badge"><span class="pulse-dot"></span> 🚑 Urgent {h1_main} Across Brisbane</span>
</div>
<div>
<span>$80 Diagnostic (Inside Repair Fee) • $0 Call-Out • Same-Day Repairs</span>
</div>
</div>
</div>

<!-- Header -->
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
<li class="nav-item"><a class="nav-link" href="/articles/">Guides & Blog</a></li>
<li class="nav-item"><a class="nav-link" href="/#pricing">Pricing</a></li>
<li class="nav-item"><a class="nav-link" href="/#locations">Locations</a></li>
<li class="nav-item"><a class="nav-link" href="/#how-it-works">How It Works</a></li>
<li class="nav-item"><a class="nav-link" href="/#reviews"><span style="color: #f59e0b; margin-right: 4px;">★</span>Reviews (112+)</a></li>
<li class="nav-item"><a class="nav-link" href="/contact.html">Contact</a></li>
</ul>
</nav>
<div class="header-contacts">
<div class="call-box">
<span class="call-sub">Speak to a technician</span>
<a class="call-tel dynamic-phone" href="tel:0401148654" title="Call Technician Now">📞 <span class="header-call-num">0401 148 654</span></a>
</div>
<a class="header-sms-pill" href="sms:0401148654?body=Hi%20Computer%20Repairs%20Fast,%20I%20need%20help%20with%20{slug}" title="Text Technician">💬 Text</a>
<a class="btn btn-emergency header-book-btn" href="#booking">Book Repair</a>
</div>
</div>
</header>
<main id="main-content">

<!-- Breadcrumbs -->
<div style="background: #f8fafc; border-bottom: 1px solid #e2e8f0; padding: 12px 0;">
  <div style="max-width: 1200px; margin: 0 auto; padding: 0 16px; font-size: 0.9rem; color: #64748b;">
    <a href="/" style="color: #64748b; text-decoration: none;">Home</a> &gt; 
    <a href="/services/" style="color: #64748b; text-decoration: none;">Services</a> &gt; 
    <span style="color: var(--red-600); font-weight: 700;">{h1_main}</span>
  </div>
</div>

<!-- Hero Section with Booking Form -->
<section class="hero-wrapper">
<div class="hero-box">
<div>
<div class="hero-pill-row">
<span class="red-pill">{icon} {category}</span>
<span class="red-pill">🏷️ {price_from}</span>
<span class="red-pill">🚗 Free Brisbane In-Home Visits</span>
</div>
<h1 class="hero-heading">{h1_main}<br/><span>{h1_sub}</span></h1>
<p class="hero-plain-text">
{meta_desc} Supporting <strong>{models}</strong> across all Brisbane suburbs. We come directly to your home or office with zero call-out fees, or you can drop your computer off at our local workshops in East Brisbane, West End, or Toowong.
</p>

<div class="hero-btn-row">
<a class="btn btn-emergency" href="tel:0401148654" style="font-size: 1.25rem;">
📞 Call Technician: <span class="dynamic-phone">0401 148 654</span>
</a>
<a class="btn btn-white" href="#booking">
📋 Instant On-Site Booking
</a>
</div>

<div class="guarantee-grid">
<div class="guarantee-item">
<div class="guarantee-icon">🩺</div>
<div class="guarantee-text">
<strong>Fixed $80 Diagnosis</strong>
<p>Isolate the exact component fault. Credited inside your repair quote.</p>
</div>
</div>
<div class="guarantee-item">
<div class="guarantee-icon">🚗</div>
<div class="guarantee-text">
<strong>No Call-Out Fee ($0)</strong>
<p>Free mobile travel anywhere in metro Brisbane.</p>
</div>
</div>
<div class="guarantee-item">
<div class="guarantee-icon">⚡</div>
<div class="guarantee-text">
<strong>Fast Turnaround</strong>
<p>Most hardware repairs and screens fitted in 1 to 3 hours.</p>
</div>
</div>
<div class="guarantee-item">
<div class="guarantee-icon">🛡️</div>
<div class="guarantee-text">
<strong>90-Day Warranty</strong>
<p>All parts and precision micro-soldering labor guaranteed.</p>
</div>
</div>
</div>
</div>

<!-- Booking Form -->
<div class="dispatch-card" id="booking">
<div class="dispatch-header">
<h2><span>{icon}</span> Book {h1_main}</h2>
<p>Mobile call-out or workshop drop-off today</p>
</div>
<div class="dispatch-price-badge">
<div class="badge-item-left">
<span class="badge-fee">$80 Fixed</span>
<span class="badge-desc">Full Diagnostic</span>
</div>
<div class="badge-item-right">
<span class="badge-pill">$0 Call-Out Fee</span>
</div>
</div>

<form action="/send-mail.php" class="ajax-booking-form" method="POST">
<div aria-hidden="true" style="position: absolute; left: -9999px; top: -9999px; height: 0; width: 0; opacity: 0; pointer-events: none;">
<input autocomplete="off" name="website_hp" tabindex="-1" type="text"/>
<input autocomplete="off" name="company_hp" tabindex="-1" type="text"/>
</div>
<input name="form_timestamp" type="hidden" value=""/>
<input name="source_page" type="hidden" value="{slug}.html"/>

<div class="form-row-2col">
<div class="form-group">
<label for="bookName">1. Name</label>
<input class="form-control" id="bookName" name="name" placeholder="Your Name" required="" type="text"/>
</div>
<div class="form-group">
<label for="bookPhone">2. Phone / Mobile</label>
<input class="form-control" id="bookPhone" name="phone" placeholder="0412 345 678" required="" type="tel"/>
</div>
</div>

<div class="form-row-2col">
<div class="form-group">
<label for="bookSuburb">3. Suburb</label>
<input class="form-control" id="bookSuburb" name="suburb" placeholder="e.g. Toowong, New Farm" required="" type="text"/>
</div>
<div class="form-group">
<label for="bookEmail">4. Email</label>
<input class="form-control" id="bookEmail" name="email" placeholder="email@example.com" required="" type="email"/>
</div>
</div>

<div class="form-group form-group-full">
<label for="bookProblem">5. Specific Problem / Hardware Model</label>
<input class="form-control" id="bookProblem" name="problem" placeholder="e.g. Smashed screen, battery swelling, won't turn on" required="" type="text"/>
</div>

<button class="btn btn-emergency" style="width: 100%; font-size: 1.15rem; padding: 14px;" type="submit">
Book Repair Technician
</button>
</form>

<div style="text-align: center; margin-top: 14px; font-size: 0.95rem; color: var(--gray-600);">
Urgent Emergency? Call: <a class="dynamic-phone" href="tel:0401148654" style="color: var(--red-600); font-weight: 800; text-decoration: underline;">0401 148 654</a>
</div>
</div>
</div>
</section>

<!-- Common Issues & Diagnostics -->
<section class="content-section">
<div class="section-title-wrap">
<span class="section-tag">Expert Diagnostics</span>
<h2 class="section-heading">Common {h1_main} We Fix Daily</h2>
<p class="section-sub">Tested and repaired by experienced hardware technicians in Brisbane.</p>
</div>
<div style="max-width: 860px; margin: 0 auto; background: #fff; padding: 28px 32px; border-radius: 12px; border: 1px solid #e2e8f0;">
  <ul style="list-style: none; padding: 0; margin: 0; font-size: 1.05rem; line-height: 1.7; color: #334155;">
    {issues_html}
  </ul>
</div>
</section>

<!-- Transparent Pricing Table -->
<section class="content-section" style="background: #f8fafc;">
<div class="section-title-wrap">
<span class="section-tag">Upfront Pricing</span>
<h2 class="section-heading">{h1_main} Price Matrix</h2>
<p class="section-sub">Honest rates with parts and labor included. No surprise invoices ever.</p>
</div>
<div style="max-width: 900px; margin: 0 auto; overflow-x: auto;">
  <table style="width: 100%; border-collapse: collapse; background: #fff; border: 1px solid #e2e8f0; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.03);">
    <thead>
      <tr style="background: #f1f5f9; text-align: left; border-bottom: 2px solid #e2e8f0;">
        <th style="padding: 14px 18px; color: #0f172a;">Service &amp; Repair Component</th>
        <th style="padding: 14px 18px; color: #0f172a;">Estimated Price Range</th>
        <th style="padding: 14px 18px; color: #0f172a;">Typical Turnaround</th>
      </tr>
    </thead>
    <tbody>
      {pricing_rows}
    </tbody>
  </table>
</div>
</section>

<!-- FAQs -->
<section class="content-section">
<div class="section-title-wrap">
<span class="section-tag">Frequently Asked Questions</span>
<h2 class="section-heading">{h1_main} FAQs</h2>
<p class="section-sub">Clear answers to your technical and repair questions.</p>
</div>
<div style="max-width: 860px; margin: 0 auto;">
{faqs_html}
</div>
</section>

</main>

<!-- Footer -->
<footer class="site-footer">
<div class="footer-container">
<div class="footer-col">
<h4>Computer Repairs Fast</h4>
<p>Brisbane's rapid mobile tech ambulance. Same-day on-site repairs and workshop drop-offs across metro Brisbane.</p>
<p>📞 Phone: <a href="tel:0401148654" style="color: #fff; font-weight: 700;">0401 148 654</a><br/>
✉️ Email: info@computerrepairsfast.com.au</p>
</div>
<div class="footer-col">
<h4>Workshop Locations</h4>
<ul class="footer-links">
<li><a href="/locations/east-brisbane.html">East Brisbane Hub (4169)</a></li>
<li><a href="/locations/west-end.html">West End Hub (4101)</a></li>
<li><a href="/locations/toowong.html">Toowong Hub (4066)</a></li>
<li><a href="/locations/new-farm.html">New Farm Hub (4005)</a></li>
<li><a href="/locations/indooroopilly.html">Indooroopilly Hub (4068)</a></li>
</ul>
</div>
<div class="footer-col">
<h4>Key Services</h4>
<ul class="footer-links">
<li><a href="/services/laptop-screen-repairs.html">Laptop Screen Replacement</a></li>
<li><a href="/services/scam-virus-removal.html">Scam &amp; Virus Cleanup</a></li>
<li><a href="/services/slow-computer-speed-up.html">Slow Computer SSD Upgrades</a></li>
<li><a href="/services/laptop-battery-replacement.html">Battery Replacement</a></li>
<li><a href="/services/data-recovery.html">Emergency Data Recovery</a></li>
</ul>
</div>
<div class="footer-col">
<h4>Company &amp; Legal</h4>
<ul class="footer-links">
<li><a href="/articles/">Guides & Blog</a></li>
<li><a href="/faq.html">FAQ Guide</a></li>
<li><a href="/contact.html">Contact Us</a></li>
<li><a href="/privacy.html">Privacy Policy</a></li>
<li><a href="/terms.html">Service Terms &amp; Warranty</a></li>
</ul>
</div>
</div>
<div class="footer-bottom">
<p>© 2026 Computer Repairs Fast. All Rights Reserved. ABN: 98 288 669 674. Fixed $80 Diagnostic • $0 Call-Out Fee across Brisbane.</p>
</div>
</footer>

<script src="/js/main.js"></script>
</body>
</html>
"""

# --- ARTICLE TEMPLATE ---
def render_article_html(a):
    slug = a["slug"]
    title = a["title"]
    h1 = a["h1"]
    meta_desc = a["meta_desc"]
    category = a["category"]
    reading_time = a["reading_time"]
    
    blocks_html = ""
    for b in a["content_blocks"]:
        if b["type"] == "snippet":
            blocks_html += f"""
            <div style="background: #f8fafc; border-left: 4px solid var(--red-600); padding: 20px 24px; border-radius: 8px; margin: 28px 0; box-shadow: 0 2px 8px rgba(0,0,0,0.03);">
              <h3 style="margin-top: 0; color: var(--red-600); font-size: 1.15rem;">{b['title']}</h3>
              <p style="margin-bottom: 0; font-size: 1.05rem; line-height: 1.6; color: #1e293b;">{b['text']}</p>
            </div>
            """
        elif b["type"] == "h2":
            blocks_html += f"""
            <h2 style="margin-top: 36px; color: #0f172a; font-size: 1.5rem; border-bottom: 2px solid #e2e8f0; padding-bottom: 8px;">{b['title']}</h2>
            <div style="font-size: 1.05rem; line-height: 1.7; color: #334155;">{b['text']}</div>
            """

    faqs_html = ""
    faq_schema_list = []
    for q, ans in a["faqs"]:
        faqs_html += f"""
        <div class="faq-item" style="background: #fff; border: 1px solid #e2e8f0; border-radius: 8px; margin-bottom: 12px; padding: 18px 24px;">
          <h3 style="margin-top: 0; color: #0f172a; font-size: 1.1rem; display: flex; align-items: center; gap: 8px;">
            <span style="color: var(--red-600); font-weight: 800;">Q.</span> {q}
          </h3>
          <p style="margin-bottom: 0; color: #475569; line-height: 1.6;">{ans}</p>
        </div>
        """
        faq_schema_list.append({
            "@type": "Question",
            "name": q,
            "acceptedAnswer": {
                "@type": "Answer",
                "text": ans
            }
        })
        
    faq_schema_json = json.dumps({
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": faq_schema_list
    }, indent=2)

    article_schema_json = json.dumps({
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": h1,
        "description": meta_desc,
        "author": {
            "@type": "Organization",
            "name": "Computer Repairs Fast",
            "url": "https://computerrepairsfast.com.au/"
        },
        "publisher": {
            "@type": "Organization",
            "name": "Computer Repairs Fast",
            "logo": {
                "@type": "ImageObject",
                "url": "https://computerrepairsfast.com.au/favicon.png"
            }
        },
        "datePublished": "2026-11-22",
        "dateModified": "2026-11-22"
    }, indent=2)

    breadcrumb_schema_json = json.dumps({
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {
                "@type": "ListItem",
                "position": 1,
                "name": "Home",
                "item": "https://computerrepairsfast.com.au/"
            },
            {
                "@type": "ListItem",
                "position": 2,
                "name": "Guides & Articles",
                "item": "https://computerrepairsfast.com.au/articles/"
            },
            {
                "@type": "ListItem",
                "position": 3,
                "name": h1,
                "item": f"https://computerrepairsfast.com.au/articles/{slug}.html"
            }
        ]
    }, indent=2)

    return f"""<!DOCTYPE html>
<html lang="en-AU">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0, viewport-fit=cover" name="viewport"/>
<meta content="#dc2626" name="theme-color"/>
<title>{title}</title>
<meta content="{meta_desc}" name="description"/>
<link href="https://computerrepairsfast.com.au/articles/{slug}.html" rel="canonical"/>

<!-- Open Graph & Social Meta -->
<meta content="{title}" property="og:title"/>
<meta content="{meta_desc}" property="og:description"/>
<meta content="https://computerrepairsfast.com.au/images/Fast-Computer-Repairs-East-Brisbane-4169.png" property="og:image"/>
<meta content="https://computerrepairsfast.com.au/articles/{slug}.html" property="og:url"/>
<meta content="article" property="og:type"/>
<meta content="en_AU" property="og:locale"/>
<meta content="summary_large_image" name="twitter:card"/>
<meta content="{title}" name="twitter:title"/>
<meta content="{meta_desc}" name="twitter:description"/>

<!-- Favicon & Styles -->
<link href="/favicon.svg" rel="icon" type="image/svg+xml"/>
<link href="/favicon.png" rel="icon" sizes="32x32" type="image/png"/>
<link href="/apple-touch-icon.png" rel="apple-touch-icon" sizes="180x180"/>
<link href="/css/style.css?v=2.3" rel="stylesheet"/>

<!-- Schemas -->
<script type="application/ld+json">
{article_schema_json}
</script>
<script type="application/ld+json">
{faq_schema_json}
</script>
<script type="application/ld+json">
{breadcrumb_schema_json}
</script>
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

<!-- Header -->
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
<li class="nav-item"><a class="nav-link" href="/articles/">Guides & Blog</a></li>
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
<a class="header-sms-pill" href="sms:0401148654?body=Hi%20Computer%20Repairs%20Fast,%20I%20have%20a%20question%20about%20{slug}" title="Text Technician">💬 Text</a>
<a class="btn btn-emergency header-book-btn" href="/#booking">Book Visit</a>
</div>
</div>
</header>
<main id="main-content">

<!-- Breadcrumbs -->
<div style="background: #f8fafc; border-bottom: 1px solid #e2e8f0; padding: 12px 0;">
  <div style="max-width: 900px; margin: 0 auto; padding: 0 16px; font-size: 0.9rem; color: #64748b;">
    <a href="/" style="color: #64748b; text-decoration: none;">Home</a> &gt; 
    <a href="/#how-it-works" style="color: #64748b; text-decoration: none;">Guides</a> &gt; 
    <span style="color: var(--red-600); font-weight: 700;">{category}</span>
  </div>
</div>

<article style="max-width: 900px; margin: 40px auto; padding: 0 20px;">
  <div style="margin-bottom: 24px;">
    <span class="red-pill">{category}</span>
    <span style="margin-left: 10px; color: #64748b; font-size: 0.95rem;">⏱️ {reading_time} • Published Nov 2026</span>
  </div>

  <h1 style="color: #0f172a; font-size: 2.2rem; line-height: 1.3; margin-bottom: 20px;">{h1}</h1>

  {blocks_html}

  <!-- In-Article Urgent CTA -->
  <div style="background: #fef2f2; border: 2px solid #fecaca; border-radius: 12px; padding: 28px; margin: 44px 0; text-align: center;">
    <h3 style="color: #b91c1c; margin-top: 0; font-size: 1.35rem;">Need Same-Day Computer Assistance in Brisbane?</h3>
    <p style="color: #4b5563; font-size: 1.05rem; margin-bottom: 20px;">
      Our mobile technician comes directly to your home or office with a <strong>fixed $80 diagnosis</strong> and <strong>$0 call-out fee</strong>.
    </p>
    <div style="display: flex; gap: 14px; justify-content: center; flex-wrap: wrap;">
      <a class="btn btn-emergency" href="tel:0401148654" style="font-size: 1.15rem;">📞 Call 0401 148 654</a>
      <a class="btn btn-white" href="/#booking" style="border: 1px solid #d1d5db;">📋 Book Mobile Visit</a>
    </div>
  </div>

  <!-- FAQs -->
  <section style="margin-top: 48px;">
    <h2 style="color: #0f172a; font-size: 1.5rem; border-bottom: 2px solid #e2e8f0; padding-bottom: 8px;">Frequently Asked Questions</h2>
    <div style="margin-top: 20px;">
      {faqs_html}
    </div>
  </section>
</article>

</main>

<!-- Footer -->
<footer class="site-footer">
<div class="footer-container">
<div class="footer-col">
<h4>Computer Repairs Fast</h4>
<p>Brisbane's rapid mobile tech ambulance. Same-day on-site repairs and workshop drop-offs across metro Brisbane.</p>
<p>📞 Phone: <a href="tel:0401148654" style="color: #fff; font-weight: 700;">0401 148 654</a><br/>
✉️ Email: info@computerrepairsfast.com.au</p>
</div>
<div class="footer-col">
<h4>Workshop Locations</h4>
<ul class="footer-links">
<li><a href="/locations/east-brisbane.html">East Brisbane Hub (4169)</a></li>
<li><a href="/locations/west-end.html">West End Hub (4101)</a></li>
<li><a href="/locations/toowong.html">Toowong Hub (4066)</a></li>
<li><a href="/locations/new-farm.html">New Farm Hub (4005)</a></li>
<li><a href="/locations/indooroopilly.html">Indooroopilly Hub (4068)</a></li>
</ul>
</div>
<div class="footer-col">
<h4>Key Services</h4>
<ul class="footer-links">
<li><a href="/services/laptop-screen-repairs.html">Laptop Screen Replacement</a></li>
<li><a href="/services/scam-virus-removal.html">Scam &amp; Virus Cleanup</a></li>
<li><a href="/services/slow-computer-speed-up.html">Slow Computer SSD Upgrades</a></li>
<li><a href="/services/laptop-battery-replacement.html">Battery Replacement</a></li>
<li><a href="/services/data-recovery.html">Emergency Data Recovery</a></li>
</ul>
</div>
<div class="footer-col">
<h4>Company &amp; Legal</h4>
<ul class="footer-links">
<li><a href="/articles/">Guides & Blog</a></li>
<li><a href="/faq.html">FAQ Guide</a></li>
<li><a href="/contact.html">Contact Us</a></li>
<li><a href="/privacy.html">Privacy Policy</a></li>
<li><a href="/terms.html">Service Terms &amp; Warranty</a></li>
</ul>
</div>
</div>
<div class="footer-bottom">
<p>© 2026 Computer Repairs Fast. All Rights Reserved. ABN: 98 288 669 674. Fixed $80 Diagnostic • $0 Call-Out Fee across Brisbane.</p>
</div>
</footer>

<script src="/js/main.js"></script>
</body>
</html>
"""

# --- BUILD EXECUTION ---

# 1. Suburbs
count_suburbs = 0
for s in SUBURBS:
    filepath = os.path.join(LOCATIONS_DIR, f"{s['slug']}.html")
    html_content = render_suburb_html(s)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html_content)
    count_suburbs += 1
print(f"Generated {count_suburbs} Suburb pages.")

# 2. Services
count_services = 0
for s in SERVICES:
    filepath = os.path.join(SERVICES_DIR, f"{s['slug']}.html")
    html_content = render_service_html(s)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html_content)
    count_services += 1
print(f"Generated {count_services} Service pages.")

# 3. Articles
count_articles = 0
for a in ARTICLES:
    filepath = os.path.join(ARTICLES_DIR, f"{a['slug']}.html")
    html_content = render_article_html(a)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html_content)
    count_articles += 1
print(f"Generated {count_articles} Article pages.")

# 4. Generate SITEMAP.XML
all_html_files = glob.glob(os.path.join(ROOT_DIR, "**", "*.html"), recursive=True)
valid_urls = []
now_str = datetime.now().strftime("%Y-%m-%d")

for f in all_html_files:
    rel = os.path.relpath(f, ROOT_DIR).replace("\\", "/")
    # Skip 404
    if rel == "404.html":
        continue
    if rel == "index.html":
        url = "https://computerrepairsfast.com.au/"
        priority = "1.0"
    elif rel.endswith("index.html"):
        url = f"https://computerrepairsfast.com.au/{rel[:-10]}"
        priority = "0.9"
    else:
        url = f"https://computerrepairsfast.com.au/{rel}"
        if rel.startswith("services/"):
            priority = "0.9"
        elif rel.startswith("locations/"):
            priority = "0.8"
        elif rel.startswith("articles/"):
            priority = "0.8"
        else:
            priority = "0.7"
    valid_urls.append((url, priority))

valid_urls.sort(key=lambda x: x[0])

sitemap_xml = ['<?xml version="1.0" encoding="UTF-8"?>',
               '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']

for url, pri in valid_urls:
    sitemap_xml.append('  <url>')
    sitemap_xml.append(f'    <loc>{url}</loc>')
    sitemap_xml.append(f'    <lastmod>{now_str}</lastmod>')
    sitemap_xml.append('    <changefreq>weekly</changefreq>')
    sitemap_xml.append(f'    <priority>{pri}</priority>')
    sitemap_xml.append('  </url>')

sitemap_xml.append('</urlset>')

sitemap_path = os.path.join(ROOT_DIR, "sitemap.xml")
with open(sitemap_path, "w", encoding="utf-8") as f:
    f.write("\n".join(sitemap_xml))

print(f"Generated sitemap.xml with {len(valid_urls)} verified indexable URLs.")
