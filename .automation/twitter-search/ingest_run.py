from pathlib import Path
import json, hashlib, re
W=Path('/var/lib/hermes/awesome-adhd')
D=W/'.automation/twitter-search'
DATE='2026-08-13'
ids={
 '2087887849819459834':'morning-ninety-minute-defense-time',
 '2087875589726175569':'pay-receive-one-set-chant',
}
items={}
for name in ['latest1.json','top1.json','latest2.json','top2.json']:
    data=json.loads((D/name).read_text())
    for t in data:
        tid=str(t.get('id',''))
        if tid in ids and tid not in items:
            items[tid]=t
created=[]
for tid, slug in ids.items():
    t=items[tid]
    a=t.get('author') or {}
    url=f"https://x.com/{a.get('username','')}/status/{tid}"
    body=[]
    body.append(f"# Tweet {tid}: {slug}\n")
    body.append(f"- URL: {url}")
    body.append(f"- Author: @{a.get('username','')} ({a.get('name','')})")
    body.append(f"- Created at: {t.get('createdAt','')}")
    body.append(f"- Metrics at ingest: replies={t.get('replyCount')}, reposts={t.get('retweetCount')}, likes={t.get('likeCount')}")
    body.append("")
    body.append("## Tweet text")
    body.append("")
    text=t.get('text','').strip()
    # keep public text needed for tactic; no profile image/media saved
    body.append(text)
    if t.get('quotedTweet'):
        q=t['quotedTweet']; qa=q.get('author') or {}
        body.append("\n## Quoted tweet")
        body.append(f"- ID: {q.get('id')}")
        body.append(f"- Author: @{qa.get('username','')} ({qa.get('name','')})")
        body.append(q.get('text','').strip())
    body_s='\n'.join(body).rstrip()+"\n"
    sha=hashlib.sha256(body_s.encode()).hexdigest()
    fm=f"---\nsource_url: {url}\ningested: {DATE}\nsha256: {sha}\n---\n\n"
    path=W/'raw/articles'/f'tweet-{tid}-{slug}.md'
    path.write_text(fm+body_s)
    created.append(str(path.relative_to(W)))
print('\n'.join(created))
