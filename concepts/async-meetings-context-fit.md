---
title: 非同期・会議・文脈適合
created: 2026-07-23
updated: 2026-07-23
type: concept
tags: [adhd, autism, work, accessibility, executive-function, attention, tool, research]
sources: [raw/papers/das-2021-accessible-remote-work-neurodivergent.md, raw/papers/liebel-2023-software-engineers-adhd-meetings.md, raw/papers/jameson-2026-sustainable-work-adhd.md, raw/papers/oconnor-2025-autistic-asynchronous-focus-group.md, raw/papers/deshmukh-2025-neurodivergent-aware-productivity-ai.md, raw/articles/welcomebrain-2026-neuroinclusive-meetings.md]
confidence: medium
---

# 非同期・会議・文脈適合

神経発達症の職場支援では、「非同期がよい」「会議が悪い」と単純化しない方がよい。重要なのは、連絡様式がその人の処理時間、作業記憶、感覚負荷、切り替え負荷、社会的安全、外部足場に合っているかである。ここでは仮に **文脈不協** を「仕事の要求・連絡様式・評価規範・本人の調整リズムが噛み合わず、実行機能や対人負荷が余分に増える状態」と呼ぶ。これは[[executive-function]]、[[working-memory]]、[[attention-control]]、[[work-routines]]、[[digital-interruptions]]と接続する。

## 非同期が助ける場面

非同期の文字中心コミュニケーションは、処理時間を確保できる、発話・表情・声色・順番取りの負荷を減らせる、後から読み返せる、記録が[[external-memory]]になる、という利点がある。自閉スペクトラム症の非同期焦点群研究では、参加者が「受け取る側・表現する側の両方で、非同期の方が処理しやすい」と述べ、書き言葉なら表情や身体言語へ注意を割かずに済むと説明している。^[raw/papers/oconnor-2025-autistic-asynchronous-focus-group.md]

ADHDの職場研究でも、会議は単なる情報共有ではなく、聴覚処理、作業記憶、メモ、あとで思い出すこと、予定を忘れないことを同時に要求する。文書、明確な期待、共有メモ、リマインダーは、この負荷を頭の中から環境へ逃がす働きをする。^[raw/papers/jameson-2026-sustainable-work-adhd.md]

## 会議が必要な場面

同期的な場が役立つこともある。外部の存在が着手や注意維持を助ける[[body-doubling]]、曖昧な前提をその場で揃える確認、感情的なすれ違いの修復、共同設計、緊急判断などは、完全非同期より同期の方が足場になる場合がある。ADHD職場研究でも、柔軟性は支援にも負荷にもなり、外部の説明責任がないと注意が散る人もいるとされる。^[raw/papers/jameson-2026-sustainable-work-adhd.md]

したがって会議は「常時開く場」ではなく、**同期でしか得にくいもの**がある時だけ使うのがよい。例: 共同で不確実性を減らす、作業開始を一緒に作る、対立や誤解を修復する、短い意思決定を閉じる。

## 文脈不協の型

1. **速度不協**: 会話が速すぎて処理・返信が追いつかない。
2. **記憶不協**: 会議で決まったことが文書化されず、作業記憶と後日の想起に依存する。
3. **切り替え不協**: 深い作業から会議・チャット・別課題へ移され、戻るための文脈再構築が高くつく。
4. **社会規範不協**: 発言順、暗黙の同意、沈黙の解釈、雑談、表情読みなどが評価に混ざる。
5. **感覚不協**: 音、画面、人数、長時間着席、カメラ常時オンが負荷になる。
6. **評価不協**: 成果ではなく即答、常時可用性、見える稼働、会議での発話量が能力評価に混ざる。
7. **足場不足**: 非同期で自由にされるが、締切、確認、優先順位、着手支援がない。

## AI支援の使いどころ

AIは会議を増やす道具ではなく、文脈不協を下げる道具として使うべきである。具体的には、会議前の論点抽出、必要性判定、議題の短文化、発言候補の下書き、会議後の決定・次の一手・担当者抽出、未返信・未処理の有限化、作業復帰の「さっき何してた？」提示がよい。ADHD向けAI支援の概念研究は、AIをタスク管理者ではなく共調整者として扱い、静かで調整可能、本人のリズムに応じる、同意と停止権を持つ設計を提案している。^[raw/papers/deshmukh-2025-neurodivergent-aware-productivity-ai.md]

ただし、注意の揺れ、遅延、会議欠席、タブ切り替えなどは職場で誤解・監視・差別につながりやすい。AIがこれらを扱う場合は、[[assistive-technology]]として本人側に閉じた支援を基本にし、上司やチームへ出す情報は本人が選ぶ「今は文字がよい」「今日は同期可」「次の確認時刻」程度に絞る。

## Toymaker / OpenBrief への設計含意

- 非同期 brief は、量を増やすのではなく「読む時間」「範囲」「終端」「次に戻る場所」を明示する。
- 会議化する前に、AIが「これは会議・非同期文書・共同作業枠・1:1確認のどれか」を提案する。
- 会議が必要なら、24時間前議題、期待される発言、事前メモ欄、チャット発言、会議後の決定ログを標準にする。
- `availability` は「暇/忙しい」ではなく、通信容量を表す: `文字なら可`, `同期10分だけ可`, `処理中、次回確認14:30`, `会議後復帰中`。
- `Return Anchor` は会議後に必須。会議メモより先に「会議前に何をしていたか」「次の一手は何か」を出す。
- チーム向け可視化は本人の同意制にする。注意推定や遅延理由を共有しない。

## 関連

- [[digital-adhd-support]]
- [[assistive-technology]]
- [[external-memory]]
- [[task-resumption]]
- [[body-doubling]]
- [[fear-of-missing-out]]
