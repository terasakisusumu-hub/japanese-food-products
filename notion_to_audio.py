#!/usr/bin/env python3
"""
Notionのスケジュール・タスクを音声ファイルに変換するスクリプト

使用方法:
1. Notion APIのトークンを取得して環境変数に設定
2. データベースIDを指定
3. スクリプトを実行してMP3ファイルを生成
"""

import os
import sys
from datetime import datetime
from typing import List, Dict, Optional
import json

try:
    from notion_client import Client
except ImportError:
    print("notion-clientライブラリがインストールされていません。")
    print("インストール方法: pip install notion-client")
    sys.exit(1)

try:
    from gtts import gTTS
except ImportError:
    print("gTTSライブラリがインストールされていません。")
    print("インストール方法: pip install gtts")
    sys.exit(1)


class NotionToAudio:
    def __init__(self, notion_token: str):
        """
        NotionToAudioクラスの初期化
        
        Args:
            notion_token: Notion APIのトークン
        """
        self.notion = Client(auth=notion_token)
    
    def get_database_pages(self, database_id: str, filter_conditions: Optional[Dict] = None) -> List[Dict]:
        """
        Notionデータベースからページを取得
        
        Args:
            database_id: NotionデータベースのID
            filter_conditions: フィルタ条件（オプション）
        
        Returns:
            ページのリスト
        """
        try:
            query = {}
            if filter_conditions:
                query["filter"] = filter_conditions
            
            results = []
            has_more = True
            start_cursor = None
            
            while has_more:
                if start_cursor:
                    query["start_cursor"] = start_cursor
                
                response = self.notion.databases.query(database_id=database_id, **query)
                results.extend(response["results"])
                has_more = response["has_more"]
                start_cursor = response.get("next_cursor")
            
            return results
        except Exception as e:
            print(f"エラー: データベースからページを取得できませんでした: {e}")
            return []
    
    def extract_text_from_page(self, page: Dict) -> str:
        """
        ページからテキストを抽出
        
        Args:
            page: Notionページオブジェクト
        
        Returns:
            抽出されたテキスト
        """
        text_parts = []
        
        # ページのプロパティから情報を抽出
        properties = page.get("properties", {})
        
        # タイトルを取得
        title = ""
        for prop_name, prop_value in properties.items():
            if prop_value.get("type") == "title":
                title_rich_text = prop_value.get("title", [])
                if title_rich_text:
                    title = "".join([rt.get("plain_text", "") for rt in title_rich_text])
                    break
        
        if title:
            text_parts.append(f"タイトル: {title}")
        
        # 日付を取得
        for prop_name, prop_value in properties.items():
            if prop_value.get("type") == "date":
                date_value = prop_value.get("date")
                if date_value:
                    date_str = date_value.get("start", "")
                    if date_str:
                        try:
                            date_obj = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
                            text_parts.append(f"日付: {date_obj.strftime('%Y年%m月%d日')}")
                        except:
                            text_parts.append(f"日付: {date_str}")
        
        # ステータスを取得
        for prop_name, prop_value in properties.items():
            if prop_value.get("type") == "select":
                select_value = prop_value.get("select")
                if select_value:
                    status = select_value.get("name", "")
                    if status:
                        text_parts.append(f"ステータス: {status}")
        
        # チェックボックス（完了/未完了）を取得
        for prop_name, prop_value in properties.items():
            if prop_value.get("type") == "checkbox":
                checked = prop_value.get("checkbox", False)
                if checked:
                    text_parts.append("完了済み")
                else:
                    text_parts.append("未完了")
        
        # リッチテキストプロパティを取得
        for prop_name, prop_value in properties.items():
            if prop_value.get("type") == "rich_text":
                rich_text = prop_value.get("rich_text", [])
                if rich_text:
                    text_content = "".join([rt.get("plain_text", "") for rt in rich_text])
                    if text_content:
                        text_parts.append(f"{prop_name}: {text_content}")
        
        return "。".join(text_parts) + "。"
    
    def format_schedule_text(self, pages: List[Dict], include_completed: bool = False) -> str:
        """
        スケジュール・タスクを読み上げ用のテキストに整形
        
        Args:
            pages: Notionページのリスト
            include_completed: 完了済みのタスクも含めるか
        
        Returns:
            整形されたテキスト
        """
        if not pages:
            return "スケジュールやタスクは見つかりませんでした。"
        
        # 日付でソート
        sorted_pages = []
        for page in pages:
            properties = page.get("properties", {})
            date_value = None
            for prop_name, prop_value in properties.items():
                if prop_value.get("type") == "date":
                    date_obj = prop_value.get("date")
                    if date_obj:
                        date_str = date_obj.get("start", "")
                        if date_str:
                            try:
                                date_value = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
                            except:
                                pass
                    break
            
            # 完了済みかチェック
            is_completed = False
            for prop_name, prop_value in properties.items():
                if prop_value.get("type") == "checkbox":
                    is_completed = prop_value.get("checkbox", False)
                    break
            
            if include_completed or not is_completed:
                sorted_pages.append((date_value or datetime.min, page))
        
        # 日付でソート
        sorted_pages.sort(key=lambda x: x[0])
        
        # テキストを生成
        text_parts = [f"スケジュールとタスクを読み上げます。全部で{len(sorted_pages)}件あります。"]
        
        current_date = None
        for date_value, page in sorted_pages:
            page_text = self.extract_text_from_page(page)
            
            # 日付が変わったら日付を読み上げ
            if date_value and date_value != datetime.min:
                date_str = date_value.strftime('%Y年%m月%d日')
                if current_date != date_str:
                    text_parts.append(f"\n{date_str}の予定。")
                    current_date = date_str
            
            text_parts.append(page_text)
        
        return "\n".join(text_parts)
    
    def text_to_speech(self, text: str, output_file: str, lang: str = "ja") -> bool:
        """
        テキストを音声ファイルに変換
        
        Args:
            text: 読み上げるテキスト
            output_file: 出力ファイル名（.mp3）
            lang: 言語コード（デフォルト: "ja"）
        
        Returns:
            成功したかどうか
        """
        try:
            print(f"音声ファイルを生成中... ({len(text)}文字)")
            tts = gTTS(text=text, lang=lang, slow=False)
            tts.save(output_file)
            print(f"音声ファイルを保存しました: {output_file}")
            return True
        except Exception as e:
            print(f"エラー: 音声ファイルの生成に失敗しました: {e}")
            return False


def main():
    """メイン処理"""
    # 環境変数からNotionトークンを取得
    notion_token = os.getenv("NOTION_TOKEN")
    if not notion_token:
        print("エラー: NOTION_TOKEN環境変数が設定されていません。")
        print("設定方法: export NOTION_TOKEN='your_token_here'")
        sys.exit(1)
    
    # データベースIDを取得（コマンドライン引数または環境変数）
    if len(sys.argv) > 1:
        database_id = sys.argv[1]
    else:
        database_id = os.getenv("NOTION_DATABASE_ID")
        if not database_id:
            print("使用方法: python notion_to_audio.py <DATABASE_ID>")
            print("または環境変数 NOTION_DATABASE_ID を設定してください。")
            sys.exit(1)
    
    # 完了済みタスクを含めるか（オプション）
    include_completed = os.getenv("INCLUDE_COMPLETED", "false").lower() == "true"
    
    # 出力ファイル名
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"schedule_{timestamp}.mp3"
    
    print("=" * 50)
    print("Notionスケジュール・タスク音声化ツール")
    print("=" * 50)
    print(f"データベースID: {database_id}")
    print(f"完了済みタスクを含める: {include_completed}")
    print()
    
    # NotionToAudioインスタンスを作成
    converter = NotionToAudio(notion_token)
    
    # データベースからページを取得
    print("Notionからデータを取得中...")
    pages = converter.get_database_pages(database_id)
    
    if not pages:
        print("警告: データが見つかりませんでした。")
        print("データベースIDとアクセス権限を確認してください。")
        sys.exit(1)
    
    print(f"{len(pages)}件のページを取得しました。")
    
    # テキストを整形
    print("テキストを整形中...")
    text = converter.format_schedule_text(pages, include_completed=include_completed)
    
    # テキストを表示（確認用）
    print("\n" + "=" * 50)
    print("読み上げるテキスト（最初の500文字）:")
    print("=" * 50)
    print(text[:500] + ("..." if len(text) > 500 else ""))
    print()
    
    # 音声ファイルを生成
    success = converter.text_to_speech(text, output_file)
    
    if success:
        print("\n" + "=" * 50)
        print("完了！")
        print(f"音声ファイル: {output_file}")
        print("スマホに転送して聞くことができます。")
        print("=" * 50)
    else:
        print("\nエラーが発生しました。")
        sys.exit(1)


if __name__ == "__main__":
    main()
