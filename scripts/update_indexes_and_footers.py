import os
import re
from data_suburbs import SUBURBS
from data_services import SERVICES
from data_articles import ARTICLES

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SERVICES_INDEX = os.path.join(ROOT_DIR, "services", "index.html")
HOME_INDEX = os.path.join(ROOT_DIR, "index.html")

print("Updating index hubs and footers with expanded services & articles...")

# 1. GENERATE BRAND & PROBLEM CARDS FOR services/index.html
brand_cards_html = ""
problem_cards_html = ""
brand_count = 0
problem_count = 0

for s in SERVICES:
    slug = s["slug"]
    h1_main = s["h1_main"]
    meta_desc = s["meta_desc"]
    icon = s.get("icon", "💻")
    price_from = s["price_from"]
    category = s["category"]

    card_html = f"""
    <article class="service-card" style="background: #fff; padding: 24px; border-radius: 12px; border: 1px solid #e2e8f0; display: flex; flex-direction: column; justify-content: space-between; transition: transform 0.2s, box-shadow 0.2s;">
      <div>
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px;">
          <div style="font-size: 2rem;">{icon}</div>
          <span style="background: #fef2f2; color: #b91c1c; font-size: 0.8rem; font-weight: 700; padding: 4px 10px; border-radius: 999px;">{price_from}</span>
        </div>
        <h3 style="margin-top: 0; font-size: 1.25rem; color: #0f172a; margin-bottom: 8px;">
          <a href="/services/{slug}.html" style="color: inherit; text-decoration: none;">{h1_main}</a>
        </h3>
        <p style="color: #64748b; font-size: 0.95rem; line-height: 1.5; margin-bottom: 16px;">
          {meta_desc[:125]}...
        </p>
      </div>
      <div>
        <a href="/services/{slug}.html" class="btn btn-emergency" style="display: block; text-align: center; text-decoration: none; padding: 10px; font-size: 0.95rem;">
          View Service Details →
        </a>
      </div>
    </article>
    """

    if category == "Brand Specialist":
        brand_cards_html += card_html
        brand_count += 1
    else:
        problem_cards_html += card_html
        problem_count += 1

insert_block = f"""<!-- Brand Specialists Grid -->
<section class="content-section" style="padding-top: 40px; padding-bottom: 40px; background: #f8fafc;">
  <div class="section-title-wrap">
    <span class="section-tag">Brand Hardware Specialists</span>
    <h2 class="section-heading">{brand_count} Brand-Specific Laptop & Desktop Repair Services</h2>
    <p class="section-subtext">Certified component-level repair for every major laptop and gaming PC manufacturer in Australia.</p>
  </div>
  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 24px; max-width: 1200px; margin: 0 auto; padding: 0 16px;">
    {brand_cards_html}
  </div>
</section>

<!-- Emergency Problems Grid -->
<section class="content-section" style="padding-top: 40px; padding-bottom: 40px;">
  <div class="section-title-wrap">
    <span class="section-tag">Specialized & Emergency Computer Services</span>
    <h2 class="section-heading">{problem_count} Specialized Problem Services We Fix On-Site</h2>
    <p class="section-subtext">From dead PCs and broken hinges to printer Wi-Fi setups, email migrations, and senior tech lessons.</p>
  </div>
  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 24px; max-width: 1200px; margin: 0 auto; padding: 0 16px;">
    {problem_cards_html}
  </div>
</section>
<!-- End Service Grids -->"""

with open(SERVICES_INDEX, "r", encoding="utf-8") as f:
    services_content = f.read()

if "<!-- Brand Specialists Grid -->" in services_content:
    pattern = re.compile(r'<!-- Brand Specialists Grid -->.*?<!-- End Service Grids -->', re.DOTALL)
    if pattern.search(services_content):
        services_content = pattern.sub(insert_block, services_content)
    else:
        # Fallback regex up to pricing comparison
        pattern2 = re.compile(r'<!-- Brand Specialists Grid -->.*?(?=<section class="content-section" id="pricing-comparison")', re.DOTALL)
        services_content = pattern2.sub(insert_block + "\n", services_content)
else:
    services_content = services_content.replace(
        '<section class="content-section" id="pricing-comparison"',
        insert_block + '\n<section class="content-section" id="pricing-comparison"'
    )

with open(SERVICES_INDEX, "w", encoding="utf-8") as f:
    f.write(services_content)
print(f"Updated services/index.html with {brand_count} brands and {problem_count} specialized services.")

# 2. GENERATE SUBURBS DIRECTORY GRID FOR index.html
suburb_links_html = ""
for s in SUBURBS:
    suburb_links_html += f"""
    <a href="/locations/{s['slug']}.html" style="background: #fff; padding: 12px 16px; border-radius: 8px; border: 1px solid #e2e8f0; text-decoration: none; color: #1e293b; font-size: 0.95rem; display: flex; justify-content: space-between; align-items: center; transition: all 0.2s ease;">
      <span><strong>{s['name']}</strong> <span style="color: #64748b; font-size: 0.85rem;">({s['postcode']})</span></span>
      <span style="color: var(--red-600); font-weight: 700;">$0 Call-Out →</span>
    </a>
    """

# Articles Showcase
articles_cards_html = ""
for a in ARTICLES[:12]:
    articles_cards_html += f"""
    <div style="background: #fff; padding: 20px; border-radius: 10px; border: 1px solid #e2e8f0;">
      <span style="background: #fef2f2; color: #b91c1c; font-size: 0.75rem; font-weight: 700; padding: 3px 8px; border-radius: 999px;">{a['category']}</span>
      <h4 style="margin: 10px 0 6px; font-size: 1.1rem; color: #0f172a;">
        <a href="/articles/{a['slug']}.html" style="color: inherit; text-decoration: none;">{a['h1'][:65]}...</a>
      </h4>
      <p style="color: #64748b; font-size: 0.9rem; margin-bottom: 12px;">{a['meta_desc'][:100]}...</p>
      <a href="/articles/{a['slug']}.html" style="color: var(--red-600); font-weight: 700; font-size: 0.9rem; text-decoration: none;">Read Guide →</a>
    </div>
    """

with open(HOME_INDEX, "r", encoding="utf-8") as f:
    home_content = f.read()

suburbs_section_html = f"""<!-- 41 Brisbane Suburbs Mobile Coverage Directory -->
<section class="content-section" id="all-suburbs" style="background: #f8fafc; padding: 60px 0;">
  <div class="section-title-wrap">
    <span class="section-tag">Brisbane-Wide Mobile Coverage</span>
    <h2 class="section-heading">41 Dedicated Suburb Hubs Across Greater Brisbane</h2>
    <p class="section-subtext">Click on your suburb to view local in-home mobile dispatch times, workshop drop-off options, and verified local reviews with $0 call-out fees.</p>
  </div>
  <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(230px, 1fr)); gap: 14px; max-width: 1200px; margin: 0 auto; padding: 0 16px;">
    <a href="/locations/east-brisbane.html" style="background: #fef2f2; padding: 12px 16px; border-radius: 8px; border: 1px solid #fca5a5; text-decoration: none; color: #b91c1c; font-weight: 700;">📍 East Brisbane Hub (4169)</a>
    <a href="/locations/west-end.html" style="background: #fef2f2; padding: 12px 16px; border-radius: 8px; border: 1px solid #fca5a5; text-decoration: none; color: #b91c1c; font-weight: 700;">📍 West End Hub (4101)</a>
    <a href="/locations/toowong.html" style="background: #fef2f2; padding: 12px 16px; border-radius: 8px; border: 1px solid #fca5a5; text-decoration: none; color: #b91c1c; font-weight: 700;">📍 Toowong Hub (4066)</a>
    <a href="/locations/new-farm.html" style="background: #fef2f2; padding: 12px 16px; border-radius: 8px; border: 1px solid #fca5a5; text-decoration: none; color: #b91c1c; font-weight: 700;">📍 New Farm Hub (4005)</a>
    <a href="/locations/indooroopilly.html" style="background: #fef2f2; padding: 12px 16px; border-radius: 8px; border: 1px solid #fca5a5; text-decoration: none; color: #b91c1c; font-weight: 700;">📍 Indooroopilly Hub (4068)</a>
    {suburb_links_html}
  </div>
</section>

<!-- Guides & Advice Showcase -->
<section class="content-section" id="featured-guides" style="padding: 60px 0;">
  <div class="section-title-wrap">
    <span class="section-tag">Guides & Problem Solving</span>
    <h2 class="section-heading">Featured Brisbane Computer Hardware Guides</h2>
    <p class="section-subtext">Real repair cost breakdowns, emergency scam relief, and hardware diagnosis from our Brisbane workshop team.</p>
  </div>
  <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 20px; max-width: 1200px; margin: 0 auto; padding: 0 16px;">
    {articles_cards_html}
  </div>
  <div style="text-align: center; margin-top: 32px;">
    <a href="/articles/" class="btn btn-emergency" style="font-size: 1.05rem; padding: 12px 28px;">View All {len(ARTICLES)} Knowledge Base Guides →</a>
  </div>
</section>
<!-- End Suburbs & Guides Section -->"""

if "<!-- 41 Brisbane Suburbs Mobile Coverage Directory -->" in home_content:
    pattern = re.compile(r'<!-- 41 Brisbane Suburbs Mobile Coverage Directory -->.*?<!-- End Suburbs & Guides Section -->', re.DOTALL)
    if pattern.search(home_content):
        home_content = pattern.sub(suburbs_section_html, home_content)
    else:
        pattern2 = re.compile(r'<!-- 41 Brisbane Suburbs Mobile Coverage Directory -->.*?(?=<section class="cta-section")', re.DOTALL)
        home_content = pattern2.sub(suburbs_section_html + "\n", home_content)
else:
    home_content = home_content.replace(
        '<section class="cta-section"',
        suburbs_section_html + '\n<section class="cta-section"'
    )

with open(HOME_INDEX, "w", encoding="utf-8") as f:
    f.write(home_content)

print(f"Updated index.html with 41 Suburbs and {len(ARTICLES)} Article Guides showcase.")
