---
title: 注意制御と妨害刺激
created: 2026-07-23
updated: 2026-08-24
type: concept
tags: [adhd, attention, executive-function, research]
sources: [raw/papers/forster-2014-distraction-task-irrelevant-stimuli-adhd.md, raw/articles/tweet-2080187975636509069-one-note-single-window-distraction-reduction.md, raw/papers/kasatskii-2023-perceptual-load-ide-adhd.md, raw/articles/tweet-2081356392972038227-interruption-tally-three-workplace-tactics.md, raw/articles/tweet-2081363947450712183-boring-to-interesting-conversion-tactic.md, raw/articles/tweet-2085933607072485405-single-task-notification-off.md, raw/articles/tweet-2086067401779548493-visual-audio-efficiency-styles.md, raw/articles/tweet-2086588348848837086-ear-blocking-noise-boundary.md, raw/articles/tweet-2083770574933991552-sensory-load-posture-glasses.md, raw/papers/carr-2026-fielded-attention-adhd-context.md, raw/articles/tweet-2088920198589911187-work-variation-width.md, raw/articles/tweet-2090251801463529921-lyrics-free-music-pink-noise.md, raw/papers/ain-2026-mind-wandering-affective-valence-adhd-ema.md, raw/articles/tweet-2090423617716994431-hide-red-notification-badges.md, raw/papers/raffaelli-2025-thought-content-variability-adhd-context.md]
confidence: medium
source_additions_2026-08-23: [raw/articles/tweet-2091433622880629062-super-single-task-physical-friction.md]
---

# 注意制御と妨害刺激

注意制御と妨害刺激のページでは、ADHDの困りごとを「集中力がない」という道徳化ではなく、作業負荷、刺激量、環境設計との相互作用として扱う。

Forsterらの研究は、成人ADHDで課題と無関係な刺激による妨害が増えうること、また知覚負荷がその妨害を変える可能性を示す研究として取り込む。^[raw/papers/forster-2014-distraction-task-irrelevant-stimuli-adhd.md]

Kasatskiiらは、IDE上のプログラミング課題で知覚負荷（視覚的に騒がしい/明瞭）を変え、ADHD症状を持つ開発者とそうでない開発者の効率指標を比較した。全体として低知覚負荷の方が最初の入力や解決時間に有利な結果があり、ADHD症状によって影響が一様ではない可能性も示された。職場や開発環境の配慮では、単に「刺激を減らす」だけでなく、課題の種類・視覚密度・戻りやすさを合わせて見る必要がある。^[raw/papers/kasatskii-2023-perceptual-load-ide-adhd.md]

## 実装上の含意

- [[environment-design]]では、視界・音・通知・タブ・机上物を減らすだけでなく、作業そのものの負荷や明確さも調整対象になる。
- [[digital-interruptions]]では、スマホ通知やSNSの割り込みを「意思が弱い」ではなく妨害刺激として扱う。
- [[task-initiation]]では、最初の一手を明確にして無関係刺激へ流れる余地を減らす。
- 作業アプリや文書を複数窓に分散させると、戻るための判断が増える場合がある。OneNoteを1窓にし、作業中の窓へいつでもワンクリックで戻れる状態にした投稿は、「戻り道を短くする」注意制御として保存する。^[raw/articles/tweet-2080187975636509069-one-note-single-window-distraction-reduction.md]
- 「気になった物は全部しまう」のように、視界に入る未処理物を減らすことは、注意を奪われてから戻すより先に妨害刺激を減らす[[environment-design]]として扱える。
- **中断の定量化**: 1日に何回作業を中断されたかを正の字で数えることで、「集中力がない」という自己責めを「環境の問題」に置き換えられる。投稿者の実測では1日平均47回の中断があり、実働2時間未満だった。紙とペンだけで始められ、診断やカミングアウトも不要。^[raw/articles/tweet-2081356392972038227-interruption-tally-three-workplace-tactics.md]
- **退屈を面白さに変換する**: ADHDの脳は退屈で注意の燃料が切れるため、勉強や作業を「好きなジャンルから入る」「クイズ形式で自分に出題する」などで面白くし、興味駆動で注意を持続させる。歯を食いしばる根性ではなく、退屈を消す工夫で注意を引き出す。^[raw/articles/tweet-2081363947450712183-boring-to-interesting-conversion-tactic.md]

- **1つ終わるまで他を触らない＋通知全OFF**: 新しいタスクやスマホ通知で作業記憶が上書きされる前提で、作業中はタスクを1つに固定し、通知を一時的に全OFFにする。これは[[task-initiation]]だけでなく、戻り道を必要とする割り込み自体を減らす[[digital-interruptions]]対策でもある。^[raw/articles/tweet-2085933607072485405-single-task-notification-off.md]
- **視覚フィードバック型と音境界型を試し分ける**: タスクを書き出して終わったら消すことで進む人もいれば、タイマーやホワイトノイズで外界との境界を作ると過集中へ入りやすい人もいる。ADHD向け対策を万能化せず、[[external-memory]]の視覚化と音環境のどちらが作業を進めるか小さく試す。^[raw/articles/tweet-2086067401779548493-visual-audio-efficiency-styles.md]

- **歌詞なし音楽＋ピンクノイズで音の境界を作る**: 頭の中や周囲音がうるさい時、歌詞なし音楽とピンクノイズを重ねて、作業中の聴覚環境を固定する体験談がある。医療的効果ではなく、注意が散る入口を音で均す低信頼度のセルフ実験として扱う。^[raw/articles/tweet-2090251801463529921-lyrics-free-music-pink-noise.md, raw/papers/ain-2026-mind-wandering-affective-valence-adhd-ema.md]

- **赤い未読バッジを消す／隠す**: 集中中に未読バッジが視界へ入り続けるなら、アプリのバッジ通知を無効化するか、通知領域を視界外へ置く。通知を「後で処理する」という判断ではなく、視覚的な入口そのものを減らす環境調整として扱う。投稿由来の低信頼度の実践例であり、効果は個人差がある。^[raw/articles/tweet-2090423617716994431-hide-red-notification-badges.md]
- **「超シングルタスク」で脱線先を先に消す**: 文章作業ならスマホを電源オフにして手の届かない引き出しへ入れ、ブラウザを閉じ、作業アプリだけを開く。単に我慢するのでなく、物理的距離と画面上の選択肢削減で、注意が移る先を少なくする。個人の低信頼度な実践例であり、緊急連絡が必要な時は代替連絡手段を確保する。[[environment-design]]と組み合わせる。^[raw/articles/tweet-2091433622880629062-super-single-task-physical-friction.md]

## 文脈としての注意

Ainら（2026）のEMA研究は、マインドワンダリングを「意図的」と「意図しない」に分ける重要性を示している。不注意症状が高い人では意図的なマインドワンダリング中の感情価が低く、過活動症状が高い人では逆に高い方向が報告されたため、[[attention-control]]の支援では「それた注意」を一律に悪者化せず、本人にとって回復・探索・回避のどれに近いかを文脈で見る。^[raw/papers/ain-2026-mind-wandering-affective-valence-adhd-ema.md]

Raffaelliら（2025）は、思考への外的・意図的な制約が少ない場面で、過活動症状と「自由に動く思考」/思考内容の変動性の関連が強まることを、Think Aloud課題と7日間EMAで示した。注意制御の実装では、「自由時間だから楽」と決めつけず、低制約の場面ほど[[time-management]]や[[environment-design]]でゆるい枠・手がかり・次の一手を置く意味がある。^[raw/papers/raffaelli-2025-thought-content-variability-adhd-context.md]

Carr（2026）は、ADHDの注意を個人内の固定的な欠陥としてだけでなく、リズム、手がかり、空間、時間構造、対人関係との相互作用として捉えるFielded Attentionを提案している。これは生物学的説明を否定するものではなく、[[environment-design]]や[[work-routines]]を治療の代替ではなく「注意が成立しやすい場の設計」として読むための概念的補助線である。^[raw/papers/carr-2026-fielded-attention-adhd-context.md]

- **作業方法の変数を変えて飽きを避ける**: 注意が途切れる時、タスクを変えるのではなく「どう処理するか」を変える。思考/単純作業、デスクワーク/歩きながら、目先/長期のような軸を持ち、嫌なタスクを別モードへ載せ替えることで、退屈や飽きが生む離脱を下げる。^[raw/articles/tweet-2088920198589911187-work-variation-width.md]

## 関連

- [[environment-design]]
- [[digital-interruptions]]
- [[task-initiation]]
- [[executive-function]]

- **周囲音を物理的に減らす**: 隣の会話や環境音を勝手に拾って作業へ戻りにくくなる場合、耳栓・イヤーマフ・ノイズキャンセリング等で「注意を奪う入口」を一つ閉じる。静かにする努力ではなく、聴覚刺激そのものを減らす環境設計として扱う。^[raw/articles/tweet-2086588348848837086-ear-blocking-noise-boundary.md]
- **姿勢保持・反射光など上流負荷を疑う**: 姿勢保持や視覚ノイズの処理に注意資源を使っている可能性を考え、姿勢保持ベルトや偏光グラスを小さく試すセルフ実験がある。これは診断や治療の主張ではなく、注意が逸れる前の感覚・姿勢負荷を[[environment-design]]で下げる候補として扱う。^[raw/articles/tweet-2083770574933991552-sensory-load-posture-glasses.md]
