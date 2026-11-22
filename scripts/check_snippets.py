from data_articles import ARTICLES
import re

for i, art in enumerate(ARTICLES):
    snippet = ""
    for b in art.get("content_blocks", []):
        if b.get("type") == "snippet":
            clean_text = b.get("text", "").replace("<strong>", "").replace("</strong>", "")
            if len(clean_text) > 175:
                clean_text = clean_text[:172] + "..."
            snippet = clean_text
            break
    if not snippet:
        snippet = art.get("meta_desc", "")
        if len(snippet) > 175:
            snippet = snippet[:172] + "..."

    if '<' in snippet:
        print(f"Card {i} ({art['slug']}) has '<' in snippet: {snippet}")
print("Done checking all snippets.")
