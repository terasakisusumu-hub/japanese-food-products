# Geminiストーリーブックで作る「タコ＆レッサーパンダのじてんしゃ冒険」ガイド

## 1. ねらいとストーリーの骨子
- **対象**: 小学2年生の男の子。今はペダルに足を乗せられるのがほんの一瞬。
- **物語の軸**:
  1. 自分で撮影したタコとレッサーパンダのぬいぐるみが相棒になる。
  2. 何度も転び、ひざに絆創膏を貼りながらも少しずつ前進。
  3. 最後に風を切って走れるようになる達成感を共有。
- **学びのポイント**: 小さな前進を言葉でほめる／安全への気配り／転んでも再チャレンジする姿勢。

## 2. 事前準備チェックリスト
|項目|具体的な準備|Geminiでの使いどころ|
|---|---|---|
|ぬいぐるみ写真2枚|タコぬい・レッサーパンダぬいを正面から明るく撮影。背景はできるだけ無地にする。|各ページのイラスト差し替えに使用。
|練習シーンの実写|転ばない程度の短い動画や写真。本人の頑張りを記録。|Geminiに参考素材として読み込ませ、描写をリアルに。
|ストーリーメモ|「初めは足が一瞬しか乗らない」「何度も転ぶ」など事実ベースのメモ。|プロンプトの文脈に入れて、個別性を保つ。
|応援フレーズ集|親子でよく使う声かけ（例:「ドンマイ！」「風を感じてみよう」）。|セリフに挿入して本人に響くストーリーに。

## 3. Geminiストーリーブック機能の使い方
1. **Gemini Advanced／Gemini for Workspace** で「ストーリーブック（Storyboard）」テンプレートを開く。
2. **"Create" > "Story"** を選び、テンプレート「Adventure」「Learning Journey」などを指定。
3. **画像アップロード**: タコとレッサーパンダの写真を最初にアップ。背景が気になる場合はGeminiの「背景除去」ツールで巾着や背景を消す。
4. **ストーリー構成**をSceneごとに入力。
   - Scene 1: 自己紹介＆目標宣言
   - Scene 2: ペダルに一瞬だけ足が乗る挑戦
   - Scene 3: 何度も転んで泣きそうになる
   - Scene 4: 応援と工夫（芝生で練習、休憩）
   - Scene 5: 足が3秒、5秒と伸びていく
   - Scene 6: 風を切って走る成功シーン
5. **「Add child-friendly tone」** をON、読み上げ機能やBGMを選択（明るいアコースティック系がおすすめ）。
6. 仕上げに「Share」>「Interactive mode」で子どもがページをめくりながら読めるリンクを発行。

## 4. プロンプト例（日本語ベース）
```
You are a creator for Gemini Storybook.
Write a 6-scene story for a 2nd-grade boy named 〇〇 who is learning to ride a bike.
Use the uploaded photos of his favorite plush octopus "Tako" and red panda "Panda-kun" as main characters.
Key beats:
1. They promise to help 〇〇 keep his feet on the pedals, even if it’s only for one second now.
2. Show scenes where he wobbles, tips over onto soft grass, and puts on cute bandage stickers.
3. Highlight how each micro-improvement (1 second → 3 seconds → 10 seconds) is celebrated.
4. Finale: 〇〇 rides freely with both plushies cheering.
Tone: warm, encouraging, playful dialogue in Japanese, short sentences, onomatopoeia.
Add interactive prompts like "どっちの応援を選ぶ?" so the child can tap.
```
- 背景の色味やアートスタイル（手描き水彩、やわらかいパステルなど）も指定すると統一感が出る。

## 5. 画像・カスタマイズのコツ
- **キャラ差し替え**: 各シーンのメインビジュアルに「Use uploaded image」→タコ or レッサーパンダを選択。必要に応じて「Blend with AI art」で背景を自転車練習場に変える。
- **ステッカー風テキスト**: セリフ枠を追加し、「キラッ」「ぐらぐら…」などの擬音を入れると小学生が読みやすい。
- **安全メッセージ**: ヘルメットやプロテクターの描写を含めるようプロンプトで指示（"always show helmet and knee pads"）。
- **進捗バー**: ストーリーブックの「Journey」レイアウトを選び、シーンごとに「ペダルに乗れた秒数」を表示して成長が見える仕組みにする。

## 6. 親子での活用アイデア
- **読み合わせ前**: 実写写真を見ながら「今日はどこまで足を乗せられた？」と振り返る。
- **インタラクティブ操作**: 子どもにセリフ選択や効果音ボタンをタップしてもらい、当事者意識を高める。
- **ごほうびページ**: 最終シーンに「次の冒険チケット（公園・アイスクリーム）」など好きなご褒美を描いてモチベーションに。
- **アップデート可能**: 新しい練習写真をアップしてシーンを差し替えれば、成長記録として継続活用できる。

## 7. 仕上げチェックリスト
- [ ] タコ＆レッサーパンダの写真が全シーンにバランスよく登場している
- [ ] ペダルに足を乗せられる秒数の変化がストーリーで明示されている
- [ ] 転倒シーンは安全配慮と前向きな声かけで締めている
- [ ] 子どもがタップできる選択肢やボタンを最低1か所入れている
- [ ] 共有リンクを家族LINEやタブレットに保存し、練習前後に読み返せるようにしている

---
この流れでGeminiのストーリーブック機能を使えば、本人のぬいぐるみ・練習状況を取り込んだ「自分だけの冒険絵本」を短時間で制作できます。親子の声かけと連動させて、転んでもチャレンジする姿勢を楽しく後押ししましょう。
