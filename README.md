# awesome-adhd

ADHD（注意欠如・多動症）に関する、実践寄りの LLM Wiki / awesome list です。

ここでは、研究・支援策・道具・当事者の工夫を Markdown の知識ベースとして整理します。普通のリンク集ではなく、取り込んだ情報をあとから読み返しやすいページにまとめ、関連する概念同士をつないでいく運用です。

> [!IMPORTANT]
> このリポジトリは医療助言ではありません。診断、薬、治療方針については医師など専門職に相談してください。個人の症状や服薬歴など、本人特定につながる情報は保存しない方針です。

## これは何？

- ADHDに関する実践的な知識ベース
- Karpathy 型の LLM Wiki 風に育てる Markdown vault
- GitHubで読める awesome-adhd リスト
- ObsidianやVS Codeでも開けるプレーンなファイル群

LLM Wiki としては、`raw/` に原資料を保存し、`entities/` や `concepts/` に整理済みページを作ります。ページ同士は `[[wikilinks]]` でつなぎます。

awesome list としては、下の「Contents」から主要トピックや道具へ直接飛べます。

## Contents

### Tools

- [Tiimo](entities/tiimo.md) — ADHDや自閉スペクトラム症の人向けに、視覚的な予定表、集中タイマー、AIタスク分解、ウィジェットなどで実行機能を支える計画アプリ。

### Concepts

- [Environment design](concepts/environment-design.md) — ADHDの困りごとを、物理配置・透明収納・制服化・睡眠環境などで外部から支える考え方。
- [Executive function](concepts/executive-function.md) — 着手・優先順位づけ・抑制・切り替え・時間管理を支える実行機能と、その外部化の考え方。
- [External memory](concepts/external-memory.md) — 紙・スマホ・タイマー・置き場所・人に記憶や判断を預け、作業記憶の負荷を下げる考え方。
- [Forgetfulness countermeasures](concepts/forgetfulness-countermeasures.md) — 玄関ランディングパッド、ドア貼りチェックリスト、透明収納、即時メモ、服の制服化などの忘れ物対策。
- [Hyperfocus control](concepts/hyperfocus-control.md) — 過集中を自力で止めるのではなく、開始前に終了条件・アラーム・ブロッカー・退室を仕込む方法。
- [Sleep](concepts/sleep.md) — ADHD文脈での睡眠に関する環境調整・過集中対策の体験談メモ。
- [Task initiation](concepts/task-initiation.md) — 5秒以内メモ、極短ポモドーロ、身体だけ動かす、タスク共有などで着手摩擦を下げる方法。
- [Time management](concepts/time-management.md) — 時間盲・遅刻・過集中に対して、視覚タイマー、アナログ時計、見積もり補正、時間アンカーを使う方法。
- [Work routines](concepts/work-routines.md) — 興味のない仕事を低消耗で通過するための2割以内ルール、手順固定、5分単位化、自動化。
- [Working memory](concepts/working-memory.md) — 頭の中で保持し続ける負荷を、メモ・配置・チェックリスト・タイマーへ逃がす考え方。

## Wiki structure

```text
.
├── README.md          # GitHub向けの入口。このファイル
├── SCHEMA.md          # Wikiの運用規約、タグ体系、注意事項
├── index.md           # Wiki内部の目録
├── log.md             # 取り込み・更新ログ
├── raw/               # 原資料。基本的に編集しない
│   ├── articles/
│   ├── papers/
│   ├── transcripts/
│   └── assets/
├── entities/          # 道具、組織、人物、制度など
├── concepts/          # 概念、困りごと、実践パターン
├── comparisons/       # 比較ページ
└── queries/           # 後で残したい調査結果
```

## How to read

GitHubでは、まずこのREADMEのContentsから気になるページへ移動してください。

Obsidianや対応エディタで開くと、`[[external-memory]]` のようなリンクがそのまま知識グラフになります。GitHub上では一部の `[[wikilinks]]` は普通のリンクとしては動かないため、入口として [index.md](index.md) も用意しています。

## What goes in

歓迎するもの:

- 実生活で使える工夫、道具、環境設計
- ADHDや実行機能に関する研究・診療指針・制度情報
- 当事者体験から抽出できる再利用可能なパターン
- アクセシビリティ、学校、仕事、家庭での支援策

入れないもの:

- 個人を特定できる健康情報
- 診断や服薬の直接的な助言
- 出典のない断定的な医療情報
- ただの炎上、ミーム、スティグマを強める内容

## Source policy

`raw/` は原資料の保管場所です。記事、投稿、メモを取り込むときは、出典URL、取り込み日、本文ハッシュを付けます。

整理済みページでは、出典の性質を分けて扱います。

- 研究・指針: できるだけ出典と対象国・時期を明記する
- 製品ページ: 道具の説明として扱い、効果検証とは分ける
- X/Twitter等の投稿: 当事者の実践メモとして扱い、医療的根拠とはみなさない

## Contributing

今は小さく育てている段階です。追加したいものがある場合は、URLやメモをIssueやPRで投げてください。

PRで追加する場合の目安:

1. 原資料は `raw/` に置く
2. 重要な概念や道具は `concepts/` または `entities/` に整理する
3. 新しいページは `index.md` に1行で追加する
4. `log.md` に作業内容を追記する
5. 医療・個人情報まわりは強く安全側に倒す

詳しい運用は [SCHEMA.md](SCHEMA.md) を見てください。

## Automation

このWikiは、Hermes Agent が定期的に公開情報を探して取り込む実験も兼ねています。たとえば `#ADHD` の実践的な工夫を検索し、有用そうなものだけを raw source と concept page に整理します。

自動取り込みは便利ですが、万能ではありません。とくに医療、薬、診断、個人情報に関わる内容は、人間が確認する前提です。

## License

未定。ライセンスを決めるまでは、再利用範囲を明示できません。

各原資料の著作権は元の著作者にあります。このリポジトリ内の引用・要約は、出典確認と学習用の整理を目的としています。
