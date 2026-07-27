---
source_url: /var/lib/hermes/.hermes/cache/documents/doc_739f5bc11f3a_deep-research-report2.md
ingested: 2026-07-24
sha256: f2739474b4053c4c82f071d68fcd0d9f70d59655ab2b7857da69937b9c7ea859
---

# 音声認識市場調査レポート

## エグゼクティブサマリー

STT市場は、単なる「文字起こし」から、リアルタイム対話、業務自動化、会議要約、医療文書化、アクセシビリティ支援を含む広い音声ワークフロー市場へ移行しています。市場定義によって規模推計はかなり異なりますが、Grand View Researchは speech-to-text API 市場を 2024年38億ドル、2026年51億ドル、2030年86億ドルと見積もり、MarketsandMarketsはより広い speech and voice recognition 市場を 2025年96.6億ドルから2030年231.1億ドルへ拡大すると見ています。つまり、狭義のSTT API自体も伸びていますが、実際に大きくなっているのは「STTを起点にした音声インテリジェンス」全体です。

競争軸は、おおむね四つに分かれます。第一に、Google・Microsoft・AWSのようなハイパースケーラ型で、クラウドAPI、管理機能、ガバナンス、各種SDKを強みとする層。第二に、Deepgram・AssemblyAIのような音声特化APIベンダーで、低遅延、開発者体験、モデル更新速度、音声後処理機能を競う層。第三に、Superwhisper・Handy STTのようなローカル実行／ローカル優先のデスクトップ層。第四に、Aqua Voice や Genio Notes のように、STTそのものより「入力補助」「ノート化」「構造化」に価値を置くワークフロー層です。Gartner も STT ソリューションを、単なる transcript 出力ではなく、メタデータ、感情・属性、下流ワークフロー更新まで含むカテゴリとして定義しています。

ご指定の製品のうち、**Aqua Voice** はクラウド型の高速ディクテーション／開発者向け入力支援、**Superwhisper** はローカル優先だがクラウドモデルも選べるハイブリッド型、**Deep Research Handy** は公開情報上は該当する正式製品名を特定できず、本レポートでは最も近い公開製品として **Handy STT** を仮置きしています。Handy STT は完全ローカル実行のオープンソースSTTアプリです。したがって、3製品はそれぞれ「クラウド最適化」「ローカル＋クラウド併用」「完全ローカル」という異なる設計思想を代表しています。

神経多様性支援の観点では、重要なのは「最高精度のASR」だけではありません。記録の再生可能性、検索可能性、速度変更、正確なキャプション、ノイズ下でも使えること、そしてタスクや要点を後から構造化できることが重要です。録画講義やキャプション・トランスクリプトは、ADHD学生にとって学習ペースの自己調整を助け、一般学生にも検索可能な復習資源として有用である一方、不正確な字幕や同期ずれは神経多様な学習者の認知負荷を上げうることも示されています。したがって、支援用途では「低遅延」よりも「信頼できる精度」「再編集可能性」「ユーザー確認可能な構造化」が優先される場面が少なくありません。

## 市場の見取り図

現在のSTT市場は、製品カテゴリ別に見ると理解しやすくなります。ハイパースケーラ型は、Google Cloud Speech-to-Text、Azure Speech、Amazon Transcribe が代表で、リアルタイム・バッチ・各種SDK・企業向け統制が揃う一方、音声UXそのものは比較的"部品"として提供されます。音声専業APIは Deepgram と AssemblyAI が目立ち、リアルタイム会話、医療、コンタクトセンター、後段LLMとの接続を前提に最適化されています。ローカル系は Handy と Superwhisper が典型で、オフライン性やプライバシーで優位です。ワークフロー／支援ツール系は Aqua Voice や Genio Notes のように、「話した内容をそのまま文字にする」より「すぐ使える入力や学習資源に変える」ことに寄っています。

AIベンチマーク側を見ると、精度と価格の競争はさらに激化しています。Artificial Analysis の 2026年比較では、Microsoft Azure、Google、Amazon、Deepgram、OpenAI、AssemblyAI などが同一ベンチマーク上で比較されていますが、同サイト自体も公開している通り、評価は独自の AA-WER 指標とデータセット重みづけに基づくため、製品選定では公式仕様と併読すべきです。ベンダーによっては、WER を公開しておらず、「高精度」「低遅延」「ベストインクラス」といった相対表現にとどめています。

導入モデルの観点では、完全クラウドだけでなく、**ハイブリッド／自社環境** が現実的な選択肢になっています。Google は Speech-to-Text On-Prem を private feature として公開し、Azure は connected container・disconnected container・embedded speech を提供し、Deepgram は self-hosted deployments と Amazon SageMaker 展開を案内し、AssemblyAI も self-hosted streaming / async をドキュメント化しています。個人向けアプリでも、Superwhisper と Handy はローカル実行を前提にしており、この潮流は「規制対応」だけでなく「待ち時間」「電波依存」「脳内ワーキングメモリ負荷」の低減とも結びつきます。

以下の表は、調達・設計の観点から主要ベンダーを並べたものです。なお、**WER と遅延は横並びの公式公開値がほとんど存在しない**ため、表中では「未公表」を明示し、独立比較が見つかる場合のみその旨を注記しています。

| ベンダー | 製品名 | 展開モデル | 価格モデル | 対応言語 | 精度指標 | 遅延 / リアルタイム | プライバシー / PII | API・SDK・統合 | 主な対象顧客 |
|---|---|---|---|---|---|---|---|---|---|
| Handy | Handy STT | ローカル実行、オフライン、Windows/macOS/Linux | 無料、MITライセンス、自己運用 | Whisper系の多言語 + Parakeet V3（CPU向け） | WER未公表 | push-to-talk型、VADあり、数値未公表 | 音声は端末内に残ると明記 | 管理APIなし、OSS拡張 | 個人、開発者、プライバシー重視ユーザー |
| Aqua Voice | Aqua Voice / Avalon API | クラウド型アプリ、Mac/Windows/iPhone | Free 1,000 words、Pro $8/月年払い、Avalon API $0.39/時 | 49言語 | 97.3% accuracy on AISpeak と公式比較ページで主張、WER未公表 | クラウド処理、数値未公表 | 公式サイトは private と訴求、ただし公開取得資料では詳細なPII統制は限定的 | Avalon API、アプリ横断入力、開発ツール文脈 | 開発者、知識労働者、高速プロンプト入力 |
| Superwhisper | Superwhisper | ローカル＋クラウド併用、macOS/Windows/iOS | Free/Pro/Enterprise、取得できた公開資料では正確な現行料金は一部不明 | 100+言語 | 標準WER未公表、公式は速度/精度を10段階で表示 | 画面上の live transcription は Nova cloud models のみ | ローカルモデルは端末実行、クラウド時は外部処理 | アプリ統合、モード/カスタム、Enterprise 管理 | 個人、開発者、ローカル優先ユーザー |
| Google | Cloud Speech-to-Text | クラウド、Streaming、On-Prem/private、On-device/private | 従量課金。V2標準 $0.016/分、dynamic batch $0.003/分 | 125+言語 | 公式WER未公表。独立研究例では Google Cloud Speech API が LibriSpeech clean 6.6、other 13.6 | ストリーミングで interim / final を返す | data logging は明示的オプトイン。デフォルトでは音声/トランスクリプトを記録しない | REST、client libraries、GCP統合、diarization | 企業アプリ、メディア、字幕、検索 |
| Microsoft | Azure Speech / Azure AI Speech | クラウド、connected/disconnected containers、embedded speech、hybrid fallback | 秒課金。現行公開価格表は地域表示で一部数値非表示 | 機能別・モード別に多数ロケール | 公式WER未公表。独立ベンチ例では MAI-Transcribe-1.5 が AA-WER 2.4、2023研究では Azure 5.0 / 9.7 | 低遅延用途、リアルタイム・fast transcription・embedded 対応 | secure environment 向け disconnected container、on-device 実行可 | Speech SDK、REST、カスタム音響/言語モデル、VS Code toolkit | 企業、組込み、規制環境、音声UI |
| AWS | Amazon Transcribe | フルマネージドクラウド、batch + streaming | 従量課金。batch 例 $0.006/分、秒課金、15秒最小 | 100+言語 | 公式WER未公表。独立研究例では LibriSpeech clean 5.2、other 9.6 | streaming 対応。推奨 chunk 50–200ms | PII redaction / identification、HIPAA eligible / BAA | AWS SDKs、HTTP/2、WebSocket、S3、Call Analytics | コンタクトセンター、医療、字幕、分析 |
| OpenAI | Whisper / WhisperX | OSSの自己ホスト、オンプレ、エッジ、任意クラウド | ソフトウェア自体はオープンソース、実運用は自前インフラ費 | 多言語 | WhisperX Large-v2 は独立研究で LibriSpeech clean 3.1、other 8.9。AA比較では OpenAI Whisper Large-v2 4.1 | WhisperX は large-v2 で 70x realtime を掲示 | 自己ホストならデータを外に出さない設計が可能 | OSSライブラリ、コミュニティ統合、word timestamps・diarization | 研究、PoC、プライベート推論、カスタム製品 |
| Deepgram | Deepgram STT / Nova-3 / Flux | クラウド、self-hosted、SageMaker | Free credit、従量課金。Nova系おおむね $0.0058–0.0092/分、redaction add-on $0.0020/分 | 45–50+言語 | 公式WER未公表。独立ベンチ例では Nova-3 AA-WER 5.2 | ultra-low latency と turn detection を訴求、数値未公表 | HIPAA / SOC 2 訴求、redaction add-on、model improvement program | 公式SDK、API、Amazon Connect 統合、voice agents | 会話AI、医療、コンタクトセンター、開発者 |
| AssemblyAI | Universal-2 / Universal-3.5 Pro / Realtime | クラウド、WebSocket、self-hosted async/streaming | U2 $0.15/時、U3.5 Pro $0.21/時、add-ons別課金 | U2 は 99言語、U3.5 Pro は18言語 | 公式WER未公表。独立比較では Universal-3 Pro が AA-WER 3.1 | Realtime API あり、公式数値未公表 | 医療モード、enterprise flexibility、自社環境展開オプション | REST、WebSocket、LiveKit/Pipecat/Zapier/Make/n8n/Power Automate | Voice AI、会議、営業、医療記録 |
| Genio | Genio Notes 旧 Glean | SaaS学習支援、録音＋文字起こし＋ノート化 | 学生/機関向け、公開価格は機関見積中心で詳細非公開 | 公開取得資料では詳細言語数不明 | WER未公表 | 録音後転写と再生同期。speaker diarisation 対応 | 学習支援文脈、詳細なPII仕様は公開取得資料で限定的 | transcript snippet を notes に送る、学習支援ワークフロー | 高等教育、障害学生支援、神経多様性支援 |

表から分かる通り、**クラウドAPIの優位は統合性**、**ローカル系の優位はデータ境界の明確さ**、**ワークフロー系の優位は"使える形に整えるUX"** にあります。神経多様性支援や実務の構造化支援では、この三者を単純な代替品として扱うより、**局所最適の組み合わせ** として設計する方が成功しやすいです。

## 神経多様性と整理支援の実証ユースケース

まず、**ADHD** に関しては、録画講義を用いた学習が、学習の pace・place・time を自分で制御できる感覚を与えたことが、学生への質的研究で示されています。これは STT 単体の効果ではありませんが、録音と検索可能な transcript があることで、聞き逃しや集中の揺れを後から補完できる点が重要です。さらに、近年の研究では、ADHD の不注意症状が高いほど、手書きよりタイピングのほうが講義学習に有利になる傾向も報告されており、音声→構造化ノートへの変換はこの流れと整合的です。

**ディスレクシア** については、STT を用いた文章産出支援が、単語・文・テキスト品質を改善したという 2024年の単一事例研究があり、また高等教育におけるディスレクシア学生の講義ノート作成困難は、処理・保持・検索の困難と時間制約が重なる点にあると整理されています。ここから導ける含意は、ディスレクシア支援では「生音声の完璧な逐語転写」より、**聞きながら全部書こうとさせないこと** と、**後から検索・再配置・再編集できること** の価値が大きいということです。

**自閉スペクトラム** については、オンライン学習における認知負荷研究が、オーディオに加えて文字が提供されることが一部の自閉スペクトラム学生には有益でありうる一方、不正確な transcript や同期の悪い caption は神経多様な学習者の認知負荷を上げると指摘しています。つまり、自閉スペクトラム支援では STT の導入自体より、**字幕品質・同期精度・表示の柔軟性** が実用性を左右します。 text を出せばよいのではなく、**誤りが少なく、ペース変更や表示切替が可能** であることが重要です。

神経多様性支援向けの**製品レイヤー**としては、Genio Notes が録音、後からの transcription、speaker diarisation、transcript 断片のノート転記を提供しており、障害学生支援での採用を前提に設計されています。公式資料でも、学生が講義中に内容理解へ集中し、後から transcript と同期再生で理解を補強できる点が強調されています。これは ADHD・ディスレクシア双方の「同時処理負荷」を下げる設計に近いです。

次に、**整理・構造化タスク** についてです。会議 transcript から action item を検出する研究は古くからあり、近年は action-item-driven summarization が、一般的な要約よりタスク中心の会議要約を改善する方向で進んでいます。2023–2024年の研究では、長い会議 transcript を区分し、action item 抽出を組み込むことで、AMI コーパス上の BERTScore を改善できたと報告されています。したがって、STT を会議メモに使うだけなら transcript で十分ですが、**実務価値を出すには "誰が・何を・いつまでに" を抽出する第2段階が必要** です。

医療や高負荷な対話では、**ASR誤りが下流要約を劣化させる** ことも確認されています。2024年の研究では、ASRノイズ率が高まるほど医療対話の要約品質が低下し、逆に ASR ノイズを考慮した訓練が要約モデルの頑健性を改善することが示されました。これは支援アプリ設計にそのまま応用でき、要約やタスク抽出を自動化するなら、**低信頼箇所を可視化し、ユーザー確認を必須化** すべき根拠になります。

さらに、**実行機能支援** に関しては、AIチャットボットと実行機能の関係を扱った 2025年のシステマティックレビューが、計画、目標達成、認知的支援にポジティブな可能性を示しつつ、まだ一般化には限界があると結論づけています。ADHD 向けの prompt 設計を評価した 2025年の混合研究も、専門家が ChatGPT による介入計画生成を評価しており、「外部化された実行機能補助」としての可能性はあるものの、全面自動化ではなく**人間中心の補助**として扱うべき段階です。

神経多様性と整理支援の観点から、実証に近いユースケースを整理すると次のようになります。

| ユースケース | 期待できる便益 | 実証・根拠 | 実装上の注意 |
|---|---|---|---|
| 講義・会議の録音＋検索可能 transcript | 聞き逃しを後から補完、自己ペース学習、復習の柔軟化 | ADHD学生は録画講義で pace/place/time の自己統制を得た。caption/transcript は検索可能な復習資源になりうる。 | 字幕誤りや同期ずれは認知負荷を増やすので、品質監視が必要。 |
| ディスレクシアの文章産出支援 | 書字負荷低減、語彙・文品質の改善 | 2024年のSTT介入研究で post-intervention 改善。 | 逐語転写より、構成支援・編集支援も必要。 |
| 自閉スペクトラム向け字幕・文字補助 | 音声と文字の併用で理解補助、背景雑音下の支援 | neurodivergent cognitive load 研究が、文字支援の有用性と品質条件を指摘。 | 全員に同じ表示を押しつけず、切替可能にする。 |
| 会議の action item 抽出 | タスクの明確化、実行機能の外部化 | 会議 transcript からの action item detection と action-item-driven summarization の研究。 | 自動確定ではなく、担当者・期限のレビューを必須にする。 |
| STT→要約→次アクション提案 | 情報圧縮、負荷軽減、次の一歩の明確化 | ASR誤りは下流要約品質を悪化させる。AI chatbots は executive skills 支援に可能性。 | 低信頼部分をハイライトし、人が承認してからタスク化する。 |

## 実装・ガバナンス・費用設計

アクセシビリティ用途では、まず **リアルタイム字幕** と **後処理構造化** を別物として設計するのが重要です。リアルタイム字幕は低遅延優先で、多少の誤りを許容する代わりに即時フィードバックを得ます。後処理構造化は、より高精度の再転写、話者分離、要約、タスク抽出、見出し付与を行います。Superwhisper が live transcription を Nova cloud model に限定していることや、Google / AWS / Azure が streaming と batch を明確に分けていることは、この二段構成が業界標準であることを示しています。

技術設計としては、支援用途では **confidence-aware UI** が特に重要です。ASR には常に誤りがあり、医療対話研究でも ASR エラーが downstream summarization を悪化させることが示されています。したがって、UI には少なくとも、低信頼語のハイライト、ワンタップ修正、固有名詞辞書、短いセグメント単位での再実行、要約前の人間確認が必要です。特に神経多様性支援では、誤った transcript をそのまま"正解"として出すことが、認知負荷と混乱の増幅につながります。

データガバナンスでは、選択肢は三段階あります。**低リスク** ならクラウド直送、**中リスク** なら端末前処理＋redaction＋クラウド要約、**高リスク** なら完全ローカルまたはコンテナ／オンプレです。Google は data logging をオプトインにしており、Azure は disconnected containers と embedded speech を用意し、AWS は PII redaction と HIPAA eligibility を提示し、Deepgram・AssemblyAI も self-hosted / compliance 路線を持っています。つまり、ベンダー間の優劣より、**データ分類に応じた経路分離** を最初から設計することが重要です。

費用は、単価だけでなく、**話者分離・redaction・要約・保管** で膨らみます。公開価格が明瞭なものだけで概算すると、月20時間の音声では、Google V2標準で約19.2ドル、Amazon Transcribe batch で約7.2ドル、Deepgram Nova系で約7.0〜11.0ドル、AssemblyAI Universal-2 で約3.0ドル、Aqua Avalon API で約7.8ドルです。これらは純粋な文字起こし原価であり、PII redaction、medical mode、LLM要約、長期保存、同時接続拡張は別料金です。Whisper/WhisperX や Handy のような自己運用型はライセンス費が低くても、GPU/CPU、デバイス調達、運用保守、人件費が実コストになります。

簡易な比較表を置くと、次のようになります。

| 目安音声量 | Google STT V2 標準 | Amazon Transcribe batch | Deepgram Nova系 | AssemblyAI U2 | Aqua Avalon API |
|---|---:|---:|---:|---:|---:|
| 20時間/月 | 約 $19.2 | 約 $7.2 | 約 $7.0–11.0 | 約 $3.0 | 約 $7.8 |
| 100時間/月 | 約 $96 | 約 $36 | 約 $34.8–55.2 | 約 $15 | 約 $39 |
| 500時間/月 | 約 $480 | 約 $180 | 約 $174–276 | 約 $75 | 約 $195 |

この表は単純な掛け算で、地域差、割引、追加機能、無料枠、同時接続上限を含みませんが、「クラウドAPI自体の生の原価は思ったより小さく、**本当の差はガバナンスと下流処理** に出る」ことを示します。

推奨方針を一文でまとめると、**支援ワークフローは local-first、summary/task extraction は consented cloud or private deployment、最終アクション確定は human-in-the-loop** が最も堅実です。

## 推奨アーキテクチャとユーザーフロー

神経多様性支援に向くアーキテクチャは、単一ベンダーに全てを委ねるより、**入力層・転写層・構造化層・行動化層** を分ける設計です。入力層では、ローカルVADと push-to-talk / hold-to-talk を使って不要な長尺録音を減らします。転写層では、端末ローカルSTTを第一候補にし、必要時のみクラウド高精度モデルへフォールバックします。構造化層では、段落化、話者分離、要点抽出、action item 抽出を行います。行動化層では、ToDo・カレンダー・ノートアプリ・学習カードへ出力します。この分離により、**リアルタイム性が必要な場面** と **高精度要約が必要な場面** を切り分けられます。

以下は、支援用途向けに推奨できる STT アプリの基本フローです。

```
flowchart TD
    A[マイク入力] --> B[ローカルVADとノイズ除去]
    B --> C{機密度は高いか}
    C -- 高い --> D[ローカルSTT]
    C -- 低い/同意あり --> E[クラウドSTTまたは自社環境STT]
    D --> F[信頼度付きトランスクリプト]
    E --> F
    F --> G[低信頼語ハイライトとユーザー修正]
    G --> H[話者分離・セグメント化]
    H --> I[要点抽出]
    H --> J[アクション項目抽出]
    I --> K[やさしい要約/学習用要点]
    J --> L[担当・期限候補]
    K --> M[ノートアプリへ保存]
    L --> N[ToDo/カレンダーへ提案]
    M --> O[暗号化保存]
    N --> O
```

このアーキテクチャに沿った **ユーザーフロー例** を二つ示します。ひとつ目は、大学の講義を受ける ADHD / dyslexia 学習者です。授業中は短いメモだけを取り、録音と軽量キャプションをバックグラウンドで走らせます。授業後に高精度再転写を実行し、見出し、キーワード、試験範囲候補、復習カード候補を生成します。ユーザーは transcript の該当箇所をクリックして原音を再確認でき、誤りを直した部分だけを正式ノートに昇格させます。これは、録画講義の自己ペース学習や、caption/transcript の検索可能性が有益だという教育研究と整合します。

ふたつ目は、知識労働者の **実行機能支援フロー** です。会議や思考の独り言を STT で取り込み、すぐに全文を見せるのではなく、「要点」「次にやること」「未確定事項」「後で確認」の4枠に自動振り分けします。さらに action item 候補には必ず責任者・期限・根拠発話を紐づけ、ユーザーが確認したものだけをタスク管理へ反映します。この設計なら、AIチャットボットや要約モデルを"外部化された実行機能"として使いながら、自動化の暴走を抑えられます。会議 action-item 研究と executive function 支援レビューの両方が、この human-in-the-loop 設計を支持します。

実務上の推奨構成を最後にまとめると、**個人利用** では Superwhisper または Handy のようなローカル系をベースにし、要約だけ必要時クラウド化する構成が安全です。**開発・プロンプト入力中心** なら Aqua Voice のような cloud dictation は強力ですが、PIIの扱いを厳密に問う用途には追加確認が必要です。**企業の本番システム** では、Google / Azure / AWS の統制機能、または Deepgram / AssemblyAI の音声特化APIを選び、会議要約・タスク抽出・学習支援UIを自社側で実装するのが最も再現性の高いアプローチです。**神経多様性支援** では、Genio Notes 型の「録る→見返す→切り出す→再整理する」UXを参考にしつつ、字幕品質監視とユーザーの選択肢を中心に据えるべきです。
