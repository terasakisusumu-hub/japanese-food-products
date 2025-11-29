#!/usr/bin/env python3
"""
テキストファイルを音声ファイルに変換するスクリプト

NotebookLMで生成したテキストを音声化する場合に使用します。

使用方法:
    python text_to_audio.py input.txt output.mp3
    または
    python text_to_audio.py input.txt  # output.mp3が自動生成される
"""

import sys
import os
from datetime import datetime

try:
    from gtts import gTTS
except ImportError:
    print("gTTSライブラリがインストールされていません。")
    print("インストール方法: pip install gtts")
    sys.exit(1)


def text_to_audio(input_file: str, output_file: str = None, lang: str = "ja", slow: bool = False) -> bool:
    """
    テキストファイルを音声ファイルに変換
    
    Args:
        input_file: 入力テキストファイルのパス
        output_file: 出力音声ファイルのパス（省略時は自動生成）
        lang: 言語コード（デフォルト: "ja"）
        slow: ゆっくり読み上げるか（デフォルト: False）
    
    Returns:
        成功したかどうか
    """
    # 入力ファイルを読み込む
    if not os.path.exists(input_file):
        print(f"エラー: ファイルが見つかりません: {input_file}")
        return False
    
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            text = f.read()
    except Exception as e:
        print(f"エラー: ファイルを読み込めませんでした: {e}")
        return False
    
    if not text.strip():
        print("エラー: ファイルが空です。")
        return False
    
    # 出力ファイル名を決定
    if not output_file:
        base_name = os.path.splitext(input_file)[0]
        output_file = f"{base_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.mp3"
    
    # 音声ファイルを生成
    try:
        print(f"音声ファイルを生成中... ({len(text)}文字)")
        print(f"入力ファイル: {input_file}")
        print(f"出力ファイル: {output_file}")
        
        tts = gTTS(text=text, lang=lang, slow=slow)
        tts.save(output_file)
        
        print(f"\n✓ 音声ファイルを保存しました: {output_file}")
        print(f"  ファイルサイズ: {os.path.getsize(output_file) / 1024 / 1024:.2f} MB")
        return True
    except Exception as e:
        print(f"エラー: 音声ファイルの生成に失敗しました: {e}")
        return False


def main():
    """メイン処理"""
    if len(sys.argv) < 2:
        print("使用方法: python text_to_audio.py <入力テキストファイル> [出力MP3ファイル]")
        print("\n例:")
        print("  python text_to_audio.py schedule.txt")
        print("  python text_to_audio.py schedule.txt output.mp3")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    # オプション: ゆっくり読み上げる
    slow = os.getenv("SLOW", "false").lower() == "true"
    
    print("=" * 50)
    print("テキスト音声化ツール")
    print("=" * 50)
    
    success = text_to_audio(input_file, output_file, slow=slow)
    
    if success:
        print("\n" + "=" * 50)
        print("完了！")
        print("スマホに転送して聞くことができます。")
        print("=" * 50)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
