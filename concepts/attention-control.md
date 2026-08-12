---
title: 注意制御と妨害刺激
created: 2026-07-23
updated: 2026-08-10
type: concept
tags: [adhd, attention, executive-function, research]
sources: [raw/papers/forster-2014-distraction-task-irrelevant-stimuli-adhd.md, raw/articles/tweet-2080187975636509069-one-note-single-window-distraction-reduction.md, raw/papers/kasatskii-2023-perceptual-load-ide-adhd.md, raw/articles/tweet-2081356392972038227-interruption-tally-three-workplace-tactics.md, raw/articles/tweet-2081363947450712183-boring-to-interesting-conversion-tactic.md, raw/articles/tweet-2085933607072485405-single-task-notification-off.md, raw/articles/tweet-2086067401779548493-visual-audio-efficiency-styles.md, raw/articles/tweet-2086588348848837086-ear-blocking-noise-boundary.md, raw/articles/tweet-2083770574933991552-sensory-load-posture-glasses.md, raw/papers/carr-2026-fielded-attention-adhd-context.md]
confidence: medium
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

## 文脈としての注意

Carr（2026）は、ADHDの注意を個人内の固定的な欠陥としてだけでなく、リズム、手がかり、空間、時間構造、対人関係との相互作用として捉えるFielded Attentionを提案している。これは生物学的説明を否定するものではなく、[[environment-design]]や[[work-routines]]を治療の代替ではなく「注意が成立しやすい場の設計」として読むための概念的補助線である。^[raw/papers/carr-2026-fielded-attention-adhd-context.md]

## 関連

- [[environment-design]]
- [[digital-interruptions]]
- [[task-initiation]]
- [[executive-function]]

- **周囲音を物理的に減らす**: 隣の会話や環境音を勝手に拾って作業へ戻りにくくなる場合、耳栓・イヤーマフ・ノイズキャンセリング等で「注意を奪う入口」を一つ閉じる。静かにする努力ではなく、聴覚刺激そのものを減らす環境設計として扱う。^[raw/articles/tweet-2086588348848837086-ear-blocking-noise-boundary.md]
- **姿勢保持・反射光など上流負荷を疑う**: 姿勢保持や視覚ノイズの処理に注意資源を使っている可能性を考え、姿勢保持ベルトや偏光グラスを小さく試すセルフ実験がある。これは診断や治療の主張ではなく、注意が逸れる前の感覚・姿勢負荷を[[environment-design]]で下げる候補として扱う。^[raw/articles/tweet-2083770574933991552-sensory-load-posture-glasses.md]
