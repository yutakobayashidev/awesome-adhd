---
title: 支援技術
type: concept
created: 2026-07-22
updated: 2026-08-10
tags: [adhd, tool, accessibility, executive-function, research]
sources: [raw/articles/deep-research-report-ai-software-adhd-2026.md, raw/articles/focusmate-homepage-2026.md, raw/papers/tan-2026-adult-adhd-assistive-technologies-scoping-review.md, raw/papers/lalwani-2025-productivity-social-robot-college-students.md, raw/articles/i-have-adhd-github-2026.md, raw/papers/arxiv-cognitive-personal-informatics-chi26-2026.md, raw/papers/pubmed-adhd-digital-text-comprehension-self-monitoring-2019.md, raw/papers/arxiv-multilingual-text-to-pictogram-reading-rehabilitation-2026.md, raw/papers/akca-2026-neuroinclusive-emotion-regulation-uxr.md, raw/papers/arakawa-2026-calmreminder-parental-engagement.md, raw/papers/kasatskii-2023-perceptual-load-ide-adhd.md, raw/articles/deep-research-report-stt-neurodiversity-2026.md, raw/papers/husain-2020-supportive-technologies-adhd-slr.md, raw/papers/ara-2026-adhd-productivity-construction-ai-vr.md, raw/papers/selin-2026-self-tracking-masking-neurodivergent.md]
confidence: medium
---

# 支援技術

ADHD文脈の支援技術は、注意・時間・記憶・着手・切り替えを「本人の努力」だけに戻さず、道具や環境へ分散するための設計領域。既存ページでは、[[external-memory]]、[[time-management]]、[[task-initiation]]、[[environment-design]]として生活上の外部化が整理されている。

## 研究から見える傾向

Tanらの成人ADHD向け支援技術スコーピングレビュー予備報告は、3,538件から46件を抽出し、成人ADHDに対する技術ベース支援の研究が近年増えている一方、多くが「肯定的な日常支援」よりも治療・介入の観点に寄っていると述べている。成人では職場や高等教育での困難が子どもとは異なるため、[[executive-function]]をどう外部化するかが設計上の焦点になりやすい。^[raw/papers/tan-2026-adult-adhd-assistive-technologies-scoping-review.md]

LalwaniとSalamの生産性支援ロボット研究は、ADHDのある学生を含む大学生の生産性課題を対象に、参加型デザインで望ましいロボット特性と倫理的配慮を整理している。ただしこれは設計知見であり、症状改善や学業成果を示す臨床試験ではない。^[raw/papers/lalwani-2025-productivity-social-robot-college-students.md]

[[i-have-adhd]] は、支援技術を「利用者本人の予定管理」だけでなく、周囲の道具やエージェントが出す情報の形にも広げる例。答えを先頭に置く、手順を番号化する、次の行動を1つに絞る、といった出力設計で、読者の[[working-memory]]や[[task-initiation]]の負荷を下げようとしている。^[raw/articles/i-have-adhd-github-2026.md]

[[focusmate|Focusmate]]は、支援技術を個人用アプリだけでなく、予約された相手の存在とビデオ共同作業へ広げる例。[[body-doubling]]を道具化しているが、公式ページは製品説明であり、ADHD症状への臨床効果を示す研究ではない。^[raw/articles/focusmate-homepage-2026.md]

センサー、生成AI、ロボット、IDE改変のような支援技術は、便利さと同時に「誰が何を測り、誰が解釈し、本人がどれだけ修正できるか」を問う必要がある。CalmReminderの研究では、保護者は通知をそのまま受け取るだけでなく、称賛、会話、活動計画など自分たちの実践に合わせて使い替えていた。^[raw/papers/arakawa-2026-calmreminder-parental-engagement.md]

開発環境の支援では、KasatskiiらのIDE知覚負荷研究が、視覚的に騒がしい環境と明瞭な環境でプログラミング効率が変わり、ADHD症状の有無によって影響の出方が異なる可能性を示している。これは[[attention-control]]と[[work-routines]]の交点にあるアクセシビリティ課題として扱える。^[raw/papers/kasatskii-2023-perceptual-load-ide-adhd.md]

## 設計上の含意

[[cognitive-personal-informatics]] は、支援技術を「アプリを使わせる」より広く、本人の認知条件を見える形にして、読む・戻る・覚える・始めるための足場を作る設計として捉える。ADHD 学生のデジタル読解と自己モニタリングのずれ、text-to-pictogram のような読解足場は、支援技術を単なる通知や予定表に閉じない根拠になる。^[raw/papers/pubmed-adhd-digital-text-comprehension-self-monitoring-2019.md] ^[raw/papers/arxiv-multilingual-text-to-pictogram-reading-rehabilitation-2026.md]


添付のAI/ソフトウェア調査報告は、支援技術を医療機器、自己管理アプリ、共同作業、服薬支援、学校・職場配慮に分け、規制承認と生活実装のしやすさが一致しない点を強調している。[[digital-adhd-support]]では、製品の便利さと医療的有効性を分けて読む。^[raw/articles/deep-research-report-ai-software-adhd-2026.md]


- 継続的な自己管理を要求するだけの道具は、ADHDの[[working-memory]]や実行機能負荷をむしろ増やすことがある。
- 視覚化、リマインダー、タスク分解、記録検索、環境側の手がかりなど、低摩擦で外部化できる設計が重要になる。
- エージェントや開発道具では、出力そのものを支援技術として設計できる。短さだけでなく、次の行動、現在地、完了したことが見えるかが重要になる。
- 支援技術はプライバシー・監視・依存・通知疲れのリスクも持つ。特にセンサー、録音、画面記録、AI要約を使う道具では、最小限の記録、ローカル処理、削除しやすさを確認したい。

## 音声認識（STT）と神経多様性支援

[[speech-to-text-neurodiversity-support|STTと神経多様性支援]] は、音声認識を ADHD・ディスレクシア・自閉スペクトラムの学習・仕事支援に使う際の設計指針を扱う。ASR の最高精度を競うより、**低信頼語のハイライト、再編集可能性、要約前の人間確認**といった confidence-aware UI が、神経多様性のある利用者の認知負荷を下げる鍵になる。録音＋検索可能な transcript は ADHD 学生の自己ペース学習や聞き逃し補完に有効だが、誤った字幕や同期ずれはむしろ負荷を増やす。^[raw/articles/deep-research-report-stt-neurodiversity-2026.md]

[[genio-notes|Genio Notes]] は、高等教育の障害学生支援向けに設計された録音・文字起こし・ノート化ツールで、「講義中は内容理解に集中し、後から transcript と同期再生で補強する」という、同時処理負荷の低減パターンを実装している。

## 注意点

このページは技術設計と研究動向の整理であり、医療上の助言ではない。製品ページや設計研究は、有効性の証拠と分けて読む。

## 受動記憶アシスタント

[[passive-memory-assistants-adhd]] では、Screenpipe、Rewind/Limitless、Recall などの受動記憶ツールを ADHD 支援として評価する。キャプチャの自動化より、作業復帰・時間定位・次の一手抽出・プライバシー制御が優先される。

## 研究ウォッチからの補助線（2026-08-10）

Husain（2020）のADHD支援技術レビューは子ども中心だが、行動介入、モニタリング、変化支援を柔軟・受容可能・アクセス可能な形で届けるという整理は、成人向け支援にも設計上の参考になる。ただし対象年齢が異なるため、成人ADHDの効果証拠へ直接外挿しない。^[raw/papers/husain-2020-supportive-technologies-adhd-slr.md]

建設現場のADHD生産性に関するAraら（2026）の探索的インタビューは、支援技術を「机上のタスク管理」だけでなく、動的で安全要求の高い職場での注意足場・社会的存在感・動機づけ支援として考える材料になる。AI/VRは有望な設計要求として示されている段階で、実装効果の証明ではない。^[raw/papers/ara-2026-adhd-productivity-construction-ai-vr.md]

Selinら（2026）の神経多様者のセルフトラッキング研究は、記録が常に自己理解を助けるとは限らず、解釈負荷・感情労働・文脈依存性を生むことを示す。ADHD向け支援技術では、データを集めるほどよいのではなく、本人の意味づけと共有の安全性を設計対象にする必要がある。^[raw/papers/selin-2026-self-tracking-masking-neurodivergent.md]

## 関連

- [[speech-to-text-neurodiversity-support]]
- [[genio-notes]]
- [[passive-memory-assistants-adhd]]
- [[screenpipe]]
- [[executive-function]]
- [[time-management]]
- [[task-initiation]]
- [[i-have-adhd]]
- [[focusmate|Focusmate]]
- [[body-doubling]]
- [[cognitive-personal-informatics]]
