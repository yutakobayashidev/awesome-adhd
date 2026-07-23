---
title: "Toymaker: 神経発達症、非同期、会議、AI支援、文脈不協"
created: 2026-07-23
updated: 2026-07-23
type: query
tags: [adhd, autism, work, accessibility, executive-function, tool, research]
sources: [concepts/async-meetings-context-fit.md, raw/papers/das-2021-accessible-remote-work-neurodivergent.md, raw/papers/liebel-2023-software-engineers-adhd-meetings.md, raw/papers/jameson-2026-sustainable-work-adhd.md, raw/papers/oconnor-2025-autistic-asynchronous-focus-group.md, raw/papers/deshmukh-2025-neurodivergent-aware-productivity-ai.md, raw/articles/welcomebrain-2026-neuroinclusive-meetings.md]
confidence: medium
---

# Toymaker: 神経発達症、非同期、会議、AI支援、文脈不協

## 結論

神経発達症の支援では、非同期ツールを増やすだけでも、会議を減らすだけでも足りない。問題は **文脈不協**、つまり「本人の処理リズム・作業記憶・感覚負荷・社会的安全・評価規範」と「連絡様式・会議形式・期待される即応性」が噛み合わないことにある。非同期は処理時間と記録を与えるが、足場がないと孤立・先延ばし・見逃し不安を増やす。同期会議は負荷が高いが、着手、共通理解、関係修復、外部説明責任には効くことがある。

## 使い分け表

| 状況 | 推奨様式 | 理由 |
|---|---|---|
| 情報共有、確認、読み返しが必要 | 非同期文書/brief | 処理時間と記録が残る |
| 発言準備が必要 | 議題付き非同期 → 短い同期 | 即答圧を下げる |
| 着手できない/生活事務を進めたい | 同期または半同期の共同作業枠 | [[body-doubling]]が足場になる |
| 前提が食い違っている | 短い同期 + その場で文書化 | 誤解修復は同期が速いことがある |
| 長い議論・発散 | brainwriting / shared doc | 速い発話競争を避ける |
| 会議後に戻れない | AI Return Anchor | [[task-resumption]]を支える |

## AI支援案

1. **会議必要性判定**: 「これは会議か、文書か、共同作業枠か、1:1か」を提案する。
2. **事前足場**: 議題、読む量、予想時間、期待される発言、未決点を短く出す。
3. **多経路参加**: 会議中チャット、事前メモ、会議後追記、音声/文字切替。
4. **会議後復帰**: 決定事項だけでなく、会議前の作業と次の一手を出す。
5. **通信容量ステータス**: `文字なら可`、`同期10分だけ可`、`今日は処理遅め`、`次回確認時刻` を本人が選べる。
6. **監視しない注意支援**: タブ切替や反応遅延は本人のローカル支援に使い、評価者へ出さない。

## OpenBriefでの実装仮説

- `Brief` は「未読の羅列」ではなく、「有限の処理枠」「終端」「次回確認」「戻り先」を持つ。
- `Meeting Brief` は、会議前後を1セットで扱う: before agenda → during capture → after return anchor。
- `Admin Night Mode` は同期の良さを使うが、本文や金額など機微情報は共有しない。
- Slack status は可用性ではなく通信容量を示す。例: `deep work, text ok after 14:30`, `meeting recovery`, `async preferred today`。
- AIは神経型を推定しない。本人が選んだ支援プリセットと局所的な作業状態だけを見る。

## 注意

- 出典の一部は概念論文・実務記事であり、厳密な介入効果は未検証。
- ADHD、自閉スペクトラム症、学習障害、不安などで支援の合う/合わないは違う。
- 非同期に寄せすぎると、構造・説明責任・関係修復が不足する人もいる。
