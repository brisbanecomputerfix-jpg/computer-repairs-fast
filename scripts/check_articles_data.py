from data_articles import ARTICLES

for i in range(len(ARTICLES)):
    a = ARTICLES[i]
    for b in a.get('content_blocks', []):
        t = b.get('text', '')
        if '<div' in t or '</div' in t or '<article' in t:
            print(f'Article {i} ({a["slug"]}) has HTML TAG: {t[:100]}')
    m = a.get('meta_desc', '')
    if '<div' in m or '</div' in m or '<article' in m:
        print(f'Article {i} meta_desc has HTML: {m}')

print('Done scanning all 48 articles.')
