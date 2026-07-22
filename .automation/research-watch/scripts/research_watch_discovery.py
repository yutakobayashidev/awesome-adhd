#!/usr/bin/env python3
"""Discover machine-readable ADHD research candidates for the awesome-adhd LLM Wiki.

No third-party dependencies. Writes compact state and append-only JSONL candidates.
"""
from __future__ import annotations

import argparse
import email.utils
import hashlib
import json
import re
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

DEFAULT_WIKI = Path("/var/lib/hermes/awesome-adhd")
UA = "awesome-adhd-research-watch/1.0 (+https://github.com/yutakobayashidev/awesome-adhd)"
ATOM = {"a": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}

HIGH_TERMS = [
    "adhd", "attention deficit", "executive function", "working memory",
    "time management", "task initiation", "digital intervention", "assistive technology",
    "ecological momentary", "smartphone", "mobile app", "reminder", "planning",
    "accessibility", "neurodiversity", "adult adhd", "workplace", "school",
]
LOW_TERMS = ["review", "meta-analysis", "systematic review", "guideline", "randomized", "trial"]
SKIP_TERMS = ["meme", "celebrity", "astrology", "zodiac"]


def utcnow() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def fetch_text(url: str, timeout: int = 30) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json, application/atom+xml, application/xml, text/xml, */*"})
    with urllib.request.urlopen(req, timeout=timeout) as r:  # noqa: S310: known configured sources only
        return r.read().decode("utf-8", "replace")


def compact(s: str | None, n: int = 1400) -> str:
    if not s:
        return ""
    s = re.sub(r"\s+", " ", s).strip()
    return s[: n - 1] + "…" if len(s) > n else s


def norm_date(s: str | None) -> str | None:
    if not s:
        return None
    s = s.strip()
    if re.match(r"^\d{4}-\d{2}-\d{2}", s):
        return s[:10]
    try:
        return email.utils.parsedate_to_datetime(s).date().isoformat()
    except Exception:
        return s[:40]


def candidate_id(prefix: str, value: str) -> str:
    value = value.strip()
    if value:
        return f"{prefix}:{value}"
    return f"{prefix}:sha256:{hashlib.sha256(value.encode()).hexdigest()[:16]}"


def score_hint(title: str, abstract: str, source: str) -> tuple[int, list[str]]:
    text = f"{title} {abstract}".lower()
    reasons: list[str] = []
    score = 1
    if any(t in text for t in SKIP_TERMS):
        return 0, ["skip term"]
    for term in HIGH_TERMS:
        if term in text:
            reasons.append(term)
    if "adhd" in text or "attention deficit" in text:
        score = 2
    if len(reasons) >= 3:
        score = 3
    if any(t in text for t in LOW_TERMS) and ("adhd" in text or "attention deficit" in text):
        score = max(score, 4)
        reasons.append("strong evidence type")
    if source in {"arxiv", "semantic_scholar"} and "adhd" not in text and "attention deficit" not in text:
        score = min(score, 2)
    return score, sorted(set(reasons))[:12]


def arxiv_url(query: str, max_results: int) -> str:
    params = {
        "search_query": query,
        "max_results": str(max_results),
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    }
    return "https://export.arxiv.org/api/query?" + urllib.parse.urlencode(params)


def discover_arxiv(items: list[dict[str, Any]]) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for q in items:
        try:
            xml = fetch_text(arxiv_url(q["query"], int(q.get("max_results", 10))))
            root = ET.fromstring(xml)
            for e in root.findall("a:entry", ATOM):
                entry_url = (e.findtext("a:id", default="", namespaces=ATOM) or "").strip().replace("http://", "https://")
                arxiv_id = entry_url.rsplit("/abs/", 1)[-1]
                title = compact(e.findtext("a:title", namespaces=ATOM), 500)
                abstract = compact(e.findtext("a:summary", namespaces=ATOM), 2000)
                authors = [compact(a.findtext("a:name", namespaces=ATOM), 160) for a in e.findall("a:author", ATOM)]
                published = norm_date(e.findtext("a:published", namespaces=ATOM))
                doi = None
                for link in e.findall("a:link", ATOM):
                    if link.get("title") == "doi":
                        doi = link.get("href")
                score, reasons = score_hint(title, abstract, "arxiv")
                out.append({
                    "id": candidate_id("arxiv", arxiv_id),
                    "source": "arxiv",
                    "query_name": q["name"],
                    "title": title,
                    "url": entry_url,
                    "pdf_url": f"https://arxiv.org/pdf/{arxiv_id}",
                    "published": published,
                    "authors": authors,
                    "abstract": abstract,
                    "doi": doi,
                    "score_hint": score,
                    "reasons": reasons,
                })
            time.sleep(3.1)  # arXiv courtesy
        except Exception as exc:
            print(f"warn: arxiv {q.get('name')} failed: {exc}", file=sys.stderr)
    return out


def discover_pubmed(items: list[dict[str, Any]]) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for q in items:
        try:
            params = urllib.parse.urlencode({"db": "pubmed", "term": q["query"], "retmode": "json", "retmax": int(q.get("max_results", 20)), "sort": "pub date"})
            data = json.loads(fetch_text("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?" + params))
            ids = data.get("esearchresult", {}).get("idlist", [])
            if not ids:
                continue
            summary_params = urllib.parse.urlencode({"db": "pubmed", "id": ",".join(ids), "retmode": "json"})
            sums = json.loads(fetch_text("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?" + summary_params)).get("result", {})
            for pmid in ids:
                r = sums.get(pmid, {})
                title = compact(r.get("title"), 500)
                authors = [a.get("name", "") for a in r.get("authors", [])[:12]]
                pubdate = norm_date(r.get("pubdate"))
                article_ids = r.get("articleids", []) or []
                doi = next((a.get("value") for a in article_ids if a.get("idtype") == "doi"), None)
                abstract = compact(f"Journal: {r.get('fulljournalname', '')}. Type: {', '.join(r.get('pubtype', []) or [])}. {title}", 1200)
                score, reasons = score_hint(title, abstract, "pubmed")
                out.append({
                    "id": candidate_id("pubmed", pmid),
                    "source": "pubmed",
                    "query_name": q["name"],
                    "title": title,
                    "url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/",
                    "published": pubdate,
                    "authors": authors,
                    "abstract": abstract,
                    "doi": doi,
                    "score_hint": score,
                    "reasons": reasons,
                })
            time.sleep(0.4)
        except Exception as exc:
            print(f"warn: pubmed {q.get('name')} failed: {exc}", file=sys.stderr)
    return out


def discover_semantic(items: list[dict[str, Any]]) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    fields = "title,authors,year,abstract,citationCount,influentialCitationCount,isOpenAccess,openAccessPdf,externalIds,publicationVenue,url"
    for q in items:
        try:
            params = urllib.parse.urlencode({"query": q["query"], "limit": int(q.get("max_results", 10)), "fields": fields})
            data = json.loads(fetch_text("https://api.semanticscholar.org/graph/v1/paper/search?" + params))
            for r in data.get("data", []) or []:
                ex = r.get("externalIds") or {}
                ident = ex.get("DOI") or ex.get("PubMed") or ex.get("ArXiv") or r.get("paperId", "")
                title = compact(r.get("title"), 500)
                abstract = compact(r.get("abstract"), 2000)
                authors = [a.get("name", "") for a in (r.get("authors") or [])[:12]]
                score, reasons = score_hint(title, abstract, "semantic_scholar")
                if r.get("citationCount", 0) >= 50:
                    reasons.append("citationCount>=50")
                    score = max(score, 3)
                if r.get("influentialCitationCount", 0) >= 10:
                    reasons.append("influentialCitationCount>=10")
                    score = max(score, 3)
                out.append({
                    "id": candidate_id("semantic_scholar", ident),
                    "source": "semantic_scholar",
                    "query_name": q["name"],
                    "title": title,
                    "url": r.get("url") or (f"https://doi.org/{ex['DOI']}" if ex.get("DOI") else ""),
                    "published": str(r.get("year")) if r.get("year") else None,
                    "authors": authors,
                    "abstract": abstract,
                    "doi": ex.get("DOI"),
                    "external_ids": ex,
                    "citation_count": r.get("citationCount"),
                    "influential_citation_count": r.get("influentialCitationCount"),
                    "is_open_access": r.get("isOpenAccess"),
                    "open_access_pdf": r.get("openAccessPdf"),
                    "score_hint": score,
                    "reasons": sorted(set(reasons)),
                })
            time.sleep(1.1)
        except Exception as exc:
            print(f"warn: semantic_scholar {q.get('name')} failed: {exc}", file=sys.stderr)
    return out


def discover_rss(items: list[dict[str, Any]]) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for q in items:
        try:
            xml = fetch_text(q["url"])
            root = ET.fromstring(xml)
            # RSS item or Atom entry
            entries = root.findall(".//item") + root.findall("a:entry", ATOM)
            for e in entries[:50]:
                title = compact(e.findtext("title") or e.findtext("a:title", namespaces=ATOM), 500)
                summary = compact(e.findtext("description") or e.findtext("summary") or e.findtext("a:summary", namespaces=ATOM), 1400)
                text = f"{title} {summary}".lower()
                if "adhd" not in text and "attention deficit" not in text:
                    continue
                link = e.findtext("link") or ""
                if not link:
                    l = e.find("a:link", ATOM)
                    link = l.get("href") if l is not None else ""
                published = norm_date(e.findtext("pubDate") or e.findtext("a:published", namespaces=ATOM) or e.findtext("a:updated", namespaces=ATOM))
                score, reasons = score_hint(title, summary, "rss")
                out.append({"id": candidate_id("rss", link or title), "source": "rss", "query_name": q["name"], "title": title, "url": link, "published": published, "authors": [], "abstract": summary, "score_hint": score, "reasons": reasons})
        except Exception as exc:
            print(f"warn: rss {q.get('name')} failed: {exc}", file=sys.stderr)
    return out


def load_json(path: Path, default: Any) -> Any:
    if not path.exists() or not path.read_text().strip():
        return default
    return json.loads(path.read_text())


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--wiki", default=str(DEFAULT_WIKI))
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--limit", type=int, default=None)
    args = ap.parse_args()

    wiki = Path(args.wiki)
    base = wiki / ".automation" / "research-watch"
    config = load_json(base / "feeds.json", {})
    state = load_json(base / "state.json", {"version": 1, "seen_ids": [], "stats": {"runs": 0, "candidates_written": 0}})
    seen = set(state.get("seen_ids", []))
    queries = config.get("queries", {})

    candidates: list[dict[str, Any]] = []
    candidates += discover_arxiv(queries.get("arxiv", []))
    candidates += discover_pubmed(queries.get("pubmed", []))
    candidates += discover_semantic(queries.get("semantic_scholar", []))
    candidates += discover_rss(queries.get("rss", []))

    dedup: dict[str, dict[str, Any]] = {}
    for c in candidates:
        if not c.get("title") or c.get("score_hint", 0) <= 0:
            continue
        key_value = c.get("doi") or c.get("id") or c.get("url")
        if not key_value:
            continue
        key = str(key_value)
        if key in dedup:
            if c.get("score_hint", 0) > dedup[key].get("score_hint", 0):
                dedup[key] = c
            continue
        dedup[key] = c

    now = utcnow()
    new = []
    for c in sorted(dedup.values(), key=lambda x: (x.get("score_hint", 0), x.get("published") or ""), reverse=True):
        cid = c["id"]
        if cid in seen:
            continue
        c["discovered_at"] = now
        c["status"] = "pending"
        new.append(c)
        if args.limit and len(new) >= args.limit:
            break
        if len(new) >= int(config.get("max_new_per_run", 40)):
            break

    if args.dry_run:
        print(json.dumps({"dry_run": True, "new_candidates": len(new), "top": new[:10]}, ensure_ascii=False, indent=2))
        return 0

    if new:
        with (base / "candidates.jsonl").open("a", encoding="utf-8") as f:
            for c in new:
                f.write(json.dumps(c, ensure_ascii=False, sort_keys=True) + "\n")
        seen.update(c["id"] for c in new)

    state["last_run_at"] = now
    state["seen_ids"] = sorted(seen)[-5000:]
    stats = state.setdefault("stats", {})
    stats["runs"] = int(stats.get("runs", 0)) + 1
    stats["candidates_written"] = int(stats.get("candidates_written", 0)) + len(new)
    tmp = base / "state.json.tmp"
    tmp.write_text(json.dumps(state, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    tmp.replace(base / "state.json")

    if new:
        print(f"ADHD research-watch: discovered {len(new)} new candidate(s). Top items:")
        for c in new[:8]:
            print(f"- score_hint={c.get('score_hint')} {c.get('source')} | {c.get('title')} | {c.get('url')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
