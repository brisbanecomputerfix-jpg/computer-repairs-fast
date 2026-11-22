import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX_PATH = os.path.join(ROOT_DIR, "index.html")

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    code = f.read()

target = '<!-- Google Reviews Link -->'
insert_nav = '''<!-- Guides & Blog Link -->
<li class="nav-item">
<a class="nav-link" href="/articles/">Guides & Blog</a>
</li>
'''

if 'href="/articles/">Guides & Blog</a>' not in code:
    code = code.replace(target, insert_nav + target)
    print("Added Guides & Blog nav link to index.html.")

# Footer link
target_footer = '<li><a href="/faq.html">FAQ Guide</a></li>'
insert_footer = '<li><a href="/articles/">Guides & Blog</a></li>\n<li><a href="/faq.html">FAQ Guide</a></li>'
if '<li><a href="/articles/">Guides & Blog</a></li>' not in code:
    code = code.replace(target_footer, insert_footer)
    print("Added Guides & Blog footer link to index.html.")

with open(INDEX_PATH, "w", encoding="utf-8") as f:
    f.write(code)
