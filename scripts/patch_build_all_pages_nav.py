import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BUILD_SCRIPT = os.path.join(SCRIPT_DIR, "build_all_pages.py")

with open(BUILD_SCRIPT, "r", encoding="utf-8") as f:
    code = f.read()

# Replace in nav lists
target_nav = '<li class="nav-item"><a class="nav-link" href="/services/">Services</a></li>'
new_nav = '<li class="nav-item"><a class="nav-link" href="/services/">Services</a></li>\n<li class="nav-item"><a class="nav-link" href="/articles/">Guides & Blog</a></li>'

code = code.replace(target_nav, new_nav)

# Replace in footers
target_footer = '<li><a href="/faq.html">FAQ Guide</a></li>'
new_footer = '<li><a href="/articles/">Guides & Blog</a></li>\n<li><a href="/faq.html">FAQ Guide</a></li>'

code = code.replace(target_footer, new_footer)

with open(BUILD_SCRIPT, "w", encoding="utf-8") as f:
    f.write(code)

print("build_all_pages.py patched with Guides & Blog navigation links.")
