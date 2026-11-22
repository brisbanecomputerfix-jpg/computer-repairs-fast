with open('articles/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('id="articlesGrid"')
print(text[idx:idx+1200])
