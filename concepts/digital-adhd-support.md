---
title: ADHD向けデジタル支援
created: 2026-07-23
updated: 2026-08-12
type: concept
tags: [adhd, tool, research, therapy, diagnosis, medication, school, work, accessibility, policy]
sources: [raw/articles/deep-research-report-ai-software-adhd-2026.md, raw/articles/tiimo-homepage-2026.md, raw/articles/screenpipe-homepage-2026.md, raw/articles/focusmate-homepage-2026.md, raw/articles/nice-ng87-recommendations-2026.md, raw/papers/pubmed-adhd-ema-daily-life-adolescents-2026.md, raw/papers/arxiv-cognitive-personal-informatics-chi26-2026.md, raw/papers/akca-2026-neuroinclusive-emotion-regulation-uxr.md, raw/papers/arakawa-2026-calmreminder-parental-engagement.md, raw/papers/nordby-2024-blended-emotion-dysregulation-adult-adhd.md, raw/papers/wilens-2024-treating-executive-function-youth-adhd-review.md, raw/papers/kennedy-2026-mhealth-emi-adhd-high-risk-alcohol.md, raw/papers/yitzhak-2025-emotional-pendulum-adhd-ema.md, raw/papers/ben-dor-cohen-2024-emotional-dysregulation-coping-adult-adhd.md, raw/articles/tweet-2085784093686669451-ai-command-thread-project-memory.md, raw/articles/tweet-2086105627697549630-grill-with-docs-milestone-review.md, raw/articles/tweet-2086302039244718116-ai-prioritization-removes-choice.md, raw/articles/tweet-2086307734161588450-two-queue-workstation.md, raw/articles/tweet-1980832956349300817-myndmap-goal-check-in.md, raw/articles/tweet-2086701376911139129-ios-app-parallel-task-focus.md, raw/papers/ara-2026-adhd-productivity-construction-ai-vr.md, raw/papers/selin-2026-self-tracking-masking-neurodivergent.md, raw/papers/ruf-2023-diet-physical-activity-impulsivity-adult-adhd-ema.md, raw/articles/tweet-2086998621673968112-claude-code-remind-watch-organize.md, raw/articles/tweet-2084915057650208912-adhd-pomodoro-no-extra-restarts-app.md, raw/articles/tweet-2087416492082258023-ai-close-meeting-attention-residue.md]
confidence: medium
---

# ADHD向けデジタル支援

ADHD向けデジタル支援は、診断、症状把握、治療補助、認知訓練、生活支援、服薬支援、コーチング、学校・職場配慮をまたぐ広い領域。添付の深層調査報告は、2026年時点では「万能な単独治療」ではなく、診療・教育・就労支援の隙間を埋める補助層として見るのが妥当だと整理している。^[raw/articles/deep-research-report-ai-software-adhd-2026.md]

## エビデンスの階層

- **比較的強い領域**: ゲーム型デジタル治療、一部の親支援アプリ、成人向けの一部オンラインCBT。報告では EndeavorRx / ENDEAVORRIDE / EndeavorOTC / Prismira などが、主に注意指標の改善を示す規制承認済みまたは市場化された例として挙げられている。^[raw/articles/deep-research-report-ai-software-adhd-2026.md]
- **中程度・限定的な領域**: QbTest / QbCheck のような診断補助。NICEは6〜17歳の標準臨床評価に追加する選択肢としてQbTestを推奨するが、単独診断は不可で、成人では研究段階とされる。これは[[diagnosis-and-management]]の補助情報として読む。^[raw/articles/deep-research-report-ai-software-adhd-2026.md]
- **研究・観察として有用な領域**: EMA（日常場面での短い反復記録）や [[cognitive-personal-informatics]]。症状を一回の尺度だけでなく場面差として見る助けになるが、入力負荷と監視化の危険がある。^[raw/papers/pubmed-adhd-ema-daily-life-adolescents-2026.md]
- **実用性は高いが医療証拠が薄い領域**: [[tiimo|Tiimo]]、Goblin Tools、Shimmer / Indy、[[focusmate|Focusmate]]のような自己管理・実行機能・共同作業支援。これらは生活上の[[task-initiation]]や[[external-memory]]には役立ちうるが、医療効果の確立とは分ける。^[raw/articles/deep-research-report-ai-software-adhd-2026.md]

## 新しい設計研究からの注意点

成人ADHDの感情調整支援では、生成AIを設計リサーチの仮説整理に使う提案や、対面グループとアプリを組み合わせる小規模な実現可能性研究が出ている。ただし、AkcaらはUXR方法論、Nordbyらは非ランダム化の予備研究であり、どちらも単独で治療効果を確立するものではない。[[emotion-regulation]]や[[cognitive-behavioural-therapy]]と接続して、設計候補と臨床エビデンスを分けて読む。^[raw/papers/akca-2026-neuroinclusive-emotion-regulation-uxr.md] ^[raw/papers/nordby-2024-blended-emotion-dysregulation-adult-adhd.md]

CalmReminderは、子どもの落ち着いた状態を腕時計センシングで推定し、保護者へジャストインタイム通知する設計プローブである。対象は成人ADHDではなく、4週間・16家族規模のHCI研究なので、医療効果ではなく「通知は本人・家族の実践に合わせて再解釈される」という[[assistive-technology]]設計の示唆として扱う。^[raw/papers/arakawa-2026-calmreminder-parental-engagement.md]


## EMA/EMIと個別化支援

Kennedyら（2026）は、高リスク飲酒を伴う若年成人ADHD向けに、EMAを自己認識・個別フィードバック・行動戦略提案へ接続するmHealth EMIの開発過程を報告している。これは効果試験ではなく設計・開発の論文だが、日常場面のデータを使う支援では、本人とコミュニティのフィードバック、人間中心設計、入力負荷、プライバシー、過剰な自己監視を慎重に扱う必要がある。^[raw/papers/kennedy-2026-mhealth-emi-adhd-high-risk-alcohol.md]

感情調整のEMA研究（Yitzhakら, 2025; Ben-Dor Cohenら, 2024）は、日常の感情変動や自己認識・戦略選択の個人差を可視化できる一方で、測定それ自体が支援になるとは限らないことも示している。[[emotion-regulation]]や[[cognitive-personal-informatics]]と同様、データは人格評価ではなく「どの文脈で支援が必要か」を本人側に戻す材料として扱う。^[raw/papers/yitzhak-2025-emotional-pendulum-adhd-ema.md] ^[raw/papers/ben-dor-cohen-2024-emotional-dysregulation-coping-adult-adhd.md]

## セルフトラッキングと文脈依存性

成人ADHDや神経多様性を扱うデジタル支援では、EMAや自己記録を「客観データを増やすほど良い」と単純化しない。Rufら（2023）は成人ADHDを含む日常EMAで、食事・身体活動・状態衝動性の短時間関係を調べたが、主要な食事成分と状態衝動性の関連は見られなかった。これは食事助言ではなく、日常データで仮説を検証することの価値と限界を示す材料として読む。^[raw/papers/ruf-2023-diet-physical-activity-impulsivity-adult-adhd-ema.md]

一方、Selinら（2026）は、神経多様者のマスキングに関するセルフトラッキングが、洞察だけでなく解釈負荷や感情的負担も生むことを示した。[[cognitive-personal-informatics]]では、本人が安全に意味づけできる最小限の記録、必要に応じたピア共有、評価・監視への転用防止を重視する。^[raw/papers/selin-2026-self-tracking-masking-neurodivergent.md]

建設現場研究（Araら, 2026）は、AI/VR支援を注意足場、社会的存在感、動機づけ支援として構想している。職場向けデジタル支援は、本人の欠陥補正ではなく、現場の[[work-routines]]と安全・連携要求に合う環境側の補助として読む。^[raw/papers/ara-2026-adhd-productivity-construction-ai-vr.md]

## 当事者実践から見えるデジタル支援パターン

- **AIツールの分業と司令塔化**: Claude Code、GPT、NotebookLM、音声入力などを用途別に分け、プロジェクトごとの司令塔スレッドに背景・判断・再開文脈を集約する実践がある。これは治療ではなく、[[external-memory]]と[[task-resumption]]をAI会話で支える生活・仕事上の工夫として扱う。入力する業務情報・個人情報・機密情報の範囲は慎重に制限する。^[raw/articles/tweet-2085784093686669451-ai-command-thread-project-memory.md]
- **マイルストーン・レビュー用AI**: AI/ドキュメント支援ツールを常時伴走ではなく、区切りごとのレビュー役として使う実践がある。これは診断・治療ではなく、作業のブレを減らす[[work-routines]]上の支援として扱う。ツール導入で満足して作業が進まないリスクも一緒に設計対象にする。^[raw/articles/tweet-2086105627697549630-grill-with-docs-milestone-review.md]
- **順番決定・待ち行列管理の外部化**: Claude Codeに優先順位と着手順を決めさせる、あるいはPC/自動処理を通常キューと緊急キューに分ける実践は、AIやデジタル道具を『何でもやる相棒』ではなく、選択肢・割り込み・再開順を外部化する装置として使う例である。機密情報を入れすぎない範囲で、[[task-initiation]]と[[work-routines]]の判断負荷を下げる用途として扱う。^[raw/articles/tweet-2086302039244718116-ai-prioritization-removes-choice.md] ^[raw/articles/tweet-2086307734161588450-two-queue-workstation.md]
- **目標チェックインの強制表示**: MyndMapのGoal Check-In投稿は、タイマー終了時に目標確認を画面へ出し、XPや再スタート時の戦略提案で継続を支える設計を示している。[[time-management]]と[[task-initiation]]をつなぐ実用UI候補だが、製品投稿なので独立した効果検証とは分ける。^[raw/articles/tweet-1980832956349300817-myndmap-goal-check-in.md]
- **自作の集中・タスク絞り込みアプリ**: 仕事を7つほど並行して何も進まなくなる場面に対し、Claude Codeで自分用のiOSアプリを作り、タスク管理と「今集中する対象」の絞り込みに使う投稿があった。既製品に合わせるだけでなく、AI開発ツールで自分の実行機能の弱点に合わせた小さな道具を作る例として扱う。医療効果ではなく、[[work-routines]]と[[task-initiation]]のデジタル補助。^[raw/articles/tweet-2086701376911139129-ios-app-parallel-task-focus.md]
- **Claude Codeの起動フック・指示書・ログを実行機能の補助へ使う**: 失敗ログ末尾5件の自動読込、雑な入力と整形の分離、ルール破りの言い訳リスト、記録漏れ検知フレーズ、場面別の「観察」ファイルは、AIに判断や記憶を丸投げするのではなく、本人が忘れやすい確認点を実行環境へ埋め込む設計として読める。機密情報や個人情報を入れすぎない範囲で、[[work-routines]]と[[external-memory]]に接続する。^[raw/articles/tweet-2086998621673968112-claude-code-remind-watch-organize.md]

- **自分用に定番技法を作り替える小アプリ**: ポモドーロが休憩後の再着手を増やして逆効果になる場合、AI開発ツール等で「動き出しを楽にする」「余計な休憩を入れない」自分用アプリへ変える実践がある。これはデジタル支援を既製品選びだけでなく、自分の失敗パターンに合わせた小さな環境改造として使う例である。^[raw/articles/tweet-2084915057650208912-adhd-pomodoro-no-extra-restarts-app.md]


- **会議後・中断前後をAIで「閉じる」**: 会議直後90秒以内にAIへメモを貼り、「決定事項」と「自分がやるタスク3つ」だけを出させる。中断前には「ここまでやった。次は○○から」と1行残し、戻った時は「最初の3分でやることだけ」を聞く。AIを万能秘書ではなく、注意残留を閉じ、再開地点を外へ置き、着手単位を小さくする[[task-resumption]]支援として使う実践。^[raw/articles/tweet-2087416492082258023-ai-close-meeting-attention-residue.md]

- **メッセージハブをAI操作の入口にする**: Beeper DesktopのMCP連携を使い、複数チャットの検索、返信案、未返信リマインドをAIに補助させる投稿があった。これは分散した連絡経路を[[external-memory]]へ集約する実践だが、AIに会話内容を渡す範囲、個人情報、送信前確認を明確にする必要がある。^[raw/articles/tweet-2087489223616336198-beeper-message-hub-ai-reminders.md]
- **生成AIによる白紙破壊**: Claude Codeに「空の関数だけ」作らせるなど、生成AIを成果物作成ではなく着手前の空白を消す道具として使う実践がある。[[task-initiation]]では、最初の一手を外部化するデジタル支援として扱う。^[raw/articles/tweet-2087487424754757725-ai-empty-function-first-step.md]

## 実装上の要点

- AIは診断の代行ではなく、臨床家・教師・本人・保護者の意思決定を支える補助として設計する。
- 症状尺度だけでなく、学業、就労、家事、欠席・欠勤、生活の質、継続率などの現実の機能指標を見る。
- 未成年者データ、行動ログ、服薬記録、生成AI入力、画面・音声・予定情報は機微情報として扱う。
- 学校・職場では、アプリそのものより、通知の量、配慮設計、負荷設計、導入後のフォロー、同意と監視化の回避が重要になる。

## Wikiでの読み方

この添付報告は有用な横断整理だが、内部に検索由来の引用記号を含む二次的な調査報告であり、一次論文・規制資料そのものではない。強い主張は、今後のingestでPMDA、FDA、NICE、RCT、系統的レビューなどの一次資料に戻して検証する。

## 非同期・会議・AI支援

[[async-meetings-context-fit]] は、AI支援を「会議を自動化する道具」ではなく、処理時間、記録、作業復帰、通信容量の調整を助ける道具として扱う。特に職場では、注意推定や反応遅延を評価者へ露出せず、本人側の[[external-memory]]と[[task-resumption]]へ閉じることが重要である。

## 関連

- [[speech-to-text-neurodiversity-support]]
- [[genio-notes]]
- [[async-meetings-context-fit]]
- [[assistive-technology]]
- [[cognitive-personal-informatics]]
- [[diagnosis-and-management]]
- [[cognitive-behavioural-therapy]]
- [[medication]]
- [[task-initiation]]
- [[external-memory]]
