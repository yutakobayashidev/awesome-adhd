---
title: 受動記憶アシスタントとADHD設計
created: 2026-07-23
updated: 2026-07-23
type: concept
tags: [adhd, tool, attention, executive-function, working-memory, accessibility, research, work]
sources: [raw/articles/deep-research-screenpipe-rewind-adhd-design-2026.md, entities/screenpipe.md, raw/articles/screenpipe-homepage-2026.md]
confidence: medium
---

# 受動記憶アシスタントとADHD設計

受動記憶アシスタント（passive memory assistant）とは、画面・音声・アプリ操作を常時または選択的に記録し、後から検索・再構築できるツールの総称である。Rewind / Limitless、Screenpipe、Microsoft Recall、Windrecorder などがこの類型に含まれる。ADHD支援として見た場合、単に「全部記録する」だけでは不十分で、**作業復帰、時間定位、外部記憶、感覚安全、利用者制御** の5軸が設計の中心になる。

## 4つの製品群とADHDとの距離

2026年時点の市場は4群に分かれる。

1. **受動記憶システム**: Screenpipe、Rewind/Limitless、Recall、Windrecorder、OpenRecall
2. **会議・音声キャプチャ**: Granola、Otter、Read AI、PLAUD
3. **注意形成・摩擦ツール**: Freedom、one sec、Opal、ScreenZen、Cold Turkey
4. **作業単純化・文脈管理**: Workona、Toby、Raycast、Mem、Morgen

ADHD向けに最も近いのは **受動記憶＋注意形成＋作業単純化の統合** であり、現時点でこれを1つの製品がすべて満たしているわけではない。

## ADHDにとって何が重要か

ADHDの中核的な困難は[[working-memory]]、[[executive-function]]、時間知覚、[[prospective-memory]]、[[task-initiation]]に及ぶ。受動記憶ツールが「全部記録する」ことは、必ずしもこの支援にならない。むしろ次の要件が優先される。

- **作業復帰**: 「さっき何をしていたか」を短く再構成できること。単なるタイムラインではなく、「最後に開いていたファイル」「次にやる操作」「中断前の意図」を返す。
- **時間定位**: 時間盲（time blindness）を補うため、作業の経過、次の予定までの残り時間、今日の時間枠を可視化する。
- **外部記憶**: 頭の中に保持し続ける負荷を下げる。キャプチャはこの手段の一つだが、キャプチャ量が増えると逆に検索と整理の負荷が増す。
- **感覚安全**: 動きの少ないUI、落ち着いた配色、効果音の抑制、視覚密度の低さ。報酬系を刺激するゲーミフィケーションより、静かで調整可能な環境が望ましい。
- **利用者制御とプライバシー**: 画面・音声・行動の記録は機微情報になる。記録のオン/オフ、保持期間、削除、エクスポート、AI処理の可否を利用者が細かく選べることが、信頼と継続利用の前提になる。

## 主要プロダクトのADHD評価

### Screenpipe

現在の最良の参照アーキテクチャ。画面と音声のローカルキャプチャ、SQLite FTS5 全文検索、REST API、MCPサーバー、プラグイン（Pipes）、オンデバイスAI対応を備える。[[screenpipe]]の項も参照。ADHD支援としては、検索力と自動化に強いが、UIは開発者・パワーユーザー向けで、認知負荷の低い日常利用には最適化されていない。

### Rewind / Limitless

Rewind は2025年12月に画面キャプチャを無効化し、Limitless プラットフォームへ移行中。Limitless は会話のライフログ、要約、Ask AI を中心とするクラウド媒介型で、厳密なローカルファーストではない。過去の「個人記憶」という位置づけは参考になるが、現在のプライバシー姿勢は ADHD 向けの機微データを預けるには弱い。

### Microsoft Recall

Windows Copilot+ PC 限定。スナップショットベースのローカル暗号化ストレージ。OS統合は強みだが、ハードウェア制限とプライバシー論争があり、ADHD特化の設計ではない。

### 注意形成ツール（one sec、ScreenZen、Opal など）

アプリを開く前に遅延や呼吸プロンプトを挟む設計は、衝動的なアプリ起動を減らす点で ADHD と相性がよい。ただし、キャプチャや作業復帰の機能は持たない。

## 設計原則

1. **記録は支援の手段であり目的ではない。** まず「再開」「思い出す」「次の一手」が先で、キャプチャはその材料。
2. **3つのホーム状態**: Now（現在の作業と時間定位）、Resume（中断前の文脈の再構成）、Follow-through（リマインダーと行動項目の短いキュー）。ダッシュボード過多を避ける。
3. **穏やかで打ち消せる通知**: 静かなリマインダー、段階的エスカレーション、文脈つきスヌーズ、「このアプリを離れたら聞く」「この会議の後に聞く」。
4. **摩擦は罰ではなく意図の再確認**: one sec のように、注意が逸れる前に本人の意図を再提示する。
5. **プライバシー・バイ・デザイン**: 初期は手動ハイライトのみ、段階的に自動キャプチャを許可、保持期間は既定で短く、記録状態の可視化、ワンクリック停止、目的別モード（学習/会議/プライベート）。
6. **WCAG 2.2 / W3C cognitive accessibility 準拠**: パスキー認証、CAPTCHA回避、冗長入力を減らす、認知的負荷を下げるUIパターン。

## Toymaker / OpenBrief との関係

OpenBrief は注意遷移を扱い、受動記憶アシスタントは作業文脈を扱う。両者は補完的である。

- OpenBrief が「いま読む・守る・退避する・戻る」を扱う入口だとすると、受動記憶アシスタントは「さっき何をしていたか・どこに戻ればいいか・次に何をすればいいか」を扱う出口/背景層。
- OpenBrief の `Return Anchor` が機能するには、ユーザーが「戻るべき作業」を覚えているか、記録から再構成できる必要がある。後者を受動記憶が支える。
- 両者とも local-first、privacy-by-design、低認知負荷UI、利用者制御が中核設計原則になる点で整合する。

## 関連

- [[assistive-technology]]
- [[external-memory]]
- [[task-resumption]]
- [[working-memory]]
- [[executive-function]]
- [[digital-adhd-support]]
- [[screenpipe]]
- [[fear-of-missing-out]]
- [[async-meetings-context-fit]]
