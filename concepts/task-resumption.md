---
title: 作業再開
created: 2026-07-23
updated: 2026-09-05
type: concept
tags: [adhd, executive-function, working-memory, attention, work, research]
sources: [raw/papers/ratwani-2008-spatial-memory-task-resumption.md, raw/papers/masicampo-2011-plan-making-unfulfilled-goals.md, raw/articles/tweet-2088418166884139504-next-line-before-close.md, raw/articles/tweet-2096176512861089838-interruption-resumption-anchor.md]
confidence: medium
---

# 作業再開

作業再開は、中断された後に「どこまでやったか」「次に何をするか」へ戻る働き。ADHDでは、通知、会議、家事、会話、タブ移動の後に作業の文脈が消えやすく、[[working-memory]]と[[executive-function]]の負荷が高くなる。

Ratwani & Traftonは、空間記憶が作業再開を導くことを示す研究として取り込む。ADHD Wikiでは、机上配置、ウィンドウ配置、カーソル位置、チェックリストの途中位置などを「再開の手がかり」として設計する根拠候補にする。^[raw/papers/ratwani-2008-spatial-memory-task-resumption.md]

Masicampo & Baumeisterの計画作成研究は、未完了目標をただ頭に置くのではなく、具体的計画として外部化することで認知的な残り続けを減らす隣接研究として読む。^[raw/papers/masicampo-2011-plan-making-unfulfilled-goals.md]

## 実装上の含意

- 中断前に「次はここから」を1行残す。
- 終了時に「次はここに数字を入れる」のような、次回そのまま実行できる一行を残してから閉じる。再開時に思い出すのではなく、終了時の文脈を[[external-memory]]へ渡す。^[raw/articles/tweet-2088418166884139504-next-line-before-close.md]
- 電話など避けられない中断の直前には、作業中の行または次操作を付箋に一行で残す。電話当番の時間分割や静かな場所の集中枠と組み合わせると、再開の記憶を探す工程を減らせる可能性がある。個人投稿に基づく低信頼度の実践であり、付箋に機密情報を残さない。^[raw/articles/tweet-2096176512861089838-interruption-resumption-anchor.md]
- 画面・紙・物理位置を、戻る場所が分かる形に保つ。
- [[screenpipe]]のような作業履歴検索や、[[i-have-adhd]]の現在地表示は、作業再開支援として読める。
- [[digital-interruptions]]をまとめると、再開回数そのものを減らせる。

## 会議後の復帰

[[async-meetings-context-fit]] では、会議後に議事録だけを出すのでは不十分で、会議前に開いていた作業、最後の状態、次の一手を短く返す `Return Anchor` が重要になる。これは同期予定が作業文脈を切る場面の復帰足場である。

## 受動記憶による復帰支援

[[passive-memory-assistants-adhd]] の文脈では、キャプチャから「最後に開いていたファイル」「次にやる操作」「中断前の意図」を自動抽出し、再開パックとして提示することが作業復帰の有力な手段になる。

## 関連

- [[passive-memory-assistants-adhd]]
- [[async-meetings-context-fit]]
- [[working-memory]]
- [[external-memory]]
- [[digital-interruptions]]
- [[executive-function]]
