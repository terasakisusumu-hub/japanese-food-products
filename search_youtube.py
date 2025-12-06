#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from youtubesearchpython import VideosSearch

# 検索クエリ
query = "竹田恒泰 吉田松陰"

# YouTube検索を実行
videosSearch = VideosSearch(query, limit=10)
results = videosSearch.result()

print(f"「{query}」の検索結果:\n")
print("=" * 80)

for i, video in enumerate(results['result'], 1):
    title = video['title']
    url = video['link']
    channel = video['channel']['name']
    duration = video.get('duration', 'N/A')
    view_count = video.get('viewCount', {}).get('text', 'N/A')
    
    print(f"\n{i}. {title}")
    print(f"   チャンネル: {channel}")
    print(f"   再生時間: {duration}")
    print(f"   再生回数: {view_count}")
    print(f"   URL: {url}")
    print("-" * 80)
