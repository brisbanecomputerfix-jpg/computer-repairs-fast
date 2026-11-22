import re
import os

BASE_DIR = r"C:\Users\PC\.gemini\antigravity-ide\scratch\computer-repairs-fast"

def clean_file(rel_path):
    filepath = os.path.join(BASE_DIR, rel_path)
    if not os.path.exists(filepath):
        print(f"Skipping {rel_path} (not found)")
        return
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # 1. Schema.org streetAddress lines
    content = re.sub(r'\s*"streetAddress":\s*"[^"]*",?\n', '\n', content)

    # 2. Footers in hub / blog
    content = content.replace("📍 33 Fisher St, East Brisbane QLD 4169<br/>", "📍 East Brisbane Hub QLD 4169 (By appointment)<br/>")
    content = content.replace("📍 36 Gray St, West End QLD 4101<br/>", "📍 West End Hub QLD 4101 (By appointment)<br/>")

    # 3. Address in workshop cards
    content = content.replace("<strong>Address:</strong> 33 Fisher St, East Brisbane QLD 4169<br/>",
                              "<strong>Service Hub:</strong> East Brisbane QLD 4169 (Workshop drop-off by appointment &amp; mobile dispatch)<br/>")
    content = content.replace("<strong>Address:</strong> 36 Gray St, West End QLD 4101<br/>",
                              "<strong>Service Hub:</strong> West End QLD 4101 (Workshop drop-off by appointment &amp; mobile dispatch)<br/>")

    # 4. In services/index.html FAQ
    content = content.replace("in East Brisbane (33 Fisher St) and West End (36 Gray St)",
                              "in East Brisbane and West End (by appointment)")

    # 5. Review in services/laptop-screen-repairs.html
    content = content.replace("Dropped it at the East Brisbane workshop on Fisher St.",
                              "Dropped it at the East Brisbane workshop.")

    # Generic catch in case of any remaining variations
    content = content.replace("33 Fisher St, East Brisbane QLD 4169", "East Brisbane QLD 4169 (Drop-off by appointment)")
    content = content.replace("36 Gray St, West End QLD 4101", "West End QLD 4101 (Drop-off by appointment)")
    content = content.replace("33 Fisher St", "East Brisbane")
    content = content.replace("36 Gray St", "West End")

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {rel_path}")
    else:
        print(f"No changes in {rel_path}")

target_files = [
    r"scripts\build_articles_hub.py",
    r"articles\index.html",
    r"blog\index.html",
    r"services\data-recovery.html",
    r"services\dell-laptop-repairs.html",
    r"services\gaming-pc-repairs.html",
    r"services\index.html",
    r"services\laptop-screen-repairs.html",
]

for tf in target_files:
    clean_file(tf)

print("\nRebuilding articles hub to ensure generated files are aligned...")
os.system(f'python "{os.path.join(BASE_DIR, "scripts", "build_articles_hub.py")}"')
