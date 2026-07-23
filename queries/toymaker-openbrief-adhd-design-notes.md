---
title: Toymaker / OpenBrief ADHD Design Notes
created: 2026-07-23
updated: 2026-07-23
type: query
tags: [adhd, executive-function, attention, work, tool, accessibility]
sources: [raw/articles/x-tmiyatake-admin-night-2026.md, raw/articles/body-doubling-life-admin-sources-2026.md, raw/papers/fitz-2019-notification-batching-fomo.md, raw/papers/elhai-2021-fomo-overview.md, raw/articles/github-open-brief-project-docs-2026.md, raw/papers/arxiv-cognitive-personal-informatics-chi26-2026.md]
confidence: medium
---

# Toymaker / OpenBrief ADHD Design Notes

## 問い

OpenBrief / Toymaker のような注意・通知・返信・生活事務支援は、ADHD Wiki のどの知識を設計材料にできるか。

## 使えそうな接続

1. **[[digital-interruptions]]** — 通知・メール・SNS は、単に消せばよいものではない。通知を完全遮断すると不安や [[fear-of-missing-out]] が上がる可能性があるため、予測可能な確認時刻、残件数、確認済み範囲、次回確認の約束が重要になる。
2. **[[task-resumption]]** — brief 後に「戻る」だけでは弱い。中断前の場所、次の一手、作業中断点、2分だけ再開する足場が必要になる。
3. **[[external-memory]]** — 頭の中で未処理の義務を保持し続けるより、確認済み・保留・次回・委任を外に置く方が作業記憶の負荷を減らせる。
4. **[[body-doubling]]** — 請求書、税務、返信、予約などの生活事務は、個別 todo より Admin Night / body doubling の有限 session に束ねると着手しやすい。
5. **[[emotion-regulation]]** — overdue、未返信、未処理を責める文言にすると回避が強まりやすい。失敗表示より、次回へ回す、準備不足、確認待ち、保留のような状態語がよい。
6. **[[cognitive-personal-informatics]]** — OpenBrief の実験は、集中力を一般点数にするより、通知条件、確認欲求、作業復帰、読みやすさを個人内で比べる設計に向く。

## 製品仮説

- `Admin Queue`: Gmail / Slack / RSS から出た「払う」「返す」「予約する」「申請する」を生活事務だけの queue に集める。
- `Admin Night Mode`: 25〜90分の時間枠で、最初に3件だけ選び、最後に done / blocked / defer だけ記録する。
- `有限 brief`: 全部読むのではなく、今回の確認範囲、残件、次回確認時刻を明示する。
- `Privacy-first body double`: 同席者に見せるのは作業名と状態だけ。本文、金額、宛先、画面は見せない。
- `CPI log`: 通知を消す/まとめる/予告する条件ごとに、確認衝動、戻るまでの時間、次の一手保持を記録する。

## LLM Wiki との切り分け

[[openbrief-vs-karpathy-llm-wiki-2026]] では、OpenBrief を「知識を蓄積する wiki」ではなく、いま読む・守る・退避する・戻るを扱う attention triage として整理する。Curiosity Capture は LLM Wiki へ送る候補になりうるが、既定では Todo や wiki page へ自動変換しない。

## 採用しない方がよい方向

- ADHD 治療や集中力改善をうたうこと。
- 通知やSNSを全面禁止すること。
- 「また戻れなかった」「未処理が多い」のように本人を責める文言。
- 金銭・医療・行政書類を AI 要約や画面共有で不用意に露出すること。
