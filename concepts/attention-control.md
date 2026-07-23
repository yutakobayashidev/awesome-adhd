---
title: 注意制御と妨害刺激
created: 2026-07-23
updated: 2026-07-23
type: concept
tags: [adhd, attention, executive-function, research]
sources: [raw/papers/forster-2014-distraction-task-irrelevant-stimuli-adhd.md, raw/articles/tweet-2080187975636509069-one-note-single-window-distraction-reduction.md, raw/papers/kasatskii-2023-perceptual-load-ide-adhd.md]
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

## 関連

- [[environment-design]]
- [[digital-interruptions]]
- [[task-initiation]]
- [[executive-function]]
