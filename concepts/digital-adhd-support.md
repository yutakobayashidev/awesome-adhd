---
title: ADHD向けデジタル支援
created: 2026-07-23
updated: 2026-07-23
type: concept
tags: [adhd, tool, research, therapy, diagnosis, medication, school, work, accessibility, policy]
sources: [raw/articles/deep-research-report-ai-software-adhd-2026.md, raw/articles/tiimo-homepage-2026.md, raw/articles/screenpipe-homepage-2026.md, raw/articles/focusmate-homepage-2026.md, raw/articles/nice-ng87-recommendations-2026.md]
confidence: medium
---

# ADHD向けデジタル支援

ADHD向けデジタル支援は、診断、症状把握、治療補助、認知訓練、生活支援、服薬支援、コーチング、学校・職場配慮をまたぐ広い領域。添付の深層調査報告は、2026年時点では「万能な単独治療」ではなく、診療・教育・就労支援の隙間を埋める補助層として見るのが妥当だと整理している。^[raw/articles/deep-research-report-ai-software-adhd-2026.md]

## エビデンスの階層

- **比較的強い領域**: ゲーム型デジタル治療、一部の親支援アプリ、成人向けの一部オンラインCBT。報告では EndeavorRx / ENDEAVORRIDE / EndeavorOTC / Prismira などが、主に注意指標の改善を示す規制承認済みまたは市場化された例として挙げられている。^[raw/articles/deep-research-report-ai-software-adhd-2026.md]
- **中程度・限定的な領域**: QbTest / QbCheck のような診断補助。NICEは6〜17歳の標準臨床評価に追加する選択肢としてQbTestを推奨するが、単独診断は不可で、成人では研究段階とされる。これは[[diagnosis-and-management]]の補助情報として読む。^[raw/articles/deep-research-report-ai-software-adhd-2026.md]
- **実用性は高いが医療証拠が薄い領域**: [[tiimo|Tiimo]]、Goblin Tools、Shimmer / Indy、[[focusmate|Focusmate]]のような自己管理・実行機能・共同作業支援。これらは生活上の[[task-initiation]]や[[external-memory]]には役立ちうるが、医療効果の確立とは分ける。^[raw/articles/deep-research-report-ai-software-adhd-2026.md]

## 実装上の要点

- AIは診断の代行ではなく、臨床家・教師・本人・保護者の意思決定を支える補助として設計する。
- 症状尺度だけでなく、学業、就労、家事、欠席・欠勤、生活の質、継続率などの現実の機能指標を見る。
- 未成年者データ、行動ログ、服薬記録、生成AI入力、画面・音声・予定情報は機微情報として扱う。
- 学校・職場では、アプリそのものより、通知の量、配慮設計、負荷設計、導入後のフォロー、同意と監視化の回避が重要になる。

## Wikiでの読み方

この添付報告は有用な横断整理だが、内部に検索由来の引用記号を含む二次的な調査報告であり、一次論文・規制資料そのものではない。強い主張は、今後のingestでPMDA、FDA、NICE、RCT、系統的レビューなどの一次資料に戻して検証する。

## 関連

- [[assistive-technology]]
- [[diagnosis-and-management]]
- [[cognitive-behavioural-therapy]]
- [[medication]]
- [[task-initiation]]
- [[external-memory]]
