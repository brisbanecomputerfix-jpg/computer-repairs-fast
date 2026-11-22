with open('articles/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
grid_start = text.find('id="articlesGrid"')
grid_end = text.find('<!-- Urgent Emergency CTA -->')
grid_html = text[grid_start:grid_end]

cards = re.findall(r'<article class="article-hub-card"[\s\S]*?</article>', grid_html)
print(f'Cards matched in grid: {len(cards)}')

for i, c in enumerate(cards):
    opens = len(re.findall(r'<div\b', c))
    closes = len(re.findall(r'</div>', c))
    p_opens = len(re.findall(r'<p\b', c))
    p_closes = len(re.findall(r'</p>', c))
    if opens != closes:
        print(f'Card {i} has unclosed div! opens: {opens}, closes: {closes}')
    if p_opens != p_closes:
        print(f'Card {i} has unclosed p! opens: {p_opens}, closes: {p_closes}')

print('Done checking tag matching in all cards.')
