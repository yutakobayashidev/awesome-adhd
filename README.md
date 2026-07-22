# awesome-adhd

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A practical ADHD LLM Wiki and awesome list.

This repo collects research, support practices, tools, and lived-experience tactics for ADHD. It is not just a link dump. Sources are saved, summarized, cross-linked, and turned into pages that can compound over time.

> [!IMPORTANT]
> This repository is not medical advice. Talk to a qualified clinician about diagnosis, medication, or treatment decisions. We avoid storing personal health details that could identify someone.

## What is this?

- A practical knowledge base about ADHD.
- A Markdown vault grown in the style of Karpathy's LLM Wiki.
- An awesome-adhd list that is readable on GitHub.
- Plain files you can open in Obsidian, VS Code, or any editor.

As an LLM Wiki, this repo keeps source material in `raw/` and turns useful ideas into pages under `entities/` and `concepts/`. Pages use `[[wikilinks]]` so related ideas stay connected.

As an awesome list, the Contents section below gives you the public-facing entry point.

## Contents

### Tools

- [i-have-adhd](entities/i-have-adhd.md) - An agent skill/plugin that makes coding-agent output more ADHD-friendly: action first, numbered steps, visible progress, concrete time estimates, and fewer tangents.
- [screenpipe](entities/screenpipe.md) - A local-first workflow-memory tool that records screen and audio context, makes work history searchable, and can trigger agents such as meeting-note automation.
- [Tiimo](entities/tiimo.md) - A visual planning app for ADHD and autistic users, with timelines, focus timers, AI task breakdowns, widgets, and other supports for executive function.

### Guidelines and evidence sources

- [NICE NG87](entities/nice-ng87.md) - UK guidance on recognition, diagnosis, and management of ADHD; useful as a structured reference, not personal medical advice.

### Concepts

- [Cognitive behavioural therapy](concepts/cognitive-behavioural-therapy.md) - CBT-based interventions for adult ADHD, summarized with Cochrane evidence limits and links to executive-function support.
- [Comorbidity](concepts/comorbidity.md) - Anxiety, depression, substance use, and broader mental-health risks that may overlap with ADHD and need specialist boundaries.
- [Diagnosis and management](concepts/diagnosis-and-management.md) - Guideline-based notes on diagnosis discussions, environmental adjustments, psychosocial support, medication, and review.
- [Emotion regulation](concepts/emotion-regulation.md) - How anxiety, low mood, anger, or rumination can interact with attention, initiation, and executive function.
- [Environment design](concepts/environment-design.md) - Using physical setup, visible storage, clothing uniforms, and sleep-environment tweaks to reduce reliance on memory and willpower.
- [Executive function](concepts/executive-function.md) - Initiation, prioritization, inhibition, task switching, time management, and ways to externalize those demands.
- [External memory](concepts/external-memory.md) - Offloading memory and decisions into notes, timers, fixed places, checklists, screens, or other people.
- [Forgetfulness countermeasures](concepts/forgetfulness-countermeasures.md) - Landing pads by the door, door checklists, transparent storage, instant notes, and clothing simplification.
- [Hyperfocus control](concepts/hyperfocus-control.md) - Setting exit conditions before starting: alarms, blockers, written stop points, and leaving the room.
- [Medication](concepts/medication.md) - Medication as a guideline topic, not individual advice: initiation, monitoring, adherence, and review should stay clinician-led.
- [Psychotic-like experiences](concepts/psychotic-like-experiences.md) - Research notes on subclinical psychotic-like experiences, rumination, negative affect, and ADHD symptoms.
- [Public support](concepts/public-support.md) - Service, school, work, and reasonable-adjustment support patterns, with jurisdiction limits.
- [Rumination](concepts/rumination.md) - Repetitive negative thinking as a bridge between attention, emotion regulation, and some comorbidity research.
- [Sleep](concepts/sleep.md) - Sleep-related environmental tweaks and hyperfocus controls in an ADHD context.
- [Sluggish cognitive tempo](concepts/sluggish-cognitive-tempo.md) - A research construct around daydreaming, mental fog, and mind-wandering that overlaps with but is not identical to ADHD.
- [Task initiation](concepts/task-initiation.md) - Reducing start friction with five-second notes, tiny Pomodoro blocks, body-first action, and shared accountability.
- [Time management](concepts/time-management.md) - Visual timers, analog clocks, estimate buffers, and time anchors for time blindness, lateness, and hyperfocus.
- [Waiting mode](concepts/waiting-mode.md) - A non-clinical term for losing usable time before an upcoming appointment or event, handled through structure, reminders, preparation, and time estimation.
- [Work routines](concepts/work-routines.md) - Low-energy ways to get through uninteresting work: fixed procedures, tiny units, automation, and templates.
- [Working memory](concepts/working-memory.md) - Moving information out of the head and into notes, places, checklists, and timers.

## Wiki structure

```text
.
├── README.md          # GitHub entry point
├── SCHEMA.md          # Wiki rules, tag taxonomy, and safety notes
├── index.md           # Internal wiki index
├── log.md             # Ingest and update log
├── raw/               # Source material; treat as immutable
│   ├── articles/
│   ├── papers/
│   ├── transcripts/
│   └── assets/
├── entities/          # Tools, organizations, people, programs, laws
├── concepts/          # Concepts, problems, tactics, patterns
├── comparisons/       # Side-by-side comparisons
└── queries/           # Saved research answers worth keeping
```

## How to read it

On GitHub, start with the Contents section above or open [index.md](index.md).

In Obsidian or another Markdown editor that supports wikilinks, links such as `[[external-memory]]` become a navigable knowledge graph. GitHub does not fully understand those links, so this README uses normal Markdown links for the main entry points.

## What belongs here

Good fits:

- Practical tactics, tools, and environment design for everyday life.
- Research, clinical guidelines, policy, and support systems related to ADHD and executive function.
- Reusable patterns extracted from lived experience.
- Accessibility practices for school, work, home, and public support.

Poor fits:

- Identifiable personal health information.
- Direct advice about diagnosis or medication.
- Unsourced medical claims.
- Drama, memes, stigma, or dunking with no reusable insight.

## Source policy

`raw/` stores source material. Ingested articles, posts, or notes should include the source URL, ingest date, and a hash of the captured body.

Curated pages separate the type of source from the claim:

- Research and guidelines should include jurisdiction, date, and source context where possible.
- Product pages are treated as descriptions of tools, not evidence that the tool works.
- X/Twitter posts and similar sources are treated as lived-experience notes, not medical evidence.

## Contributing

This is early and intentionally small. If you have something to add, open an issue or PR with the URL, note, paper, or tool.

For PRs:

1. Put source material under `raw/`.
2. Summarize important tools or concepts under `entities/` or `concepts/`.
3. Add new pages to [index.md](index.md) with a one-line summary.
4. Append the work to [log.md](log.md).
5. Be conservative around medical claims and personal information.

See [SCHEMA.md](SCHEMA.md) for the full operating rules.

## Automation

This repo also dogfoods Hermes Agent as a curator. A scheduled job can search public sources, such as practical `#ADHD` posts, and ingest only the ones that look reusable.

Automation is useful, but it is not a substitute for review. Medical, medication, diagnostic, or personal information should be checked by a human before it hardens into wiki knowledge.

## License

Not decided yet. Until a license is added, reuse rights are not explicit.

Copyright for source material belongs to the original authors. Summaries and excerpts in this repo are kept for source tracking, study, and curation.
