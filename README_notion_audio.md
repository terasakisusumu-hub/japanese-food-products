# Notionスケジュール・タスク音声化ツール

Notionに書いてあるスケジュールやタスクを、運転中でも聞ける音声ファイルに変換するツールです。

## クイックスタート

### 1. インストール
```bash
pip install -r requirements.txt
```

### 2. 環境変数を設定
```bash
export NOTION_TOKEN='your_notion_token'
export NOTION_DATABASE_ID='your_database_id'
```

### 3. 実行
```bash
python notion_to_audio.py
```

### 4. 音声ファイルを確認
`schedule_YYYYMMDD_HHMMSS.mp3` が生成されます。

## 詳細な使い方

詳細は [notion_schedule_audio_guide.md](documents/notion_schedule_audio_guide.md) を参照してください。

## 主な機能

- ✅ Notion APIからスケジュール・タスクを自動取得
- ✅ 日付順に整理して読み上げ用テキストを生成
- ✅ Google Text-to-Speechで音声ファイル（MP3）を生成
- ✅ 完了済みタスクの除外オプション
- ✅ スマホで聞ける形式で出力

## 必要なもの

- Python 3.7以上
- Notion APIトークン（[取得方法](https://www.notion.so/my-integrations)）
- NotionデータベースID
- インターネット接続（gTTS使用時）

## ファイル構成

- `notion_to_audio.py` - メインスクリプト
- `requirements.txt` - 必要なPythonパッケージ
- `documents/notion_schedule_audio_guide.md` - 詳細ガイド

## ライセンス

このツールは自由に使用・改変できます。
