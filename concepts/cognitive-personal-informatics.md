---
title: 認知パーソナルインフォマティクス
created: 2026-07-23
updated: 2026-07-23
type: concept
tags: [adhd, attention, executive-function, working-memory, accessibility, tool, research]
sources: [raw/papers/arxiv-cognitive-personal-informatics-chi26-2026.md, raw/papers/pubmed-adhd-digital-text-comprehension-self-monitoring-2019.md, raw/papers/arxiv-multilingual-text-to-pictogram-reading-rehabilitation-2026.md, raw/papers/pubmed-adhd-ema-daily-life-adolescents-2026.md]
confidence: medium
---

# 認知パーソナルインフォマティクス

認知パーソナルインフォマティクスは、集中、記憶、読解、予定、切り替えなどの認知状態を、本人の生活文脈に沿って記録・可視化・支援する考え方である。ADHD Wiki では、平均的な集中力を点数化する道具ではなく、本人がどの条件で読みやすいか、戻りやすいか、忘れにくいかを扱う [[assistive-technology]] として読む。^[raw/papers/arxiv-cognitive-personal-informatics-chi26-2026.md]

## ADHD 支援への含意

- **状態を人格評価にしない**: 注意がそれた、読めなかった、戻れなかった、を「だらしない」ではなく、媒体・時間帯・通知・疲労・作業量の条件として記録する。
- **自己報告だけにしない**: ADHD 学生はデジタル文章で理解得点が下がり、自分の出来の予測もずれやすいという研究がある。自己モニタリングそのものが難しくなるため、読み終わり、要点確認、紙/画面の違いなど、行動指標も見る。^[raw/papers/pubmed-adhd-digital-text-comprehension-self-monitoring-2019.md]
- **読解の足場を作る**: text-to-pictogram のような読み支援は、長文理解や抽象語を外部化する [[external-memory]] として扱える。ただし障害名で固定せず、読みにくい条件で使える選択肢として置く。^[raw/papers/arxiv-multilingual-text-to-pictogram-reading-rehabilitation-2026.md]
- **日内変動を前提にする**: EMA（日常場面での短い反復記録）は、症状を一回の質問紙だけでなく場面ごとに見る方法である。負荷が高すぎる記録は継続しないため、最小限の入力と自動化が必要になる。^[raw/papers/pubmed-adhd-ema-daily-life-adolescents-2026.md]

## 設計パターン

- [[digital-interruptions]] と合わせて、通知を消す/まとめる/予告する条件ごとに作業復帰を比べる。
- [[task-resumption]] と合わせて、中断前の場所、次の一手、戻るまでの時間を記録する。
- [[working-memory]] と合わせて、頭の中に保持していた項目数を、メモ、予定、画面表示へ逃がす。
- [[fear-of-missing-out]] と合わせて、見逃し不安が強い場面で「確認済み範囲」と「次回確認時刻」が効くかを見る。

## 注意点

認知状態の記録は、支援にも監視にもなりうる。学校・職場・家族が本人同意なしに行動ログを評価へ使うと害が大きい。ADHD 支援では、本人が自分の条件を知るための記録と、他者が監督するための記録を明確に分ける。

## 関連

- [[assistive-technology]]
- [[digital-adhd-support]]
- [[task-resumption]]
- [[digital-interruptions]]
- [[external-memory]]
- [[fear-of-missing-out]]
