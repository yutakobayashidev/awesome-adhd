# Research Watch Automation

Recurring source discovery and curation for the `awesome-adhd` LLM Wiki.

## Files

- `feeds.json` — machine-readable discovery sources and queries.
- `interest-profile.md` — scoring rubric for what belongs in the wiki.
- `state.json` — compact state: seen IDs, run times, and counters.
- `candidates.jsonl` — append-only candidate queue, one JSON object per source.
- `scripts/research_watch_discovery.py` — deterministic discovery script.

## Pipeline

```text
arXiv / PubMed / RSS
  -> discovery script
  -> candidates.jsonl + state.json
  -> LLM curation cron
  -> raw/papers, raw/articles, concepts, entities, comparisons, index, log
```

Discovery is mechanical and cheap. It does not edit wiki concept pages. Curation is LLM-driven and conservative.

Semantic Scholar is intentionally not polled in the default discovery loop because the unauthenticated API rate-limits easily. Use it during curation to enrich specific candidate papers with citation counts, related work, and open-access PDF metadata.

## Candidate schema

Each line in `candidates.jsonl` is JSON:

```json
{
  "id": "pubmed:12345678",
  "source": "pubmed",
  "query_name": "adult-adhd-digital-support",
  "title": "...",
  "url": "https://pubmed.ncbi.nlm.nih.gov/12345678/",
  "published": "2026-07-22",
  "authors": ["..."],
  "abstract": "...",
  "doi": "...",
  "score_hint": 3,
  "reasons": ["adult ADHD", "digital support", "executive function"],
  "discovered_at": "2026-07-22T00:00:00Z",
  "status": "pending"
}
```

The curation job may add `status: accepted|raw-only|skipped|processed` records to state, but should avoid rewriting the append-only candidate log unless necessary.
