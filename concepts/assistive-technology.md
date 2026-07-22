---
title: 支援技術
type: concept
created: 2026-07-22
updated: 2026-07-22
tags: [adhd, tool, accessibility, executive-function, research]
sources: [raw/papers/tan-2026-adult-adhd-assistive-technologies-scoping-review.md, raw/papers/lalwani-2025-productivity-social-robot-college-students.md, raw/articles/i-have-adhd-github-2026.md]
confidence: medium
---

# 支援技術

ADHD文脈の支援技術は、注意・時間・記憶・着手・切り替えを「本人の努力」だけに戻さず、道具や環境へ分散するための設計領域。既存ページでは、[[external-memory]]、[[time-management]]、[[task-initiation]]、[[environment-design]]として生活上の外部化が整理されている。

## 研究から見える傾向

Tanらの成人ADHD向け支援技術スコーピングレビュー予備報告は、3,538件から46件を抽出し、成人ADHDに対する技術ベース支援の研究が近年増えている一方、多くが「肯定的な日常支援」よりも治療・介入の観点に寄っていると述べている。成人では職場や高等教育での困難が子どもとは異なるため、[[executive-function]]をどう外部化するかが設計上の焦点になりやすい。^[raw/papers/tan-2026-adult-adhd-assistive-technologies-scoping-review.md]

LalwaniとSalamの生産性支援ロボット研究は、ADHDのある学生を含む大学生の生産性課題を対象に、参加型デザインで望ましいロボット特性と倫理的配慮を整理している。ただしこれは設計知見であり、症状改善や学業成果を示す臨床試験ではない。^[raw/papers/lalwani-2025-productivity-social-robot-college-students.md]

[[i-have-adhd]] は、支援技術を「利用者本人の予定管理」だけでなく、周囲の道具やエージェントが出す情報の形にも広げる例。答えを先頭に置く、手順を番号化する、次の行動を1つに絞る、といった出力設計で、読者の[[working-memory]]や[[task-initiation]]の負荷を下げようとしている。^[raw/articles/i-have-adhd-github-2026.md]

## 設計上の含意

- 継続的な自己管理を要求するだけの道具は、ADHDの[[working-memory]]や実行機能負荷をむしろ増やすことがある。
- 視覚化、リマインダー、タスク分解、記録検索、環境側の手がかりなど、低摩擦で外部化できる設計が重要になる。
- エージェントや開発道具では、出力そのものを支援技術として設計できる。短さだけでなく、次の行動、現在地、完了したことが見えるかが重要になる。
- 支援技術はプライバシー・監視・依存・通知疲れのリスクも持つ。特にセンサー、録音、画面記録、AI要約を使う道具では、最小限の記録、ローカル処理、削除しやすさを確認したい。

## 注意点

このページは技術設計と研究動向の整理であり、医療上の助言ではない。製品ページや設計研究は、有効性の証拠と分けて読む。

## 関連

- [[external-memory]]
- [[executive-function]]
- [[time-management]]
- [[task-initiation]]
- [[i-have-adhd]]
