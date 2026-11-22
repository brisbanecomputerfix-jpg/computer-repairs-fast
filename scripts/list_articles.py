import sys
sys.path.append('scripts')
from data_articles import ARTICLES

for i, a in enumerate(ARTICLES):
    cat = a.get('category', 'Hardware')
    slug = a.get('slug', '')
    title = a.get('h1', '')
    print(f"{i+1:2d}. [{cat}] {slug} -> {title[:40]}")
