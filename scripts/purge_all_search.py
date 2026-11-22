"""
Purge all search subbar markup from EVERY html file in the project.
"""

import os
import re

ROOT_DIR = r"C:\Users\PC\.gemini\antigravity-ide\scratch\computer-repairs-fast"

# Pattern matches any variant of the subbar search
pattern = re.compile(
    r'\s*<!--\s*Sub-Bar Search Strip[\s\S]*?</div>\s*</div>\s*</div>\s*',
    re.MULTILINE
)
pattern_bare = re.compile(
    r'\s*<div class="site-subbar-search"[\s\S]*?</div>\s*</div>\s*</div>\s*',
    re.MULTILINE
)

count = 0
for root, dirs, files in os.walk(ROOT_DIR):
    if '.git' in dirs: dirs.remove('.git')
    for file in files:
        if file.endswith('.html'):
            p = os.path.join(root, file)
            with open(p, 'r', encoding='utf-8') as f:
                content = f.read()
            if 'site-subbar-search' in content or 'siteSubbarSearch' in content:
                new_c = pattern.sub('\n', content)
                new_c = pattern_bare.sub('\n', new_c)
                if new_c != content:
                    with open(p, 'w', encoding='utf-8') as f:
                        f.write(new_c)
                    count += 1
                    print(f"Purged search bar from: {os.path.relpath(p, ROOT_DIR)}")

# Delete obsolete patch scripts
for obsolete in ["apply_search_to_all_html.py", "patch_search_subbar.py"]:
    obs_p = os.path.join(ROOT_DIR, "scripts", obsolete)
    if os.path.exists(obs_p):
        os.remove(obs_p)
        print(f"Deleted obsolete script: {obsolete}")

print(f"Total HTML files cleaned: {count}")
