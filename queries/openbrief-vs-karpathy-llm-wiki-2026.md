---
title: OpenBrief と Karpathy LLM Wiki の違い
created: 2026-07-23
updated: 2026-07-23
type: query
tags: [adhd, attention, executive-function, tool, accessibility, research]
sources: [raw/articles/karpathy-llm-wiki-pattern-2026.md, raw/articles/github-open-brief-project-docs-2026.md, queries/toymaker-openbrief-adhd-design-notes.md, concepts/cognitive-personal-informatics.md, concepts/async-meetings-context-fit.md, concepts/task-resumption.md, concepts/external-memory.md, concepts/fear-of-missing-out.md]
confidence: medium
---

# OpenBrief と Karpathy LLM Wiki の違い

## 結論

**Karpathy の LLM Wiki は「知識を蓄積・編集する様式」で、OpenBrief は「注意遷移を安全に通す製品/実験」である。**

両者が似て見えるのは、どちらも「LLMが情報を読んで、構造化し、あとで使える形にする」からである。ただし、主語と成功条件が違う。

- LLM Wiki の主語は **知識ベース**。成功は、source から得た知識が wiki に蓄積され、後の query で再利用できること。
- OpenBrief の主語は **人間の注意遷移**。成功は、情報探索・返信・集中・復帰の間で、義務や元作業を見失わず、本人の自律性を保てること。

## 一言で分ける

| 観点 | Karpathy LLM Wiki | OpenBrief |
|---|---|---|
| 何か | LLMが保守する個人/チーム知識ベース | Attention Triage / 注意遷移支援 |
| 中心問題 | RAG が毎回知識を再発見して蓄積しない | 情報探索・通知・返信で元の意図や作業へ戻れない |
| 主な対象 | source、entity、concept、comparison、query | Gmail/RSS/Slack等から来る observation、protected intent、brief session、return anchor |
| 入力 | 人が選んだ文書・記事・論文・メモ | 未読、通知、返信候補、RSS、作業中断点、通信状態 |
| 出力 | markdown wiki、index、log、相互リンク | 有限 brief、Capture、Signal、Return Anchor、本人確認付き status |
| 成功 | 知識が compounding artifact になる | 探索価値を保ちながら、義務見落とし・探索超過・復帰失敗が減る |
| 失敗 | 重複ページ、古い要約、リンク切れ、出典不明 | 重要義務の隠蔽、新しい Inbox 化、監視化、強制感、戻れない |
| 時間軸 | 長期の知識蓄積 | セッション中の注意遷移と日常運用 |
| 誰が読むか | 人間と将来のLLM | まず本人。必要最小限だけ周囲に共有 |

## 似ているところ

1. **raw source を尊重する**  
   LLM Wiki は raw sources を変更せず、その上に wiki を作る。OpenBrief も Gmail/RSS/外部タスクを source of truth とし、OpenBrief 内で勝手に複製・最終判断しない。

2. **LLM は結論ではなく編集者/補助者**  
   LLM Wiki では LLM が要約、相互リンク、矛盾検出、ログ更新を担当する。OpenBrief では LLM が分類・要約・理由・候補を作るが、重要度や返信要否の最終決定は本人に残す。

3. **query が成果物になる**  
   LLM Wiki では良い query answer を wiki に戻す。OpenBrief でも Curiosity Capture や brief で得た問いは、Todo ではなく「あとで戻れる問い」として保存される。この点が似ている。

4. **Obsidian 的な蓄積と相性がよい**  
   OpenBrief の Capture は、放っておくと義務 backlog になるが、LLM Wiki に流すなら「興味のある問いを知識として寝かせる」経路になる。

## 決定的に違うところ

### 1. LLM Wiki は knowledge workflow、OpenBrief は attention workflow

LLM Wiki は、読んだ情報を長期記憶へ変える仕組みである。Karpathy の原典では、RAG が毎回 source fragments から答えを再構成するのに対し、LLM Wiki は persistent, compounding artifact として entity / concept / comparison / query を保守する。^[raw/articles/karpathy-llm-wiki-pattern-2026.md]

OpenBrief は、読むことそのものより **読む前・読んでいる間・読んだ後に、何を見失わないか** が中心である。OpenBrief の流れは `Protect → Signal → Explore / Focus → Capture → Return` で、知識化ではなく注意遷移の境界、義務の可視化、復帰手掛かりを扱う。^[raw/articles/github-open-brief-project-docs-2026.md]

### 2. LLM Wiki は「保存して育てる」、OpenBrief は「有限化して戻す」

LLM Wiki のよい動きは、source を読むたびに wiki が増え、後から query しやすくなること。量が増えることは基本的に価値である。

OpenBrief では、量が増えることは危険にもなる。未読、Capture、AI要約、カード、通知が増えすぎると、OpenBrief 自体が新しい Inbox や儀式になる。OpenBrief の客観評価でも kill risk として「OpenBrief自体が新しいInboxや儀式になる」ことが挙げられている。^[raw/articles/github-open-brief-project-docs-2026.md]

### 3. LLM Wiki の query は知識化、OpenBrief の Capture は義務化しない退避

LLM Wiki では query を保存することが強い。よい比較、分析、接続を wiki に戻すことで知識が複利化する。

OpenBrief の Curiosity Capture は、保存しても Todo、deadline、calendar event を作らない。これは「気になった問い」を新しい義務へ変えず、探索を終えるための退避先にする設計である。ここを混同すると、OpenBrief は「すべてを wiki/タスクへ ingest する装置」になり、ADHD支援として逆効果になりうる。^[raw/articles/github-open-brief-project-docs-2026.md]

### 4. LLM Wiki は LLM が書く。OpenBrief は本人が選ぶ。

Karpathy の LLM Wiki は「Obsidian が IDE、LLM が programmer、wiki が codebase」という比喩で、LLM が wiki layer をかなり所有する。人間は source selection と方向づけを担う。^[raw/articles/karpathy-llm-wiki-pattern-2026.md]

OpenBrief は、AIが表示理由・根拠・不明点・確信度を出しても、本人の選択を残す。Slack status も AI 推定だけで公開しない。自動返信、自動委任、自動カレンダー登録、AI推定だけを trigger にした status 更新は非目標に置かれている。^[raw/articles/github-open-brief-project-docs-2026.md]

## 混乱の原因

### A. OpenBrief の Capture が LLM Wiki の ingest に見える

どちらも「気になったことを後で使える形にする」ので似る。しかし:

- LLM Wiki ingest: source を読んで知識に統合する。
- OpenBrief Capture: 探索を終えるため、問いを義務化せず退避する。

Capture の行き先として LLM Wiki を使うのは自然だが、Capture 自体は wiki ではない。

### B. OpenBrief の brief が LLM Wiki の query に見える

どちらも LLM が要約・整理する。しかし:

- LLM Wiki query: 既存 wiki を読んで答え、価値があれば保存する。
- OpenBrief brief: いま注意を向ける範囲を有限化し、元作業へ戻す。

OpenBrief brief は、よい答えを作ることより、**終端、範囲、復帰** が重要である。

### C. 両方とも local-first / markdown / LLM agent と相性がよい

実装部品が似るため、製品目的まで同じに見える。だが部品が似ても、目的関数が違う。

## Toymaker での整理

Toymaker 全体を考えるなら、LLM Wiki と OpenBrief は上下関係ではなく、**隣接する2つの層**として扱うのがよい。

```text
外部source / 日常の出来事
        ↓
OpenBrief: いま読むか、守るか、退避するか、戻るかを扱う
        ↓ 必要なものだけ
LLM Wiki: 長期的に残す価値がある問い・source・整理を知識化する
```

つまり OpenBrief は **入口の注意遷移 gate**、LLM Wiki は **出口の知識蓄積 store**。

## 実装上の分離案

### OpenBrief が持つべきもの

- source coverage: どこまで確認したか
- ProtectedIntent: 今日見失いたくない返信・予定・中断作業
- BriefSession: 今回読む範囲、推定時間、終端
- CuriosityCapture: 気になった問い、起点、義務化しない状態
- ReturnAnchor: 元作業、再開点、次の一手
- AttentionSignal: 本人が選んだ応答状態と復帰予定

### LLM Wiki が持つべきもの

- raw source
- entity / concept / comparison
- filed query
- log / index
- 出典つきの長期 synthesis
- 矛盾・未検証仮説・保留判断

### 接続してよい部分

- OpenBrief の `CuriosityCapture` のうち、本人が「残す価値あり」と選んだものだけ LLM Wiki query にする。
- OpenBrief の `BriefSession` から、日次/週次で「残した問い一覧」を作る。
- LLM Wiki 側の既存 concept を OpenBrief の分類理由や設計根拠として読む。
- OpenBrief の研究ログを、個人が望む範囲だけ LLM Wiki の raw/queries に保存する。

### 接続しない方がよい部分

- OpenBrief の全未読を自動 ingest しない。
- CuriosityCapture を全部 Todo や wiki page にしない。
- LLM Wiki の「蓄積するほど価値が増す」感覚を、OpenBrief の未処理 backlog に持ち込まない。
- OpenBrief の注意状態や遅延理由を、チーム共有 wiki に自動保存しない。

## 最終整理

OpenBrief と Karpathy LLM Wiki の関係は、次が一番近い。

> **OpenBrief は、日常の情報流から「今扱うもの」と「あとで知識化してもよいもの」を分け、元の作業へ戻す attention triage。LLM Wiki は、選ばれた source と query を長期的に育てる knowledge compiler。**

したがって OpenBrief を作る時の問いは、

- これは wiki に残すべきか？

ではなく、まず

- 今これは読むべきか？
- 今の義務や元作業を見失わないか？
- 気になったことを義務にせず退避できるか？
- 終わったあと戻れるか？

である。そこを通過した後に、初めて LLM Wiki へ入れるかを選ぶ。

## 関連

- [[toymaker-openbrief-adhd-design-notes]]
- [[cognitive-personal-informatics]]
- [[async-meetings-context-fit]]
- [[task-resumption]]
- [[external-memory]]
- [[fear-of-missing-out]]
