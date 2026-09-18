---
title: デジタル割り込み
created: 2026-07-23
updated: 2026-09-10
type: concept
tags: [adhd, attention, time-management, executive-function, tool, research, lived-experience, japanese-context]
sources: [raw/papers/baughan-2022-design-influences-dissociation-social-media.md, raw/papers/fitz-2019-batching-smartphone-notifications-wellbeing.md, raw/papers/kushlev-2015-checking-email-less-stress.md, raw/papers/hiniker-2016-mytime-smartphone-non-use.md, raw/papers/forster-2014-distraction-task-irrelevant-stimuli-adhd.md, raw/articles/tweet-2082033754877661336-smartphone-friction-notification-off.md, raw/articles/tweet-2087071615096074718-game-login-pre-timer-friction.md, raw/articles/tweet-2088971788453580825-procrastinate-bad-habits-friction.md]
source_additions_2026-09-10_research_watch: [raw/papers/misirlic-2026-engagement-trap-short-form-video-adhd.md]
source_additions_2026-09-10_x: [raw/articles/tweet-2098012610939551918-recommended-tab-blocker.md]
confidence: medium
---

# デジタル割り込み

デジタル割り込みは、スマホ通知、メール確認、SNSの流れ、アプリ設計によって注意が細切れになる問題。ADHD Wikiでは、本人の意志だけでなく、通知設計・画面設計・再開手がかり・環境調整の問題として扱う。

Baughanらは、SNS設計が利用中の解離的な体験にどう影響するかを扱うHCI研究として取り込む。Fitzらはスマホ通知をまとめること、Kushlev & Dunnはメール確認頻度を減らすこと、Hinikerらはスマホ非利用を支えるMyTime介入を扱う研究として取り込む。^[raw/papers/baughan-2022-design-influences-dissociation-social-media.md]^[raw/papers/fitz-2019-batching-smartphone-notifications-wellbeing.md]^[raw/papers/kushlev-2015-checking-email-less-stress.md]^[raw/papers/hiniker-2016-mytime-smartphone-non-use.md]

ForsterらのADHD妨害刺激研究と合わせると、通知やSNSは単なる誘惑ではなく、課題無関係刺激として[[attention-control]]と[[task-resumption]]の負荷を増やすものとして設計できる。^[raw/papers/forster-2014-distraction-task-irrelevant-stimuli-adhd.md]

## 実装上の含意

- 通知は即時受信ではなく、まとめて受ける時間を作る。
- メール確認は常時開放せず、確認回数と時間帯を決める。
- SNSや動画は開始前に終了条件、アプリ制限、物理的な離席を用意する。
- スマホ自体を触りにくくする。グレースケール化、SNSアプリをホーム画面から消す、別室に置くなど、小さな摩擦を入れる。電話以外の通知を切り、対応時間を明記しておくと「見ないこと」への不安も下げられる。^[raw/articles/tweet-2082033754877661336-smartphone-friction-notification-off.md]
- 中断後の[[task-resumption]]を助けるため、作業中の次の一手を残す。

- **ゲームを開く前にタイマーを1つ増やす**: 「ログインだけ」が1時間に伸びる問題は、開いた後に我慢するより、開く前に15分タイマーをかけるなど入口に摩擦と終了手がかりを置く。SNS制限と同じく、本人の意志ではなくアプリ開始前の儀式で時間の境界を作る。^[raw/articles/tweet-2087071615096074718-game-login-pre-timer-friction.md]

- **やめたい習慣を先延ばしさせる**: スマホやSNSを我慢するのではなく、触るまでの動作を面倒にする。スマホを玄関に置く、Xを開く前に英単語8割正解を要求する自作拡張を挟む、など「先延ばししても、実行しても勝ち」になる摩擦を入口へ置く。[[task-initiation]]で弱点になる先延ばしを、望まない行動の抑制へ逆利用する設計。^[raw/articles/tweet-2088971788453580825-procrastinate-bad-habits-friction.md]

- **おすすめフィードの入口を消す／条件化する**: おすすめタブを非表示にする拡張機能、または閲覧前に別の行動を求める拡張機能のように、無限スクロールの「最初の一手」に摩擦を置く。開いた後の自己制御ではなく入口設計に委ねる低信頼度の個人実践であり、拡張機能は権限・データ収集・提供元を確認してから使う。^[raw/articles/tweet-2098012610939551918-recommended-tab-blocker.md]

## 研究ウォッチからの更新（2026-09-10）

Misirlicら（2026）は、TikTok・Instagram Reels・YouTube Shortsのような短尺動画推薦を「エンゲージメント・トラップ」として整理し、Prolific成人302人（ADHD報告150人、非ADHD 152人）の調査で、推薦内容の関連性は群間で大きく否定されない一方、ADHD群では視聴を止めにくいこと、時間感覚の喪失、利用後の後悔、否定的感情が高いと報告した。これは短尺動画を単なる意志力問題ではなく、[[attention-control]]、[[time-management]]、[[impulsivity-countermeasures]]を同時に圧迫する推薦システム上のアクセシビリティ問題として読む材料になる。^[raw/papers/misirlic-2026-engagement-trap-short-form-video-adhd.md]

同論文が質問紙上で提示した支援案は、フィード除去のフォーカスモード、利用リマインダー、強制休憩、固定本数モード、無限スクロールをやめる手動送り、視覚的な経過時間表示、ラビットホールを崩す多様性注入である。ただし、これらは実装評価ではなく記述に対する好意度評価なので、効果証拠ではなく、短尺動画・SNS設計で外部停止手がかりと利用量の上限をどう埋め込むかの設計候補として扱う。^[raw/papers/misirlic-2026-engagement-trap-short-form-video-adhd.md]

## 関連

- [[attention-control]]
- [[task-resumption]]
- [[hyperfocus-control]]
- [[time-management]]
- [[environment-design]]
