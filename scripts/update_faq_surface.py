import os
import json
import re

ROOT_DIR = r"C:\Users\PC\.gemini\antigravity-ide\scratch\computer-repairs-fast"
faq_path = os.path.join(ROOT_DIR, "faq.html")

with open(faq_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Add schema question if not present
schema_entry = {
    "@type": "Question",
    "name": "Do you repair Microsoft Surface Pro tablets or Surface laptops?",
    "acceptedAnswer": {
        "@type": "Answer",
        "text": "No, we strictly do not perform hardware repairs on Microsoft Surface Pro or Surface Laptop devices due to their non-repairable glued unibody construction and ultra-thin glass. We recommend contacting Microsoft Support for whole-unit replacement. However, we do offer emergency data recovery if your Surface has stopped working and you need your files back."
    }
}

surface_faq_card = """<div class="faq-card" style="border: 2px solid #fecaca; background: #fff5f5; border-radius: 8px;">
<button aria-expanded="false" class="faq-q" style="color: #b91c1c;">
<span>⚠️ Do you repair Microsoft Surface Pro tablets or Surface laptops?</span>
<span class="faq-toggle-icon">+</span>
</button>
<div class="faq-a" style="display: none;">
<p><strong>No, we strictly do not perform hardware repairs on Microsoft Surface devices</strong> (including Surface Pro, Surface Laptop, and Surface Book screens, swollen batteries, or logic boards). Microsoft manufactures Surface hardware with non-modular, heavily glued unibody enclosures and fused 0.4mm glass. These cannot be opened without an unacceptable risk of cosmetic casing deformation and screen fractures, and genuine replacement parts are not sold by Microsoft. We advise contacting official Microsoft Support directly for whole-unit replacement. <em>(Note: We CAN provide emergency data recovery if your Surface has died and essential files are needed).</em></p>
</div>
</div>"""

if "Do you repair Microsoft Surface Pro" not in content:
    target_needle = 'Can you replace cracked Apple MacBook Retina display screens?</span>\n<span class="faq-toggle-icon">+</span>\n</button>\n<div class="faq-a" style="display: none;">\n<p>Yes. We replace full upper Retina display lid assemblies for MacBook Air and MacBook Pro (M1, M2, M3 and Intel models). Pricing generally ranges from $290 to $550+ depending on the screen size and model generation.</p>\n</div>\n</div>'
    
    if target_needle in content:
        content = content.replace(target_needle, target_needle + "\n" + surface_faq_card)
        print("Inserted Surface FAQ card into HTML.")
    else:
        print("Needle not found, looking for alternative insertion point...")
        content = content.replace('<div class="faq-box">', '<div class="faq-box">\n' + surface_faq_card, 1)
        print("Inserted at first faq-box.")

    with open(faq_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("faq.html updated.")
else:
    print("Surface FAQ already present in faq.html")
