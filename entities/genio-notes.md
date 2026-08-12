---
title: Genio Notes
created: 2026-07-24
updated: 2026-07-30
type: entity
tags: [tool, accessibility, school, work]
sources: [raw/articles/deep-research-report-stt-neurodiversity-2026.md]
confidence: medium
---

# Genio Notes

旧称 Glean。高等教育における学習支援を目的とした SaaS で、**録音・文字起こし・ノート化**を一つのワークフローに統合している。障害学生支援での採用を前提に設計されており、神経多様性（ADHD、ディスレクシアなど）のある学習者に向けた「同時処理負荷の低減」が中核的な価値提案である。

## 主な機能

- **録音** — 講義や授業の音声を録音
- **後からの transcription** — 録音後に高精度な文字起こしを実行
- **speaker diarisation** — 話者分離により、複数話者の発言を区別
- **transcript 断片のノート転記** — transcript の該当箇所をクリックしてノートへ送る
- **同期再生** — 文字起こしと音声の同期再生により、該当箇所の音声を聞き直せる

## ADHD・神経多様性との接点

公式資料では、学生が**講義中に内容理解へ集中し、後から transcript と同期再生で理解を補強できる**点が強調されている。これは、ADHD の「聞き逃しや集中の揺れを後から補完する」ニーズ、およびディスレクシアの「聞きながら全部書こうとしない」設計方針の双方に合致する。

Genio Notes の「録る→見返す→切り出す→再整理する」という UX フローは、[[executive-function|実行機能]]の外部化と[[external-memory|外部記憶]]のパターンとして参照できる。リアルタイムの逐語転写精度を競うのではなく、**後処理での構造化とユーザーによる取捨選択**に価値を置いている点が、[[speech-to-text-neurodiversity-support|STTと神経多様性支援]]の design principle と整合する。

## 注意点

- **公開価格は機関見積中心で詳細非公開**。学生個人ではなく教育機関向けのライセンスモデルとみられる。
- **詳細な PII 仕様は公開取得資料で限定的**。学習支援文脈での音声・文字起こしデータの取り扱いについては、導入前に機関側での確認が必要。
- WER（Word Error Rate）などの精度指標は公表されていない。
- 本ページは公開情報と二次的な市場調査に基づく製品説明であり、独立した有効性評価ではない。

## 関連ページ

- [[speech-to-text-neurodiversity-support]] — STT 全般の神経多様性支援設計
- [[assistive-technology]] — より広い支援技術の枠組み
- [[digital-adhd-support]] — デジタル ADHD 支援の全体像
- 学校・教育現場での ADHD 支援 — 学校・教育現場での支援文脈（専用ページ未作成）
