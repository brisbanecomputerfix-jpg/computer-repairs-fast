import glob
import os
import re
from bs4 import BeautifulSoup

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 1. Update build_all_pages.py template string
build_path = os.path.join(ROOT_DIR, "scripts", "build_all_pages.py")
with open(build_path, "r", encoding="utf-8") as f:
    b = f.read()

old_desc = 'Local same-day computer repairs in {name} QLD {postcode}. Laptop screen replacement, scam virus cleanup, slow PC speedups & data recovery. Fixed $80 diagnostic, $0 call-out fee. Call 0401 148 654.'
new_desc = 'Fast computer repairs in {name} QLD {postcode}. Laptop screens, scam cleanup & SSD speed-ups. Fixed $80 diagnosis, $0 call-out fee. Call 0401 148 654.'

b = b.replace(old_desc, new_desc)
with open(build_path, "w", encoding="utf-8") as f:
    f.write(b)

# 2. Re-run build_all_pages.py
import subprocess
subprocess.run([os.sys.executable, os.path.join(ROOT_DIR, "scripts", "build_all_pages.py")], cwd=os.path.join(ROOT_DIR, "scripts"))

# 3. Trim any remaining descriptions > 160
files = glob.glob(os.path.join(ROOT_DIR, "**", "*.html"), recursive=True)
trimmed = 0

for f in files:
    content = open(f, encoding="utf-8", errors="ignore").read()
    soup = BeautifulSoup(content, "html.parser")
    desc_tag = soup.find("meta", {"name": "description"})
    if desc_tag and desc_tag.get("content") and len(desc_tag["content"]) > 160:
        d = desc_tag["content"]
        short_d = d[:155].rsplit(" ", 1)[0]
        if not short_d.endswith("."):
            short_d += "."
        
        # Replace meta description tag safely
        pattern = re.compile(r'<meta\s+content="[^"]*"\s+name="description"/?>', re.IGNORECASE)
        pattern2 = re.compile(r'<meta\s+name="description"\s+content="[^"]*"/?>', re.IGNORECASE)
        
        replacement = f'<meta content="{short_d}" name="description"/>'
        new_c = pattern.sub(replacement, content)
        if new_c == content:
            new_c = pattern2.sub(replacement, content)
            
        with open(f, "w", encoding="utf-8") as out:
            out.write(new_c)
        trimmed += 1

print(f"Trimmed descriptions in {trimmed} files.")
