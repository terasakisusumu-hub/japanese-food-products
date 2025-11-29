# Notionスケジュール・タスクを音声で聞く方法

運転中でも聞けるように、Notionのスケジュールやタスクを音声ファイルに変換する方法を説明します。

## 方法1: Pythonスクリプトで直接変換（推奨）

### 必要なもの
- Python 3.7以上
- Notion APIトークン
- NotionデータベースID

### セットアップ手順

#### 1. 必要なライブラリをインストール
```bash
pip install -r requirements.txt
```

#### 2. Notion APIトークンを取得
1. https://www.notion.so/my-integrations にアクセス
2. 「+ New integration」をクリック
3. 名前を入力（例：「スケジュール音声化」）
4. 「Submit」をクリック
5. 表示された「Internal Integration Token」をコピー

#### 3. データベースにインテグレーションを接続
1. Notionで対象のデータベースを開く
2. 右上の「...」メニューをクリック
3. 「Connections」→「Add connections」を選択
4. 作成したインテグレーションを選択

#### 4. データベースIDを取得
1. Notionでデータベースを開く
2. URLからIDを取得
   - URL例: `https://www.notion.so/1234567890abcdef?v=...`
   - データベースID: `1234567890abcdef`（32文字の英数字）

#### 5. 環境変数を設定
```bash
export NOTION_TOKEN='your_token_here'
export NOTION_DATABASE_ID='your_database_id_here'
```

#### 6. スクリプトを実行
```bash
python notion_to_audio.py
```

または、データベースIDを直接指定：
```bash
python notion_to_audio.py your_database_id_here
```

#### 7. 完了済みタスクも含める場合
```bash
export INCLUDE_COMPLETED=true
python notion_to_audio.py
```

### 出力ファイル
- `schedule_YYYYMMDD_HHMMSS.mp3` というファイルが生成されます
- スマホに転送して聞くことができます

---

## 方法2: NotebookLMを使った方法

NotebookLMを使って、より柔軟にテキストを整形してから音声化する方法です。

### 手順

#### 1. Notionからデータをエクスポート
1. Notionでデータベースを開く
2. 右上の「...」メニューをクリック
3. 「Export」を選択
4. 形式を「Markdown & CSV」または「CSV」に設定
5. 「Export」をクリックしてダウンロード

#### 2. NotebookLMにインポート
1. https://notebooklm.google.com/ にアクセス
2. 「+ New notebook」をクリック
3. ノートブックに名前を付ける（例：「スケジュール音声化」）
4. 「Add source」をクリック
5. エクスポートしたファイルをアップロード

#### 3. NotebookLMでプロンプトを実行
以下のプロンプトをNotebookLMに入力：

```
このデータベースから、スケジュールとタスクを抽出して、読み上げ用のテキストに整形してください。

以下の形式で出力してください：
- 日付順に並べる
- 各項目は「日付、タイトル、ステータス」の順で読み上げる
- 完了済みのタスクは除外する（または最後にまとめる）
- 簡潔に、運転中でも聞き取りやすいように
- ストーリーや説明は不要で、単純にスケジュールとタスクを読み上げるだけ

例：
2024年1月15日の予定。
タイトル: 会議。日時: 14時。場所: 会議室A。
タイトル: 買い物。場所: スーパー。
```

#### 4. 生成されたテキストをコピー
NotebookLMが生成したテキストをコピーします。

#### 5. テキストを音声に変換
以下のいずれかの方法で音声化：

**方法A: オンラインTTSサービス**
- Google Text-to-Speech (https://cloud.google.com/text-to-speech)
- Amazon Polly (https://aws.amazon.com/polly/)
- ブラウザの読み上げ機能（Chromeの拡張機能など）

**方法B: Pythonスクリプト**
```python
from gtts import gTTS

text = """ここにNotebookLMで生成したテキストを貼り付け"""

tts = gTTS(text=text, lang='ja', slow=False)
tts.save('schedule.mp3')
```

**方法C: スマホアプリ**
- iPhone: 「ショートカット」アプリで「テキストを読み上げ」アクションを使用
- Android: 「TalkBack」や「Google テキスト読み上げ」を使用

---

## 方法3: 自動化スクリプト（NotebookLM + 音声化）

NotebookLMのAPI（利用可能な場合）と組み合わせて自動化する方法です。

### 注意点
- NotebookLMのAPIは現在公開されていない可能性があります
- その場合は、方法1または方法2を使用してください

---

## スマホで聞く方法

### iPhone
1. iTunesまたはFinderでMP3ファイルを転送
2. 「ミュージック」アプリで再生
3. 運転中はCarPlayやBluetoothで聞く

### Android
1. USBケーブルまたはクラウドストレージでMP3ファイルを転送
2. 「ミュージック」アプリで再生
3. 運転中はAndroid AutoやBluetoothで聞く

### クラウド経由
1. Google Drive、Dropbox、iCloudなどにアップロード
2. スマホアプリでダウンロード
3. 再生

---

## カスタマイズ

### 読み上げ速度を変更
`notion_to_audio.py`の`text_to_speech`メソッドで：
```python
tts = gTTS(text=text, lang=lang, slow=True)  # slow=Trueでゆっくり
```

### 読み上げ内容をカスタマイズ
`format_schedule_text`メソッドを編集して、読み上げる項目や順序を変更できます。

### フィルタリング
特定の条件のタスクだけを抽出する場合：
```python
# 例: 今日から7日以内のタスクのみ
from datetime import datetime, timedelta
filter_conditions = {
    "property": "日付",
    "date": {
        "on_or_after": datetime.now().isoformat(),
        "on_or_before": (datetime.now() + timedelta(days=7)).isoformat()
    }
}
pages = converter.get_database_pages(database_id, filter_conditions)
```

---

## トラブルシューティング

### Notion APIでエラーが出る
- トークンが正しく設定されているか確認
- データベースにインテグレーションが接続されているか確認
- データベースIDが正しいか確認（32文字の英数字）

### 音声ファイルが生成されない
- インターネット接続を確認（gTTSはオンラインで動作）
- テキストが空でないか確認
- エラーメッセージを確認

### 読み上げが聞き取りにくい
- テキストを短くする
- 句読点を適切に入れる
- 専門用語を避ける

---

## 定期実行（オプション）

cronやタスクスケジューラーで定期実行する場合：

### Linux/Mac (cron)
```bash
# 毎朝7時に実行
0 7 * * * cd /path/to/workspace && /usr/bin/python3 notion_to_audio.py
```

### Windows (タスクスケジューラー)
1. タスクスケジューラーを開く
2. 「基本タスクの作成」を選択
3. トリガーを設定（例：毎日7:00）
4. 操作で`python notion_to_audio.py`を実行

---

## 参考資料

- [Notion API ドキュメント](https://developers.notion.com/)
- [NotebookLM 公式サイト](https://notebooklm.google.com/)
- [gTTS ドキュメント](https://gtts.readthedocs.io/)
