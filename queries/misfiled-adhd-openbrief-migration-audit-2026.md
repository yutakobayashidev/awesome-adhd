---
title: Misfiled ADHD / OpenBrief Migration Audit
created: 2026-07-23
updated: 2026-07-23
type: query
tags: [adhd, tool, accessibility, research]
sources: [raw/articles/github-open-brief-project-docs-2026.md, raw/articles/x-tmiyatake-admin-night-2026.md, raw/papers/arxiv-cognitive-personal-informatics-chi26-2026.md]
confidence: medium
---

# Misfiled ADHD / OpenBrief Migration Audit

## 目的

`/var/lib/hermes/wiki` に誤投入された ADHD / OpenBrief / Toymaker 関連の raw / concept / query を監査し、`/var/lib/hermes/awesome-adhd` へ移すべきものを移した記録。

## 移植したもの

### FOMO / 通知 / SNS

- `raw/papers/przybylski-2013-fomo-scale.md`
- `raw/papers/elhai-2021-fomo-overview.md`
- `raw/papers/fitz-2019-notification-batching-fomo.md`
- `raw/papers/montag-2023-fomo-cognitive-failure.md`
- `raw/papers/akbari-2021-fomo-internet-use-meta-analysis.md`
- `raw/papers/groenestein-2024-fomo-social-media-longitudinal.md`
- `concepts/fear-of-missing-out.md`

理由: ADHD 支援の [[digital-interruptions]]、[[task-resumption]]、[[emotion-regulation]] と直接接続するため。

### Admin Night / body doubling

- `raw/articles/x-tmiyatake-admin-night-2026.md`
- `raw/articles/body-doubling-life-admin-sources-2026.md`
- `concepts/body-doubling.md` に「アドミン・ナイト」節を追加

理由: `Admin Night` は単独の強い用語ではないが、生活事務に特化した [[body-doubling]] として ADHD Wiki に有用。動画はユーザー指示により文字起こししていない。

### 認知パーソナルインフォマティクス / 読解 / EMA

- `raw/papers/arxiv-cognitive-personal-informatics-chi26-2026.md`
- `raw/papers/arxiv-multilingual-text-to-pictogram-reading-rehabilitation-2026.md`
- `raw/papers/arxiv-neurodiversity-demographics-education-research-2026.md`
- `raw/papers/pubmed-adhd-digital-text-comprehension-self-monitoring-2019.md`
- `raw/papers/pubmed-adhd-ema-daily-life-adolescents-2026.md`
- `concepts/cognitive-personal-informatics.md`
- `concepts/assistive-technology.md` を更新
- `concepts/digital-adhd-support.md` を更新

理由: 認知状態の記録、デジタル読解、自己モニタリング、日常場面での短い反復記録は、ADHD 支援技術の設計資料として有用。ただし監視化の危険を明記する。

### OpenBrief / Toymaker

- `raw/articles/github-open-brief-project-docs-2026.md`
- `queries/toymaker-openbrief-adhd-design-notes.md` を更新

理由: OpenBrief は ADHD 専用プロジェクトではないが、通知、作業復帰、生活事務、FoMO、body doubling を試す Toymaker 文脈の設計対象として扱える。

### i-have-adhd / Tiimo

- `raw/articles/i-have-adhd-agent-output-skill-2026.md`
- `raw/articles/tiimo-neurodivergent-planner-2026.md`
- `entities/i-have-adhd.md` を更新
- `entities/tiimo.md` を更新

理由: 既存 entity があったため新規ページではなく sources と補足説明を追加した。

## 移植しなかった / 統合扱いにしたもの

- `/var/lib/hermes/wiki/concepts/body-doubling-admin-night.md` は、awesome-adhd では独立ページにせず `concepts/body-doubling.md` へ統合した。
- `/var/lib/hermes/wiki/raw/articles/theconversation-waiting-mode-neurodivergent-time-2026.md` は、awesome-adhd に `raw/articles/waiting-mode-the-conversation-2026.md` として既に同一 source があるため追加しなかった。
- 一般 LLM infrastructure / agent security / MLOps / graph RAG / formal proof などは ADHD Wiki の主領域外なので `/var/lib/hermes/wiki` 側に残した。

## 検証

- raw frontmatter の sha256 は再計算済み。
- ページ数: 38 pages。
- broken wikilinks: 0。
- index missing pages: 0。
- raw sha mismatches: 0。

## 再発防止

今後 awesome-adhd 関連の ingest 前には、`findmnt -T /var/lib/hermes/awesome-adhd` と `git -C /var/lib/hermes/awesome-adhd status` を確認する。`WIKI_PATH=/var/lib/hermes/wiki` は一般 LLM Wiki であり、ADHD / Toymaker / OpenBrief の ADHD 支援文脈は `/var/lib/hermes/awesome-adhd` を正とする。
