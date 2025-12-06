#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess
import json
import sys

# 検索クエリ
query = "竹田恒泰 吉田松陰"

# yt-dlpで検索してJSON形式で取得
cmd = [
    "/home/ubuntu/.local/bin/yt-dlp",
    "--flat-playlist",
    "--print", "%(title)s\n%(url)s\n%(channel)s\n%(duration)s\n",
    "ytsearch20:" + query
]

try:
    result = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
    output = result.stdout
    
    print(f"「{query}」の検索結果:\n")
    print("=" * 100)
    
    lines = output.strip().split('\n')
    for i in range(0, len(lines), 4):
        if i + 3 < len(lines):
            title = lines[i]
            url = lines[i+1] if i+1 < len(lines) else "N/A"
            channel = lines[i+2] if i+2 < len(lines) else "N/A"
            duration = lines[i+3] if i+3 < len(lines) else "N/A"
            
            print(f"\n【{i//4 + 1}】")
            print(f"タイトル: {title}")
            print(f"URL: {url}")
            print(f"チャンネル: {channel}")
            print(f"再生時間: {duration}")
            print("-" * 100)
            
except Exception as e:
    print(f"エラーが発生しました: {e}", file=sys.stderr)
    sys.exit(1)
