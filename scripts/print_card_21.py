with open('articles/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
cards = re.findall(r'<article class="article-hub-card"[\s\S]*?</article>', text)
print(f"Total cards: {len(cards)}")
print("=== CARD 21 (0-indexed 21) ===")
print(cards[21])
print("=== CARD 22 ===")
print(cards[22])
print("=== CARD 23 ===")
print(cards[23])
