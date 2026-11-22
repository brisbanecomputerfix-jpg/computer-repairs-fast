import os
import re

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_SERVICES_PATH = os.path.join(ROOT_DIR, "scripts", "data_services.py")
DATA_SUBURBS_PATH = os.path.join(ROOT_DIR, "scripts", "data_suburbs.py")
DATA_ARTICLES_PATH = os.path.join(ROOT_DIR, "scripts", "data_articles.py")
FAQ_PATH = os.path.join(ROOT_DIR, "faq.html")

print("Removing Microsoft Surface repair offerings...")

# 1. Update data_services.py: Remove surface-pro-laptop-repairs dictionary
with open(DATA_SERVICES_PATH, "r", encoding="utf-8") as f:
    services_text = f.read()

# Pattern matching the entire surface-pro dict
pattern = re.compile(r'\{\s*"slug":\s*"surface-pro-laptop-repairs".*?\}\s*,\s*', re.DOTALL)
services_text = pattern.sub('', services_text)

with open(DATA_SERVICES_PATH, "w", encoding="utf-8") as f:
    f.write(services_text)
print("data_services.py updated.")

# 2. Update data_suburbs.py:
# - Remove "Microsoft Surface" from Coorparoo brand list
# - Update Newstead FAQ to state we DO NOT repair Surface
with open(DATA_SUBURBS_PATH, "r", encoding="utf-8") as f:
    suburbs_text = f.read()

suburbs_text = suburbs_text.replace(
    'Microsoft Surface, and custom gaming towers.',
    'and custom gaming towers.'
)

suburbs_text = suburbs_text.replace(
    '("Can you repair Microsoft Surface Pro laptops in Newstead?", "Yes, we repair Surface Pro screen cracks, swollen batteries, and charging ports.")',
    '("Do you repair Microsoft Surface Pro laptops in Newstead?", "No, we strictly do not perform hardware repairs on Microsoft Surface devices due to their non-repairable glued construction and high risk of screen breakage. We recommend contacting Microsoft directly for replacement. However, we repair all Dell, HP, Lenovo, ASUS, Acer, MSI, and Apple laptops!")'
)

with open(DATA_SUBURBS_PATH, "w", encoding="utf-8") as f:
    f.write(suburbs_text)
print("data_suburbs.py updated.")

# 3. Update data_articles.py:
with open(DATA_ARTICLES_PATH, "r", encoding="utf-8") as f:
    articles_text = f.read()

articles_text = articles_text.replace(
    'Dell 2-in-1, Surface Pro',
    'Dell 2-in-1, ASUS Flip'
)

with open(DATA_ARTICLES_PATH, "w", encoding="utf-8") as f:
    f.write(articles_text)
print("data_articles.py updated.")

# 4. Add Surface Advisory to faq.html
with open(FAQ_PATH, "r", encoding="utf-8") as f:
    faq_text = f.read()

surface_faq_html = """
        <div class="faq-item" style="background: #fff; border: 2px solid #fecaca; border-radius: 8px; margin-bottom: 16px; padding: 20px 24px;">
          <h3 style="margin-top: 0; color: #b91c1c; font-size: 1.15rem; display: flex; align-items: center; gap: 8px;">
            <span>🚫</span> Do you repair Microsoft Surface Pro tablets or Surface laptops?
          </h3>
          <p style="margin-bottom: 8px; color: #1e293b; line-height: 1.6; font-size: 1.05rem;">
            <strong>No, we do not perform hardware repairs on Microsoft Surface devices</strong> (screens, batteries, or logic boards).
          </p>
          <p style="margin-bottom: 0; color: #475569; line-height: 1.6;">
            Microsoft manufactures Surface Pro, Surface Laptop, and Surface Book hardware with non-modular, heavily glued unibody enclosures and fused 0.4mm glass. These cannot be safely serviced without an unacceptable risk of cosmetic casing deformation and screen fractures. Even Microsoft authorized centers replace whole units rather than repairing them. If your Surface has hardware issues, we recommend contacting official Microsoft Support. <em>(Note: We CAN assist with emergency data recovery if your Surface has died and files are needed).</em>
          </p>
        </div>
"""

if "Do you repair Microsoft Surface Pro tablets" not in faq_text:
    faq_text = faq_text.replace(
        '<div class="faq-accordion">',
        '<div class="faq-accordion">\n' + surface_faq_html
    )
    with open(FAQ_PATH, "w", encoding="utf-8") as f:
        f.write(faq_text)
    print("faq.html updated with Microsoft Surface non-repair notice.")
