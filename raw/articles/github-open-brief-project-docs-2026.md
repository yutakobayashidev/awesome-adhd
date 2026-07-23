---
source_url: https://github.com/yutakobayashidev/open-brief/tree/main
ingested: 2026-07-23
sha256: a5b0e26c17823f6203ef24a25d6f53b785c20a3a224cf2378b13e6ac3efad002
---

# GitHub source snapshot: yutakobayashidev/open-brief
- Repository: https://github.com/yutakobayashidev/open-brief
- Snapshot commit: `7d4f363`
- Ingested for wiki query: 2026-07-23


---

## Source file: `README.md`

# OpenBrief

Androidアプリの静的解析と認知科学・HCI研究を、独立したAttention Triageアプリの設計へ変換するための調査リポジトリです。

## Architecture Decisions

- [ADR一覧](docs/adr/README.md)
- [ADR 0001: Local-firstなデータ境界とModel Gateway](docs/adr/0001-adopt-local-first-data-and-model-boundaries.md)
- [ADR 0002: Attention SignalとSlack Status Output](docs/adr/0002-adopt-attention-signals-and-slack-status-output.md)

## Tiimo調査レポート

- [調査概要と目次](docs/reverse-engineering/tiimo/README.md)
- [独自実装ブループリント](docs/reverse-engineering/tiimo/05-reimplementation-blueprint.md)

## Attention Triage研究

- [研究概要と目次](docs/research/attention-triage/README.md)
- [Gmail＋RSSゴールデンケース](docs/research/attention-triage/03-golden-case.md)
- [TiimoとOpenBriefの比較](docs/research/attention-triage/05-tiimo-comparison.md)
- [構想の客観評価](docs/research/attention-triage/06-objective-assessment.md)
- [GC-01実装fixture](fixtures/golden-cases/gc-01-gmail-rss-return.json)
- [評価プロトコル](docs/research/attention-triage/04-study-protocol.md)

解析対象APKは `apks/com.tiimo.androidappreactnative/` に置かれています。APKや復元コードを配布・転載することを目的としていません。


---

## Source file: `docs/research/attention-triage/README.md`

# Attention Triage研究

## まず読む

OpenBriefの目標は、好奇心を抑えることではありません。

> 知りたいことを有限の探索へ変え、探索前に持っていた意図へ戻れるようにする。

ユーザーはニュースから着想を得たい一方、無限スクロールへ入ると、返信、締切、中断中の作業が見えなくなることがあります。OpenBriefは情報を禁止せず、探索の境界、好奇心の退避先、元の作業へ戻る手掛かりを提供します。

## 60秒で分かる構想

```text
Gmail / RSS
    ↓ 常駐Agentが読み取り専用で収集
Observation Inbox
    ↓ 重複排除・トピック化・根拠保持
Protect: 見失いたくない意図を最大3件だけ確認
    ↓
Signal: 応答状態と復帰予定を本人確認後に周囲へ共有
    ↓
Explore / Focus: 最大6件の有限ブリーフ、または集中作業
    ↓
Capture: 気になった問いを義務にせず退避
    ↓
Return: 探索前の作業と次の一手を再提示
```

最初の研究質問は次です。

> 有限ブリーフ、好奇心の退避、再開手掛かりは、着想価値と自律性を維持しながら、予定外の探索延長と義務の見落としを減らせるか。

## 文書一覧

| 文書 | 読む目的 |
|---|---|
| [01 Research foundations](01-research-foundations.md) | 認知科学・HCIの根拠と限界を確認する |
| [02 Product model](02-product-model-and-hypotheses.md) | 製品仮説、設計原則、反証条件を確認する |
| [03 Golden case](03-golden-case.md) | Gmail＋RSSを使う理想的な1セッションを共有する |
| [04 Study protocol](04-study-protocol.md) | N-of-1と小規模比較研究を実施する |
| [05 Tiimo comparison](05-tiimo-comparison.md) | 静的解析したTiimoとOpenBriefの共通点・相違点を確認する |
| [06 Objective assessment](06-objective-assessment.md) | 構想の強み、kill risk、継続・停止条件を確認する |
| [GC-01 fixture](../../../fixtures/golden-cases/gc-01-gmail-rss-return.json) | ゴールデンケースを実装・テスト用の入力と期待状態として使う |

## 根拠の読み方

本文では、研究の質とOpenBriefへの適用距離を混同しないため、主張を次のtierへ分けます。

| 表記 | 意味 |
|---|---|
| E1 | OpenBrief自体を対象にした実証結果。現時点では存在しない |
| E2 | 近接する認知機構やUIを扱った実験・field study |
| E3 | 観察、自己報告、質的研究、review、間接的な知見 |
| H | OpenBrief固有の未検証仮説 |
| R | プライバシー、自律性、安全性から置く規範的要件 |

「ADHDなら必ずこうなる」「無限スクロールはドーパミン依存を起こす」「hyperfocusはADHDの中核症状」とは断定しません。診断の有無ではなく、探索中に以前の意図が見えなくなる行動パターンを対象にします。

## Oracleレビュー

2026-07-21にOracleからGPT-5.6 SolをExtra High reasoningで利用し、既存のUX、実装、セキュリティ文書を添付して第二モデルレビューを行いました。Oracleの回答は助言として扱い、本文の研究主張は一次論文または原著論文へのリンクで再確認しました。

Oracleと文献調査が一致した重要点は次です。

- 好奇心を義務達成の報酬にしない
- Curiosity CaptureをTodoへ自動変換しない
- ニュース閲覧前にReturn Anchorを残す
- 強制ロックではなく、本人が上書きできる摩擦を使う
- 単純な通知バッチングを上回るか検証する

## 現在の決定

- 義務系の最初のsource: Gmail
- 好奇心系の最初のsource: RSS / OPML
- Slack message input: Gmail＋RSSで中核仮説を検証した後に追加
- Slack status output: 最初のOutput Adapterとして、本人操作とexpiration付きで追加
- カレンダー書き込み: ユーザーの明示確認後だけ
- 自動返信、自動委任、強制ブロック: MVP対象外


---

## Source file: `docs/research/attention-triage/01-research-foundations.md`

# 01. 認知科学・HCIの研究基盤

## 結論

OpenBriefは「集中力を増やすアプリ」ではなく、好奇心を残しながら、遅延した意図と元作業への復帰経路を保護するシステムとして設計します。

研究から直接言えるのは、好奇心には学習上の価値があること、情報取得や通知の頻度を有限化すると負担が下がる場合があること、中断後の復帰には外部手掛かりが役立つことです。

一方、有限トピックブリーフ、Curiosity Capture、Return Anchorを組み合わせた効果は未検証です。ここがOpenBriefの研究対象です。

## 対象となる問題

```text
返信・義務
├── 報酬が遅い
├── 開始点が曖昧
└── 実行まで意図を保持する必要がある

ニュース・SNS
├── 新奇性と不確実性がある
├── 情報取得自体に価値がある
└── 次の項目が無制限に供給される

競合すると
└── 元の意図が見えなくなり、探索後の復帰に失敗する
```

この連鎖全体をADHD成人で直接実証した研究はありません。各要素を別の研究が支え、統合した因果モデルは製品仮説です。

## エビデンス表

| 論点 | 主な結果 | Tier | 設計への含意 |
|---|---|---|---|
| 好奇心 | 好奇心は情報を得るための行動、報酬関連活動、記憶向上と関連した | E2 | 好奇心を除去せず、安全な探索方法へ変換する |
| Hyperfocus | ADHD特性と長時間の没入に自己報告上の関連がある | E3 | 診断語ではなく、切替困難を行動として測る |
| 遅延した意図 | ADHD成人の実験では、記憶保持より計画形成と切替で大きな差が出た | E2 | 「後で」を具体的な次の一手と時刻へ変換する |
| 中断と再開 | 中断後の復帰には元目標の文脈・視覚的位置などの手掛かりが役立つ | E2 | 探索前にReturn Anchorを保存する仮説へつなげる |
| 終了手掛かり | reading-history labelや「確認済み」が終了基準として使われた | E2/E3 | 残件数と明示的な終端を検証する |
| 通知バッチング | 予測可能な時刻への通知集約が、通常通知より注意や統制感を改善した | E2 | 収集は常時、提示は1日2回から始める |
| 通知なし | 通知を表示しない条件でFoMOや不安が高かった | E2 | 情報アクセスを禁止せず、override可能にする |
| 価値ベースの制御 | 本人が無価値と判断した利用だけを減らし、価値ある利用を維持できた | E2 | 総利用時間ではなく、後悔する利用を減らす |

E1は空欄です。OpenBrief固有の効果は、実装後のN-of-1から初めて埋まります。

## 好奇心は保護対象である

Kangらの実験では、好奇心の高さが情報を得るための資源支出、報酬関連領域の活動、後の記憶と関連しました。好奇心を単なる誘惑として扱うと、OpenBriefが守るべき学習と着想まで損ないます。

KobayashiとHsuは、情報の主観的価値と金銭的報酬に共通する神経表現を報告しました。ただし、これを「SNSは薬物と同じ」「ドーパミン依存」と言い換えることはできません。

設計上の結論は、情報価値を否定せず、無境界な供給形式だけを変更することです。

## Hyperfocusの扱い

成人Hyperfocus質問紙の研究では、ADHD症状との関連や、趣味・画面利用など複数場面での自己報告が示されています。ただし、初期研究は新規尺度と自己報告診断を多く含みます。

したがって、研究文書では次の観測可能な語を使います。

- 新奇情報による注意捕捉
- 探索からの離脱困難
- 意図したタスク切替の遅延
- 元作業への復帰失敗

OpenBriefはADHDの診断、症状判定、治療を行いません。

## 遅延した意図と計画

Fuermaierらは、ADHD成人45人と対照45人を比較し、複雑なprospective memory課題で、特に計画形成とタスク切替に大きな群差を報告しました。一方、計画の想起と自己開始の差は小さい、または有意でない部分がありました。

この結果から「ADHDの人は返信を忘れる」と一般化はできません。製品上は、返信候補をInboxへ置くだけでなく、次の物理的行動、実行時刻、実行文脈を本人が確定できるようにします。

## 有限性と提示タイミング

Baughanらは、43人が4週間使うカスタムTwitterクライアントへreading-history label、list、時間dialogなどを導入しました。「確認済み」を終了基準にしたという知見には質的発言が含まれ、日次集約データから因果方向を確定できない限界があります。これは有限トピックブリーフの直接証拠ではなく、明確な終端を検討する近接証拠です。

Fitzらの237人のランダム化field studyでは、通知を1日3回にまとめた条件で注意、生産性、気分、統制感が改善しました。通知を表示しない条件では不安やFoMOが高くなりましたが、アプリを開いて情報へアクセスすること自体は禁止されていません。

KushlevとDunnの124人の被験者内実験では、メール確認を1日3回に制限した週の方が、無制限の週より日々のストレスが低くなりました。

OpenBriefはこれらから「収集は常時、提示は予測可能な有限セッション」という仮説を導きます。

## 再開手掛かり

RatwaniとTraftonの研究では、元作業の視覚的位置が中断後の再開を導きました。MasicampoとBaumeisterは、未完了目標について具体的な計画を作ることで、別課題への認知的干渉が下がることを報告しました。

OpenBriefのReturn Anchorは次を保存します。

```text
戻る対象: 認証テストの修正
再開点: refresh tokenの失敗ケース
次の一手: 401を期待するtestを1件追加
戻る時刻: 13:00
```

この短いカード自体の効果は未検証です。既存研究から導いた、検証対象の設計仮説です。

## 直接は支持されていない主張

- 無限スクロールがADHD固有の依存を起こす
- HyperfocusがADHDの確立した中核症状である
- ニュースを義務の報酬にすれば実行率が上がる
- AIの重要度判定が人間の判断より正確である
- 情報閲覧時間が短いほど健康または生産的である

## 主要文献

- Kang et al. (2009), [Epistemic Curiosity Activates Reward Circuitry and Enhances Memory](https://doi.org/10.1111/j.1467-9280.2009.02402.x)
- Kobayashi & Hsu (2019), [Common neural code for reward and information value](https://doi.org/10.1073/pnas.1820145116)
- Hupfeld et al. (2019), [Living in the zone: hyperfocus in adult ADHD](https://doi.org/10.1007/s12402-018-0272-y)
- Hupfeld et al. (2024), [Validation of the dispositional adult hyperfocus questionnaire](https://doi.org/10.1038/s41598-024-70028-y)
- Forster et al. (2014), [Increased distraction by task-irrelevant stimuli in adults with ADHD](https://doi.org/10.1037/neu0000020)
- Fuermaier et al. (2013), [Complex Prospective Memory in Adults with ADHD](https://doi.org/10.1371/journal.pone.0058338)
- Jylkkä et al. (2023), [Everyday prospective memory in adult ADHD](https://doi.org/10.1038/s41598-023-36351-6)
- Ratwani & Trafton (2008), [Spatial memory guides task resumption](https://doi.org/10.1080/13506280802025791)
- Masicampo & Baumeister (2011), [Plan making can eliminate cognitive effects of unfulfilled goals](https://doi.org/10.1037/a0024192)
- Baughan et al. (2022), [How Design Influences Dissociation on Social Media](https://doi.org/10.1145/3491102.3501899)
- Fitz et al. (2019), [Batching smartphone notifications can improve well-being](https://doi.org/10.1016/j.chb.2019.07.016)
- Kushlev & Dunn (2015), [Checking email less frequently reduces stress](https://doi.org/10.1016/j.chb.2014.11.005)
- Hiniker et al. (2016), [MyTime: Designing and Evaluating an Intervention for Smartphone Non-Use](https://doi.org/10.1145/2858036.2858403)


---

## Source file: `docs/research/attention-triage/02-product-model-and-hypotheses.md`

# 02. 製品モデルと検証仮説

## 中核命題

> OpenBriefは、価値ある探索や集中へ安全に入り、応答状態を周囲へ伝え、元の作業と会話へ戻るためのAttention Transition layerである。

成功とはSNS利用時間が短くなることだけではありません。本人が価値を感じる探索を維持したまま、探索前の意図へ戻れる確率が上がり、集中中の不在と復帰予定を周囲が予測できることです。

## 概念モデル

```text
新奇な情報
    ↓
情報探索の内発的価値が高まる
    ↓
終了地点のない探索が続く
    ↓
元作業の文脈と遅延した意図が弱まる
    ↓
返信・締切・作業への復帰が遅れる
    ↓
後悔、焦り、回避が生じる
```

OpenBriefは次の5点へ介入します。

| 介入 | 役割 |
|---|---|
| Boundary | 無限ストリームを終了地点のあるトピックへ変える |
| Offload | 気になる問いを、義務にせず退避する |
| Continuity | 探索前の作業と次の一手を残す |
| Agency | 続ける、戻る、後回し、無視を本人が決める |
| Social legibility | 応答不能と復帰予定を本人が選んだ範囲で周囲へ伝える |

次の式は法則ではなく、測定変数を整理するためのモデルです。

```text
意図の見落としリスク
≈ 新奇性の誘引 × 情報の無境界性 × 切替回数
  ÷ 義務の可視性 × 再開手掛かり × 自己決定感
```

## 設計原則

### 1. 好奇心ではなく配信形式を有限化する

- 1回のブリーフは最大6トピック
- 残件数と推定読了時間を表示
- 「今回分は以上」を必ず表示
- 自動追加、自動再生、無限スクロールを使わない

### 2. Curiosity CaptureをTodoにしない

保存するのはリンクだけでなく、「何が気になったか」「次に知りたい問い」「起点トピック」です。期限、優先度、見積時間は要求しません。

状態は`気になる / 一度読んだ / 深掘り候補 / 手放す`とします。未処理件数や完了率を成功指標にしません。

### 3. 探索前にReturn Anchorを残す

最低限、現在の作業、再開点、次の物理的操作を保存します。入力は10秒以内、一文で完了できる必要があります。

### 4. 義務をニュースの入場券にしない

返信を完了するまでニュースを禁止しません。見失う損失が大きい可能性のある項目を最大3件だけ見せ、本人が`今日扱う / 後で / 対象外 / 委任候補`を選びます。

### 5. AIは結論ではなく判断材料を作る

カードには、表示理由、情報源、日時、根拠、不明点、確信度を含めます。AIが重要と判断したことと、本人にとって重要であることを区別します。

### 6. 摩擦は制裁ではなく遷移点に置く

摩擦は、深掘り開始、時間延長、外部サービスへの書き込みだけに置きます。すべてのカード操作へ確認を要求しません。overrideは常に可能で、overrideを失敗として扱いません。

### 7. 認識済みタスクは複製せず参照する

Todoist、GitHub、calendarなどに既に存在するタスクは、元サービスをsource of truthとします。OpenBriefはtitle、期限、完了、繰り返し、subtaskを管理し直しません。

OpenBriefが所有するのは、「なぜ今見るか」「今日守るか」「次の一手」「探索後にどこへ戻るか」です。完了や予定変更を外部へ書き戻す場合は、対象と変更内容を本人が確認してから実行します。

### 8. 注意状態を本人の内側だけで完結させない

集中や探索を始める本人の操作に合わせ、応答状態と復帰予定のSignalを周囲へ共有できます。Signalは任意であり、FocusやExploreの入場条件にしません。

最初のOutput AdapterはSlack custom statusです。作業内容ではなくavailabilityだけを既定で共有し、expirationを必須にします。AIによる状態推定だけで公開せず、本人のSlack上の変更を上書きしません。詳細は[ADR 0002](../../adr/0002-adopt-attention-signals-and-slack-status-output.md)で固定します。

## ドメイン上の役割

| Entity | 意味 | タスク化されるか |
|---|---|---|
| Observation | Gmail/RSSから得た根拠付きの出来事 | されない |
| Topic | 複数Observationを束ねた話題 | されない |
| DecisionCandidate | 返信、確認、深掘りなどの判断候補 | 本人が決める |
| ProtectedIntent | 見失いたくない返信・予定・中断作業 | 本人が確定する |
| ExternalTaskRef | 外部サービスが所有する認識済みタスクへの参照と状態snapshot | 複製されない |
| AttentionSignal | 応答状態、復帰予定、共有先、実際の適用結果 | 外部へ書く前に本人が選ぶ |
| CuriosityCapture | 後で戻れる問いと起点 | デフォルトではされない |
| ReturnAnchor | 探索前の作業と次の一手 | 再開時に提示する |

Gmailをすべて義務、RSSをすべて好奇心とは扱いません。ニュースレターはGmailでも好奇心になり、セキュリティ警告はRSSでも義務候補になります。

CuriosityCaptureは、本人が明示的に`タスクにする`を選んだ場合だけ外部タスク管理へhandoffします。作成後はExternalTaskRefを保持し、同じ問いから重複タスクを作りません。

## 仮説

| ID | 仮説 | 主要評価 |
|---|---|---|
| H1 | 有限ブリーフは生フィードより探索超過時間を減らす | 選択時間からの超過分 |
| H2 | Curiosity Captureは好奇心満足を落とさず終了率を上げる | 終端到達率、好奇心満足 |
| H3 | Return Anchorは元作業への復帰を早める | 復帰率、復帰時間 |
| H4 | Override可能な摩擦は強制ロックより迂回と反発が少ない | override、外部SNS、リアクタンス |
| H5 | Protect段階は返信・期限の見落としを減らす | 自己設定期限の超過率 |
| H6 | ブリーフ化しても価値ある着想が維持される | 24時間後も有用な着想数 |
| H7 | 本人操作とexpiration付きのSlack statusは、privacy discomfortを増やさず復帰予定を周囲に伝える | 追加ping、復帰予測、privacy discomfort |

## 反証条件

次の場合、中核仮説を棄却または大幅修正します。

- 探索時間と同時に、高価値な着想も継続的に減る
- 十分な取得精度と利用率があっても、返信や作業復帰が改善しない
- 有限化、Capture、Returnが単純な通知バッチングを上回らない
- Curiosity Captureが罪悪感のあるバックログになる
- native feedへの迂回、アプリ回避、雑な完了処理が増える
- AIの偽陰性により、通常利用より重要項目の発見が遅れる
- 修正、分類、source管理の負担が削減した負担を上回る

## 非目標

- ADHDの診断または治療
- ニュース、SNS、好奇心の禁止
- スクリーン時間の最小化
- AIによる重要度・返信要否の最終決定
- 生産性スコア、streak、ランキングによる評価
- 自動返信、自動委任、自動カレンダー登録
- AIの推定だけをtriggerにしたstatus更新、DND、channel投稿


---

## Source file: `docs/research/attention-triage/03-golden-case.md`

# 03. Gmail＋RSSゴールデンケース

実装・テストで使う機械可読版は[GC-01 fixture](../../../fixtures/golden-cases/gc-01-gmail-rss-return.json)です。fixtureの入力境界は、Gmail/RSSの生データではなく、常駐Agentが共通形式へ正規化した直後の`Observation`です。

## ゴール

> 面白いニュースを安心して探索し、得た着想を失わず、探索前の作業と今日必要な返信へ戻れる。

このケースは完全なAI判定を前提にしません。sourceの同期状態、AIの確信度、ユーザーの訂正、外部サイトへ移動した場合まで含めます。

## Personaではなく行動条件

利用者を診断名で定義しません。次の状態を対象とします。

- 技術ニュースから新しい着想を得ることに価値を感じる
- 面白い話題を見つけると予定以上に探索することがある
- 探索後、返信や元の作業を思い出すまで時間がかかる
- ニュースを禁止したいのではなく、安全に読みたい

## シナリオ

火曜日の12:30です。ユーザーは認証テストを修正しています。昼のブリーフ時刻になりました。

常駐Agentは次を収集済みです。

### Gmail

- 直近24時間のInbox: 12 thread
- 返信候補: 1件
- 参考共有: 1件
- newsletter / automated: 10件
- 最終同期: 12:27

返信候補は、共同研究者から届いた「木曜の実験枠を確定できますか」というメールです。AIは返信必要の確信度を`0.84`としていますが、断定はしません。

### RSS

- OPML登録feed: 18
- 新規item: 47件
- 重複排除後: 31件
- トピックcluster: 4件
- 最終同期: 12:25

最上位トピックは、常駐Agentの新しいmemory設計に関する3記事です。ユーザーのOpenBrief構想と関係します。

## End-to-end flow

| 時刻 | User | System | 保存する状態 | 研究上の観測 |
|---|---|---|---|---|
| 12:30 | ブリーフを開く | source coverageとAnchor Checkを表示 | BriefSession開始 | 開始時刻 |
| 12:31 | メールを「今日扱う」にする | 15:30、10分の予定案を提示 | ProtectedIntent | AI判定修正、予定選択 |
| 12:31 | 予定案を確認する | 明示確認後にcalendarへ書く | Calendar link | 確認回数 |
| 12:32 | 現在地を一文で保存する | Return Anchorを確定 | 認証test、次の一手 | 入力時間 |
| 12:32 | 有限ブリーフを読む | 4トピック、推定8分、残件数を表示 | Topic read state | 閲覧時間、切替数 |
| 12:35 | Agent memoryを「今見る」にする | 3件の有限なevidence packetを表示 | Exploration開始 | 深掘り開始理由 |
| 12:40 | 新しい問いを保存する | タスク化せずCuriosity Captureへ保存 | 問い、起点、source | Capture時間 |
| 12:41 | 「今回分は以上」に到達する | Return Anchorを再表示 | Exploration終了 | 終端到達 |
| 12:42 | 認証testへ戻る | 対象fileまたはFocusを開く | Return実行 | 復帰時間 |
| 15:30 | 返信枠を開始する | 根拠付き返信cardを表示 | Intent開始 | 着手・完了 |

## 画面1: Anchor Check

最初に全Todoや未読件数を見せません。

```text
見失いたくないことが1件あります

共同研究者から実験枠の確認
受信: 今日 09:14
候補理由: 質問文あり / 木曜への言及 / 自分が宛先
確信度: 84%

[今日扱う] [後で確認] [返信不要] [委任候補]

ニュースを先に見ることもできます
```

「今日扱う」は即時返信を強制しません。ユーザーが時刻と所要時間を確認してから予定化します。

## 画面2: Return Anchor

ブリーフ前の入力は10秒以内を目標にします。

```text
ニュースの後、どこへ戻りますか？

認証testの修正
次: refresh失敗時に401を期待するtestを追加

[保存してブリーフへ]
```

Focus中なら現在のItemとsubtaskから候補を作れますが、自動確定しません。

## 画面3: Finite Brief

```text
昼のブリーフ
4トピック・約8分

1. Agent memory設計に3件の更新
2. 利用中libraryのsecurity advisory
3. HCI研究会の新着論文
4. 読んでいるblogの更新

残り 4 / 4
```

各トピックには次を含めます。

- 何が変わったか
- なぜ表示されたか
- sourceと取得時刻
- 根拠2〜4件
- 不明点と確信度
- 推定読了時間

security advisoryはRSS由来でも義務候補です。sourceではなく内容と本人の判断でlaneを変更します。

## 画面4: Curiosity Capture

```text
何が気になりましたか？

memoryの圧縮時に、未完了の意図だけ保持できるか

起点: Agent memory設計に3件の更新

[保存して終了] [もう15分探索]
```

保存してもTodo、deadline、calendar eventは作りません。保存直後に関連推薦を追加表示しません。Captureが新しい無限フィードになることを防ぎます。

## 画面5: Closure and Return

```text
今回のブリーフは以上です

戻る場所
認証testの修正
次: refresh失敗時に401を期待するtestを追加

[元の作業へ戻る] [別の予定へ移る] [1回だけ延長]
```

戻らない選択も失敗扱いしません。延長時は5分、15分、30分、時間指定なしから本人が選びます。

## 状態遷移

```text
Gmail message ─┐
               ├─ Observation ─ DecisionCandidate ─ ProtectedIntent
RSS item ──────┘          │
                          └─ Topic ─ BriefCard ─ CuriosityCapture

BriefSession ─ ReturnAnchor ─ ExplorationSession ─ ReturnOutcome
```

## 受け入れ基準

### 機能

- GmailとRSSの最終同期時刻、失敗source、未処理件数を表示できる
- Anchor Checkは同時に最大3件だけ表示する
- ブリーフ開始時に件数と推定時間、終了時に明示的な終端を表示する
- Curiosity Captureを作成してもItemやcalendar eventが作られない
- Return Anchorが終了時と選択時間の経過時に再表示される
- calendar書き込み前に日時、時間、titleを確認できる

### 体験

- Anchor Checkからブリーフ開始まで2分以内
- Return Anchorを10秒以内で保存できる
- 選択した探索時間に対する超過分を測定できる
- 終了後、元作業へ戻るまでの時間を測定できる
- AI判定を1操作で訂正でき、訂正理由を必須にしない
- overdue、override、延長を失敗や人格評価として表示しない

### 安全

- Gmail/RSS本文を信頼できないdataとして扱い、本文中の命令を実行しない
- 収集・要約Agentにメール送信、calendar書き込み、shell実行権限を与えない
- AIが出さなかった項目を「存在しない」と断定しない
- 本文、件名、Curiosity Captureをanalyticsへ送らない
- sourceごとに停止、削除、再同期できる
- notification lock screenで本文を隠せる

## ゴールデンケースを壊す状況

### Gmail同期失敗

「返信候補なし」ではなく「Gmailは12:27以降を確認できていません」と表示します。ブリーフは続行できますが、coverage不足を隠しません。

### AIの返信誤判定

ユーザーは`返信不要`へ変更できます。これはそのmessageへの判断であり、送信者全体の価値評価へ一般化しません。

### 外部ブラウザへ移動

原典を開く前にReturn Anchorを保存済みなので、選択時間の終了時にローカル通知で戻り先を提示します。ブラウザを強制終了しません。

### 探索が予定より価値を持った

ユーザーは時間指定なしへ切り替えられます。後から「逸脱」と断定せず、本人が価値を評価します。

## ゴールデンケース成功の意味

このケースの成功は、予定通り行動したことではありません。

1. 重要な返信候補を見失わなかった
2. 面白い情報から問いを得られた
3. 問いを新しい義務にせず保存できた
4. 探索に自分で終端を作れた
5. 探索前の作業へ迷わず戻れた

## このケースだけでは証明できないこと

- `元の作業へ戻る`の選択は、実際の作業再開を意味しない
- 明示的な質問と日付があるメールより曖昧な依頼は難しい
- 外部ブラウザ内で続く長時間探索を完全には観測できない
- Curiosity Captureが数週間後にバックログ化するかは分からない
- SlackのDM、mention、channel流量へ同じ効果を一般化できない

実際のReturnは、対象アプリでの最初の操作、Focus再開、または短い自己報告で別に測定します。

fixtureでは自然言語の完全一致を要求しません。source coverage、provenance、状態遷移、副作用の有無を契約とし、所要時間や主観評価はE2E計測または研究指標として扱います。


---

## Source file: `docs/research/attention-triage/04-study-protocol.md`

# 04. 評価プロトコル

## 研究目的

OpenBriefの目的は、利用時間の最小化ではありません。価値ある探索を保ちながら、義務の見落とし、予定外の探索延長、元作業への復帰コストを減らせるか検証します。

## Primary research question

> GmailとRSSを有限トピックブリーフへ変換し、Curiosity CaptureとReturn Anchorを提供すると、同じ候補を時系列で提示する通知バッチより、着想価値と自律性を維持しながら、探索超過時間と意図の見落としを減らせるか。

通常のGmail・RSS利用との差はWeek 1のbaselineで探索的に確認します。機構の因果効果を比べる主比較では、提示内容を揃えた条件Aを使います。

## N-of-1

### 対象

最初は開発者本人を対象にします。診断や臨床症状の改善ではなく、日常の注意遷移と意図保持を評価します。

### 期間

合計6週間を想定します。

| 期間 | 条件 | 目的 |
|---|---|---|
| Week 1 | 通常のGmail・RSS利用 | baseline取得 |
| Week 2〜5 | セッション単位でA/B/C/Dをランダム化 | 各機構の追加効果を比較 |
| Week 6 | フル構成を自由利用 | 自発的に継続できるか確認 |

### 条件

| 条件 | 体験 |
|---|---|
| A | 同じ候補を時系列で並べた通知batch |
| B | Aと同数の最大6件をtopic単位へまとめた有限ブリーフ |
| C | B＋Curiosity Capture |
| D | C＋Return AnchorとAnchor Check |

各条件で候補となるObservation poolと表示件数を揃えます。条件Dだけ重要なメールを多く見せると、UI機構ではなく内容差を測ることになります。

### 比較と反証

| Claim | Comparator | Primary measure | Fidelity gate | Falsifier |
|---|---|---|---|---|
| topic化の効果 | B vs A | 探索超過、重要情報の再認 | 同じObservation pool | 差がない、またはBが悪い |
| Captureの効果 | C vs B | 終端到達、好奇心満足 | Captureを利用可能 | 終端が増えない、backlog負担が増える |
| Returnの効果 | D vs C | Return率、latency | Anchorが保存済み | 復帰が改善しない |
| 統合効果 | D vs A | 見落とし、探索超過、着想価値 | source同期成功 | batching以上の便益がない |

### Primary outcomes

| 指標 | 定義 |
|---|---|
| 探索超過時間 | 実際の探索時間 − 開始時に選んだ時間 |
| 意図の見落とし | 本人が扱うと決めた返信・作業が自己設定期限を超えた数 |
| Return率 | ブリーフ後30分以内にReturn Anchorの作業へ戻った割合 |
| Return latency | 終了画面から元作業の最初の操作までの時間 |

時間指定なしを選んだsessionは探索超過時間から除外し、別に集計します。

### Secondary outcomes

- 24時間後にも価値があると評価した着想数
- Curiosity Captureの後日利用率
- native Gmail/RSS/SNSへの迂回率
- AI判定修正率と偽陰性
- 主観的な好奇心満足、自律性、圧迫感、後悔

## 短い主観評価

毎回すべてを尋ねると、測定自体が介入になります。各ブリーフ後は次の4項目だけを7段階で取得します。

1. 今の行動を自分で選んだと感じる
2. 好奇心を満たせた
3. 元の作業へ戻りやすかった
4. 操作に邪魔された、または責められたと感じる

週次にはNASA-TLX、自律性満足・阻害、FoMO、システム負担を追加できます。MVPでは尺度を増やしすぎず、行動ログを主要評価にします。

## 暫定判断基準

次は科学的に確立された閾値ではなく、開発前に固定する製品判断基準です。

- 探索超過時間がbaselineより20%以上減る
- 意図の見落としまたは自己設定期限超過が減る
- 高価値と評価した着想数がbaselineの90%未満へ落ちない
- 自律性または好奇心満足が7段階で0.5点以上悪化しない
- native sourceへの迂回率が継続的に増えない

結果を見て閾値を変更する場合は、探索的分析として明示します。

## 小規模比較研究

N-of-1で実装と測定可能性を確認した後、24〜36人の被験者内探索研究を行います。

募集は診断名ではなく、次の行動条件で行います。

- 情報を追って予定以上の時間を使うことがある
- その後、返信や元作業を忘れることがある
- ニュースや情報探索自体はやめたくない

比較条件は`通常利用 / 有限ブリーフ / フル構成`です。義務先行の強制ゲートは主要製品条件にせず、override可能な短い実験条件として、反発と迂回を確認する場合だけ使います。

## 分析

- 参加者内の差を中心にする
- 曜日、時間帯、メール量、締切量を記録する
- 平均だけでなく、参加者ごとの効果方向を示す
- p値だけでなく効果量と不確実性区間を報告する
- ADHD診断の有無による事後的な因果説明をしない

source同期に失敗したsession、eligible item数が条件間で揃わないsession、Return Anchorが保存されなかったsessionは、UI仮説の失敗と分けてfidelity failureとして報告します。除外する場合も件数と理由を残します。

## Falsification checklist

- [ ] 有限化により高価値な着想まで減っていないか
- [ ] 単純な通知バッチングより追加効果があるか
- [ ] Curiosity Captureが未処理バックログになっていないか
- [ ] Return Anchorが実際の作業復帰を改善しているか
- [ ] AIの偽陰性が通常利用より見落としを増やしていないか
- [ ] 修正・分類・source管理の負担が便益を上回っていないか
- [ ] 強制感、恥、アプリ回避、別端末への迂回が増えていないか

## Data minimization

研究ログへ保存するのは、時刻、状態遷移、所要時間、判定修正、本人による価値評価です。次はanalyticsへ保存しません。

- Gmail本文、件名、送信者
- RSS本文とCuriosity Captureの内容
- Return Anchorの本文
- access token、source固有ID
- AI promptとraw response

研究用IDとproduction user IDを分けます。参加者はsource単位で収集停止、データ確認、削除、exportを行える必要があります。

## 実装前に固定するもの

- Primary outcomeと算出方法
- session除外条件
- source取得失敗の扱い
- baseline期間
- 判断閾値
- exploratory analysisの範囲

これらを実装後に決めると、都合のよい指標だけを選ぶ余地が増えます。


---

## Source file: `docs/research/attention-triage/06-objective-assessment.md`

# 06. OpenBrief構想の客観評価

## 結論

**研究用prototypeは続行する。独立SaaSへの本格投資は保留する。**

2026-07-21時点のOpenBriefには、検証する価値のある研究仮説があります。一方、製品市場適合、重大メールの見落としを防ぐ安全性、継続利用、事業上の防御力は実証されていません。

```text
現在の判断

研究prototype     Go
local-first OSS   条件付きGo
独立B2C SaaS      Hold
大規模事業化       No-Goに近い
```

総合点をあえて1つにすると、現時点では **5.5 / 10前後** です。この点数は「弱いアイデア」という意味ではありません。問題は重要で、仮説も明確ですが、効果と事業性を示すOpenBrief固有の証拠がまだない、という意味です。

次に作るべきものは統合基盤ではなく、3週間で中核仮説を壊せる比較実験です。

> 単純な有限batchと一行の復帰手掛かりを超える複雑さに、本当に追加価値があるか。

## 評価の前提

- 評価日: 2026-07-21
- 対象: 現在の研究文書、GC-01 fixture、Tiimo静的解析との比較
- E1: OpenBrief自体の実証結果はまだ存在しない
- 第二モデルレビュー: Oracle経由のGPT-5.6 Sol、Extra High reasoning
- 外部確認: 一次研究、公式製品ページ、Google公式要件

この評価は完全な意味で「客観的」ではありません。現在入手できる証拠に評価範囲を限定し、支持する材料と中止理由を同じ基準で並べたスナップショットです。

競合の機能は各社の公式説明に基づきます。利用者数、継続率、実際の効果までは独立に確認していません。Oracleの回答も結論ではなく、見落としを減らすための助言として扱います。

## 何を作ろうとしているか

OpenBriefの価値は、複数sourceの収集やAI要約そのものではありません。仮説の中心は、注意の遷移を次の順番で支援することです。

```text
義務を見失わない
    ↓
応答できない状態と復帰予定を周囲へ伝える
    ↓
好奇心を有限に探索する
    ↓
気になった問いをタスク化せず残す
    ↓
探索前の作業へ戻る
```

この流れを製品用語へ置き換えると、`Protect → Signal → Explore / Focus → Capture → Return`です。Signalは、集中や探索で応答できない状態と復帰予定を、本人が選んだ範囲で周囲へ出力します。

- Protect: Gmailなどから、今日見失いたくない意図だけを本人が確定する
- Signal: 応答状態と復帰予定を、本人が選んだ範囲で周囲へ伝える
- Explore / Focus: RSSなどを有限のtopicとして読む、または集中作業を行う
- Capture: 気になった問いを新しい義務へ変えず退避する
- Return: 探索前のcontextと次の一手を再提示する

個々の仕組みには近接研究があります。

- 通知のbatchingは、通知の割り込み方とwell-beingの関係を変え得る
- 明示的な終端やstop cueは、無限feedより利用終了を助け得る
- 中断前のresumption cueは、作業再開を助け得る

ただし、それらを統合したOpenBriefの効果は未検証です。したがって、現段階で主張できるのは「効果がある」ではなく「安価に反証でき、検証する意味がある」です。

## スコアカード

10点は強い証拠があり危険が低い状態、5点はもっともらしいが未検証の状態を表します。

| 観点 | 点数 | 判断理由 |
|---|---:|---|
| 問題の重要性 | 8 / 10 | 義務の見落とし、探索超過、作業復帰は明確で切実な問題 |
| 概念上の差別化 | 6 / 10 | CaptureをTodo化せず、Returnまで一連に扱う点は特徴がある |
| 研究上の新規性 | 6 / 10 | 個別要素は既知だが、注意遷移protocolとしての統合は検証余地がある |
| 構成概念妥当性 | 4 / 10 | 現行指標では「戻ると選んだ」と「実作業へ復帰した」が混ざる |
| prototype実現性 | 8 / 10 | Wizard-of-Ozとlocal dataだけで中核仮説を試せる |
| 複数sourceの製品化 | 5 / 10 | adapter、認証、同期失敗、source差を扱う必要がある |
| 採用と信頼 | 4 / 10 | 重要情報を隠す製品には、一度の重大な見落としでも不信が生じる |
| 防御力 | 3 / 10 | 要約、prompt、adapter、有限feedは模倣されやすい |
| 製品市場適合 | 4 / 10 | 強い個人的painはあるが、他者の継続利用と支払意思は未確認 |
| 安全性・privacy準備 | 5 / 10 | read-only、人間確認は良いが、運用・監査設計は未完成 |

用途別の判断は次のとおりです。

| 位置づけ | 評価 | 理由 |
|---|---:|---|
| HCI研究テーマ | 7 / 10 | 反証可能な問いと測定対象を作れる |
| 個人用local-first OSS | 8 / 10 | privacyとdistributionの負担を抑えて本人のpainを解ける |
| 特定prosumer向けtool | 6 / 10 | 開発者・研究者などには行動patternが合う可能性がある |
| 独立B2C SaaS | 4 / 10 | trust、継続率、Gmail要件、支払意思が未検証 |
| VC型の大規模事業 | 3 / 10 | distributionと防御力の根拠が弱い |

## 最も強いBuild argument

最も強い続行理由は、**重要で、統合に意味があり、しかも安価に反証できる仮説**だからです。

普通の情報整理toolは「より多く集め、より効率よく読む」方向へ進みます。OpenBriefは、情報接触の前後まで扱います。

1. 探索前に守りたい意図を外在化する
2. 探索範囲に終端を作る
3. 着想を義務へ変えず保存する
4. 元のcontextへ戻る手掛かりを出す
5. 実際に戻れたかを測る

特に`Curiosity Capture`と`Return Anchor`の組み合わせは、単なるdigestとの差を作れる可能性があります。これが実測で効けば、研究上も製品上もOpenBriefの中心になります。

## 最も強いStop argument

最も強い中止理由は、**価値を出すには情報を隠す必要がある一方、安全であるには重要な義務を隠してはならない**という緊張です。

OpenBriefは接触情報量を減らすほど便利になります。しかし、返信期限、請求、セキュリティ警告などを一度でも誤って隠すと、ユーザーは元のInboxを二重確認します。その時点で注意負荷が減らず、OpenBriefが新しいInboxとして増えます。

```text
絞り込みを弱める
    → 安全だが、元のInboxと差がない

絞り込みを強める
    → 便利だが、重大なfalse negativeが怖い
```

この問題を解かないままGmail API、複数adapter、LLM分類、calendar連携を作ると、高コストな統合基盤だけが先に完成します。

## 市場で既に提供されているもの

2026-07-21時点で、次の機能単体は差別化になりません。

- 複数sourceの収集
- AI要約
- daily brief
- 重要メールとTodoの抽出
- RSSや動画の有限digest
- 音声briefing
- アプリを開く前の摩擦や時間制限

公式ページ上では、近接製品が既に次を提供しています。

| 製品 | 近接機能 | OpenBriefへの含意 |
|---|---|---|
| Google Gemini Daily Brief | Gmail、Calendar、Gemini chatsの優先表示、返信や予定化の提案 | Gmail起点のdaily priorityだけでは差別化できない |
| DailyStack | Gmail、Outlook、Calendar、GitHub、Linear、Jira、Todoistなどのdigest | 多source統合そのものは既存category |
| Nudget | RSS、YouTube、X、podcast、newsletterなどのmorning briefing | 好奇心sourceの集約と要約は既に提供される |
| Shortwave | AIによるmail整理、重要mail、Todo、bundle、配信schedule | Gmail triageは成熟した競争領域 |
| one sec | app前のfriction、意図確認、制限、blocking | 強制せず注意遷移を支えるUXも近接領域がある |

したがって、OpenBriefが検証すべき差は次の3点です。

1. Curiosity CaptureをTodoへ変換しないこと
2. 探索前の作業contextを保存し、後で再提示すること
3. `return_chosen`と実際の作業復帰を分けて測ること

## 防御力の評価

現時点の競争上の防御力は弱いです。

- promptは模倣できる
- source adapterは競合も作れる
- topic化とsummaryはmodelの標準能力になる
- 有限feedはUIとして再現しやすい

将来、次のいずれかが実証されれば防御力になり得ます。

- OpenBrief固有protocolによる実測済みのReturn改善
- 個人ごとに、どの介入が効くかを学習するpolicy
- agentやCLIから安全に書き込めるadapter ecosystem
- local-first、read-only、根拠表示による信頼
- 「読む効率化」ではなく「注意遷移」というcategory framing

ただし、これらは現時点ではmoatではなく候補です。

## Top 5 kill risks

### 1. 重要な義務をAIが隠す

- 発生確率: 中〜高
- 重大度: 致命的
- 早期signal: 元Inboxの二重確認、保護漏れ、critical mailの見落とし
- 対応: 初期実験ではshadow modeにし、AIにmailを非表示にさせない

### 2. OpenBrief自体が新しいInboxや儀式になる

- 発生確率: 高
- 重大度: 高
- 早期signal: 未処理badge、Capture backlog、長い朝のtriage、罪悪感
- 対応: CaptureをTodo化しない、残件を義務表示しない、処理時間を測る

### 3. 単純な有限batchと復帰メモに勝てない

- 発生確率: 中〜高
- 重大度: 致命的
- 早期signal: topic化、AI理由、分類を足してもReturnや探索超過が改善しない
- 対応: content量を揃えた比較で、各機構の増分効果を測る

### 4. source、認証、privacyの費用が便益を超える

- 発生確率: 高
- 重大度: 高
- 早期signal: adapter保守に研究時間の大半を使う、OAuth審査が必要になる
- 対応: 最初はlocal import、manual export、Wizard-of-Ozで試す

### 5. 成功しても既存製品に吸収される

- 発生確率: 高
- 重大度: 高
- 早期signal: competitorがReturnやfinite briefingを標準機能として追加する
- 対応: 機能数ではなく、対象行動、実測効果、信頼modelに集中する

## 研究設計の評価

### 現在の位置づけ

- 研究上の新規性: 6 / 10
- 構成概念妥当性: 4 / 10
- 現在のfull paper readiness: 3 / 10
- 再設計とfield study後の可能性: 7 / 10

現在のN-of-1は、instrumentationと本人の行動patternを確認するpilotとして有用です。しかし、OpenBriefの有効性、ADHDへの効果、一般的な製品市場適合の証拠にはなりません。

### 直すべき交絡

#### 1. Return条件で複数要素を同時に変えない

Return AnchorとAnchor Checkを同じ条件だけへ入れると、どちらが効いたか分かりません。最初はReturn Anchorの有無だけを変えます。

#### 2. deep linkを全条件へ揃える

Anchor条件だけtargetへのlinkを持つと、復帰改善が記憶支援ではなくnavigation短縮で説明できます。全条件へ同じlinkを置き、保存contextの有無だけを変えます。

#### 3. 実作業への復帰を測る

`return_chosen`や最初のtarget操作だけでは、実質的な作業復帰とは言えません。

暫定的には次を満たした場合を`substantive return`とします。

```text
対象contextを開く
かつ
2分以上継続する、または意味のある編集・操作を行う
```

#### 4. AIが隠した対象も安全性評価へ含める

ユーザーがProtectしたmailだけを分母にすると、AIが候補へ出さなかった重要mailが測れません。独立したaudit用gold setを作り、action-required recallとhigh-loss false negativeを評価します。

#### 5. 時間を記録できないsessionを捨てない

測定不能sessionを除外すると、失敗しやすい条件だけが消える可能性があります。発生率を記録し、総時間とsession単位の結果を併記します。

#### 6. 24時間後の着想価値を過信しない

自己評価は期待や需要特性の影響を受けます。保存後に実際に参照、共有、試作、執筆へ使われたかも補助指標にします。

#### 7. 対象者を診断名で広げない

初期対象は、診断の有無ではなく次の行動条件で募集します。

> 情報を調べ始めると、直前の作業へ戻ることが難しいと自己報告する人。

RSS利用者は技術系prosumerへ偏ります。また、有限RSSだけの結果を無限SNSへ一般化できません。

## 最初に狙う利用者

最初から「ADHD向け生産性アプリ」として広く売るべきではありません。診断や治療効果を主張せず、行動patternで対象を絞る方が妥当です。

有望な初期対象は次です。

- 開発者
- 研究者
- security analyst
- creator
- GmailとRSSや技術newsを頻繁に使うprosumer
- 情報収集の価値を感じる一方、元作業への復帰に失敗しやすい人

初期形態は、企業による従業員監視型serviceではなく、個人用のlocal-first tool、browser extension、IDE extensionが適しています。

## 技術・privacy feasibility

local-firstなデータ境界、BYOM、remote送信条件は、[ADR 0001](../../adr/0001-adopt-local-first-data-and-model-boundaries.md)でAcceptedの技術判断として固定しています。Signal段階とSlack Status Outputの境界は、[ADR 0002](../../adr/0002-adopt-attention-signals-and-slack-status-output.md)で固定しています。

### prototype

中核仮説のprototypeは実現可能です。production用Gmail APIや常駐agentは不要です。

- mailとRSSを手動またはlocal fileで入力する
- 人間が裏で候補を作るWizard-of-Oz方式を使う
- 実験UIだけを作る
- sourceへの書き込みは行わない
- 全Observationをaudit可能に残す

### public Gmail integration

公開SaaSでrestricted Gmail dataをserver側へ保存、転送、処理する場合、OAuth verificationや年次security assessmentが必要になる可能性があります。

また、Gmail pushの`watch`は少なくとも7日ごとの更新が必要で、notificationの遅延や欠落も考慮しなければなりません。

したがって、Gmailは「小さなadapter」ではありません。personal use、test環境、local処理は初期検証を軽くしますが、そのままpublic distributionの解決にはなりません。

## 3週間の最小実験

### 今回は作らないもの

- production Gmail API連携
- 複数source adapter基盤
- LLMによる自動重要度分類
- Calendar書き込み
- 常駐agent運用
- 認証、課金、組織管理
- podcast、動画生成

### 実験デザイン

2×2のwithin-subject randomized designを使います。

| 要因 | 条件1 | 条件2 |
|---|---|---|
| presentation | 時系列の有限batch | topic化した有限brief |
| resumption | Return Anchorなし | 一行のReturn Anchorあり |

全条件で次を揃えます。

- 同じObservation pool
- 同じ情報量とおおむね同じ文字量
- 同じsource linkとdeep link
- 同じ残件数、見積時間、明示的終端
- 同じscratch note機能

Curiosity Captureの有無は最初の比較で変えません。presentationとresumptionの効果を測った後、必要なら独立した要因として追加します。

### 参加者とsession

- 最低8〜12人
- 1人10〜12 session
- 合計100〜120 sessionを目安にする
- 行動条件でscreeningする
- founder N-of-1は先にinstrumentation確認へ使う

### Primary outcome

10分以内の`substantive return`率をprimary outcomeにします。

```text
対象contextを開いた
かつ
2分以上作業を継続した、または意味のある編集・操作を行った
```

### Safety co-primary outcome

独立auditでaction-requiredと判断された義務に対する、criticalまたはhigh-loss false negativeを測ります。

### Secondary outcomes

- Return latency
- 予定時間を超えた探索率
- 後で実際に利用された着想の割合
- 自律性と納得感
- irritationと圧迫感
- native sourceへ脱線した回数
- setupと修正に要した時間
- 4週間継続したいか
- 少額でも実際に支払うか

## 暫定Continue gates

次は科学的に確立された閾値ではなく、過剰投資を防ぐための事前判断基準です。

以下を満たす場合、OpenBrief MVPへ進みます。

- Return率が15 percentage point以上改善する、またはmedian latencyが25%以上短くなる
- topic化により探索超過が20%以上減る
- 高価値の着想がcontrolの90%以上維持される
- seriousなcritical mail見落としが0件
- setupと修正のmedianが90秒以内
- 10人中4人以上が、さらに4週間使いたいと答える
- SaaSを主張するなら、10人中2人以上が少額を実際に支払うかdepositする

## Stop conditions

次のいずれかなら、現在の構想またはその一部を止めます。

- content量を揃えてもtopic化がfinite batchを上回らない
- Return Anchorを置いても実作業への復帰が改善しない
- Curiosity Captureが新しいbacklogと罪悪感を作る
- 重要mailのfalse negativeを許容範囲へ下げられない
- setup、修正、二重確認の時間が削減時間を上回る
- 参加者が実験後に継続利用を望まない
- privacy懸念によりreal dataでは使われない

## 結果別の判断

| 実験結果 | 判断 |
|---|---|
| topic化とReturnの両方が効く | OpenBrief MVPへ進む |
| Returnだけが効く | aggregatorを作らずbrowser / IDE Return extensionへ縮小する |
| finite batchだけが効く | 既存RSS・mail client設定で十分。独自aggregatorを止める |
| Curiosity Captureが負担になる | coreから外す |
| 効果はあるがprivacyで拒否される | local-first OSSまたはpluginへ限定する |
| 効果がなく継続希望もない | 研究と製品化を止める |

## 最終recommendation

OpenBriefは、現段階では「作るべき完成製品」ではなく、**試すべき注意遷移protocol**です。

実装順は次の1本に絞ります。

1. GC-01を使って2×2実験UIを作る
2. shadow modeで安全性指標を実装する
3. founder N-of-1で計測不良を直す
4. 8〜12人の行動screened participantで試す
5. 事前に決めたContinue / Stop条件で判断する

ここで効果が出るまで、adapter数、podcast生成、calendar連携、public Gmail OAuthへ投資しません。

名称も、効果が実証されるまでは保証を連想させる`Attention Firewall`より、`Attention Transition`または`Brief and Return`の方が正確です。

## 参考文献・公式情報

### 近接研究

- Fitz et al. (2019), [Batching smartphone notifications can improve well-being](https://doi.org/10.1016/j.chb.2019.07.016)
- Baughan et al. (2022), [How explicit stopping cues affect digital media use](https://doi.org/10.1145/3491102.3501899)
- Ratwani and Trafton (2008), [The role of resumption cues in interrupted task performance](https://doi.org/10.1080/13506280802025791)

### 近接製品

- [Google Gemini Daily Brief](https://gemini.google/us/overview/daily-brief/?hl=en)
- [DailyStack](https://dailystack.ai/)
- [Nudget](https://nudget.app/)
- [Shortwave](https://www.shortwave.com/)
- [one sec](https://one-sec.app/)

### Gmail実装・審査要件

- Google, [OAuth restricted scope verification](https://developers.google.com/identity/protocols/oauth2/production-readiness/restricted-scope-verification)
- Google, [Cloud application security assessment](https://support.google.com/cloud/answer/13465431?hl=en)
- Google, [Gmail push notifications](https://developers.google.com/workspace/gmail/api/guides/push)


---

## Source file: `docs/adr/0001-adopt-local-first-data-and-model-boundaries.md`

# ADR 0001: Local-firstなデータ境界とModel Gatewayを採用する

## Status

Accepted — 2026-07-21

## Decision

OpenBriefをlocal-firstなAttention Control Planeとして実装し、raw source dataは端末内へ保持します。AI処理はModel Gatewayを介し、ユーザーがrules-only、local model、remote providerを明示的に選択できるようにします。

remote providerへの暗黙の送信と、自動cloud fallbackは禁止します。

## Decision Drivers

- Gmail、RSS、Slack、GitHubなどを統合すると、個別service以上に詳細な行動profileが生まれる
- ユーザーが保存場所、送信先、model、削除時期を制御できる必要がある
- OpenClaw、Hermes Agent、CLIなど既存の収集手段を再利用したい
- OpenBriefが全sourceのcredentialとadapterを所有する構成を避けたい
- 特定model providerのSDK、料金、利用規約、可用性へ中核domainを結合したくない
- 研究prototypeから始めるため、production SaaS基盤を先行実装したくない

## Context

OpenBriefは、複数sourceから得たObservationを、`Protect → Signal → Explore / Focus → Capture → Return`という注意遷移へ変換します。Signalの外部書き込み境界は[ADR 0002](0002-adopt-attention-signals-and-slack-status-output.md)で定義します。

単一sourceの要約と異なり、複数sourceを統合したstoreからは次の情報を推測できます。

- 誰と連絡しているか
- どの仕事に責任を持つか
- 何へ関心を向けているか
- いつ作業し、どこで中断したか
- 何を重要または不要と判断したか

この集約dataを必ずproject運営者のserverへ送る構成は、OpenBriefが解こうとしている注意問題とは別に、大きなprivacy riskと運用責任を生みます。

一方、local modelだけを必須にすると、端末性能、model品質、context長、structured outputの差により利用者を限定します。そのためlocal処理を既定にしつつ、本人がremote providerを選択できる境界が必要です。

### Facts

- 現時点では研究文書とfixtureがcontractであり、移行対象となるproduction実装はない
- 最初のsource候補は義務系のGmailと好奇心系のRSSである
- source収集には常駐agentまたはCLIを利用する構想がある
- OpenBrief固有の効果を示すE1実証結果はまだない

### Assumptions

- 初期利用者はlocal agentまたはCLIを自分の端末で動かせる
- OpenClaw、Hermes Agentなどは、共通schemaのfileまたはlocal endpointへ書き込める
- 一部の利用者はlocal modelの品質や速度よりも、端末外へ送信しないことを優先する
- 一部の利用者は、明示的な同意の下でremote modelの品質を選ぶ

## Architecture Boundary

```text
Gmail / RSS / Slack / GitHub / Git
                 ↓
      OpenClaw / Hermes Agent / CLI
                 ↓ local write
         Observation Ingress
                 ↓
       Local Observation Store
                 ↓
     Policy / Redaction / Selection
                 ↓ bounded request
           Model Gateway
      ┌──────────┼──────────┐
  rules-only  local model  remote BYOM
      └──────────┼──────────┘
                 ↓
   Brief / Decision / Return records
                 ↓
              Local UI
```

BYOMはBring Your Own Modelを意味します。remote利用時は、API key、provider、modelをユーザーが選択します。

### Data ownership

| Data | Owner / source of truth | Default location |
|---|---|---|
| source credential | 収集agentまたはOS secret store | local |
| raw email、feed item、message | source serviceとLocal Observation Store | local |
| normalized Observation | OpenBrief | local |
| ProtectedIntent、CuriosityCapture、ReturnAnchor | OpenBrief | local |
| provider API key | ユーザーとOS secret store | local |
| remote request payload | ユーザーが選択したprovider | explicit opt-in時だけ送信 |
| application log | OpenBrief | local、content非保持が既定 |

OpenBriefの運営serverをraw dataの必須中継点にしません。

### Ingress contract

収集agentはsource固有dataを、version付きのObservation schemaへ正規化して書き込みます。OpenBriefのdomain処理は、GmailやSlack固有のSDKを直接呼びません。

最初の実装transportは別途決定します。file、stdin、localhost APIのいずれを選んでも、同じschemaとprovenance要件を使います。

各Observationには最低限、次を含めます。

- 一意なsource ID
- source type
- 発生時刻と取得時刻
- contentまたはlocal content reference
- 元情報へ戻るためのprovenance
- 重複排除に使えるthreadまたはtopic hint

### Model Gateway contract

domain処理はprovider固有SDKではなく、task単位のModel Gatewayを呼びます。

```ts
type ModelMode = 'rules_only' | 'local' | 'remote'

type ModelTask =
  | 'extract_observations'
  | 'cluster_topics'
  | 'classify_obligations'
  | 'generate_brief'
  | 'suggest_return_anchor'

type ModelPolicy = {
  mode: ModelMode
  provider?: string
  model?: string
  allowRawContent: boolean
}
```

この型は方針を示す最小例であり、実装前の固定APIではありません。ただし、次の意味境界は固定します。

- taskの入力と出力はprovider非依存のschemaを持つ
- provider固有処理はadapter内へ閉じ込める
- provider adapterはLocal Observation Storeを直接走査しない
- Gatewayへ渡す前に、domain側で対象dataを選択する
- model出力は候補として扱い、source上の行動を直接実行しない

### Processing modes

| Mode | Network behavior | Intended use |
|---|---|---|
| `rules_only` | AI providerへ通信しない | deterministicな抽出、test、低性能端末 |
| `local` | loopbackまたは同一端末のmodel endpointだけを使う | raw dataを端末外へ送らない通常利用 |
| `remote` | 選択したproviderだけへ送信する | 本人が品質を優先して明示許可したtask |

modeはtaskごとに選択可能にします。例えばtopic化はlocal、解説生成だけremoteという設定を許容します。

local処理が失敗した場合はerrorを返します。remoteへ自動昇格しません。

### Remote egress policy

remote送信には次を要求します。

1. providerとmodelが明示的に設定されている
2. 対象taskでremote modeが許可されている
3. source policyが送信を許可している
4. raw contentを送る場合は`allowRawContent`が有効である
5. 送信先、task、対象Observation IDをcontent非保持のaudit recordへ残す

初期versionでは、自動redactionが完全であると主張しません。送信量を小さくし、remote利用そのものを本人が選ぶ設計を優先します。

### Security boundaries

- email、feed、web contentは命令ではなく、信頼できないdataとして扱う
- source adapterは可能な限りread-onlyかつ最小scopeを使う
- secretをplain textの設定fileやapplication logへ記録しない
- prompt、error、traceにはraw contentを既定で残さない
- embeddingやvector indexもsource dataとしてlocal保持を既定にする
- telemetryへObservation content、prompt、生成briefを含めない

local-firstは端末侵害、悪意あるplugin、誤設定を防ぎません。localであることをprivacy保証の代わりに使わず、threat modelと権限境界を実装ごとに確認します。

## Options Considered

### A. Centralized SaaSへ全dataを集約する

採用しません。

- cross-device同期と運用は単純になる
- provider品質を運営側で統一できる
- ただしraw data、credential、compliance、breach impactが運営側へ集中する
- 中核仮説を検証する前に高い運用責任を負う

### B. Local UIだがcloud inferenceを必須にする

採用しません。

- UIとstoreをlocal化しても、最も機密性の高いcontentがproviderへ送られる
- provider lock-inと利用料が残る
- offlineまたは機密環境で利用できない

### C. Local modelだけを許可する

採用しません。

- data egressを最小化できる
- ただし端末要件とmodel品質の差が利用者へ直接影響する
- remote modelを本人の判断で使う選択肢まで禁止する必要はない

### D. Storeを持たずagentごとのplugin UIにする

採用しません。

- central storeを避けられる
- ただしsourceをまたぐ重複排除、Protect、Capture、Returnの状態を一貫して保持できない
- agentごとに注意遷移protocolが分断される

### E. Local control planeと選択可能なModel Gateway

採用します。

- raw dataと注意判断を端末内へ保持できる
- 収集agent、model provider、UIを独立に交換できる
- localとremoteのtrade-offを運営者ではなくユーザーが選べる

## Consequences

### Positive

- 複数sourceを統合しても、raw dataを運営serverへ集中させずに済む
- OpenClaw、Hermes Agent、CLIのadapter ecosystemを利用できる
- local model、self-hosted model、remote providerを同じdomainから扱える
- provider終了、価格変更、障害によるlock-inを小さくできる
- data flowをOSSとして監査、変更、self-hostできる

### Negative

- install、model選択、resource不足などをユーザーが意識する場面が増える
- modelごとのstructured output、context長、品質差を吸収するtestが必要になる
- local端末のbackup、malware、他processからのアクセスは利用者側riskとして残る
- cloud SaaSよりcross-device同期とsupportを提供しにくい
- OSS、local-first、provider選択性だけでは競争上のmoatにならない

### Follow-up

- version付きObservation schemaをfixtureとして定義する
- 最小のingress transportを1つだけ選ぶ
- Model Gatewayのcontract testを作る
- networkを遮断したoffline integration testを作る
- retention、暗号化、secret保存を別ADRまたはdesign docで決める

## Adoption and Exceptions

このADRはcode reviewとtestで次のように維持します。

- 新しいnetwork egressには、送信data、送信先、保持期間を説明するpolicyを要求する
- provider adapterからstore全体を直接参照させない
- local失敗時にremoteへfallbackしないtestを置く
- offline modeで中核flowが動くintegration testを置く
- sourceへのwrite、送信、calendar登録は別の明示確認境界を通す

例外はrepository maintainerが承認します。例外には次の証拠を必要とします。

- localでは実現できない理由
- 送信されるdataの一覧
- user consentとUI上の表示方法
- retentionと削除方法
- failure時に別providerへ拡散しないことを示すtest

恒久的な例外はこのADRを直接曖昧にせず、新しいADRで変更理由を記録します。

## Open Questions

- 最初のingressをatomicなfile drop、stdin、localhost APIのどれにするか
- Local Observation Storeをどの形式で暗号化するか
- OS keychain間の差をどこまでcoreで吸収するか
- raw Observationと生成物の既定retentionを何日にするか
- cross-device同期を非目標のまま維持するか、暗号化同期として別途扱うか

これらは実装前に決定しますが、local-first、明示的remote opt-in、自動fallback禁止という本ADRの採用を妨げません。


---

## Source file: `docs/adr/0002-adopt-attention-signals-and-slack-status-output.md`

# ADR 0002: Attention SignalとSlack Status Outputを採用する

## Status

Accepted — 2026-07-21

## Decision

OpenBriefの注意遷移へ`Signal`段階を追加し、Slack custom statusを最初のOutput Adapterとして採用します。

Signalは、集中や探索に入る本人の状態を推測して自動公開する機能ではありません。本人が開始または延長を選んだとき、公開内容と終了時刻を確認できる形で、周囲へ応答状態を伝える機能です。

```text
Observe → Protect → Signal → Explore / Focus → Return
```

## Decision Drivers

- 集中や探索へ入ると、本人だけでなく会話相手にも応答不能の影響が生じる
- 「無視している」のか「いつ戻る」のかが分からない状態を減らしたい
- OpenBriefを情報のInputだけで完結させず、本人が選んだ注意状態を社会的contextへOutputしたい
- 自動返信より小さく、可逆で、誤動作時の損失が限定された出力から始めたい
- 作業内容や診断情報を公開せず、必要最小限のavailabilityだけを伝えたい

## Context

これまでのOpenBriefは、GmailやRSSを収集し、本人のためにProtect、Explore、Capture、Returnを支援するInput中心の構想でした。

しかし、集中や探索中にSlackの会話から離脱すると、次の問題は本人の画面内だけでは解決しません。

- 会話相手が返信時刻を予測できない
- 追加のpingや確認が増える
- 本人が後から未返信への焦りや罪悪感を持つ
- 集中を守るための離脱が、関係上は無言の不在に見える

Signalは、本人の集中を周囲へ説明し、復帰予定を共有するための出力境界です。

### Facts

- Slackの`users.profile.set`はcustom statusのtext、emoji、expirationを設定できる
- custom statusの更新にはuser tokenと`users.profile:write` scopeが必要である
- custom statusはavailabilityの表示であり、通知を止めるDNDとは別機能である
- ADR 0001は外部serviceへのwriteに明示確認境界を要求している

### Assumptions

- 初期利用者は、集中中の状態と復帰予定をSlackへ共有する価値を感じる
- genericなstatusでも、無言の離脱より会話相手の予測可能性が上がる
- 毎回別dialogを出さず、Focus開始画面内のpreviewと開始操作で十分な同意を得られる
- status更新に失敗しても、OpenBrief内のFocusやReturnは継続できる

## Signal Model

```text
ProtectedIntent / ReturnAnchor
              ↓
    AttentionSignalProposal
              ↓ preview + user action
       SlackStatusAdapter
              ↓
      AttentionSignalReceipt
              ↓ expire / reconcile
            Return
```

最小entityは次の責務を持ちます。

| Entity | Responsibility |
|---|---|
| `AttentionSignalProposal` | 公開先、status text、emoji、終了時刻の候補 |
| `AttentionSignalConsent` | workspace単位の許可と、今回の開始操作 |
| `AttentionSignalReceipt` | Slackへ実際に適用した値、時刻、結果 |
| `PreviousStatusSnapshot` | 上書き前のstatusと、復元可能性の判断材料 |

実装時の概念schemaは次を起点にします。

```ts
type AttentionSignalProposal = {
  adapter: 'slack_status'
  workspaceId: string
  statusText: string
  statusEmoji: string
  expiresAt: string
  includesWorkContext: boolean
}

type AttentionSignalReceipt = {
  proposalId: string
  appliedAt?: string
  appliedText?: string
  appliedEmoji?: string
  expiresAt?: string
  outcome: 'applied' | 'failed' | 'skipped'
  errorCode?: string
}
```

この型は実装前の固定APIではありません。ただし、proposalと実際の適用結果を分け、失敗を成功として扱わない境界は固定します。

## User Flow

### FocusまたはExplore開始

開始画面に、Slackへ公開するstatusと終了時刻を表示します。

```text
🧠 集中中・15:00ごろ戻ります
緊急の場合はメンションしてください

公開先: Example Workspace
終了: 15:00

[Slackで共有して開始] [共有せず開始]
```

`共有せず開始`を常に選べます。SignalはFocusやExploreの入場条件ではありません。

workspace設定で継続的な同期を許可していても、background inferenceだけを理由にstatusを更新しません。本人による開始または延長操作をtriggerにします。

### Focus延長

Focusを延長した場合だけ、新しいexpirationをpreviewして更新します。timerの遅れやmodel推定だけで延長しません。

### Return

終了時はSlack側のexpirationをcleanupの第一手段にします。OpenBriefが稼働している場合は現在statusを読み、OpenBriefが適用した値と一致するときだけclearまたは以前のstatus復元を試みます。

Slack上で本人がstatusを変更していた場合、その値を上書きしません。

## Privacy-safe Defaults

既定templateは、作業内容ではなくavailabilityだけを伝えます。

- 公開する: 集中中であること、復帰予定時刻、緊急時の連絡方法
- 公開しない: task title、email subject、project名、診断名、AIの推定状態
- permanent statusを作らず、expirationを必須にする
- AIによる自由文生成を必須にしない
- workspaceごとに個別に許可し、全workspaceへ自動fan-outしない

詳細な作業内容を含むtemplateは本人が明示的に選んだ場合だけ許容します。

## Ownership and Reconciliation

OpenBriefがSlack上の手動操作と競合しないため、次の順序を使います。

1. 書き込み前に現在のstatusを取得する
2. 置き換える内容とexpirationを本人へ表示する
3. 適用した完全な値をreceiptへ保存する
4. clearまたは復元前に現在のstatusを再取得する
5. 現在値がreceiptと一致しない場合は何もしない

アプリ停止やnetwork failureでreconcileできない場合も、Slack側のexpirationによってstatusが残り続けない設計にします。

以前のstatus復元はbest effortです。復元できない場合に、本人の新しいstatusを上書きしてまで整合させません。

## Failure Behavior

- Slack書き込み失敗はFocusやExploreを止めない
- UIは`共有済み`と表示せず、失敗と再試行操作を示す
- retryは同じproposalを使い、expirationが過去なら再確認する
- remote serviceの失敗を別workspaceへの送信で補わない
- status更新を繰り返しpollingせず、状態遷移時だけ書き込む

## Output Adapter Boundary

Slack固有処理はOutput Adapterへ閉じ込めます。

```ts
interface AttentionSignalAdapter {
  preview(proposal: AttentionSignalProposal): Promise<SignalPreview>
  readCurrent(target: SignalTarget): Promise<ExternalSignalState>
  apply(proposal: AttentionSignalProposal): Promise<AttentionSignalReceipt>
  reconcile(receipt: AttentionSignalReceipt): Promise<ReconcileResult>
}
```

domain側はSlack API method、token形式、rate limitを知りません。将来Calendar、Teams、Discordなどへ出力する場合も、各adapterが同じproposal、receipt、ownership原則に従います。

## Scope

### MVPに含める

- 1つのSlack workspaceへのcustom status
- privacy-safeな固定template
- status text、emoji、expirationのpreview
- Focus開始、延長、Returnに連動した更新
- 書き込み結果とownership check

### MVPに含めない

- Slack message、DM、mentionのInput収集
- DNDの自動設定
- channelへの自動投稿
- 自動返信または返信時刻の個別送信
- AIがハイパーフォーカスを推定して開始するstatus更新

Slack Input Adapterは、Gmail＋RSSの中核仮説を検証した後に扱います。Slack Status Output Adapterとは権限とriskが異なるため、同じ機能として実装しません。

## Options Considered

### A. OpenBrief内だけにFocus状態を表示する

採用しません。本人の注意は支援できますが、会話相手から見た無言の離脱は変わりません。

### B. Focus開始時に自動返信またはchannel投稿する

採用しません。通知量が増え、宛先や文脈を誤る損失がcustom statusより大きいためです。

### C. 行動を検知して完全自動でstatusを更新する

採用しません。誤推定、privacy disclosure、本人のagency低下を招きます。

### D. Slack custom statusを本人操作とexpiration付きで同期する

採用します。workspace全体へ低い通知負荷でavailabilityを示せて、失効による安全弁を持てます。

## Consequences

### Positive

- OpenBriefがInput整理だけでなく、社会的な注意調整を扱える
- 無言の離脱を、復帰予定のある状態へ変換できる
- 自動返信より通知負荷と誤送信riskが小さい
- Slack固有実装をOutput Adapterとして交換可能にできる
- Returnを個人作業だけでなく、会話への復帰として拡張できる

### Negative

- user token、write scope、workspace承認が必要になる
- statusが本人の実際の状態とずれる可能性がある
- 自動statusを監視や生産性表示と解釈される可能性がある
- workspaceごとの文化やstatus利用習慣に効果が依存する
- custom statusだけでは未読会話の復帰支援を提供できない

### Follow-up

- Signalを含むgolden caseとfixtureを別ケースとして作る
- Slack status adapterのcontract testを作る
- manual status変更を模したownership testを作る
- Signalが会話相手と本人へ与える効果をpilotで測る
- Slack Inputとre-entry briefは別の判断として設計する

## Research Hypothesis

Signalの効果は未検証です。最初の仮説を次のように置きます。

> 本人操作とexpirationを伴うSlack statusは、privacy discomfortを増やさず、集中中の応答可能性を会話相手が予測しやすくする。

主要な観測候補は次です。

- Focus中の追加ping数
- Focus終了前の応答期待に関する問い合わせ数
- 会話相手が認識した復帰予定の正確さ
- 本人の未返信不安とReturn後の会話復帰時間
- status内容に対するprivacy discomfort

message数の減少だけを成功にしません。緊急連絡を遅らせたり、会話相手がstatusを信用しなくなった場合は失敗です。

## Adoption and Exceptions

code reviewとtestで次を要求します。

- expirationのないSlack statusを書き込まない
- explicitな開始または延長操作なしにstatusを書き込まない
- task titleなどのwork contextをdefault templateへ含めない
- manual変更後のstatusをclearまたは復元で上書きしない
- API失敗時にFocusを止めず、共有成功とも表示しない

例外はrepository maintainerが承認します。例外には、公開data、trigger、expiration、manual override、失敗時動作を示すtestとUI説明が必要です。

恒久的な変更は本ADRを曖昧に書き換えず、新しいADRで`Superseded`にします。

## Open Questions

- 最初のstatus有効時間と上限を何分にするか
- 以前のstatusを自動復元するか、候補だけ提示するか
- 複数workspace対応をいつ追加するか
- 緊急連絡方法を固定文にするか、workspaceごとに設定するか
- Slack会話へのReturnをどのeventで測るか

## References

- Slack, [`users.profile.set`](https://api.slack.com/methods/users.profile.set)
- Slack, [Web API methods](https://api.slack.com/web)
- [ADR 0001: Local-firstなデータ境界とModel Gateway](0001-adopt-local-first-data-and-model-boundaries.md)


---

## Source file: `docs/reverse-engineering/tiimo/README.md`

# Tiimo Android 静的解析レポート

## まず読む

独自実装を始める場合は、最初に[機能とUX](03-features-and-ux.md)、次に[再実装ブループリント](05-reimplementation-blueprint.md)を読んでください。

このレポートは、Tiimo Android `1.1.4` のAPKを静的解析し、ADHD支援アプリを独立実装するための設計上の学びを整理したものです。ソースコードの復元・転載やTiimoのバックエンド利用を目的としません。

## 最重要の発見

Tiimoの中心的なドメイン分離は次の3段階です。

1. `Todo`: やる必要はあるが、実行時刻は未確定
2. `Activity`: 日時・時間帯・繰り返しが決まった予定
3. `Focus`: 今取り組むActivityを1件に絞った実行画面

この分離により、「思いついたことを忘れない」「いつ実行するか決める」「今は1つだけ見る」という、ADHDユーザーの異なる認知負荷を別々の画面で扱えます。

## 文書一覧

| 文書 | 内容 |
|---|---|
| [01 APK inventory](01-apk-inventory.md) | APK、Manifest、権限、SDK、解析条件 |
| [02 Client architecture](02-client-architecture.md) | 画面構造、状態管理、通知、課金、分析SDK |
| [03 Features and UX](03-features-and-ux.md) | ADHD支援機能、ユーザーフロー、設計原則 |
| [04 Network and backend](04-network-and-backend.md) | 観測API、認証、データモデル、責務境界 |
| [05 Reimplementation blueprint](05-reimplementation-blueprint.md) | 独自アプリの決定済みアーキテクチャと開発順序 |
| [06 Security, privacy, limitations](06-security-privacy-and-limitations.md) | クリーンルーム方針、個人情報、解析限界 |
| [Evidence](evidence/observations.md) | コマンド、ハッシュ、根拠となる観測一覧 |
| [TiimoとOpenBriefの比較](../../research/attention-triage/05-tiimo-comparison.md) | 観測したTiimoと独自Attention Triage構想の境界 |

## 確度の表記

- **確認**: APK、Manifest、DEX、Hermesバイトコードから直接確認
- **推定**: 複数の確認事項を組み合わせた合理的な推定
- **提案**: 独自アプリ向けの設計判断。Tiimoの実装事実ではない

## 調査範囲

- ADBで取得したbase APKと4つのsplit APK
- Hermes Bytecode v96の逆アセンブル・擬似コード化
- Manifest、DEX、Expo設定、ネイティブライブラリの静的確認
- ライブAPIへのアクセス、通信傍受、認証回避、動的計装は未実施
- SDKキー、DSN、トークン、ユーザーデータは収集・記載していない

## 結論

独自版のMVPでは、週次計画、Todo、Focus、ローカル通知、チェックリストだけを実装します。オンボーディング質問、AI分解、課金、外部カレンダー、マーケティングSDKは、利用価値が検証できるまで追加しません。
