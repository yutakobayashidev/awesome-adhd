# ADHD Research Watch Interest Profile

This file guides automated source discovery and curation for the `awesome-adhd` LLM Wiki.

## High-signal sources

- Systematic reviews, meta-analyses, clinical guidelines, and well-described trials about ADHD support.
- Adult ADHD, executive function, working memory, time management, task initiation, attention regulation, sleep, and work/school accommodations.
- Digital tools, reminders, planning apps, wearables, ecological momentary interventions, assistive technology, and HCI/accessibility research.
- Neurodiversity and accessibility work that yields reusable design or support patterns.
- Public-interest or policy material about accommodations, welfare, education, labor, disability rights, or access to care.

## Medium-signal sources

- Single studies that are relevant but small, early, or narrowly scoped.
- Preprints with concrete methods or useful literature references.
- Product pages or implementation reports that describe a tool pattern clearly, but do not independently establish effectiveness.

## Low-signal / skip by default

- Generic ADHD explainers with no new actionable or evidentiary value.
- SEO health pages, ads, affiliate pages, thin summaries, and listicles.
- Medication, diagnosis, or treatment advice without strong source context.
- Content focused only on children when no broader support or design pattern is extractable.
- Stigma, drama, memes, personal conflict, or sensational claims.

## Scoring

Use the curated-source-ingest scale:

- `0`: skip.
- `1`: keep only in automation state.
- `2`: save raw source only.
- `3`: save raw source and update existing wiki page.
- `4`: save raw source and create or substantially update a page.

For automatic curation, default to conservative behavior:

- Score `>=2`: raw save is acceptable.
- Score `>=3`: concept/entity/index/log update is acceptable.
- Score `4`: only for central, durable sources such as reviews, guidelines, or unusually relevant tool/design papers.

## Safety

Separate source type from claim strength:

- Research/guidelines: source-bound evidence, with population, date, method, and limits.
- Product pages: tool descriptions, not proof of effect.
- X/Twitter and lived experience: practical notes, not medical evidence.

Do not write personal medical advice. Do not save identifying health information. Medication and diagnostic claims must be cautious and source-bound.
