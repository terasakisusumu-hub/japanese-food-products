import urllib.request
import re

url = 'https://www.aozora.gr.jp/cards/000081/files/456_15050.html'
response = urllib.request.urlopen(url)
content = response.read().decode('shift_jis')

# 栗鼠を検索
matches = list(re.finditer(r'栗鼠|りす', content, re.IGNORECASE))
print(f'Found {len(matches)} matches')

for i, m in enumerate(matches[:5]):
    start = max(0, m.start() - 500)
    end = min(len(content), m.end() + 1000)
    text = content[start:end]
    text = re.sub(r'<[^>]+>', '', text)
    print(f'\n--- Match {i+1} ---')
    print(text[:2000])
