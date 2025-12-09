import urllib.request
import re

url = 'https://www.aozora.gr.jp/cards/000081/files/456_15050.html'
response = urllib.request.urlopen(url)
content = response.read().decode('shift_jis')

# 電気栗鼠を検索
idx = content.find('電気')
if idx > 0:
    # 電気の周辺を確認
    start = max(0, idx - 1000)
    end = min(len(content), idx + 3000)
    text = content[start:end]
    
    # 電気栗鼠の部分を探す
    match = re.search(r'電気.*?栗鼠.*?。', text, re.DOTALL)
    if match:
        context = content[max(0, idx - 2000):min(len(content), idx + 4000)]
        context = re.sub(r'<[^>]+>', '', context)
        print(context)
    else:
        # 電気の周辺を表示
        text = re.sub(r'<[^>]+>', '', text)
        print(text)
