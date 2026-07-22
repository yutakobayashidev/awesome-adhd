# Wiki Schema

## Domain

ADHD（注意欠如・多動症）に関する知識ベース。研究、支援策、生活・学習・仕事の工夫、当事者体験、制度、道具、併存しやすい課題、誤解や論争を扱う。

このWikiは医療判断の代替ではない。診断、処方、治療方針は医師など専門職に確認する。個人の体験・症状・服薬情報を扱う場合は、本人特定につながる情報を保存しない。

## Conventions

- File names: lowercase, hyphens, no spaces（例: `working-memory.md`）
- Every wiki page starts with YAML frontmatter（下記）
- Use `[[wikilinks]]` to link between pages（各ページ最低2本の外部リンクを目標）
- When updating a page, always bump the `updated` date
- Every new page must be added to `index.md` under the correct section
- Every action must be appended to `log.md`
- `raw/` は原資料置き場。原則として取り込んだ後は変更しない
- ADHD当事者・家族・支援者の個人情報は保存しない。必要なら匿名化し、出典にも注意する
- 医療・薬・診断については断定しすぎず、出典、対象国、時期、限界を書く
- 日本語では自然な日本語を優先し、必要以上に英語・片仮名語へ寄せない

## Frontmatter

```yaml
---
title: Page Title
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity | concept | comparison | query | summary
tags: [from taxonomy below]
sources: [raw/articles/source-name.md]
confidence: high | medium | low
contested: true
contradictions: [other-page-slug]
---
```

`confidence`, `contested`, `contradictions` は任意。ただし単一出典、意見が分かれる話題、医療・薬・制度のように変わりやすい話題では `confidence` を付ける。

## raw/ Frontmatter

```yaml
---
source_url: https://example.com/article
ingested: YYYY-MM-DD
sha256: <hex digest of the raw content below the frontmatter>
---
```

`sha256` は frontmatter を除いた本文に対して計算する。

## Tag Taxonomy

### Core
- adhd
- attention
- impulsivity
- hyperactivity
- executive-function
- working-memory
- time-management
- emotion-regulation

### Life Contexts
- school
- work
- home
- relationships
- parenting
- accessibility
- public-support

### Health / Care
- diagnosis
- medication
- therapy
- sleep
- comorbidity
- autism
- anxiety
- depression
- substance-use

### Sources / Meta
- research
- guideline
- lived-experience
- tool
- policy
- controversy
- comparison
- japanese-context

Rule: every tag on a page must appear in this taxonomy. If a new tag is needed, add it here first, then use it.

## Page Thresholds

- **Create a page** when an entity/concept appears in 2+ sources OR is central to one source
- **Add to existing page** when a source mentions something already covered
- **DON'T create a page** for passing mentions, minor details, or things outside the domain
- **Split a page** when it exceeds ~200 lines
- **Archive a page** when its content is fully superseded — move to `_archive/`, remove from index

## Entity Pages

One page per notable entity. Include:
- Overview / what it is
- Key facts and dates
- Relationship to other entities and concepts via `[[wikilinks]]`
- Source references

Entities may include researchers, institutions, guidelines, tools, laws, support programs, books, or organizations.

## Concept Pages

One page per concept or topic. Include:
- Definition / explanation
- Current state of knowledge
- Practical implications
- Limits, cautions, or contested points
- Related concepts via `[[wikilinks]]`

## Comparison Pages

Side-by-side analyses. Include:
- What is being compared and why
- Dimensions of comparison, preferably as a table
- Verdict or synthesis
- Sources

## Update Policy

When new information conflicts with existing content:
1. Check the dates and jurisdiction — newer or local sources may supersede older/general sources
2. If genuinely contradictory, note both positions with dates and sources
3. Mark the contradiction in frontmatter: `contradictions: [page-name]`
4. Flag for user review in the lint report

## Safety Notes

- Avoid giving personal medical advice. Summarize sources and encourage professional consultation when relevant
- Do not store identifying personal health information
- Treat medication details as source-bound facts, not recommendations
- Distinguish research findings, clinical guidance, personal experience, and productivity tips
