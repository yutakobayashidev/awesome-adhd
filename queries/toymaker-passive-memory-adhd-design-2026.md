---
title: Toymaker: 受動記憶・ADHD設計・Screenpipe/Rewind調査
created: 2026-07-23
updated: 2026-07-23
type: query
tags: [adhd, tool, attention, executive-function, working-memory, accessibility, research]
sources: [raw/articles/deep-research-screenpipe-rewind-adhd-design-2026.md, concepts/passive-memory-assistants-adhd.md, concepts/async-meetings-context-fit.md, concepts/task-resumption.md, concepts/external-memory.md, entities/screenpipe.md]
confidence: medium
---

# Toymaker: 受動記憶・ADHD設計・Screenpipe/Rewind調査

## 調査の背景

受動記憶ツール（スクリーンキャプチャ・音声記録・検索）はADHDの作業記憶補助として有望だが、現行製品はADHD向けに特化していない。この調査では Rewind/Limitless、Screenpipe、Recall、競合群と ADHD 認知研究を照合し、Toymaker で作るべきプロダクトの要件を整理した。

## 主要な発見

### 1. 市場は4層に分かれる

- 受動記憶（Screenpipe、Rewind、Recall）
- 会議キャプチャ（Granola、Otter）
- 注意摩擦（one sec、Opal、ScreenZen）
- 作業単純化（Workona、Raycast、Morgen）

**どの層も単独ではADHD支援として不十分。** 必要なのは「受動記憶×注意摩擦×時間定位×低認知負荷UI」の統合。

### 2. Screenpipe が現在の最良の参照アーキテクチャ

- ローカルファースト（SQLite FTS5、オンデバイス）
- イベント駆動キャプチャ（画面＋音声）
- REST API、MCPサーバー、Pipesプラグイン
- Rust + TypeScript + Tauri
- プライバシー制御が比較的強い

ただしUIは開発者向けで、認知負荷の低い日常利用には最適化されていない。

### 3. ADHD設計の中心は「作業復帰」と「外部記憶」

ADHD研究が示す中核課題:
- [[working-memory]] の弱さ → 記録は「全部保存」より「再開に必要な最小限」が効く
- [[prospective-memory]] の弱さ → 画面キャプチャより「次の一手」の抽出が価値を持つ
- 時間盲 → 時間定位（経過・残り・次の予定）が必須
- 実行機能の個人差が大きい → 強制ではなく調整可能な支援

### 4. Rewind は設計参照としての価値が下がった

- 2025年12月に画面キャプチャ無効化
- 現在は Limitless プラットフォーム（クラウド媒介）へ移行中
- プライバシー姿勢が ADHD 向けの機微データには弱い
- 「記憶」という製品フレーミングは参考になる

## Toymaker への設計示唆

### 絶対にやるべきこと

1. **3状態UI**: Now（現在の作業＋時間定位）、Resume（中断前の文脈再構成）、Follow-through（リマインダー＋次の一手）
2. **手動ハイライトから始める**: 全自動キャプチャは信頼を得てから。最初は「ここを覚えておいて」ボタンだけ。
3. **「次の一手」抽出**: キャプチャから操作意図を推測し、「最後は○○を編集中。次は△△を保存してから××を開く」のような再開パックを作る。
4. **穏やかな通知**: 静かなリマインダー、文脈つきスヌーズ、段階的エスカレーション。報酬系刺激は避ける。
5. **時間定位**: 見やすいアナログ時計風、経過表示、次の予定までの残り時間。
6. **プライバシー・バイ・デザイン**: ローカル保存、短い既定保持期間、目的別モード（学習/会議/プライベート）、ワンクリック停止、エクスポート/削除。

### やってはいけないこと

- 全画面の常時動画記録（ストレージ・プライバシー・認知負荷の三重苦）
- ゲーミフィケーション（streak、ランキング、報酬音）
- AIによる行動の自動評価や人格判断
- チームへの自動共有（同意なき注意状態の露出）
- キャプチャ履歴の無限保持

### OpenBrief との接続

OpenBrief は注意遷移の入口、受動記憶アシスタントは作業文脈の背景層。

- OpenBrief の `Return Anchor` を受動記憶が補強: 会議や探索の前の作業状態をキャプチャから自動で再構成する。
- OpenBrief の `BriefSession` 中に受動記憶が「この記事を読む前に何をしていたか」を表示する。
- Capture した問いを、受動記憶のタイムライン上で「この時点で気になったこと」として関連付ける。

### 技術スタック案

- デスクトップシェル: Tauri
- ローカル検索: SQLite FTS5
- 文字起こし: whisper.cpp（ローカル）
- OCR: Tesseract（フォールバック）
- ローカルAPI: MCPサーバー
- プライバシー: オンデバイス処理、保持期間制限、エクスポート/削除API

このスタックは Screenpipe の実績ある構成と一致し、ADHD特化のUI/UX層を上に載せる差別化が可能。

## 実装優先順位

| 優先度 | 機能 | 理由 |
|---|---|---|
| P0 | 手動ハイライト＋再開パック | 信頼構築と中核価値の証明 |
| P0 | Now / Resume / Follow-through UI | ADHD向けの最小限の認知負荷 |
| P0 | ローカル保存＋エクスポート/削除 | プライバシー信頼の前提 |
| P1 | 画面コンテキストの自動キャプチャ | 手動の限界を補う |
| P1 | 「次の一手」抽出 | 外部記憶としての価値 |
| P1 | リマインダー＋時間定位 | 時間盲の支援 |
| P2 | 音声キャプチャ＋文字起こし | 会議・通話の文脈復帰 |
| P2 | MCP/API | AIクライアント連携 |
| P3 | 暗号化同期 | 複数端末 |
| P3 | 注意摩擦ルール | one sec 的衝動制御 |

## リスク

- **過剰キャプチャ**: 全部記録すると検索と整理の負荷が増し、ADHD支援として逆効果。
- **監視と誤解**: 行動ログが職場や家族の監視・評価に使われる危険。ローカル保存と明示的同意が必須。
- **通知疲れ**: 多すぎるリマインダーは無視されるか、新たなストレス源になる。
- **AIの誤推定**: 「重要」「気が散っている」「先延ばし」などのラベル付けは、本人の主観とずれると害になる。

## 関連

- [[passive-memory-assistants-adhd]]
- [[toymaker-openbrief-adhd-design-notes]]
- [[openbrief-vs-karpathy-llm-wiki-2026]]
- [[toymaker-neurodivergent-async-meetings-ai-2026]]
- [[assistive-technology]]
- [[external-memory]]
- [[task-resumption]]
- [[screenpipe]]
