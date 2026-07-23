---
title: ADHD向けデジタル支援
created: 2026-07-23
updated: 2026-07-23
type: concept
tags: [adhd, tool, research, therapy, diagnosis, medication, school, work, accessibility, policy]
sources: [raw/articles/deep-research-report-ai-software-adhd-2026.md, raw/articles/tiimo-homepage-2026.md, raw/articles/screenpipe-homepage-2026.md, raw/articles/focusmate-homepage-2026.md, raw/articles/nice-ng87-recommendations-2026.md, raw/papers/pubmed-adhd-ema-daily-life-adolescents-2026.md, raw/papers/arxiv-cognitive-personal-informatics-chi26-2026.md, raw/papers/akca-2026-neuroinclusive-emotion-regulation-uxr.md, raw/papers/arakawa-2026-calmreminder-parental-engagement.md, raw/papers/nordby-2024-blended-emotion-dysregulation-adult-adhd.md]
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

- [[async-meetings-context-fit]]
- [[assistive-technology]]
- [[cognitive-personal-informatics]]
- [[diagnosis-and-management]]
- [[cognitive-behavioural-therapy]]
- [[medication]]
- [[task-initiation]]
- [[external-memory]]
