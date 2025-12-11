import urllib.request
import re

url = 'https://www.aozora.gr.jp/cards/000081/files/456_15050.html'
response = urllib.request.urlopen(url)
content = response.read().decode('shift_jis')

queries = [
    "石炭袋",
    "涙がこぼれる",
    "実験でちゃんと"
]

for q in queries:
    print(f"--- Search: {q} ---")
    idx = content.find(q)
    if idx > 0:
        start = max(0, idx - 500)
        end = min(len(content), idx + 800)
        text = content[start:end]
        text = re.sub(r'<[^>]+>', '', text)
        print(text)
    else:
        print("Not found")
    print("\n")
