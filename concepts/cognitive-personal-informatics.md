---
title: 認知パーソナルインフォマティクス
created: 2026-07-23
updated: 2026-08-10
type: concept
tags: [adhd, attention, executive-function, working-memory, accessibility, tool, research]
sources: [raw/papers/arxiv-cognitive-personal-informatics-chi26-2026.md, raw/papers/pubmed-adhd-digital-text-comprehension-self-monitoring-2019.md, raw/papers/arxiv-multilingual-text-to-pictogram-reading-rehabilitation-2026.md, raw/papers/pubmed-adhd-ema-daily-life-adolescents-2026.md, raw/papers/selin-2026-self-tracking-masking-neurodivergent.md, raw/papers/ruf-2023-diet-physical-activity-impulsivity-adult-adhd-ema.md, raw/papers/carr-2026-fielded-attention-adhd-context.md]
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

## 文脈・感情労働・日常測定

Selinら（2026）は、自閉・ADHDを含む神経多様者がマスキング経験を視覚化し、少人数でセルフトラッキングを試した研究で、記録が自己洞察だけでなく解釈負荷や感情労働を生むことを示した。認知パーソナルインフォマティクスでは、測る対象を増やすより、本人が安全に読める形式、文脈を失わない記録、ピア共有の支えを設計する必要がある。^[raw/papers/selin-2026-self-tracking-masking-neurodivergent.md]

Rufら（2023）の成人ADHDを含むEMA研究は、食事、身体活動、状態衝動性の短時間関係を日常生活で測ろうとした例である。結果は食事成分と衝動性の単純な短時間関連を支持せず、EMAは「原因をすぐ特定する装置」ではなく、仮説の粒度・入力負荷・測定期間を慎重に設計する方法として扱う。^[raw/papers/ruf-2023-diet-physical-activity-impulsivity-adult-adhd-ema.md]

Carr（2026）のFielded Attentionは、注意を個人内の固定特性だけでなく、リズム、環境の手がかり、社会・物質的文脈との関係で生じるものとして捉える。これは[[attention-control]]や[[environment-design]]のページで扱う「注意を環境側にも分散する」発想を、概念面から補強する。^[raw/papers/carr-2026-fielded-attention-adhd-context.md]

## 注意点

認知状態の記録は、支援にも監視にもなりうる。学校・職場・家族が本人同意なしに行動ログを評価へ使うと害が大きい。ADHD 支援では、本人が自分の条件を知るための記録と、他者が監督するための記録を明確に分ける。

## 関連

- [[assistive-technology]]
- [[digital-adhd-support]]
- [[task-resumption]]
- [[digital-interruptions]]
- [[external-memory]]
- [[fear-of-missing-out]]
