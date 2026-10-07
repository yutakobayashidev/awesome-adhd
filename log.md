# Wiki Log

> Chronological record of all wiki actions. Append-only.
> Format: `## [YYYY-MM-DD] action | subject`
> Actions: ingest, update, query, lint, create, archive, delete
> Rotate when this file exceeds 500 entries.

## [2026-07-22] create | Wiki initialized
- Domain: ADHD（注意欠如・多動症）に関する研究、支援策、生活・学習・仕事の工夫、当事者体験、制度、道具、併存課題、論争
- Structure created with SCHEMA.md, index.md, log.md
- Root: `/var/lib/hermes/awesome-adhd`

## [2026-07-22] ingest | X/Twitter Japanese ADHD practical tips batch
- Searches: Japanese `#ADHD`, `ADHD`, and `#ADHDのパワー系ソリューション` practical-tip queries via bird CLI.
- Created raw sources:
  - `raw/articles/tweet-2079789503863242941-forgetfulness-zero-checklist.md`
  - `raw/articles/tweet-2079767897938051576-five-second-todo.md`
  - `raw/articles/tweet-2079678863580500109-hyperfocus-end-first.md`
  - `raw/articles/tweet-2079499121107341499-two-tenths-work-rule.md`
  - `raw/articles/tweet-2079178248676860144-time-blindness-countermeasures.md`
  - `raw/articles/tweet-2079760615485448609-ziplock-bag-in-bag.md`
  - `raw/articles/tweet-2078379045746848120-pp-sheet-zip-bags.md`
  - `raw/articles/tweet-2070840382343291218-heavy-blanket-sleep-hack.md`
  - `raw/articles/tweet-2068357308481261936-clothing-uniform.md`
- Created concept pages:
  - `concepts/forgetfulness-countermeasures.md`
  - `concepts/external-memory.md`
  - `concepts/environment-design.md`
  - `concepts/time-management.md`
  - `concepts/task-initiation.md`
  - `concepts/hyperfocus-control.md`
  - `concepts/work-routines.md`
  - `concepts/working-memory.md`
  - `concepts/executive-function.md`
  - `concepts/sleep.md`
- Updated `index.md`.
- Note: X posts were treated as lived-experience/practical-tip sources, not medical evidence; concept pages use `confidence: low`.


## [2026-07-22] ingest | Tiimo Japanese homepage
- Source: https://www.tiimoapp.com/ja
- Created raw source:
  - `raw/articles/tiimo-homepage-2026.md`
- Created entity page:
  - `entities/tiimo.md`
- Updated concept pages:
  - `concepts/time-management.md`
  - `concepts/external-memory.md`
  - `concepts/task-initiation.md`
  - `concepts/work-routines.md`
  - `concepts/environment-design.md`
- Updated `index.md`.
- Note: Tiimo homepage is vendor-provided product text; treated as a tool description, not independent evidence of effectiveness.

## [2026-07-22] ingest | screenpipe homepage
- Source: https://screenpipe.com/
- Created raw source:
  - `raw/articles/screenpipe-homepage-2026.md`
- Created entity page:
  - `entities/screenpipe.md`
- Updated concept pages:
  - `concepts/external-memory.md`
  - `concepts/work-routines.md`
  - `concepts/executive-function.md`
- Updated navigation:
  - `index.md`
  - `README.md`
- Note: screenpipe homepage is vendor-provided product text; treated as a tool description. Continuous screen/audio capture has high privacy risk, so the wiki stores only product-level descriptions and reusable patterns.


## [2026-07-22] ingest | Research-watch machine-readable candidate curation
- Reviewed: 5 high-priority candidates from `.automation/research-watch/candidates.jsonl`.
- Created raw sources:
  - `raw/papers/tan-2026-adult-adhd-assistive-technologies-scoping-review.md`
  - `raw/papers/bergmann-2026-digital-cognitive-training-adult-adhd-rct.md`
  - `raw/papers/xu-2026-exercise-executive-functions-adult-adhd-meta-analysis.md`
  - `raw/papers/lalwani-2025-productivity-social-robot-college-students.md`
  - `raw/papers/zastudil-2025-neurodiversity-computing-education-review.md`
- Created concept pages:
  - `concepts/assistive-technology.md`
  - `concepts/exercise.md`
- Updated concept pages:
  - `concepts/executive-function.md`
  - `concepts/working-memory.md`
- Updated `index.md`.
- Note: research claims are source-bound and cautious; product/design sources are not treated as evidence of clinical effectiveness.

## [2026-07-22] ingest | i-have-adhd GitHub repository
- Source: https://github.com/ayghri/i-have-adhd
- Commit inspected: `ccce9e793a0d9fa008e9fb42199c39463f73a70a`
- Created raw source:
  - `raw/articles/i-have-adhd-github-2026.md`
- Created entity page:
  - `entities/i-have-adhd.md`
- Updated concept pages:
  - `concepts/assistive-technology.md`
  - `concepts/external-memory.md`
  - `concepts/task-initiation.md`
- Updated navigation:
  - `index.md`
  - `README.md`
- Note: treated as an ADHD-aware information-design/developer-tool source, not clinical evidence.

## [2026-07-22] ingest | X/Twitter ADHDパワー系ソリューション定期検索
- Searches: Japanese ADHD practical-tip queries across `Latest` and `Top`; deduplicated by tweet id.
- Created raw sources:
  - `raw/articles/tweet-1740351903421337650-routine-timer-morning.md`
  - `raw/articles/tweet-1740366768441602453-lock-check-key-cover.md`
  - `raw/articles/tweet-1739953040227287247-minimalism-less-stuff.md`
  - `raw/articles/tweet-1797396340231770380-geofence-auto-off.md`
  - `raw/articles/tweet-1740321810779103522-one-place-documents.md`
  - `raw/articles/tweet-2079859998449193147-hyperfocus-peak-time.md`
- Updated concept pages:
  - `concepts/time-management.md`
  - `concepts/forgetfulness-countermeasures.md`
  - `concepts/environment-design.md`
  - `concepts/external-memory.md`
  - `concepts/hyperfocus-control.md`
- Updated navigation:
  - `index.md` summaries for expanded existing concept pages.
- Note: X/Twitter posts are treated as lived-experience/practical tips only, not medical evidence.

## [2026-07-22] ingest | The Conversation waiting mode article
- Source: https://theconversation.com/do-you-lose-your-whole-day-to-one-appointment-waiting-mode-may-be-why-280608
- Created raw source:
  - `raw/articles/waiting-mode-the-conversation-2026.md`
- Created concept page:
  - `concepts/waiting-mode.md`
- Updated concept pages:
  - `concepts/time-management.md`
  - `concepts/task-initiation.md`
  - `concepts/external-memory.md`
  - `concepts/executive-function.md`
- Updated navigation:
  - `index.md`
  - `README.md`
- Note: treated as an explanatory article and lived-experience vocabulary, not a formal clinical term or medical guidance.

## [2026-07-22] ingest | ADHD guidelines and adult research batch
- Sources:
  - NICE NG87 recommendations: https://www.nice.org.uk/guidance/ng87/chapter/recommendations
  - Cochrane CBT review: https://pmc.ncbi.nlm.nih.gov/articles/PMC6494390/
  - NICE NG87 appendices PDF: https://www.nice.org.uk/guidance/ng87/evidence/appendices-16-pdf-4783651312
  - SCT / task-unrelated thought study: https://pmc.ncbi.nlm.nih.gov/articles/PMC7047632/
  - ADHD, rumination, negative affect, PLEs study: https://pmc.ncbi.nlm.nih.gov/articles/PMC11594572/
- Created raw sources:
  - `raw/articles/nice-ng87-recommendations-2026.md`
  - `raw/papers/lopez-2018-cbt-adults-adhd-cochrane.md`
  - `raw/papers/nice-ng87-appendices-2008.md`
  - `raw/papers/fredrick-2020-sct-adhd-task-unrelated-thought.md`
  - `raw/papers/gelner-2024-adhd-rumination-negative-affect-psychotic-like.md`
- Created entity/concept pages:
  - `entities/nice-ng87.md`
  - `concepts/diagnosis-and-management.md`
  - `concepts/cognitive-behavioural-therapy.md`
  - `concepts/sluggish-cognitive-tempo.md`
  - `concepts/rumination.md`
  - `concepts/psychotic-like-experiences.md`
  - `concepts/emotion-regulation.md`
  - `concepts/public-support.md`
  - `concepts/medication.md`
  - `concepts/comorbidity.md`
- Updated concept pages:
  - `concepts/executive-function.md`
  - `concepts/working-memory.md`
  - `concepts/task-initiation.md`
- Updated navigation:
  - `index.md`
  - `README.md`
- Note: medical and guideline sources are summarized as source-bound evidence. They are not diagnosis, treatment, medication, or prescribing advice.

## [2026-07-22] ingest | X/Twitter ADHDパワー系ソリューション定期検索 2
- Searches: Japanese ADHD practical-tip queries across `Latest` and `Top`; deduplicated by tweet id. Skipped generic empathy, discourse, medical claims without concrete workflow, and already-ingested tweet ids.
- Created raw sources:
  - `raw/articles/tweet-2039229335836696862-forgetfulness-company-locker-fixed-bag.md`
  - `raw/articles/tweet-2079936763024322772-body-doubling-phone-call.md`
  - `raw/articles/tweet-1992406682652336231-long-task-ai-25min-breakdown.md`
  - `raw/articles/tweet-2079844647199715690-hyperfocus-end-time-before-start.md`
  - `raw/articles/tweet-2079903068330574127-visible-time-arrival-readiness.md`
  - `raw/articles/tweet-2041992479973765361-sticky-note-game-task-hack.md`
- Updated concept pages:
  - `concepts/forgetfulness-countermeasures.md`
  - `concepts/time-management.md`
  - `concepts/task-initiation.md`
  - `concepts/external-memory.md`
  - `concepts/hyperfocus-control.md`
  - `concepts/work-routines.md`
- Updated navigation:
  - `index.md`
- Note: X/Twitter posts are treated as lived-experience/practical tips only, not medical evidence; existing concept pages remain `confidence: low`.

## [2026-07-23] ingest | X/Twitter ADHDパワー系ソリューション定期検索 3
- Searches: Japanese ADHD practical-tip queries across `Latest` and `Top`; deduplicated by tweet id. Skipped already-ingested tweets, generic empathy, vague motivation, memes, diagnosis discourse, and medical claims without concrete workflow.
- Created raw sources:
  - `raw/articles/tweet-2080063711180701705-seria-forgetfulness-checker-summer-tasks.md`
  - `raw/articles/tweet-2080065407822823866-night-decides-morning-trace-only.md`
  - `raw/articles/tweet-2080060334786887716-housework-automation-no-fold-laundry.md`
- Updated concept pages:
  - `concepts/time-management.md`
  - `concepts/task-initiation.md`
  - `concepts/forgetfulness-countermeasures.md`
  - `concepts/environment-design.md`
  - `concepts/external-memory.md`
- Updated navigation:
  - `index.md`
- Note: X/Twitter posts are treated as lived-experience/practical tips only, not medical evidence; existing concept pages remain `confidence: low`.

## [2026-07-23] ingest | Focusmate homepage
- Source: https://www.focusmate.com
- Created raw source:
  - `raw/articles/focusmate-homepage-2026.md`
- Created entity/concept pages:
  - `entities/focusmate.md`
  - `concepts/body-doubling.md`
- Updated concept pages:
  - `concepts/task-initiation.md`
  - `concepts/external-memory.md`
  - `concepts/work-routines.md`
  - `concepts/assistive-technology.md`
- Updated navigation:
  - `index.md`
  - `README.md`
- Note: treated as an official product description and virtual body-doubling pattern, not as medical evidence or ADHD treatment advice.

## [2026-07-23] ingest | Deep research report on AI and software for ADHD
- Source: Discord attachment `deep-research-report.md`
- Cached source file: `/var/lib/hermes/.hermes/cache/documents/doc_7130d5e36751_deep-research-report.md`
- Created raw source:
  - `raw/articles/deep-research-report-ai-software-adhd-2026.md`
- Created concept page:
  - `concepts/digital-adhd-support.md`
- Updated concept pages:
  - `concepts/assistive-technology.md`
  - `concepts/diagnosis-and-management.md`
  - `concepts/cognitive-behavioural-therapy.md`
  - `concepts/external-memory.md`
- Updated navigation:
  - `index.md`
  - `README.md`
- Note: treated as a secondary attached research report. Claims about digital therapeutics, diagnosis support, and AI tools should be verified against primary sources before being treated as high-confidence evidence.

## [2026-07-23] ingest | Curiosity, hyperfocus, prospective memory, and digital interruption research batch
- Sources: 13 DOI records provided by user, spanning curiosity/reward, hyperfocus in adult ADHD, ADHD distraction, prospective memory, task resumption, plan making, notification batching, email checking, social media dissociation, and smartphone non-use design.
- Created raw paper records:
  - `raw/papers/kang-2009-curiosity-reward-memory.md`
  - `raw/papers/kobayashi-2019-reward-information-value.md`
  - `raw/papers/hupfeld-2019-living-in-the-zone-hyperfocus-adhd.md`
  - `raw/papers/hupfeld-2024-adult-hyperfocus-questionnaire-validation.md`
  - `raw/papers/forster-2014-distraction-task-irrelevant-stimuli-adhd.md`
  - `raw/papers/fuermaier-2013-complex-prospective-memory-adult-adhd.md`
  - `raw/papers/jylkka-2023-everyday-prospective-memory-adult-adhd.md`
  - `raw/papers/ratwani-2008-spatial-memory-task-resumption.md`
  - `raw/papers/masicampo-2011-plan-making-unfulfilled-goals.md`
  - `raw/papers/baughan-2022-design-influences-dissociation-social-media.md`
  - `raw/papers/fitz-2019-batching-smartphone-notifications-wellbeing.md`
  - `raw/papers/kushlev-2015-checking-email-less-stress.md`
  - `raw/papers/hiniker-2016-mytime-smartphone-non-use.md`
- Created concept pages:
  - `concepts/curiosity-reward-memory.md`
  - `concepts/attention-control.md`
  - `concepts/prospective-memory.md`
  - `concepts/task-resumption.md`
  - `concepts/digital-interruptions.md`
- Updated concept pages:
  - `concepts/hyperfocus-control.md`
  - `concepts/working-memory.md`
  - `concepts/executive-function.md`
  - `concepts/time-management.md`
  - `concepts/task-initiation.md`
- Updated navigation:
  - `index.md`
  - `README.md`
- Note: several sources are adjacent cognitive/HCI evidence rather than ADHD-specific clinical evidence; they are used for design implications, not treatment advice.

## [2026-07-23] ingest | FOMO and Admin Night keyword research
- Corrected target from `/var/lib/hermes/wiki` to this awesome-adhd wiki root.
- Added FoMO research raw sources:
  - `raw/papers/przybylski-2013-fomo-scale.md`
  - `raw/papers/elhai-2021-fomo-overview.md`
  - `raw/papers/fitz-2019-notification-batching-fomo.md`
  - `raw/papers/montag-2023-fomo-cognitive-failure.md`
  - `raw/papers/akbari-2021-fomo-internet-use-meta-analysis.md`
  - `raw/papers/groenestein-2024-fomo-social-media-longitudinal.md`
- Added Admin Night / body doubling raw sources:
  - `raw/articles/x-tmiyatake-admin-night-2026.md`
  - `raw/articles/body-doubling-life-admin-sources-2026.md`
- Created concept page: `concepts/fear-of-missing-out.md`
- Updated concept page: `concepts/body-doubling.md`
- Created query page: `queries/toymaker-openbrief-adhd-design-notes.md`
- Updated `index.md`.
- Note: the attached X video was not transcribed; the Admin Night ingest used bird metadata, post text, and keyword-based surrounding sources.

## [2026-07-23] ingest | Misfiled ADHD/OpenBrief wiki migration audit
- Audited untracked ADHD/OpenBrief/Toymaker candidates in `/var/lib/hermes/wiki` and migrated remaining relevant material to `/var/lib/hermes/awesome-adhd`.
- Added raw sources:
  - `raw/papers/arxiv-cognitive-personal-informatics-chi26-2026.md`
  - `raw/papers/arxiv-multilingual-text-to-pictogram-reading-rehabilitation-2026.md`
  - `raw/papers/arxiv-neurodiversity-demographics-education-research-2026.md`
  - `raw/papers/pubmed-adhd-digital-text-comprehension-self-monitoring-2019.md`
  - `raw/papers/pubmed-adhd-ema-daily-life-adolescents-2026.md`
  - `raw/articles/github-open-brief-project-docs-2026.md`
  - `raw/articles/i-have-adhd-agent-output-skill-2026.md`
  - `raw/articles/tiimo-neurodivergent-planner-2026.md`
- Created concept page: `concepts/cognitive-personal-informatics.md`.
- Updated concept/entity/query pages: `concepts/assistive-technology.md`, `concepts/digital-adhd-support.md`, `entities/i-have-adhd.md`, `entities/tiimo.md`, `queries/toymaker-openbrief-adhd-design-notes.md`.
- Updated `index.md`.
- Left non-ADHD/general LLM-infrastructure material in `/var/lib/hermes/wiki`.
- Created audit query page: `queries/misfiled-adhd-openbrief-migration-audit-2026.md`.
- Updated `index.md` total pages to 38 after audit page creation.

## [2026-07-23] ingest | X/Twitter ADHDパワー系ソリューション定期検索 4
- Searches: Japanese ADHD practical-tip queries across `Latest` and `Top`; deduplicated by tweet id. Skipped already-ingested tweets, generic empathy, diagnosis/stigma discourse, vague motivation, unsafe medical-style hacks, and posts without concrete workflow.
- Created raw sources:
  - `raw/articles/tweet-2080187975636509069-one-note-single-window-distraction-reduction.md`
  - `raw/articles/tweet-2080186209872351354-impulse-buying-notification-card-friction.md`
  - `raw/articles/tweet-2080159574649401476-careless-mistake-situation-note.md`
- Created concept pages:
  - `concepts/impulsivity-countermeasures.md`
  - `concepts/careless-mistake-countermeasures.md`
- Updated concept pages:
  - `concepts/attention-control.md`
  - `concepts/environment-design.md`
  - `concepts/external-memory.md`
  - `concepts/working-memory.md`
- Updated navigation:
  - `index.md`
- Note: X/Twitter posts are treated as lived-experience/practical tips only, not medical evidence; new tweet-based pages use `confidence: low`.


## [2026-07-23] ingest | Research-watch curated adult/digital ADHD support batch
- Reviewed and accepted: 5 machine-readable candidates from `.automation/research-watch/candidates.jsonl`.
- Created raw sources:
  - `raw/papers/akca-2026-neuroinclusive-emotion-regulation-uxr.md`
  - `raw/papers/arakawa-2026-calmreminder-parental-engagement.md`
  - `raw/papers/gibbs-2026-female-adhd-academia-work.md`
  - `raw/papers/kasatskii-2023-perceptual-load-ide-adhd.md`
  - `raw/papers/nordby-2024-blended-emotion-dysregulation-adult-adhd.md`
- Updated concept pages:
  - `concepts/emotion-regulation.md`
  - `concepts/digital-adhd-support.md`
  - `concepts/assistive-technology.md`
  - `concepts/attention-control.md`
  - `concepts/work-routines.md`
  - `concepts/public-support.md`
  - `concepts/cognitive-behavioural-therapy.md`
- Updated automation state: `.automation/research-watch/curation-state.json`.
- Note: sources were treated cautiously; HCI/design studies are not clinical efficacy evidence, and medication/diagnosis advice was not added.

## [2026-07-23] ingest | Neurodivergent async communication, meetings, AI support, and context fit
- Created concept: `concepts/async-meetings-context-fit.md`.
- Created query: `queries/toymaker-neurodivergent-async-meetings-ai-2026.md`.
- Created raw sources:
  - `raw/papers/das-2021-accessible-remote-work-neurodivergent.md`
  - `raw/papers/liebel-2023-software-engineers-adhd-meetings.md`
  - `raw/papers/jameson-2026-sustainable-work-adhd.md`
  - `raw/papers/oconnor-2025-autistic-asynchronous-focus-group.md`
  - `raw/papers/deshmukh-2025-neurodivergent-aware-productivity-ai.md`
  - `raw/articles/welcomebrain-2026-neuroinclusive-meetings.md`
- Updated: `concepts/digital-adhd-support.md`, `concepts/work-routines.md`, `concepts/task-resumption.md`, `index.md`.
- Synthesis: async communication helps processing time and written memory; meetings can still help body-doubling, repair, and alignment; the key design target is context fit rather than async-vs-sync absolutism.

## [2026-07-23] query | OpenBrief vs Karpathy LLM Wiki
- Created raw source: `raw/articles/karpathy-llm-wiki-pattern-2026.md`.
- Created query: `queries/openbrief-vs-karpathy-llm-wiki-2026.md`.
- Updated: `queries/toymaker-openbrief-adhd-design-notes.md`, `index.md`, `log.md`.
- Synthesis: LLM Wiki is a persistent knowledge compiler; OpenBrief is an attention-transition product that finite-izes exploration, protects obligations, and returns the user to prior context. OpenBrief can feed an LLM Wiki, but should not automatically turn every capture into a task or wiki page.

## [2026-07-23] ingest | X/Twitter ADHDパワー系ソリューション定期検索 5
- Searches: 4 queries across `Latest` and `Top` products (Japanese practical-tip keywords). Deduplicated by tweet ID. Skipped already-ingested tweets, generic empathy, diagnosis/stigma discourse, vague motivation, and posts without concrete workflow.
- Created raw sources:
  - `raw/articles/tweet-2079957567120564475-adhd-burnout-energy-management.md`
  - `raw/articles/tweet-2080292256523936015-adhd-self-experimentation-method.md`
  - `raw/articles/tweet-2001281922069340279-41-adhd-parenting-tactics.md`
- Created concept pages:
  - `concepts/energy-management.md`
  - `concepts/self-experimentation.md`
  - `concepts/parenting.md`
- Updated navigation:
  - `index.md` (total pages: 43 → 46)
- Note: X/Twitter posts are treated as lived-experience/practical tips only, not medical evidence; new tweet-based pages use `confidence: low`.

## [2026-07-23] ingest | Deep research report: Screenpipe, Rewind, and ADHD-centered passive-memory design
- Created raw source: `raw/articles/deep-research-screenpipe-rewind-adhd-design-2026.md`.
- Created concept: `concepts/passive-memory-assistants-adhd.md`.
- Created query: `queries/toymaker-passive-memory-adhd-design-2026.md`.
- Updated: `concepts/assistive-technology.md`, `concepts/external-memory.md`, `concepts/task-resumption.md`, `entities/screenpipe.md`, `index.md`, `log.md`.
- Synthesis: passive memory tools (Screenpipe, Rewind/Limitless, Recall) are promising ADHD scaffolding but must prioritize resume, time anchoring, externalized next-steps, sensory safety, and privacy-by-design over raw capture breadth. Screenpipe is the best current reference architecture; Rewind's legacy local-first model is informative but it is sunsetting into a cloud-mediated Limitless platform.

## [2026-07-27] ingest | X/Twitter ADHDパワー系ソリューション定期検索 7
- Searches: 4 queries across `Latest` and `Top` products (Japanese practical-tip keywords). Deduplicated by tweet ID. Skipped already-ingested tweets, generic empathy, diagnosis/stigma discourse, vague motivation, and medical claims without concrete workflow.
- Created raw sources:
  - `raw/articles/tweet-2080841443212665173-receipt-print-child-task-management.md`
  - `raw/articles/tweet-1995472174837068093-sleep-in-pe-uniform-morning-routine.md`
  - `raw/articles/tweet-2081356392972038227-interruption-tally-three-workplace-tactics.md`
  - `raw/articles/tweet-2080984407700111391-subtraction-boredom-true-interests.md`
  - `raw/articles/tweet-2081220465864187989-ai-automation-iterate-fix-systems.md`
  - `raw/articles/tweet-2081363947450712183-boring-to-interesting-conversion-tactic.md`
- Updated concept pages:
  - `concepts/parenting.md` (receipt task management, sleep in PE uniform)
  - `concepts/task-initiation.md` (boredom→interest conversion, subtraction method, PE uniform)
  - `concepts/work-routines.md` (interruption tally + 3 workplace tactics, AI automation iterative fixing)
  - `concepts/attention-control.md` (interruption quantification, boredom→interest)
  - `concepts/self-experimentation.md` (subtraction method for discovering true interests)
  - `concepts/environment-design.md` (paper task management, night-before prep, systems breaking & fixing)
- Updated navigation:
  - `index.md` (last updated date)
- Note: X/Twitter posts are treated as lived-experience/practical tips only, not medical evidence; existing concept pages remain `confidence: low`.

## [2026-07-24] ingest | X/Twitter ADHDパワー系ソリューション定期検索 6
- Searches: 4 queries across `Latest` and `Top` products (Japanese practical-tip keywords focused on パワー系/物理/仕組み化/タイマー etc). Deduplicated by tweet ID. Skipped 37 already-ingested tweets, generic empathy, diagnosis discourse without tactics, and English-only content.
- Created raw sources:
  - `raw/articles/tweet-2080128266187190604-deadline-declaration-tactic.md`
  - `raw/articles/tweet-2057461664791077048-relationship-shelf-life-countermeasures.md`
  - `raw/articles/tweet-2080308025915785565-overdeposit-auto-payment.md`
  - `raw/articles/tweet-1970853461433753680-white-black-thinking-countermeasures.md`
  - `raw/articles/tweet-1971854125399978149-asd-adhd-structuring-comparison.md`
  - `raw/articles/tweet-2003712226386227420-adhd-happiness-tier.md`
  - `raw/articles/tweet-2008757004173799597-brain-fatigue-physical-countermeasures.md`
- Created concept pages:
  - `concepts/relationships.md`
  - `concepts/all-or-nothing-thinking.md`
- Created comparison page:
  - `comparisons/asd-adhd-structuring.md`
- Updated concept pages:
  - `concepts/time-management.md` (deadline-declaration tactic)
  - `concepts/forgetfulness-countermeasures.md` (financial over-deposit tactic)
  - `concepts/energy-management.md` (brain fatigue physical countermeasures section)
  - `concepts/emotion-regulation.md` (white-black thinking link)
- Updated navigation:
  - `index.md` (total pages: 48 → 51)
- Note: X/Twitter posts are treated as lived-experience/practical tips only, not medical evidence. Happiness-tier tweet was ingested as raw source for cross-referencing but did not generate a standalone page (techniques already covered across existing concepts).

## [2026-07-27] ingest | Research-watch curated candidate curation (batch 3)

- Reviewed 5 unprocessed candidates from `.automation/research-watch/candidates.jsonl`.
- Accepted 3 for raw + page update (score 3) and 2 for raw-only (score 2).

### Accepted (score 3): raw + wiki page update
- `pubmed:38178649` — Wilens et al. (2024), "Treating Executive Function in Youth With ADHD: A Review of Pharmacological and Non-Pharmacological Interventions" (systematic review, 136 RCTs, 11,443 participants)
  - Raw source: `raw/papers/wilens-2024-treating-executive-function-youth-adhd-review.md`
  - Updated: `concepts/executive-function.md`, `concepts/medication.md`, `concepts/digital-adhd-support.md`, `concepts/cognitive-behavioural-therapy.md`
- `pubmed:42500318` — Popit et al. (2026), "Prevalence of pharmacologically treated ADHD: systematic review and meta-analysis" (systematic review + meta-analysis, 13 studies)
  - Raw source: `raw/papers/popit-2026-prevalence-pharmacologically-treated-adhd-meta-analysis.md`
  - Updated: `concepts/medication.md`, `concepts/diagnosis-and-management.md`
- `pubmed:42159952` — Iwanami et al. (2026), "Safety and Effectiveness of Guanfacine Hydrochloride Extended-Release in Adult Patients with ADHD in Japan: A Post-Marketing Surveillance Study" (PMS, 961 patients, 155 Japanese sites)
  - Raw source: `raw/papers/iwanami-2026-guanfacine-adult-adhd-japan-pms.md`
  - Updated: `concepts/medication.md`

### Accepted (score 2): raw-only
- `pubmed:42433964` — Fuengfoo et al. (2026), "Parent training for preschool ADHD risk" (RCT, Thailand)
  - Raw source: `raw/papers/fuengfoo-2026-parent-training-preschool-adhd-thailand-rct.md`
- `pubmed:41237171` — Winter & O'Neill (2026), "Screen time impact on ADHD symptoms" (narrative review, children/adolescents)
  - Raw source: `raw/papers/winter-2026-screen-time-adhd-children-adolescents-narrative-review.md`

- Updated: `index.md` (date bump), `log.md`, `.automation/research-watch/curation-state.json`.
- Note: all drug/medication references are source-bound summaries, not prescribing or treatment advice. Wilens review is youth-focused; adult generalisation should be cautious. Iwanami PMS is industry-funded post-marketing surveillance, not an RCT. Japanese context added to medication page.

## [2026-07-27] ingest | X/Twitter ADHDパワー系ソリューション定期検索 8
- Searches: 4 queries across `Latest` and `Top` products (Japanese practical-tip keywords). Deduplicated by tweet ID. Skipped already-ingested tweets, generic empathy, diagnosis/stigma discourse, vague motivation, medical claims without concrete workflow, and non-actionable content.
- Created raw sources:
  - `raw/articles/tweet-2081682049648439480-willpower-to-systems-three-tactics.md`
  - `raw/articles/tweet-2081688580913545612-time-visualization-predict-record.md`
  - `raw/articles/tweet-2081695224825626992-mental-accounting-auto-save.md`
  - `raw/articles/tweet-2081575303542104352-short-time-disability-employment.md`
  - `raw/articles/tweet-2081700413070512286-external-memory-justification.md`
  - `raw/articles/tweet-2081670676457591068-five-forgetfulness-systems.md`
  - `raw/articles/tweet-2081302504999207021-self-commentary-task-initiation.md`
- Updated concept pages:
  - `concepts/impulsivity-countermeasures.md` (24hr rule, credit limit, auto-save)
  - `concepts/time-management.md` (predict-record time estimation training)
  - `concepts/work-routines.md` (short-time disability employment, forced reset)
  - `concepts/task-initiation.md` (self-commentary technique)
  - `concepts/external-memory.md` (外付けメモリ framing, 5-point system)
  - `concepts/forgetfulness-countermeasures.md` (定時確認ルーティン)
  - `concepts/hyperfocus-control.md` (forced reset technique)
  - `concepts/environment-design.md` (financial environment design)
  - `concepts/working-memory.md` (外付けメモリ framing)
- Updated navigation:
  - `index.md` date bump (total pages unchanged at 51)
- Note: X/Twitter posts are treated as lived-experience/practical tips only, not medical evidence; existing concept pages remain `confidence: low`.

## [2026-07-27] ingest | X/Twitter ADHDパワー系ソリューション定期検索 9
- Searches: 4 queries across `Latest` and `Top` products (Japanese practical-tip keywords). Deduplicated by tweet ID. Skipped already-ingested tweets, generic empathy, diagnosis/stigma discourse, vague motivation, medical claims without concrete workflow, and non-actionable content.
- Created raw sources:
  - `raw/articles/tweet-2081752543818821682-eight-adhd-tricks.md` (8 tactics batch: 5秒ルール, 2分だけやる, ボディダブリング, 見える化作戦, 3段階アラーム, 靴を履く, 完璧禁止, スマホ隔離)
  - `raw/articles/tweet-2081731399271461102-gps-schedule-forced-systems.md` (GPS on keys/wallet + hourly schedule checks)
  - `raw/articles/tweet-2081718500041900538-hyperfocus-dont-stop-timer.md` (don't stop hyperfocus when flowing)
  - `raw/articles/tweet-2081726188532477959-low-gi-diet-brain-fog.md` (low-GI diet + reduced portions for post-meal brain fog)
  - `raw/articles/tweet-2081760716277899506-shopping-impulse-investment.md` (redirect shopping impulse to investment trusts)
  - `raw/articles/tweet-2081740061046088085-otonotone-brown-noise-app.md` (おとのもり brown noise app for ADHD)
  - `raw/articles/tweet-2081662616582361210-dopamine-addiction-systems.md` (building systems to quit addictive dopamine behaviors)
- Updated concept pages:
  - `concepts/hyperfocus-control.md` (don't stop timer when hyperfocus is flowing)
  - `concepts/forgetfulness-countermeasures.md` (GPS tag on keys/wallet)
  - `concepts/time-management.md` (hourly schedule check routine)
  - `concepts/energy-management.md` (low-GI diet for brain fog)
  - `concepts/impulsivity-countermeasures.md` (shopping→investment redirection, addiction systems)
  - `concepts/task-initiation.md` (shoes indoors for work mode switch)
- Updated navigation:
  - `index.md` date bump (total pages unchanged at 51)
- Note: X/Twitter posts are treated as lived-experience/practical tips only, not medical evidence; existing concept pages remain `confidence: low`.

## [2026-07-28] ingest | X/Twitter ADHDパワー系ソリューション定期検索 10
- Searches: 4 queries across `Latest` and `Top` products (Japanese practical-tip keywords). Deduplicated by tweet ID. Skipped already-ingested tweets, generic empathy, diagnosis discourse without tactics, English-only content, and vague motivation posts.
- Created raw sources:
  - `raw/articles/tweet-2081895802356851193-hyperfocus-punctuate-water.md` (45分タイマー＋水一口で過集中を「区切る」戦略)
  - `raw/articles/tweet-2081891109413007381-ai-task-coach-prompt.md` (AI専属タスク消化コーチプロンプト全文＋設計思想＋5原則)
  - `raw/articles/tweet-2081875013561708615-rsd-seven-symptoms-five-countermeasures.md` (RSD 7現象＋5対策)
  - `raw/articles/tweet-2081888402581176448-self-distrust-procrastination-alert.md` (「自分はやらない人間」と信頼して後回しセンサーを育てる)
- Updated concept pages:
  - `concepts/hyperfocus-control.md` (「区切る」戦略追記)
  - `concepts/task-initiation.md` (AI専属コーチで毎日報告＋褒めで着手回す)
  - `concepts/body-doubling.md` (AIを24時間のボディダブルとして使う新節)
  - `concepts/emotion-regulation.md` (RSD対策5選の新節)
  - `concepts/relationships.md` (RSD対策セクションへのクロスリンク追記)
  - `concepts/work-routines.md` (後回しセンサー戦略＋AIコーチ毎日ルーティン)
- Updated navigation:
  - `index.md` date bump (total pages unchanged at 51)
- Note: X/Twitter posts are treated as lived-experience/practical tips only, not medical evidence; existing concept pages remain `confidence: low`. The AI coach prompt (tweet 2081891109413007381) is the richest single find this run — a complete, copy-paste-able Japanese prompt for task accountability + pattern discovery.

## [2026-07-28] ingest | X/Twitter ADHDパワー系ソリューション定期検索 11
- Searches: 4 queries across `Latest` and `Top` products (Japanese practical-tip keywords). Deduplicated by tweet ID across products. Skipped already-ingested tweets, generic empathy, diagnosis discourse, personal arguments, English-only, self-promotion without actionable content, and vague motivation.
- Created raw sources:
  - `raw/articles/tweet-2081967583767802139-ten-second-record.md` (思いついた瞬間に10秒でスマホに記録、「後でまとめて」をしない)
  - `raw/articles/tweet-2081966844601344356-post-it-search-drift.md` (検索前に「調べること」を付箋に書いてPCに貼る脱線防止)
  - `raw/articles/tweet-2081992548311298078-physical-money-controls.md` (医師による遅延報酬の割引解説＋口座分離・カード不携帯・使う日事前決定)
  - `raw/articles/tweet-2081905102391300471-credit-limit-auto-transfer.md` (自己肯定感低下→大盤振る舞いの心理メカニズム＋クレカ上限・先取り振替)
  - `raw/articles/tweet-2081991150618177582-rsd-mistake-defense-three-tactics.md` (RSDミス指摘時悪循環＋その場で結論出さない/事実・解釈・対策分離/謝罪→仕組み化の3対策)
  - `raw/articles/tweet-2081938632881955135-taxi-cost-benefit-reframe.md` (タクシー1200円vs有給8時間損失、目先の節約と未来の損失の比較視点)
- Updated concept pages:
  - `concepts/external-memory.md` (10秒以内の即時記録)
  - `concepts/hyperfocus-control.md` (検索脱線防止の物理付箋)
  - `concepts/impulsivity-countermeasures.md` (物理的金銭管理3策＋大盤振る舞い心理メカニズム＋コスト比較リフレーミング)
  - `concepts/emotion-regulation.md` (ミス指摘時防衛反応への3つの対策)
  - `concepts/energy-management.md` (目先の節約と未来の損失の数字比較)
- Updated navigation: `index.md` date unchanged (already 2026-07-28 from earlier run); total pages unchanged at 51.
- Note: X/Twitter posts are treated as lived-experience/practical tips only, not medical evidence. The RSD mistake-defense 3 tactics (tweet 2081991150618177582) is the richest find this run — a clear, structured framework connecting RSD, cognitive dissonance, and system-building.

## [2026-07-28] ingest | X/Twitter ADHDパワー系ソリューション定期検索 12
- Searches: 4 queries across `Latest` and `Top` products (Japanese practical-tip keywords). Deduplicated by tweet ID across products. Skipped already-ingested tweets, generic empathy, diagnosis discourse, memes, and vague motivation.
- Created raw sources:
  - `raw/articles/tweet-2082058495449579544-subscription-model-tidying.md` (片付けの会費モデル：「戻すのが1歩以下」の場所へ住所を移す)
  - `raw/articles/tweet-2082068756692685166-calendar-visualization-keep-present.md` (旅行計画忘れへの仕組み：カレンダー視覚化、LINE/紙に残す、「今も進行中の話」として再登場、期待値調整)
  - `raw/articles/tweet-2082018626513817874-five-mistake-prevention-systems.md` (ミス防止5つの仕組み：即メモ、チェックリスト化、ダブルチェック、作業細分化、急がない)
  - `raw/articles/tweet-2082035838532157764-night-prep-by-neurotype-morning-panic.md` (特性別・前夜準備：ASD/ADHD/AuDHDの3類型で朝のパニック防止)
  - `raw/articles/tweet-2082047175236759863-overspending-social-three-countermeasures.md` (奢りすぎ防止3策：月額上限、現金減らす、割り勘練習)
- Updated concept pages:
  - `concepts/environment-design.md` (会費モデルの片付け＋特性別前夜準備)
  - `concepts/careless-mistake-countermeasures.md` (5つのミス防止仕組みの新節)
  - `concepts/external-memory.md` (会話の外部記憶化＋「今も進行中」フレーミング)
  - `concepts/relationships.md` (パートナーとのコミュニケーション設計の新節)
  - `concepts/impulsivity-countermeasures.md` (人に奢る衝動への物理的対策)
  - `concepts/sleep.md` (特性別・前夜準備で朝パニック防止の新節)
- Updated navigation: `index.md` date already 2026-07-28 from earlier run; total pages unchanged at 51.
- Note: X/Twitter posts are treated as lived-experience/practical tips only, not medical evidence. The 会費モデル (tweet 2082058495449579544) is the richest single concept this run — a genuinely novel metaphor that reframes tidying as subscription cost rather than moral failing.

## [2026-07-28] ingest | X/Twitter ADHDパワー系ソリューション定期検索 13
- Searches: 4 queries across `Latest` and `Top` products. Deduplicated by tweet ID across products. Skipped already-ingested tweets, generic diagnosis discourse, stigma/personal attacks, vague promotion, and medical claims without practical tactics.
- Created raw sources:
  - `raw/articles/tweet-2082131881970315336-infinite-socks.md` (同型靴下を大量に揃え、ペア合わせ・片方紛失問題を消す)
  - `raw/articles/tweet-2082114468558090488-actual-task-duration-log.md` (反復タスクの実所要時間を測って、体感ではなく記録で見積もる)
  - `raw/articles/tweet-2082033754877661336-smartphone-friction-notification-off.md` (スマホを触りにくくし、電話以外通知を切る)
  - `raw/articles/tweet-1276000118047531008-housework-automation-appliances.md` (掃除ロボット・食洗機・ドラム式洗濯乾燥機へ家事工程を移す)
- Updated concept pages:
  - `concepts/forgetfulness-countermeasures.md` (無限靴下)
  - `concepts/environment-design.md` (無限靴下＋家事自動化家電)
  - `concepts/time-management.md` (反復タスクの所要時間ログ)
  - `concepts/digital-interruptions.md` (スマホ摩擦＋通知遮断)
- Updated navigation: `index.md` total pages unchanged at 51.
- Note: X/Twitter posts are treated as lived-experience/practical tips only, not medical evidence.

## [2026-07-30] ingest | Research-watch curated candidate curation (batch 4)

- Reviewed 5 unprocessed candidates from `.automation/research-watch/candidates.jsonl`.
- Accepted 5 for raw + existing page update (score 3); created no new wiki pages.
- Created raw sources:
  - `raw/papers/canu-2026-cbt-group-telehealth-college-adhd.md`
  - `raw/papers/solanto-2026-executive-self-management-college-adhd.md`
  - `raw/papers/kennedy-2026-mhealth-emi-adhd-high-risk-alcohol.md`
  - `raw/papers/yitzhak-2025-emotional-pendulum-adhd-ema.md`
  - `raw/papers/ben-dor-cohen-2024-emotional-dysregulation-coping-adult-adhd.md`
- Updated concept pages:
  - `concepts/cognitive-behavioural-therapy.md`
  - `concepts/executive-function.md`
  - `concepts/emotion-regulation.md`
  - `concepts/digital-adhd-support.md`
- Updated navigation/state: `index.md`, `.automation/research-watch/curation-state.json`.
- Maintenance: fixed pre-existing broken wikilink in `entities/genio-notes.md` (`[[school]]` → plain text placeholder).
- Note: telehealth/group CBT and EMA/EMI sources are summarized cautiously. Open-label and development studies are not treated as proof of clinical effectiveness; no personal medical advice was added.

## [2026-07-31] ingest | X/Twitter ADHDパワー系ソリューション定期検索 14
- Searches: 4 queries across `Latest` and `Top` products (Japanese practical-tip keywords). Deduplicated by tweet ID across products. Skipped already-ingested tweets, generic empathy, diagnosis discourse, memes, vague motivation, and medical claims without concrete tactics.
- Created raw sources:
  - `raw/articles/tweet-2082983162096029890-time-attack-gamification.md` (ストップウォッチ＋タイマーで時間を見える化しタイムアタック化・ゲーム感覚で取り組む)
  - `raw/articles/tweet-2082976727215857993-accept-forgetfulness-bring-spares.md` (忘れ物をしないのは無理→忘れてもいいものを複数持っていく受容戦略)
  - `raw/articles/tweet-2082923063763751422-multi-stage-reminder-cascade.md` (Googleカレンダーで3日前〜15分前の多段リマインダーを仕込む)
  - `raw/articles/tweet-2082444170292257176-five-decision-making-systems.md` (決断力5つの仕組み：選択肢3つ以下・制限時間・70点OK・小さい決断練習・決断日記)
  - `raw/articles/tweet-2082977786084683856-morning-cafe-environment-switch.md` (自宅作業不可→朝マック等外出で環境強制切り替え)
- Updated concept pages:
  - `concepts/time-management.md` (タイムアタック化、多段リマインダーカスケード)
  - `concepts/forgetfulness-countermeasures.md` (忘れる前提の複数持ち戦略)
  - `concepts/executive-function.md` (決断力5つの仕組み)
  - `concepts/task-initiation.md` (カフェ外出による環境強制切り替え)
- Updated navigation: `index.md` date bump (total pages unchanged at 51)
- Note: X/Twitter posts are treated as lived-experience/practical tips only, not medical evidence; existing concept pages remain `confidence: low`. The decision-making 5 systems (tweet 2082444170292257176) is the richest find this run — a structured, copyable framework for a domain (decision paralysis) that was previously underrepresented in the wiki.

## [2026-07-31] ingest | X/Twitter ADHDパワー系ソリューション定期検索 15

- Searches: 4 queries across `Latest` and `Top` products (Japanese practical-tip keywords). Deduplicated by tweet ID across products. Evaluated ~80 tweets; skipped already-ingested, generic empathy, diagnosis discourse, memes, vague motivation, coaching promos, and medical claims without concrete tactics. Ingested 10 new tweets.
- Created raw sources:
  - `raw/articles/tweet-2082793578904846370-no-todo-list-immediate-action.md` (Todoリストを使わずその場で即やり切る脳筋スタイル — 優先付け・見積もり苦手を回避)
  - `raw/articles/tweet-2083030892310942096-timelapse-self-recording.md` (タイムラプス自己撮影でボディダブリング・スマホ封印・報酬効果)
  - `raw/articles/tweet-2083039955907985690-money-management-five-tactics.md` (固定費分離・決済方法絞り・週単位予算・翌日判断・支払い自動化の5点)
  - `raw/articles/tweet-2083028275752783965-relationship-reconnect-one-message.md` (「最近どう？」1通LINEで疎遠関係へ戻る力)
  - `raw/articles/tweet-2082658478016053276-phone-call-body-doubling.md` (通話開始だけで魔法のように動けるボディダブリング — 12Kいいね)
  - `raw/articles/tweet-2083021519412961526-reset-impulse-countermeasures.md` (リセット衝動への3対策: 保留・実況・相談 + 小さなリセット)
  - `raw/articles/tweet-2082377839211389129-asset-building-dopamine-hijack.md` (購買衝動を資産形成欲で打ち消すドーパミン・リダイレクト)
  - `raw/articles/tweet-1983393290721603589-calendar-organizer-name.md` (カレンダーに予定名ではなく責任者名を書く)
  - `raw/articles/tweet-2002943114731003956-hyperfocus-entry-eight-tactics.md` (過集中スイッチを入れる8つの準備動作)
  - `raw/articles/tweet-1740680164168913193-smart-lock-forgetfulness.md` (スマートロックで鍵の携帯記憶ごと不要にする — 41Kいいねの古典)
- Updated concept pages:
  - `concepts/task-initiation.md` (Todoリスト廃止即実行、タイムラプス撮影、通話ボディダブリング、過集中8準備動作)
  - `concepts/impulsivity-countermeasures.md` (お金管理5工夫、資産形成欲で衝動上書き)
  - `concepts/relationships.md` (疎遠関係へ戻る力 — 1通LINE + 完璧主義回避)
  - `concepts/emotion-regulation.md` (リセット衝動対策 — 保留・実況・相談・小さなリセット)
  - `concepts/external-memory.md` (カレンダー責任者名)
  - `concepts/hyperfocus-control.md` (過集中スイッチ8準備動作)
  - `concepts/forgetfulness-countermeasures.md` (スマートロック)
- Updated navigation: `index.md` (date already current; total pages unchanged at 51)
- Note: X/Twitter posts are treated as lived-experience/practical tips only, not medical evidence. The Todoリスト廃止 (tweet 2082793578904846370) and 通話ボディダブリング (tweet 2082658478016053276, 12K likes) are the highest-signal finds this run — both are counterintuitive, immediately actionable, and backed by strong engagement. The リセット衝動対策 (tweet 2083021519412961526) fills a previously empty niche in the emotion-regulation page.

## [2026-08-08] ingest | X/Twitter ADHDパワー系ソリューション定期検索 16
- Searches: 4 queries across `Latest` and `Top` products. Deduplicated 75 unique tweet IDs; skipped 5 already-ingested tweets plus generic empathy, memes, diagnosis discourse, stigma/personal attacks, vague motivation, and medical/supplement claims without sources.
- Created raw sources:
  - `raw/articles/tweet-2085857313966166048-three-second-external-memory-six-tactics.md` (3秒メモ・店別リスト・LINE通知時刻・洗濯終了タイマー・視界保持・今日3件表示)
  - `raw/articles/tweet-2085741805275099550-hotcook-cooking-forgetfulness.md` (鍋忘れ対策として刻みタイマー＋自動調理器へ火の管理を移す)
  - `raw/articles/tweet-2085924875181363581-no-folder-first-drop-one-item.md` (整理準備で満足しないため、フォルダ作成より先に1個入れる)
  - `raw/articles/tweet-2085933607072485405-single-task-notification-off.md` (1タスク固定＋スマホ通知一時全OFF)
  - `raw/articles/tweet-2085680350315827567-himmel-role-model-imitation.md` (人物模倣で着手する「ヒンメル戦法」)
  - `raw/articles/tweet-2085784093686669451-ai-command-thread-project-memory.md` (AI司令塔スレッドにプロジェクト記憶を集約し再開を助ける)
- Updated concept pages:
  - `concepts/external-memory.md`
  - `concepts/task-initiation.md`
  - `concepts/time-management.md`
  - `concepts/environment-design.md`
  - `concepts/attention-control.md`
  - `concepts/digital-adhd-support.md`
- Updated navigation: `index.md` date bump (total pages unchanged at 51)
- Note: X/Twitter posts are treated as lived-experience/practical tips only, not medical evidence; related concept pages remain low/medium confidence according to source mix.

## [2026-08-08] ingest | X/Twitter ADHDパワー系ソリューション定期検索 17
- Searches: 4 searches across `Latest` and `Top` products via bird. Deduplicated candidates by tweet ID and skipped already-ingested tweets, diagnosis discourse without tactics, vague motivation, medical/supplement claims without sources, memes, stigma/personal attacks, and posts exposing unnecessary personal detail.
- Created raw sources:
  - `raw/articles/tweet-2086044768136831454-reward-bundling-task-initiation.md` (面倒タスクをごほうび行動と束ねて着手ボタン化)
  - `raw/articles/tweet-2086014654325911629-timer-one-line-record.md` (タイマー＋1日1行記録で時間を外部化)
  - `raw/articles/tweet-2085867026594336842-deadline-paper-first-step.md` (紙の見える化・最初の一歩・2日前締切)
  - `raw/articles/tweet-1740646259206373382-hanger-storage-boxes.md` (ハンガー収納＋仕切り付きボックスで畳む工程を削減)
- Updated concept pages:
  - `concepts/task-initiation.md`
  - `concepts/time-management.md`
  - `concepts/environment-design.md`
  - `concepts/external-memory.md`
- Updated navigation: `index.md` unchanged (no new wiki pages; date already current at 2026-08-08).
- Note: X/Twitter posts are treated as lived-experience/practical tips only, not medical evidence; related concept pages remain `confidence: low`.

## [2026-08-08] ingest | X/Twitter ADHDパワー系ソリューション定期検索 18
- Searches: 4 searches across `Latest` and `Top` products via bird. Deduplicated by tweet ID; skipped already-ingested tweets, diagnosis discourse without tactics, vague motivation, medical/supplement claims without sources, memes, stigma/personal attacks, self-promotion without enough workflow detail, and posts exposing unnecessary personal detail.
- Created raw sources:
  - `raw/articles/tweet-2086135350314061910-five-person-relationship-reminders.md` (大事な人5人だけを年3回通知し、定型文で関係維持を外部化)
  - `raw/articles/tweet-2086067401779548493-visual-audio-efficiency-styles.md` (視覚化型・音境界型の効率化を試し分ける)
  - `raw/articles/tweet-2086059865575657531-minimum-verb-task-resolution.md` (大きなタスクを「最小の動詞」まで下げる)
  - `raw/articles/tweet-2086105627697549630-grill-with-docs-milestone-review.md` (AI/ドキュメントツールをマイルストーン区切りのレビュー役に限定)
- Updated concept pages:
  - `concepts/relationships.md`
  - `concepts/external-memory.md`
  - `concepts/task-initiation.md`
  - `concepts/attention-control.md`
  - `concepts/work-routines.md`
  - `concepts/digital-adhd-support.md`
- Updated navigation: no new wiki pages; `index.md` unchanged (date already 2026-08-08, total pages unchanged at 51).
- Note: X/Twitter posts are treated as lived-experience/practical tips only, not medical evidence; related tweet-derived content remains low-confidence.

## [2026-08-09] ingest | X/Twitter ADHDパワー系ソリューション定期検索 19
- Searches: 4 searches across `Latest` and `Top` products via bird. Deduplicated 72 unique tweet IDs; skipped 11 already-ingested tweets plus generic empathy, memes, diagnosis discourse, stigma/personal attacks, vague motivation, self-promotion without enough workflow detail, and medical/supplement claims without sources.
- Created raw sources:
  - `raw/articles/tweet-2086225948614303824-fixed-cost-one-item-review.md`
  - `raw/articles/tweet-2086193708740083838-morning-action-before-thinking.md`
  - `raw/articles/tweet-2086158105579315645-exam-stationery-preplacement.md`
  - `raw/articles/tweet-2014465170400280892-systematize-steady-effort.md`
- Updated concept pages:
  - `concepts/impulsivity-countermeasures.md`
  - `concepts/task-initiation.md`
  - `concepts/time-management.md`
  - `concepts/environment-design.md`
  - `concepts/work-routines.md`
- Updated navigation: `index.md` date bump; total pages unchanged.
- Note: X/Twitter posts are treated as lived-experience/practical tips only, not medical evidence; tweet-derived additions remain low-confidence.

## [2026-08-09] ingest | X/Twitter ADHDパワー系ソリューション定期検索 20
- Searches: 4 searches across `Latest` and `Top` products via bird. Deduplicated 76 unique tweet IDs; skipped 8 already-ingested tweets plus generic empathy, memes, diagnosis discourse, stigma/personal attacks, vague motivation, self-promotion without enough workflow detail, medical/supplement claims without sources, and duplicate/near-duplicate tactics already represented in the wiki.
- Created raw sources:
  - `raw/articles/tweet-2086316627231170570-first-action-on-paper.md`
  - `raw/articles/tweet-2086302039244718116-ai-prioritization-removes-choice.md`
  - `raw/articles/tweet-2086307734161588450-two-queue-workstation.md`
  - `raw/articles/tweet-2086256158608928882-housework-gamification.md`
- Updated concept pages:
  - `concepts/task-initiation.md`
  - `concepts/work-routines.md`
  - `concepts/digital-adhd-support.md`
- Updated navigation: `index.md` summaries for expanded existing concept pages; total pages unchanged.
- Note: X/Twitter posts are treated as lived-experience/practical tips only, not medical evidence; tweet-derived additions remain low-confidence.


## [2026-08-09] ingest | X/Twitter ADHDパワー系ソリューション定期検索 21
- Searches: 4 searches across `Latest` and `Top` products via bird. Deduplicated candidates by tweet ID; skipped already-ingested tweets, generic empathy, memes, diagnosis discourse, vague motivation, self-promotion without enough workflow detail, medical/supplement claims without sources, duplicate tactics already represented in the wiki, and posts exposing unnecessary personal detail.
- Created raw sources:
  - `raw/articles/tweet-2086407172221759835-no-script-implementation-intention.md`
  - `raw/articles/tweet-2086407145357279659-reduce-writing-oral-answer-processing-speed.md`
- Updated concept pages:
  - `concepts/relationships.md`
  - `concepts/public-support.md`
- Updated navigation: `index.md` date bump; total pages unchanged.
- Note: X/Twitter posts are treated as lived-experience/practical/educational tips only, not medical evidence; tweet-derived additions remain low-confidence and source-bound.


## [2026-08-09] ingest | X/Twitter ADHDパワー系ソリューション定期検索 22
- Searches: 4 searches across `Latest` and `Top` products via bird. Deduplicated 75 unique tweet IDs; skipped already-ingested tweets, stigma/personal attacks, generic diagnosis discourse, medical/medication or anemia-related posts without appropriate source context, vague motivation/self-promotion without enough workflow detail, and duplicate tactics already represented in the wiki.
- Created raw sources:
  - `raw/articles/tweet-2086493971350766006-verbalization-list-fragments.md`
  - `raw/articles/tweet-1980832956349300817-myndmap-goal-check-in.md`
- Updated concept pages:
  - `concepts/external-memory.md`
  - `concepts/task-initiation.md`
  - `concepts/digital-adhd-support.md`
- Updated navigation: `index.md` external-memory summary; total pages unchanged.
- Note: X/Twitter posts are treated as lived-experience/product-practical tips only, not medical evidence; tweet-derived additions remain low/medium-confidence and source-bound.


## [2026-08-10] ingest | X/Twitter ADHDパワー系ソリューション定期検索 23
- Searches: 4 searches across `Latest` and `Top` products via bird. Deduplicated candidates by tweet ID; skipped already-ingested tweets, generic empathy, memes, diagnosis discourse, stigma/personal attacks, vague motivation/self-promotion without enough workflow detail, medical/medication claims without sources, and posts exposing unnecessary personal detail.
- Created raw sources:
  - `raw/articles/tweet-2086606283055202702-end-alarm-before-start.md`
  - `raw/articles/tweet-2086601199089049749-linear-checklist-pr-ai-final-ten-percent.md`
  - `raw/articles/tweet-2086588348848837086-ear-blocking-noise-boundary.md`
  - `raw/articles/tweet-2086550541883277342-hyperfocus-stop-technology.md`
- Updated concept pages:
  - `concepts/time-management.md`
  - `concepts/hyperfocus-control.md`
  - `concepts/attention-control.md`
  - `concepts/work-routines.md`
- Updated navigation: `index.md` date and summaries; total pages unchanged.
- Note: X/Twitter posts are treated as lived-experience/practical tips only, not medical evidence; tweet-derived additions remain low-confidence/source-bound.


## [2026-08-10] ingest | X/Twitter ADHDパワー系ソリューション定期検索 24
- Searches: 4 searches across `Latest` and `Top` products via bird. Deduplicated candidates by tweet ID; skipped already-ingested tweets, generic empathy, memes, diagnosis discourse, stigma/personal attacks, vague motivation/self-promotion without enough workflow detail, medical/medication claims without sources, duplicate tactics already represented in the wiki, and posts exposing unnecessary personal detail.
- Created raw sources:
  - `raw/articles/tweet-2086701376911139129-ios-app-parallel-task-focus.md`
  - `raw/articles/tweet-2086658804285149597-fixed-tray-pouring-zone.md`
  - `raw/articles/tweet-2086659219496083720-fifteen-minute-single-goal-break.md`
  - `raw/articles/tweet-2083770574933991552-sensory-load-posture-glasses.md`
- Updated concept pages:
  - `concepts/digital-adhd-support.md`
  - `concepts/work-routines.md`
  - `concepts/time-management.md`
  - `concepts/task-initiation.md`
  - `concepts/environment-design.md`
  - `concepts/attention-control.md`
- Updated navigation: `index.md` summaries; total pages unchanged.
- Note: X/Twitter posts are treated as lived-experience/practical tips or self-experiments only, not medical evidence; tweet-derived additions remain low-confidence/source-bound.

## [2026-08-10] ingest | Research-watch curated context and self-tracking batch

- Reviewed 5 unprocessed candidates from `.automation/research-watch/candidates.jsonl`.
- Accepted 5 for raw + existing page updates (score 3); skipped 0 duplicates.
- Created raw sources:
  - `raw/papers/husain-2020-supportive-technologies-adhd-slr.md` — Investigating Current State-of-The-Art Applications of Supportive Technologies for Individuals with ADHD
  - `raw/papers/ara-2026-adhd-productivity-construction-ai-vr.md` — Understanding ADHD Productivity in Construction Work: Toward AI-enabled VR Interventions
  - `raw/papers/selin-2026-self-tracking-masking-neurodivergent.md` — "Chasing Shadows": Understanding Personal Data Externalization and Self-Tracking for Neurodivergent Individuals
  - `raw/papers/ruf-2023-diet-physical-activity-impulsivity-adult-adhd-ema.md` — Microtemporal Dynamics of Dietary Intake, Physical Activity, and Impulsivity in Adult Attention-Deficit/Hyperactivity Disorder: Ecological Momentary Assessment Study Within Nutritional Psychiatry
  - `raw/papers/carr-2026-fielded-attention-adhd-context.md` — Fielded Attention: Reframing ADHD Through a Relational Ontology of Context
- Updated concept pages:
  - `concepts/assistive-technology.md`
  - `concepts/attention-control.md`
  - `concepts/cognitive-personal-informatics.md`
  - `concepts/digital-adhd-support.md`
  - `concepts/environment-design.md`
  - `concepts/impulsivity-countermeasures.md`
  - `concepts/work-routines.md`
- Updated navigation/state: `index.md`, `.automation/research-watch/curation-state.json`.
- Note: EMA, self-tracking, AI/VR, and contextual-attention sources are design/evidence inputs, not diagnosis, treatment, nutrition, medication, or workplace-surveillance advice.


## [2026-08-10] ingest | X/Twitter ADHDパワー系ソリューション定期検索 25
- Searches: 4 searches across `Latest` and `Top` products via bird. Deduplicated candidates by tweet ID; skipped already-ingested tweets, generic empathy, memes, diagnosis discourse, stigma/personal attacks, vague motivation/self-promotion without enough workflow detail, medical/medication claims without sources, duplicate tactics already represented in the wiki, and posts exposing unnecessary personal detail.
- Created raw sources:
  - `raw/articles/tweet-2086748673787199621-forgetfulness-tool-bundle.md`
  - `raw/articles/tweet-2086742519904420303-error-manualization-routine.md`
- Updated concept pages:
  - `concepts/forgetfulness-countermeasures.md`
  - `concepts/external-memory.md`
  - `concepts/environment-design.md`
  - `concepts/careless-mistake-countermeasures.md`
  - `concepts/work-routines.md`
- Updated navigation: `index.md`; total pages unchanged.
- Note: X/Twitter posts are treated as lived-experience/practical tips only, not medical evidence; tweet-derived additions remain low-confidence/source-bound.


## [2026-08-10] ingest | X/Twitter ADHDパワー系ソリューション定期検索 26
- Searches: 4 searches across `Latest` and `Top` products via bird. Deduplicated 74 candidate tweets by tweet ID; skipped already-ingested tweets, generic empathy/diagnosis discourse, stigma or attacks, medical claims without source, vague promotions, and tactics already represented in the wiki.
- Created raw sources:
  - `raw/articles/tweet-1141299353497161728-one-sentence-task-splitting.md`
- Updated concept pages:
  - `concepts/task-initiation.md`
- Navigation: `index.md` already listed `[[task-initiation]]`; total pages unchanged.
- Note: X/Twitter posts are treated as lived-experience/practical tips only, not medical evidence; this addition remains low-confidence/source-bound.


## [2026-08-11] ingest | X/Twitter ADHDパワー系ソリューション定期検索 27
- Searches: 4 searches across `Latest` and `Top` products via bird. Deduplicated candidates by tweet ID; skipped already-ingested tweets, generic empathy/diagnosis discourse, stigma or attacks, vague promotions, medical claims without source, and tactics already represented without new detail.
- Created raw sources:
  - `raw/articles/tweet-2086889863656448054-left-right-task-split.md`
  - `raw/articles/tweet-2086935624599388361-early-delay-reporting.md`
  - `raw/articles/tweet-2086950776140886029-delayed-response-after-freeze.md`
  - `raw/articles/tweet-2086971764631040095-sleep-on-decisions-time-sense.md`
- Updated concept pages:
  - `concepts/work-routines.md`
  - `concepts/external-memory.md`
  - `concepts/emotion-regulation.md`
  - `concepts/impulsivity-countermeasures.md`
  - `concepts/time-management.md`
- Updated navigation: `index.md`; total pages unchanged.
- Note: X/Twitter posts are treated as lived-experience/practical tips only, not medical evidence; tweet-derived additions remain low-confidence/source-bound.

## [2026-08-11] ingest | X/Twitter ADHDパワー系ソリューション定期検索 28
- Searches: 4 searches across `Latest` and `Top` products via bird. Deduplicated candidates by tweet ID; skipped already-ingested tweets, generic empathy/diagnosis discourse, stigma or attacks, vague promotions, medical claims without source, and tactics already represented without new detail.
- Created raw sources:
  - `raw/articles/tweet-2086991993071374820-morning-three-hour-focus-routine.md`
  - `raw/articles/tweet-2087011129990300065-overnight-budget-before-spending.md`
  - `raw/articles/tweet-2086998621673968112-claude-code-remind-watch-organize.md`
- Updated concept pages:
  - `concepts/work-routines.md`
  - `concepts/task-initiation.md`
  - `concepts/time-management.md`
  - `concepts/impulsivity-countermeasures.md`
  - `concepts/digital-adhd-support.md`
- Updated navigation: `index.md`; total pages unchanged.
- Note: X/Twitter posts are treated as lived-experience/practical tips only, not medical evidence; tweet-derived additions remain low-confidence/source-bound.

## [2026-08-11] ingest | X/Twitter ADHDパワー系ソリューション定期検索 29
- Searches: 4 searches across `Latest` and `Top` products via bird. Deduplicated candidates by tweet ID; skipped already-ingested tweets, generic empathy/diagnosis discourse, stigma or attacks, vague promotions, medical/supplement claims without source, duplicate tactics already represented without new detail, and posts exposing unnecessary personal detail.
- Created raw sources:
  - `raw/articles/tweet-2087147124240650316-door-knob-sports-gear-prep.md`
  - `raw/articles/tweet-2087132477525745945-single-task-hotpot-cooking.md`
  - `raw/articles/tweet-2087071615096074718-game-login-pre-timer-friction.md`
  - `raw/articles/tweet-2087012072114569533-after-work-recovery-cost.md`
  - `raw/articles/tweet-2087094923179004098-twenty-minute-forced-break-agreement.md`
- Updated concept/navigation pages:
  - `concepts/forgetfulness-countermeasures.md`
  - `concepts/environment-design.md`
  - `concepts/digital-interruptions.md`
  - `concepts/energy-management.md`
  - `concepts/work-routines.md`
  - `index.md`
- Note: X/Twitter posts are treated as lived-experience/practical tips only, not medical evidence; tweet-derived additions remain low-confidence/source-bound.

## [2026-08-11] ingest | X/Twitter ADHDパワー系ソリューション定期検索 30
- Searches: 4 searches across `Latest` and `Top` products via bird. Deduplicated 73 unique tweet IDs; skipped already-ingested tweets, Kindle/book-sale noise, generic empathy/diagnosis discourse, self-promotion without enough concrete workflow, medical/supplement claims without source, duplicate tactics already represented without new detail, and posts exposing unnecessary personal detail.
- Created raw sources:
  - `raw/articles/tweet-2087185060562907424-fixed-sequence-departure-check.md`
- Updated concept/navigation pages:
  - `concepts/forgetfulness-countermeasures.md`
  - `index.md`
- Note: X/Twitter posts are treated as lived-experience/practical tips only, not medical evidence; tweet-derived additions remain low-confidence/source-bound.

## [2026-08-12] ingest | X/Twitter ADHDパワー系ソリューション定期検索 31
- Searches: 4 searches across `Latest` and `Top` products via bird. Deduplicated 76 unique tweet IDs; skipped already-ingested tweets, generic empathy/diagnosis discourse, medical/supplement claims without source, self-promotion without enough workflow detail, duplicate tactics already represented without new detail, and posts exposing unnecessary personal detail.
- Created raw sources:
  - `raw/articles/tweet-2087328213190217749-thoughts-inbox-evening-triage.md`
  - `raw/articles/tweet-2084915057650208912-adhd-pomodoro-no-extra-restarts-app.md`
- Updated concept/navigation pages:
  - `concepts/task-initiation.md`
  - `concepts/external-memory.md`
  - `concepts/time-management.md`
  - `concepts/digital-adhd-support.md`
  - `index.md`
- Note: X/Twitter posts are treated as lived-experience/practical tips only, not medical evidence; tweet-derived additions remain low-confidence/source-bound.
## [2026-08-12] ingest | X/Twitter ADHDパワー系ソリューション定期検索 32
- Searches: 4 searches across `Latest` and `Top` products via bird. Deduplicated candidates by tweet ID; skipped already-ingested tweets, generic empathy/diagnosis discourse, self-promotion without enough workflow detail, medical/supplement claims without source, duplicate tactics already represented without new detail, and posts exposing unnecessary personal detail.
- Created raw sources:
  - `raw/articles/tweet-2087416492082258023-ai-close-meeting-attention-residue.md`
  - `raw/articles/tweet-2087387483411738659-manual-ui-trade-admin-workflow.md`
- Updated concept/navigation pages:
  - `concepts/digital-adhd-support.md`
  - `concepts/work-routines.md`
  - `concepts/external-memory.md`
  - `concepts/task-initiation.md`
  - `index.md`
- Note: X/Twitter posts are treated as lived-experience/practical tips only, not medical evidence; tweet-derived additions remain low-confidence/source-bound.

## [2026-08-12] ingest | X/Twitter ADHDパワー系ソリューション定期検索 33
- Searches: 4 searches across `Latest` and `Top` products via bird. Deduplicated candidates by tweet ID; skipped already-ingested tweets, generic empathy/diagnosis discourse, medical/supplement claims without source, duplicate tactics already represented without new detail, self-promotion without enough workflow detail, and posts exposing unnecessary personal detail.
- Created raw sources:
  - `raw/articles/tweet-2087524179860246583-start-of-day-walltalk-task-capture.md`
  - `raw/articles/tweet-2087489223616336198-beeper-message-hub-ai-reminders.md`
  - `raw/articles/tweet-2087487424754757725-ai-empty-function-first-step.md`
- Updated concept/navigation pages:
  - `concepts/external-memory.md`
  - `concepts/task-initiation.md`
  - `concepts/digital-adhd-support.md`
  - `concepts/work-routines.md`
  - `index.md`
- Note: X/Twitter posts are treated as lived-experience/practical tips only, not medical evidence; tweet-derived additions remain low-confidence/source-bound.


## [2026-08-12] ingest | X/Twitter ADHDパワー系ソリューション定期検索 34
- Searches: 4 searches across `Latest` and `Top` products via bird. Deduplicated 76 unique tweet IDs; skipped already-ingested tweets, generic empathy/diagnosis discourse, medical/supplement claims without source, duplicate tactics already represented without new detail, self-promotion without enough workflow detail, and posts exposing unnecessary personal detail.
- Created raw sources:
  - `raw/articles/tweet-2087516955498709345-future-passbook-cashflow.md`
- Updated concept/navigation pages:
  - `concepts/impulsivity-countermeasures.md`
  - `index.md`
- Note: X/Twitter posts are treated as lived-experience/practical tips only, not medical or financial advice; tweet-derived additions remain low-confidence/source-bound.

## [2026-08-13] ingest | X/Twitter ADHDパワー系ソリューション定期検索 35
- Searches: 4 searches across `Latest` and `Top` products via bird. Deduplicated 70 unique tweet IDs; skipped already-ingested tweets, generic empathy/diagnosis discourse, medical/supplement claims without source, duplicate tactics without new detail, self-promotion without enough workflow detail, and posts exposing unnecessary personal detail.
- Created raw sources:
  - `raw/articles/tweet-2087645502275776597-analog-clock-single-exit-alarm.md`
  - `raw/articles/tweet-2087670435681087636-office-walking-distance-lateness-environment.md`
  - `raw/articles/tweet-2087645349330698667-delegate-automate-execution.md`
- Updated concept/navigation pages:
  - `concepts/time-management.md`
  - `concepts/environment-design.md`
  - `concepts/work-routines.md`
  - `concepts/task-initiation.md`
  - `index.md`
- Note: X/Twitter posts are treated as lived-experience/practical tips only, not medical evidence; tweet-derived additions remain low-confidence/source-bound.

## [2026-08-13] ingest | X/Twitter ADHDパワー系ソリューション定期検索 36
- Searches: 4 searches across `Latest` and `Top` products via bird. Deduplicated 72 unique tweet IDs; skipped already-ingested tweets, generic empathy/diagnosis discourse, stigma/attacks, medical claims without source, duplicate tactics without new detail, self-promotion without enough workflow detail, and posts exposing unnecessary personal detail.
- Created raw sources:
  - `raw/articles/tweet-2087783566897991746-stale-idea-ai-handover.md`
  - `raw/articles/tweet-2087750857970565344-ai-history-auto-task-display.md`
  - `raw/articles/tweet-2087735907990597693-done-record-success-memory.md`
  - `raw/articles/tweet-2087766095440781483-night-before-morning-prep.md`
- Updated concept/navigation pages:
  - `concepts/task-initiation.md`
  - `concepts/external-memory.md`
  - `concepts/digital-adhd-support.md`
  - `concepts/environment-design.md`
  - `concepts/time-management.md`
- Navigation: `index.md` already current at 2026-08-13; no new wiki pages created.
- Note: X/Twitter posts are treated as lived-experience/practical tips only, not medical evidence; tweet-derived additions remain low-confidence/source-bound.

## [2026-08-13] ingest | Research-watch curated comorbidity, AI support, and raw-only design candidates

- Reviewed 5 unprocessed candidates from `.automation/research-watch/candidates.jsonl`.
- Accepted 3 for raw + existing page updates (score 3) and 2 for raw-only (score 2); created no new wiki pages.
- Created raw sources:
  - `raw/papers/garcia-argibay-2026-adhd-autism-medication-patterns-sweden.md` — ADHD+ASD youth medication patterns in Swedish national registers
  - `raw/papers/montoya-2026-ai-quest-based-therapy-adhd-case-report.md` — AI-assisted quest-based psychotherapy delivery case report
  - `raw/papers/gelner-2026-adhd-symptoms-ple-temporal-network-esm.md` — ADHD symptoms, PLEs, negative affect, cortisol, and ESM temporal networks
  - `raw/papers/lin-2025-perceptual-reality-transformer-neurological-perception.md` — raw-only neurological perception simulation preprint
  - `raw/papers/lin-2025-intelligent-monitoring-physical-exercise-children-adhd.md` — raw-only child ADHD exercise monitoring preprint
- Updated concept/navigation pages:
  - `concepts/medication.md`
  - `concepts/comorbidity.md`
  - `concepts/psychotic-like-experiences.md`
  - `concepts/emotion-regulation.md`
  - `concepts/digital-adhd-support.md`
  - `index.md`
- Updated automation state: `.automation/research-watch/curation-state.json`.
- Note: medication findings are source-bound and not treatment advice; AI case report is hypothesis-generating only; child/preprint sources were kept raw-only to avoid overgeneralising to adults.

## [2026-08-13] ingest | X/Twitter ADHDパワー系ソリューション定期検索 37
- Searches: 4 searches across `Latest` and `Top` products via bird. Deduplicated candidates by tweet ID; skipped already-ingested tweets, generic empathy/diagnosis discourse, stigma/attacks, medical/supplement claims without source, duplicate tactics without new detail, self-promotion without enough workflow detail, and posts exposing unnecessary personal detail.
- Created raw sources:
  - `raw/articles/tweet-2087887849819459834-morning-ninety-minute-defense-time.md`
  - `raw/articles/tweet-2087875589726175569-pay-receive-one-set-chant.md`
- Updated concept/navigation pages:
  - `concepts/work-routines.md`
  - `concepts/task-initiation.md`
  - `concepts/forgetfulness-countermeasures.md`
  - `concepts/external-memory.md`
  - `index.md` (not rewritten: file is currently detected as binary by the editor tools; existing entries still cover the updated concepts)
- Note: X/Twitter posts are treated as lived-experience/practical tips only, not medical evidence; tweet-derived additions remain low-confidence/source-bound.

## [2026-08-13] ingest | X/Twitter ADHDパワー系ソリューション定期検索 38
- Searches: 4 searches across `Latest` and `Top` products via bird. Deduplicated 76 unique tweet IDs; skipped already-ingested tweets, diagnosis/stigma discourse, generic empathy, medical/supplement claims without source, duplicate tactics without new detail, and posts exposing unnecessary personal detail.
- Created raw sources:
  - `raw/articles/tweet-2087920921881309189-sixty-minute-twist-timer-meeting.md`
  - `raw/articles/tweet-2085290732919632166-robot-vacuum-floor-constraint.md`
- Updated concept/navigation pages:
  - `concepts/time-management.md`
  - `concepts/hyperfocus-control.md`
  - `concepts/work-routines.md`
  - `concepts/environment-design.md`
  - `index.md` (not rewritten: file is currently detected as binary by the editor tools; existing concept entries still cover the updated pages)
- Note: X/Twitter posts are treated as lived-experience/practical tips only, not medical evidence; tweet-derived additions remain low-confidence/source-bound.


## [2026-08-14] ingest | X/Twitter ADHDパワー系ソリューション定期検索 39
- Searches: 4 searches across `Latest` and `Top` products via bird. Deduplicated 77 unique tweet IDs; skipped already-ingested tweets, generic empathy/diagnosis discourse, stigma/attacks, medical/supplement claims without source, duplicate tactics without new detail, and posts exposing unnecessary personal detail.
- Created raw sources:
  - `raw/articles/tweet-1740408697166422428-stock-label-directly.md`
  - `raw/articles/tweet-1740335770572034332-concierge-five-outfit-capsule.md`
  - `raw/articles/tweet-1740348604106387795-lost-first-storage-location.md`
  - `raw/articles/tweet-2088068099551695288-artificial-early-deadline-pressure.md`
- Updated concept/navigation pages:
  - `concepts/forgetfulness-countermeasures.md`
  - `concepts/external-memory.md`
  - `concepts/environment-design.md`
  - `concepts/time-management.md`
  - `concepts/task-initiation.md`
  - `index.md`
- Note: X/Twitter posts are treated as lived-experience/practical tips only, not medical evidence; tweet-derived additions remain low-confidence/source-bound.

## [2026-08-14] ingest | X/Twitter ADHDパワー系ソリューション定期検索 40
- Searches: 4 searches across `Latest` and `Top` products via bird. Deduplicated 84 unique tweet IDs; skipped already-ingested tweets, generic empathy/diagnosis discourse, stigma/attacks, medical claims without source, duplicate tactics without new detail, and posts exposing unnecessary personal detail.
- Created raw sources:
  - `raw/articles/tweet-2088128495599890644-visible-fixed-location.md`
  - `raw/articles/tweet-2088122314894516524-duplicate-spares-by-location.md`
  - `raw/articles/tweet-1011452472458502145-vocalize-open-avoidant-task.md`
  - `raw/articles/tweet-1740396049225887887-station-departure-countdown-widget.md`
  - `raw/articles/tweet-1740384815730585736-routine-timer-morning-housework.md`
- Updated concept/navigation pages:
  - `concepts/forgetfulness-countermeasures.md`
  - `concepts/external-memory.md`
  - `concepts/time-management.md`
  - `concepts/task-initiation.md`
  - `concepts/environment-design.md`
  - `index.md`
- Note: X/Twitter posts are treated as lived-experience/practical tips only, not medical evidence; tweet-derived additions remain low-confidence/source-bound.

## [2026-08-14] ingest | X/Twitter ADHDパワー系ソリューション定期検索 41
- Searches: 4 searches across `Latest` and `Top` products via bird. Deduplicated across products; skipped already-ingested tweets, generic empathy/diagnosis discourse, stigma/attacks, medical claims without source, duplicate tactics without new detail, and posts exposing unnecessary personal detail.
- Created raw sources:
  - `raw/articles/tweet-2088249303223652708-point-and-call-belongings-check.md`
  - `raw/articles/tweet-2088238475082674603-dm-call-find-phone.md`
  - `raw/articles/tweet-2088204763397779721-waiting-mode-backward-alarm.md`
  - `raw/articles/tweet-1263751107001499653-discord-zoom-task-dump.md`
- Updated concept/navigation pages:
  - `concepts/forgetfulness-countermeasures.md`
  - `concepts/external-memory.md`
  - `concepts/waiting-mode.md`
  - `concepts/time-management.md`
  - `concepts/body-doubling.md`
  - `concepts/task-initiation.md`
- Note: X/Twitter posts are treated as lived-experience/practical tips only, not medical evidence; tweet-derived additions remain low-confidence/source-bound.


## [2026-08-14] ingest | X/Twitter ADHDパワー系ソリューション定期検索 42
- Searches: 4 searches across `Latest` and `Top` products via bird. Deduplicated tweet IDs across products; skipped already-ingested tweets, generic empathy/diagnosis discourse, stigma/attacks, medical claims without source, duplicate tactics without new detail, and posts exposing unnecessary personal detail.
- Created raw sources:
  - `raw/articles/tweet-2088309691353079858-immediate-reward-pairing.md`
  - `raw/articles/tweet-2088294258113479117-no-thinking-walk-brain-fatigue.md`
  - `raw/articles/tweet-2088264584587317280-outing-tasks-ordered-night-before.md`
  - `raw/articles/tweet-1740450997737255310-ikea-measuring-cup-as-mug.md`
  - `raw/articles/tweet-1726008484150591650-child-bike-access-constraint.md`
- Updated concept/navigation pages:
  - `concepts/task-initiation.md`
  - `concepts/energy-management.md`
  - `concepts/time-management.md`
  - `concepts/external-memory.md`
  - `concepts/environment-design.md`
  - `concepts/parenting.md`
- Note: X/Twitter posts are treated as lived-experience/practical tips only, not medical evidence; tweet-derived additions remain low-confidence/source-bound.


## [2026-08-15] ingest | X/Twitter ADHDパワー系ソリューション定期検索 43
- Searches: 4 searches across `Latest` and `Top` products via bird. Deduplicated tweet IDs across products; skipped already-ingested tweets, duplicate routine-timer/old evergreen tactics without new detail, generic discourse, memes, medical claims without source, and posts exposing unnecessary personal detail.
- Created raw sources:
  - `raw/articles/tweet-2088454379410251809-smartphone-at-entrance-start-trigger.md`
  - `raw/articles/tweet-2088418166884139504-next-line-before-close.md`
- Updated concept/navigation pages:
  - `concepts/task-initiation.md`
  - `concepts/environment-design.md`
  - `concepts/task-resumption.md`
  - `index.md`
- Note: X/Twitter posts are treated as lived-experience/practical tips only, not medical evidence; tweet-derived additions remain low-confidence/source-bound.

## [2026-08-15] ingest | X/Twitter ADHDパワー系ソリューション定期検索 44
- Searches: 4 searches across `Latest` and `Top` products via bird. Deduplicated 72 unique tweet IDs; skipped already-ingested tweets, generic empathy/diagnosis discourse, stigma/attacks, medical claims without source, duplicate tactics without new detail, self-promotion without enough workflow detail, and posts exposing unnecessary personal detail.
- Created raw sources:
  - `raw/articles/tweet-2088489145278620041-interest-injection-start.md`
  - `raw/articles/tweet-2088476213589491939-one-tool-notification-subtraction.md`
  - `raw/articles/tweet-1831974163546038535-vibration-timer-pomodoro.md`
  - `raw/articles/tweet-1741335759955857793-bell-on-wallet-airpods.md`
- Updated concept/navigation pages:
  - `concepts/task-initiation.md`
  - `concepts/digital-adhd-support.md`
  - `concepts/time-management.md`
  - `concepts/hyperfocus-control.md`
  - `concepts/forgetfulness-countermeasures.md`
- Note: X/Twitter posts are treated as lived-experience/practical tips only, not medical evidence; tweet-derived additions remain low-confidence/source-bound.

## [2026-08-15] ingest | X/Twitter ADHDパワー系ソリューション定期検索 45
- Searches: 4 searches across `Latest` and `Top` products via bird. Deduplicated 74 unique tweet IDs; skipped already-ingested tweets, generic empathy/diagnosis discourse, memes, medical claims without source, duplicate routine-timer/GPS-tag/appliance tactics without new detail, self-promotion without enough workflow detail, and posts exposing unnecessary personal detail.
- Created raw sources:
  - `raw/articles/tweet-2088582900614844801-shopping-meal-system.md`
  - `raw/articles/tweet-2088557429147726317-remove-cause-before-study.md`
  - `raw/articles/tweet-2026984818442178853-five-minutes-sixty-percent-rest.md`
- Updated concept/navigation pages:
  - `concepts/task-initiation.md`
  - `concepts/environment-design.md`
  - `concepts/energy-management.md`
  - `index.md`
- Note: X/Twitter posts are treated as lived-experience/practical tips only, not medical evidence; tweet-derived additions remain low-confidence/source-bound.

## [2026-08-15] ingest | X/Twitter ADHDパワー系ソリューション定期検索 46
- Searches: 4 searches across `Latest` and `Top` products via bird. Deduplicated tweet IDs across products; skipped already-ingested tweets, generic empathy/diagnosis discourse, memes, medical claims without source, duplicate small-step/timer/home-appliance tactics without new detail, self-promotion without enough workflow detail, and posts exposing unnecessary personal detail.
- Created raw sources:
  - `raw/articles/tweet-2088732461316636961-gemini-voice-google-tasks.md`
- Updated concept/navigation pages:
  - `concepts/external-memory.md`
  - `concepts/digital-adhd-support.md`
  - `index.md`
- Tip summary: Geminiに自然文で話した複数の用事をGoogle Tasksへ整理・登録させ、手入力・アプリ切替・保持負荷を減らす。
- Note: X/Twitter posts are treated as lived-experience/practical tips only, not medical evidence; tweet-derived additions remain low-confidence/source-bound.

## [2026-08-16] ingest | X/Twitter ADHDパワー系ソリューション定期検索 47
- Searches: 4 searches across `Latest` and `Top` products via bird. Deduplicated tweet IDs across products; skipped already-ingested tweets, generic empathy/diagnosis discourse, medical claims without source, duplicate timer/home-appliance/money tactics without new detail, self-promotion without enough workflow detail, and posts exposing unnecessary personal detail.
- Created raw sources:
  - `raw/articles/tweet-2088805945656656356-residual-count-alert-automation.md`
- Updated concept/navigation pages:
  - `concepts/work-routines.md`
  - `concepts/external-memory.md`
  - `concepts/environment-design.md`
  - `index.md`
- Tip summary: 予約投稿や在庫のように減っていく仕組みは、残数を数えて閾値で通知し、空になる前に補充へ戻す。
- Note: X/Twitter posts are treated as lived-experience/practical tips only, not medical evidence; tweet-derived additions remain low-confidence/source-bound.

## [2026-08-16] ingest | X/Twitter ADHDパワー系ソリューション定期検索 48
- Searches: 4 searches across `Latest` and `Top` products via bird. Deduplicated tweet IDs across products; skipped already-ingested tweets, generic empathy/diagnosis discourse, memes, medical claims without source, duplicate timer/home-appliance/recovery-cost/money tactics without new detail, self-promotion without enough workflow detail, and posts exposing unnecessary personal detail.
- Created raw sources:
  - `raw/articles/tweet-2088914159073218947-automation-health-output-count.md`
  - `raw/articles/tweet-2088880046996152439-codex-claude-code-state-support.md`
  - `raw/articles/tweet-2088748316020604979-payday-money-guardrails.md`
- Updated concept/navigation pages:
  - `concepts/work-routines.md`
  - `concepts/digital-adhd-support.md`
  - `concepts/task-initiation.md`
  - `concepts/impulsivity-countermeasures.md`
- Tip summaries:
  - 自動化は「起動したか」ではなく、在庫・成果物が実際に増えたかを健康指標にする。
  - Codex/Claude Codeを、作業代行だけでなく「作業できる状態」までの補佐・入口づくりに使う。
  - 給料日移動、カード1枚、毎日利用額確認、24時間待機でお金の衝動を先回りして縛る。
- Note: X/Twitter posts are treated as lived-experience/practical tips only, not medical evidence; tweet-derived additions remain low-confidence/source-bound.

## [2026-08-16] ingest | X/Twitter ADHDパワー系ソリューション定期検索 49
- Searches: 4 searches across `Latest` and `Top` products via bird. Deduplicated 74 unique tweet IDs; skipped 11 already-ingested tweets plus generic empathy, diagnosis discourse, memes, medical/supplement claims without source, self-promotion without enough workflow detail, duplicate GPS/timer/ChatGPT-general tactics without new detail, and posts exposing unnecessary personal detail.
- Created raw sources:
  - `raw/articles/tweet-2088834572637380766-ai-secretary-always-on-checkins.md`
  - `raw/articles/tweet-2088971788453580825-procrastinate-bad-habits-friction.md`
  - `raw/articles/tweet-2088920198589911187-work-variation-width.md`
- Updated concept/navigation pages:
  - `concepts/digital-adhd-support.md`
  - `concepts/digital-interruptions.md`
  - `concepts/task-initiation.md`
  - `concepts/work-routines.md`
  - `concepts/attention-control.md`
  - `index.md`
- Tip summaries:
  - GPTをAI秘書・常時通話のボディダブルにし、10分ごとの進捗確認や次行動選択を外部化する。
  - スマホやXに入口摩擦を置き、やめたい習慣を自然に先延ばしさせる。
  - 思考/単純作業、机上/歩行、目先/長期など作業方法のふり幅を持ち、飽きを減らす。
- Note: X/Twitter posts are treated as lived-experience/practical tips only, not medical evidence; tweet-derived additions remain low-confidence/source-bound. The AI-secretary tactic has high privacy risk if screen/audio/logs are shared too broadly.

## [2026-08-16] ingest | X/Twitter ADHDパワー系ソリューション定期検索 50
- Searches: 4 searches across `Latest` and `Top` products via bird. Deduplicated tweet IDs across products; skipped already-ingested tweets, generic empathy/diagnosis discourse, memes, medical claims without source, duplicate timer/AI/money tactics without new detail, self-promotion without enough workflow detail, and posts exposing unnecessary personal detail.
- Created raw sources:
  - `raw/articles/tweet-2089094947009859850-separate-living-budget-account.md`
  - `raw/articles/tweet-2088485397483708626-anyplanner-lockscreen-task-timeline.md`
  - `raw/articles/tweet-2088430745987785009-routine-timer-playlist-morning.md`
- Updated concept/navigation pages:
  - `concepts/impulsivity-countermeasures.md`
  - `concepts/digital-adhd-support.md`
  - `concepts/external-memory.md`
  - `concepts/time-management.md`
  - `index.md`
- Tip summaries:
  - 生活費口座だけに月予算を入れ、残高が空になったら終了にする。
  - 思いついたタスクを「あとで」へ逃がし、タイムライン・通知・ロック画面/ウィジェットで再提示する。
  - ルーチンタイマーと専用プレイリストで朝の支度順序と時間経過を外部化する。
- Note: X/Twitter posts are treated as lived-experience/practical tips only, not medical evidence; tweet-derived additions remain low-confidence/source-bound.

## [2026-08-17] ingest | X/Twitter ADHDパワー系ソリューション定期検索 51
- Searches: 4 searches across `Latest` and `Top` products via bird. Deduplicated tweet IDs across products; skipped already-ingested tweets, generic empathy/diagnosis discourse, memes, medical claims without source, duplicate timer/AI/money/environment tactics without new detail, engagement-bait/link posts without enough workflow detail, and posts exposing unnecessary personal detail.
- Created raw sources:
  - `raw/articles/tweet-2089146950558113832-ai-brain-dump-priority-prompt.md`
- Updated concept/navigation pages:
  - `concepts/task-initiation.md`
  - `concepts/external-memory.md`
  - `concepts/digital-adhd-support.md`
  - `index.md`
- Tip summary:
  - 朝のフリーズ時、未整理のタスク・予定・不安をAIへそのまま貼り、「今日中／後日／不安」に分けさせ、今日中の1件と最初の3分だけを返させる。
- Note: X/Twitter posts are treated as lived-experience/practical tips only, not medical evidence; tweet-derived additions remain low-confidence/source-bound. Cloud AI inputs should minimize workplace, family, medical, and other sensitive details.

## [2026-08-17] ingest | Research-watch VR mindfulness RCT and low-signal child risk model

- Reviewed 2 unprocessed research-watch candidates from `.automation/research-watch/candidates.jsonl`.
- Accepted 1 for raw + existing page update (score 3): Lee et al. 2026 VR-based mindfulness RCT for college students with ADHD symptoms.
- Skipped/state-only 1 low-signal candidate (score 1): school-age child ADHD nomogram/risk-factor study, because it is child-focused and not a reusable support/design source for the current wiki priorities.
- Created raw source:
  - `raw/papers/lee-2026-vr-mindfulness-college-adhd-rct.md`
- Updated concept/navigation pages:
  - `concepts/digital-adhd-support.md`
  - `concepts/environment-design.md` (fixed a pre-existing broken `[[home]]` wikilink found during verification)
- Updated automation state: `.automation/research-watch/curation-state.json`.
- Note: VR mindfulness findings are source-bound, short-term, and not personal medical advice; cybersickness/adverse-event withdrawals are kept with the finding.

## [2026-08-17] ingest | X/Twitter ADHDパワー系ソリューション定期検索 52
- Searches: 4 searches across `Latest` and `Top` products via bird. Deduplicated tweet IDs across products; skipped already-ingested tweets, generic empathy/diagnosis discourse, stigma/personal attacks, medical claims without source, low-detail product/engagement posts, and tactics already captured without new detail.
- Created raw sources:
  - `raw/articles/tweet-2089276145225420933-artificial-deadline-date.md`
  - `raw/articles/tweet-2089245859645133240-fixed-start-cue.md`
  - `raw/articles/tweet-2088950567490191473-hyperfocus-ninety-minute-stop.md`
- Updated concept/navigation pages:
  - `concepts/task-initiation.md`
  - `concepts/time-management.md`
  - `concepts/hyperfocus-control.md`
  - `index.md`
- Tip summaries:
  - 締切のないタスクに仮の日付を1つ書き込み、起動合図を外部化する。
  - 気分待ちではなく、決まった動作を作業開始・休憩復帰の合図にする。
  - 過集中で燃え尽きる前に90分タイマーで一度手を止め、完了まで走る前提を外す。
- Note: X/Twitter posts are treated as lived-experience/practical tips only, not medical evidence; tweet-derived additions remain low-confidence/source-bound.


## [2026-08-17] ingest | X/Twitter ADHDパワー系ソリューション定期検索 53
- Searches: 4 searches across `Latest` and `Top` products via bird. Deduplicated tweet IDs across products; skipped already-ingested tweets, generic empathy/diagnosis discourse, stigma/personal attacks, medical claims without source, low-detail posts, and tactics already captured without new detail.
- Created raw sources:
  - `raw/articles/tweet-2089374389334573266-document-checklist-quality-gate.md`
  - `raw/articles/tweet-2089321593935925410-environment-switch-smartphone-cafe-silence.md`
  - `raw/articles/tweet-2089306298018120095-single-departure-time-no-buffer-loop.md`
  - `raw/articles/tweet-2089305319868657792-now-or-memo-paper-schedule-todo.md`
- Updated concept/navigation pages:
  - `concepts/work-routines.md`
  - `concepts/environment-design.md`
  - `concepts/task-initiation.md`
  - `concepts/time-management.md`
  - `concepts/external-memory.md`
- Tip summaries:
  - 資料提出前の数字・誤字・参照漏れ確認を、注意力ではなく固定チェックリストの品質ゲートにする。
  - 作業前にスマホを別室へ置く、カフェへ移動する、イヤホンで無音化するなど、意志力より環境切替を使う。
  - 遅刻対策では余白時間を増やすより、出る時刻を1つだけ固定して逆算ループを消す。
  - 仕事中のタスクは「今やる／メモする」の二択にし、アポ時間割とToDoを同じ紙へ置く。
- Note: X/Twitter posts are treated as lived-experience/practical tips only, not medical evidence; tweet-derived additions remain low-confidence/source-bound.

## [2026-08-17] ingest | X/Twitter ADHDパワー系ソリューション定期検索 54
- Searches: 4 searches across `Latest` and `Top` products via bird. Deduplicated tweet IDs across products; skipped already-ingested tweets, generic empathy/diagnosis discourse, stigma/personal attacks, medical claims without source, low-detail posts, and tactics already captured without new detail.
- Created raw sources:
  - `raw/articles/tweet-2089457453100380595-name-repeat-feature-memo.md`
  - `raw/articles/tweet-2089412622936588784-external-search-window.md`
- Updated concept/navigation pages:
  - `concepts/external-memory.md`
  - `concepts/relationships.md`
  - `index.md`
- Tip summaries:
  - 名前を聞いた直後に復唱し、会話中にも呼び、別れた直後に「名前＋非センシティブな特徴」をメモして次回前に見返す。
  - 思いつきを完全な文章にする前に、単語・音声・スクリーンショットなど最小の検索キーとして外へ出す。
- Note: X/Twitter posts are treated as lived-experience/practical tips only, not medical evidence; tweet-derived additions remain low-confidence/source-bound.

## [2026-08-18] ingest | X/Twitter ADHDパワー系ソリューション定期検索 55
- Searches: 4 searches across `Latest` and `Top` products via bird. Deduplicated tweet IDs across products; skipped already-ingested tweets, generic empathy/diagnosis discourse, stigma/personal attacks, medical claims without source, low-detail posts, private/sensitive disclosures, and tactics already captured without new detail.
- Created raw sources:
  - `raw/articles/tweet-2089547898518466725-purchase-friction-not-waiting.md`
  - `raw/articles/tweet-2089501687077646681-ninety-minute-smartphone-away-single-task.md`
  - `raw/articles/tweet-2089524384524574723-flexible-meeting-time-contract.md`
- Updated concept/navigation pages:
  - `concepts/impulsivity-countermeasures.md`
  - `concepts/work-routines.md`
  - `concepts/environment-design.md`
  - `concepts/time-management.md`
  - `index.md`
- Tip summaries:
  - 衝動買いは「三日待つ」より、購入手続き自体を物理的に重くして入口摩擦を増やす。
  - 90分だけスマホを別室へ置き、メール・Slack・細かい返答へ逃げる選択肢を消して本命タスクをシングルタスク化する。
  - 遅刻しやすい私的な待ち合わせでは、相手の同意を前提に厳密な時刻ではなく幅のある到着目標として契約し直す。
- Note: X/Twitter posts are treated as lived-experience/practical tips only, not medical evidence; tweet-derived additions remain low-confidence/source-bound.

## [2026-08-18] ingest | X/Twitter ADHDパワー系ソリューション定期検索 56
- Searches: 4 searches across `Latest` and `Top` products via bird. Deduplicated tweet IDs across products; skipped already-ingested tweets, generic empathy/diagnosis discourse, stigma/personal attacks, medical claims without source, low-detail posts, private/sensitive disclosures, and tactics already captured without new detail.
- Created raw sources:
  - `raw/articles/tweet-2089044426756854257-conditions-self-manual.md`
  - `raw/articles/tweet-2088786301571289251-reward-task-first.md`
  - `raw/articles/tweet-2088834068779835687-rest-training-breath-stretch-pole.md`
- Updated concept/navigation pages:
  - `concepts/self-experimentation.md`
  - `concepts/task-initiation.md`
  - `concepts/energy-management.md`
  - `index.md`
- Tip summaries:
  - 「できる／できない」ではなく、凸が出る条件と止まる条件を棚卸しし、凹はメモ・AI・人・環境変更などの仕組みで補う。
  - 「1分だけ」でも重い時は、好きな作業・ご褒美作業を一日の最初に置いて着手に即時報酬を貼る。
  - 疲れ対策として、呼吸エクササイズやストレッチポールを使い、副交感神経モードへ入る休養ルーティンを練習する。
- Note: X/Twitter posts are treated as lived-experience/practical tips only, not medical evidence; tweet-derived additions remain low-confidence/source-bound.


## [2026-08-18] ingest | X/Twitter ADHDパワー系ソリューション定期検索 57
- Searches: 4 searches across `Latest` and `Top` products via bird. Deduplicated 77 unique tweet IDs; skipped already-ingested tweets, English/non-Japanese noise, generic empathy/diagnosis discourse, medical claims without source, low-detail posts, duplicate tactics without new detail, and posts exposing unnecessary personal detail.
- Created raw sources:
  - `raw/articles/tweet-2089601897808474477-human-presence-workplace-cafe.md`
  - `raw/articles/tweet-2089621706415698135-visible-storage-wire-rack.md`
  - `raw/articles/tweet-2089646987637580066-batch-same-phase-work.md`
  - `raw/articles/tweet-2089665226186908143-confirmation-done-mark-checklist.md`
  - `raw/articles/tweet-2089676299358949645-hyperfocus-double-alarm-food-breaks.md`
  - `raw/articles/tweet-2089706380219564459-departure-buffer-physically-wait.md`
  - `raw/articles/tweet-2089720617516028204-rubber-band-wrist-kitchen-timer.md`
- Updated concept/navigation pages:
  - `concepts/task-initiation.md`
  - `concepts/environment-design.md`
  - `concepts/work-routines.md`
  - `concepts/careless-mistake-countermeasures.md`
  - `concepts/hyperfocus-control.md`
  - `concepts/time-management.md`
  - `index.md`
- Tip summaries:
  - 人目はあるが干渉されないカフェ等へ通い、軽い緊張感を着手スイッチにする。
  - ワイヤーラックやスチール棚で物を隠さず、存在を視界に残す。
  - メール等を同じ処理段階ごとに束ね、「今は理解だけ」のように認知操作を限定する。
  - 確認回数を増やす代わりに、確認済みチェック欄を残して確認ループを閉じる。
  - 過集中前に二重終了アラーム、休憩・食事の予定化、手元の即食燃料を置く。
  - 出発前の余白は靴を履いて玄関で待つ／外へ出ることで物理的に潰す。
  - 輪ゴム付きキッチンタイマーを腕時計風にして、スマホなしの身体装着タイマーにする。
- Note: X/Twitter posts are treated as lived-experience/practical tips only, not medical evidence; tweet-derived additions remain low-confidence/source-bound.


## [2026-08-18] ingest | X/Twitter ADHDパワー系ソリューション定期検索 58
- Searches: 4 searches across `Latest` and `Top` products via bird. Deduplicated candidate tweets across products; skipped already-ingested tweets, non-practical posts, PR/generic article cards with insufficient detail, diagnosis/medical claims without source, and posts with unnecessary personal detail.
- Created raw sources:
  - `raw/articles/tweet-2089768299999703211-work-call-body-doubling.md`
  - `raw/articles/tweet-1955833681530249477-frozen-meal-dedicated-freezer.md`
  - `raw/articles/tweet-1740494192500146510-colornote-home-screen-memo.md`
- Updated concept pages:
  - `concepts/body-doubling.md`
  - `concepts/task-initiation.md`
  - `concepts/environment-design.md`
  - `concepts/external-memory.md`
- Tip summaries:
  - 「あと5分したらやる」が続く作業は、作業通話を先に始めて人の同席感を着手スイッチにする。
  - 食材管理・調理・食器洗いを減らすため、専用冷凍庫と月次冷凍弁当で平日の食事工程を固定する。
  - スマホのホーム画面をメモ帳化し、重要度と日付で配置を分けて毎回見る画面へタスクを常駐させる。
- Note: X/Twitter posts are treated as lived-experience/practical tips only, not medical evidence; tweet-derived additions remain low-confidence/source-bound.

## [2026-08-19] ingest | X/Twitter ADHDパワー系ソリューション定期検索 59
- Searches: 4 searches across `Latest` and `Top` products via bird. Deduplicated 76 unique tweet IDs; skipped already-ingested tweets, generic empathy/diagnosis discourse, medical claims without source, duplicate smartphone/timer/visible-storage tactics without new detail, self-promotion without enough workflow detail, and posts exposing unnecessary personal detail.
- Created raw sources:
  - `raw/articles/tweet-2089910225205968955-touch-only-when-used.md`
  - `raw/articles/tweet-2089900093008941342-a3-journaling-association-brake.md`
  - `raw/articles/tweet-2089896496695214305-zoom-now-body-doubling-admin.md`
- Updated concept/navigation pages:
  - `concepts/forgetfulness-countermeasures.md`
  - `concepts/external-memory.md`
  - `concepts/task-initiation.md`
  - `concepts/body-doubling.md`
  - `index.md`
- Tip summaries:
  - 鍵などの必需品は使った瞬間・使う瞬間だけ触る導線にして、覚える場面を減らす。
  - A3用紙へ連想を全部出し、「大事なことは紙にある」という安心感を注意のブレーキ代わりにする。
  - 生活事務や金融手続きはZoom等をつないで「今ここでやる」同席枠にし、内容は見せすぎず開始合図だけ借りる。
- Note: X/Twitter posts are treated as lived-experience/practical tips only, not medical, financial, or clinical evidence; tweet-derived additions remain low-confidence/source-bound.

## [2026-08-19] ingest | X/Twitter ADHDパワー系ソリューション定期検索 60
- Searches: 4 searches across `Latest` and `Top` products via bird. Deduplicated 77 unique tweet IDs; skipped already-ingested tweets, generic empathy/diagnosis discourse, medical claims without source, duplicates of existing smartphone/timer/reward tactics without new detail, and posts with unnecessary personal detail.
- Created raw sources:
  - `raw/articles/tweet-2090002469308998006-boredom-structured-load-exercise-deadline.md`
  - `raw/articles/tweet-2089934117664436674-mobile-order-forced-outing-deadline.md`
- Updated concept/navigation pages:
  - `concepts/energy-management.md`
  - `concepts/work-routines.md`
  - `concepts/task-initiation.md`
  - `concepts/environment-design.md`
  - `index.md`
- Tip summaries:
  - 暇が休息にならない場合、毎日の運動や締切のある作業など、仕事が担っていた強制構造の代替を低〜中強度で置く。
  - モバイルオーダーを先に入れて、受け取り時刻を外出・作業場所移動の強制締切にする。
- Note: X/Twitter posts are treated as lived-experience/practical tips only, not medical or clinical evidence; tweet-derived additions remain low-confidence/source-bound.


## [2026-08-20] ingest | X/Twitter ADHDパワー系ソリューション定期検索 61
- Searches: 4 searches across `Latest` and `Top` products via bird. Deduplicated 74 unique tweet IDs; skipped already-ingested tweets, generic empathy/diagnosis discourse, stigma/attacks, medical claims without usable source, duplicate timer/smartphone/visible-storage tactics without new detail, and posts with unnecessary personal health detail.
- Created raw sources:
  - `raw/articles/tweet-2090278901255676137-completion-verify-by-state.md`
  - `raw/articles/tweet-2090271623433933188-visible-pending-box.md`
  - `raw/articles/tweet-2090251801463529921-lyrics-free-music-pink-noise.md`
  - `raw/articles/tweet-2090052007751217600-three-start-patterns.md`
  - `raw/articles/tweet-2090091481843532208-cleaning-memory-items-separate-zone.md`
- Updated concept/navigation pages:
  - `concepts/external-memory.md`
  - `concepts/environment-design.md`
  - `concepts/attention-control.md`
  - `concepts/task-initiation.md`
  - `index.md`
- Tip summaries:
  - 完了判定を記憶ではなく状態確認に移す
  - 保留物をラベル付きの見える置き場へ逃がす
  - 歌詞なし音楽＋ピンクノイズで音の境界を作る
  - 着手をミニタスク・人目/締切・開始儀式の3型で作る
  - 片付け中の思い出品は掃除場所から物理的に分ける
- Note: X/Twitter posts are treated as lived-experience/practical tips only, not medical or clinical evidence; tweet-derived additions remain low-confidence/source-bound.

## [2026-08-20] ingest | PubMed research-watch batch: EMA/mind wandering and selected raw-only studies
- Reviewed 5 unprocessed PubMed candidates from `.automation/research-watch/candidates.jsonl`.
- Accepted with page updates: `pubmed:41400041` (EMA, mind wandering, ADHD symptom dimensions, affective valence).
- Accepted raw-only: `pubmed:42152730`, `pubmed:42288756`, `pubmed:41923132`, `pubmed:41055221`.
- Updated concept pages: `concepts/cognitive-personal-informatics.md`, `concepts/attention-control.md`, `concepts/emotion-regulation.md`.
- Created raw sources:
  - `raw/papers/yi-2026-context-dependent-adhd-risk-coupling-commentary.md`
  - `raw/papers/karimi-2026-adolescent-parent-treatment-experiences-adhd.md`
  - `raw/papers/ibilola-2026-guanfacine-prescribing-child-development-service.md`
  - `raw/papers/ain-2026-mind-wandering-affective-valence-adhd-ema.md`
  - `raw/papers/folkins-2026-long-acting-stimulants-academic-outcomes.md`

## [2026-08-20] ingest | 日本の大学入試におけるADHD・発達障害の受験上の配慮
- Created raw source: `raw/articles/jasso-dnc-university-entrance-accommodations-2026-08.md`.
- Updated: `concepts/public-support.md`.
- Evidence: official JASSO case No.2324 confirms an ADHD applicant received a separate room, written instructions, answer checking, and 14-point enlarged plus standard test papers; the supplied briefing also links related JASSO cases and the 2027 Common Test guidance.
- Scope: a source-grounded institutional overview, not individual legal, admissions, or medical advice.

## [2026-08-20] ingest | X/Twitter ADHDパワー系ソリューション定期検索 62
- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; deduplicated by tweet ID and checked existing raw sources/log entries.
- Created raw sources:
  - `raw/articles/tweet-2090334021419196445-voice-ai-slack-daily-review.md`
  - `raw/articles/tweet-2090309711589707975-small-bag-capacity-constraint.md`
- Updated concept/navigation pages:
  - `concepts/external-memory.md`
  - `concepts/environment-design.md`
  - `index.md`
- Tip summaries:
  - 終業時に紙メモを音声入力＋AI要約し、自分宛てSlackへ送り、翌朝に見直して当日タスク化する。
  - バッグを小さくして、不要物が増える容量そのものに物理上限を作る。
- Note: X/Twitter posts are lived-experience/practical tips only, not medical or clinical evidence; additions are source-bound and low-confidence. AI/Slackへ送る内容は最小限にする。

## [2026-08-20] ingest | X/Twitter ADHDパワー系ソリューション定期検索 63
- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; deduplicated by tweet ID and checked existing raw sources/log entries.
- Created raw source:
  - `raw/articles/tweet-2090423617716994431-hide-red-notification-badges.md`
- Updated concept/navigation pages:
  - `concepts/attention-control.md`
  - `index.md`
- Tip summary: 赤い未読バッジを消す・隠すことで、視覚的な割り込みの入口を物理的に減らす。
- Note: X/Twitter投稿は当事者的な実践例であり、医療的・臨床的根拠ではない。追記は出典限定・低信頼度として扱う。

## [2026-08-21] ingest | X ADHD practical-tip search 64
- Searches: 4 Japanese practical-tip searches across Latest and Top via bird; deduplicated 84 unique tweet IDs and checked existing raw sources/log entries.
- Created raw source: raw/articles/tweet-2090578808286200182-active-learning-short-blocks.md
- Updated: concepts/parenting.md; index.md.
- Tip: 子どもの学習を座位に固定せず、1回5〜10分の立位・音読・手書き／描画から選べる「動く学習枠」にする。
- Note: X投稿は家庭での低信頼度な実践例であり、教育的・医療的効果の根拠ではない。

## [2026-08-21] ingest | X ADHD practical-tip search 65
- Searches: 4 Japanese practical-tip searches across Latest and Top via bird; deduplicated candidates by tweet ID and checked existing raw sources/log entries.
- Created raw source: `raw/articles/tweet-2090710501399363893-visual-partition-peripheral-noise.md`.
- Updated: `concepts/environment-design.md`; `index.md`.
- Tip: 卓上パーテーションや棚配置で周辺視野の動きを遮り、作業場所の視覚刺激を減らす。
- Note: 事業所によるX投稿を低信頼度・出典限定の環境調整例として扱い、医療的・臨床的効果の根拠とはしない。


## [2026-08-21] ingest | X ADHD practical-tip search 66
- Searches: 4 Japanese practical-tip searches across Latest and Top via bird; deduplicated by tweet ID and checked existing raw sources/log entries.
- Created raw source: `raw/articles/tweet-2090804780730036357-sessionstart-rule-injection.md`.
- Updated: `entities/i-have-adhd.md`, `index.md`.
- Tip: AIの出力規則をSessionStartで自動注入し、毎回の指示入力をなくす。規則は行動レベルに分解し、安全上の例外と自動実行コードの確認をセットにする。
- Note: X投稿は開発者による実務例であり、医療的・臨床的効果の根拠ではない。第三者プラグインの自動実行は導入前に内容を確認する。

## [2026-08-21] ingest | X ADHD practical-tip search 67
- Searches: 4 Japanese practical-tip searches across Latest and Top via bird; deduplicated 79 unique tweet IDs and checked existing raw sources/log entries.
- Created raw source: `raw/articles/tweet-2090645446649905599-no-agenda-call-body-doubling.md`.
- Updated: `concepts/body-doubling.md`, `index.md`.
- Tip: 作業相談や監督ではなく、雑談・無言を許す「用件なし」の低負荷通話を先に開始し、同席感だけを片付け・洗濯・外出などの着手合図として借りる。
- Note: X投稿は当事者による実践提案であり、医療的・臨床的根拠ではない。投稿内の神経科学的説明は採用せず、内容・画面・音声の共有は最小限にする。

## [2026-08-22] ingest | X ADHD practical-tip search 68
- Searches: 4 Japanese practical-tip searches across Latest and Top via bird; deduplicated candidates by tweet ID and checked existing raw sources/log entries.
- Created raw sources:
  - `raw/articles/tweet-2090765524024332757-bath-fill-kitchen-timer.md`
  - `raw/articles/tweet-2090976487130440023-repeat-instructions-confirm-order.md`
- Updated: `concepts/time-management.md`; `concepts/external-memory.md`; `index.md`.
- Tips: 湯張り開始と同時にキッチンタイマーを起動して完了を音で戻す。複数の口頭指示は復唱して順番を確認し、後から見返せる形に残す。
- Note: X投稿は低信頼度な実践例であり、医療的・臨床的効果の根拠ではない。火気・湯張り設備は安全機能と取扱説明を確認し、職場・学校の指示確認は場のルールに合わせる。

## [2026-08-22] ingest | X ADHD practical-tip search 69
- Searches: 4 Japanese practical-tip searches across Latest and Top via bird; deduplicated candidates by tweet ID and checked existing raw sources/log entries.
- Created raw source: `raw/articles/tweet-2091012485365305802-holiday-first-action-night-before.md`.
- Updated: `concepts/task-initiation.md`.
- Tip: 締切や人目のない休日に止まりやすい時は、前夜に「起きたら最初にする小さな一個」だけを決め、当日の予定全体を組まない。
- Note: X投稿による低信頼度の個人実践であり、医療的・臨床的効果の根拠ではない。

## [2026-08-22] ingest | X ADHD practical-tip search 70
- Searches: 4 Japanese practical-tip searches across Latest and Top via bird; deduplicated candidates by tweet ID and checked existing raw sources/log entries.
- Created raw sources:
  - `raw/articles/tweet-2091150142426505386-follow-up-automation.md`
  - `raw/articles/tweet-2091120949928284489-core-possessions-list.md`
- Updated: `concepts/work-routines.md`, `concepts/environment-design.md`, `concepts/impulsivity-countermeasures.md`, `index.md`.
- Tips: 反復する連絡漏れは、誰に・いつ・何を送るかを決めた小さなフォローアップ自動化へ移す。所有物の一軍リストを先に決め、物量と衝動購入の入口を絞る。
- Note: X投稿は低信頼度の当事者／実務実践であり、医療的・臨床的根拠ではない。自動連絡は誤送信・個人情報に注意し、物の処分は不可逆な判断を急がない。

## [2026-08-22] ingest | X ADHD practical-tip search 71
- Searches: 4 Japanese practical-tip searches across Latest and Top via bird; deduplicated candidates by tweet ID and checked existing raw sources/log entries.
- Created raw source: `raw/articles/tweet-2091003209934619022-dense-trash-bins-laundry-transfer.md`.
- Updated: `concepts/environment-design.md`, `index.md`.
- Tip: ごみが出る生活動線へゴミ箱を高密度に置き、洗濯物の大量移動はきれいな運搬より摩擦の低い運び方を優先する。
- Note: X投稿は低信頼度な当事者の家庭内実践例であり、医療的・臨床的効果の根拠ではない。共有空間の衛生・安全と衣類の破損に配慮する。

## [2026-08-23] ingest | X ADHD practical-tip search 72
- Searches: 4 Japanese practical-tip searches across Latest and Top via bird; deduplicated candidates by tweet ID and checked existing raw sources/log entries.
- Created raw sources:
  - `raw/articles/tweet-2091438166284906541-batch-housework-large-baskets.md`
  - `raw/articles/tweet-2091408866466754801-spare-time-task-menu.md`
- Updated: `concepts/environment-design.md`, `concepts/time-management.md`, `index.md`.
- Tips: 毎日維持ではなく、まとめて家事を戻せる大かご・容量を先に用意する。空白時間には5分・15分・30分別の候補リストを作り、休憩も選択肢に入れる。
- Note: X投稿は低信頼度の個人実践であり、医療的・臨床的効果の根拠ではない。家事の滞留には衛生・害虫・安全の閾値を別途置く。

## [2026-08-23] ingest | X ADHD practical-tip search 73
- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; deduplicated 76 unique tweet IDs and checked existing raw sources/log entries.
- Created raw source: `raw/articles/tweet-2091465476341960817-remote-work-artificial-scaffolding.md`.
- Updated: `concepts/work-routines.md`, `concepts/body-doubling.md`, `index.md`.
- Tip: 在宅の始業では、開始時刻の短い宣言、機密を共有しない低負荷な作業通話、着替え、仕事用／休息用の場所分離を一組の「人工的な足場」として先に作る。
- Note: X投稿は低信頼度の個人実践であり、医療的・臨床的根拠ではない。作業通話は監視や機密共有を目的にせず、共有する情報を最小限にする。

## [2026-08-23] ingest | X ADHD practical-tip search 74
- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; deduplicated candidates by tweet ID and checked existing raw sources/log entries.
- Created raw sources:
  - `raw/articles/tweet-2091551619934830743-spare-shoes-at-destination.md`
  - `raw/articles/tweet-2091433622880629062-super-single-task-physical-friction.md`
- Updated: `concepts/forgetfulness-countermeasures.md`, `concepts/attention-control.md`, `index.md`.
- Tips: 使用場所に予備を常備して、持ち出し忘れの被害を止める。スマホを電源オフで手の届かない所へ置き、ブラウザを閉じて作業アプリだけを開き、脱線先を先に消す。
- Note: X投稿は低〜中信頼度の個人実践であり、医療的・臨床的根拠ではない。予備の保管可否・衛生を確認し、連絡を断つ集中法では緊急時の代替連絡手段を確保する。

## [2026-08-24] ingest | X ADHD practical-tip search 75
- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; deduplicated candidate tweet IDs and checked existing raw sources/log entries.
- Created raw source: `raw/articles/tweet-2091723111896883238-three-minute-permission-start.md`.
- Updated: `concepts/task-initiation.md`, `index.md`.
- Tip: ゲームを始めるハードルには、コントローラーを手に取るだけを開始条件にし、「3分でやめてよい」という退出条件を先に置く。
- Note: X投稿は低信頼度の個人実践であり、医療的・臨床的根拠ではない。

## [2026-08-24] ingest | PubMed research-watch batch: EMA, thought dynamics, university self-esteem
- Reviewed 5 unprocessed candidates from `.automation/research-watch/candidates.jsonl`.
- Accepted with page updates: `pubmed:40118952` (thought content variability and context), `pubmed:40933806` (daily activities and self-esteem in university students), `pubmed:35882042` (EMA symptom monitoring in adolescents).
- Accepted raw-only: `pubmed:40191073` (small feasibility study of wearable/EMA outburst measurement in young children).
- Skipped as duplicate existing raw source: `pubmed:30981195`.
- Created raw sources:
  - `raw/papers/raffaelli-2025-thought-content-variability-adhd-context.md`
  - `raw/papers/turner-2025-daily-activities-self-esteem-university-adhd.md`
  - `raw/papers/singh-2025-ema-emotional-dysregulation-outbursts-youth-adhd.md`
  - `raw/papers/kennedy-2024-ema-perceived-adhd-symptoms-adolescents.md`
- Updated concept pages: `concepts/cognitive-personal-informatics.md`, `concepts/attention-control.md`, `concepts/emotion-regulation.md`, `concepts/digital-adhd-support.md`.

## [2026-08-24] ingest | X ADHD practical-tip search 76
- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; deduplicated candidate tweet IDs and checked existing raw sources/log entries.
- Created raw source: `raw/articles/tweet-2091775011078259125-emotion-switch-timer-movement.md`.
- Updated: `concepts/emotion-regulation.md`, `index.md`.
- Tip: 感情が強い時は10分だけ扱うタイマーを先に置き、その後に散歩・ストレッチなど軽い身体活動へ移って切り替えの足場を作る。
- Note: X投稿は低信頼度の個人実践であり、医療的・臨床的効果の根拠ではない。強い苦痛や危険がある場合は生活ハックだけで抱えない。

## [2026-08-24] ingest | X ADHD practical-tip search 77
- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; deduplicated candidate tweet IDs and checked existing raw sources/log entries.
- Created raw source: `raw/articles/tweet-2091963783891857438-schedule-at-day-edges-waiting-mode.md`.
- Updated: `concepts/waiting-mode.md`, `index.md`.
- Tip: 予定を午前の最初または一日の最後へ寄せ、中間の待機時間を減らすことで、予定前に他の作業へ入りにくい状態を小さくする。
- Note: X投稿は低信頼度の個人実践であり、ADHDに固有の認知機構や効果を示す医学的根拠ではない。

## [2026-08-25] ingest | X ADHD practical-tip search 78
- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; deduplicated 75 candidate tweet IDs and checked existing raw sources/log entries.
- Created raw sources:
  - `raw/articles/tweet-2092082789831352332-immediate-capture-calendar-multi-device-reminders.md`
  - `raw/articles/tweet-2092069372609351942-rotating-routine-return-path.md`
- Updated: `concepts/external-memory.md`, `concepts/work-routines.md`, `index.md`.
- Tips: 依頼を即時に一つの入力先へ入れ、朝昼夜の確認と複数端末通知で再提示する。通知が背景化したら場所・道具・表示方法を替え、途切れても戻れる経路を残す。
- Note: X投稿は低信頼度の個人実践であり、医療的・臨床的効果の根拠ではない。

## [2026-08-25] ingest | X ADHD practical-tip search 79
- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; deduplicated candidate tweet IDs and checked existing raw sources/log entries.
- Created raw source: `raw/articles/tweet-2092235566654050763-preemptive-food-reminder.md`.
- Updated: `concepts/external-memory.md`, `index.md`.
- Tip: 作業に入り込む前提で、昼・夕方のアラームと手元ですぐ取れる選択肢を用意し、内的な気づきに依存しない。
- Note: X投稿は低信頼度の個人実践であり、食事・健康についての医療的助言や効果の根拠ではない。

## [2026-08-26] ingest | X ADHD practical-tip search 80
- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; deduplicated candidate tweet IDs and checked existing raw sources/log entries.
- Created raw sources:
  - `raw/articles/tweet-2092440259871359148-estimate-double-rule.md`
  - `raw/articles/tweet-2092446947265405087-schedule-change-reset.md`
- Updated: `concepts/time-management.md`, `index.md`.
- Tips: 所要時間の予測値へ固定倍率を掛けて予定を組む。急な予定変更では変更を短くメモし、「今やること」を一つへ縮約して、タイマー・指差し確認・必要時の他者への共有で次の行動へ切り替える。
- Note: X投稿は低信頼度の個人実践であり、医学的・心理学的効果の根拠ではない。

## [2026-08-26] ingest | X ADHD practical-tip search 81
- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; deduplicated candidates by tweet ID and checked existing raw sources/log entries.
- Created raw source: `raw/articles/tweet-2092573234235691486-current-action-five-minute-todo.md`.
- Updated: `concepts/digital-adhd-support.md`, `concepts/task-initiation.md`, `index.md`.
- Tip: ToDo画面から残件数・サブタスクを外し、「今やること」と手を動かした秒数だけを中心に置き、5分を既定の集中単位にする。
- Note: X投稿と添付画像に基づく低信頼度の開発中アプリ案であり、医療的・臨床的効果や製品仕様を示す根拠ではない。

## [2026-08-26] ingest | X ADHD practical-tip search 82
- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; deduplicated candidates by tweet ID and checked existing raw sources/log entries.
- Created raw source: `raw/articles/tweet-2092721738421506108-bag-attached-sports-gear.md`.
- Updated: `concepts/forgetfulness-countermeasures.md`, `index.md`.
- Tip: 持参物を手で持たずバッグへ安全に固定し、バッグを持つ一動作へ統合して、出発時の置き忘れ経路を減らす。
- Note: X投稿は低信頼度の個人実践であり、医療的・臨床的効果の根拠ではない。固定の安全性、周囲への接触、学校・職場の規則を確認する。

## [2026-08-27] ingest | Research-watch machine-readable candidates
- Reviewed 5 unprocessed candidates from `.automation/research-watch/candidates.jsonl`.
- Accepted raw sources:
  - `raw/papers/lidstrom-holmqvist-2026-lgo-time-management-rct.md` — adult/clinical time-management pragmatic RCT.
  - `raw/papers/goh-2026-adhd-internalizing-college-time-series.md` — college ADHD/internalizing day-to-day time-series study.
  - `raw/papers/micic-2026-delayed-sleep-wake-phase-disorder-review.md` — DSWPD review with ADHD/autism/anxiety/depression comorbidity note.
  - `raw/papers/ma-2026-clinical-phenotypes-chinese-children-adhd.md` — child ADHD phenotype/nursing pathway study; raw-only due lower adult-support fit.
- Updated wiki pages: `concepts/time-management.md`, `concepts/emotion-regulation.md`, `concepts/comorbidity.md`, `concepts/sleep.md`.
- State-only duplicate: `pubmed:37775284` already existed as `raw/papers/pubmed-adhd-ema-daily-life-adolescents-2026.md`.

## [2026-08-27] ingest | X ADHD practical-tip search 83
- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; deduplicated candidate tweet IDs and checked existing raw sources/log entries.
- Created raw source: `raw/articles/tweet-2092924129762775308-google-calendar-single-source-auto-sync.md`.
- Updated: `concepts/external-memory.md`, `concepts/digital-adhd-support.md`, `index.md`.
- Tip: 予定を一つのカレンダーへ集約し、メール・予約サイトの自動連携と複数端末での確認を使って、手入力・二重登録・情報の分散を減らす。AI補助の予定内容は本人が確認する。
- Note: X投稿は低信頼度の個人実践であり、医療的・臨床的効果やカレンダー／AIの正確性を示す根拠ではない。予定データの共有・連携範囲に注意する。

## [2026-08-28] ingest | X ADHD practical-tip search 84
- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; deduplicated candidates by tweet ID and checked existing raw sources/log entries.
- Created raw source: `raw/articles/tweet-2092912888398983634-work-structure-ten-hacks.md`.
- Updated: `concepts/work-routines.md`, `index.md`.
- Tip: 退屈な仕事の前の短い運動、デスクリセット、当日A4 ToDo、逆算マイルストーン、資料余白メモ、指示の即時テキスト化、通知・メール・割り込みの制限を、一組の仕事環境として運用する。
- Note: X投稿は当事者の職場実践であり、医療的・臨床的根拠ではない。既存のタイマー、外部記憶、注意制御、品質ゲートの実装例を束ねる低信頼度の出典限定メモとして扱う。

## [2026-08-28] ingest | X ADHD practical-tip search 85
- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; deduplicated candidate tweet IDs and checked existing raw sources/log entries.
- Created raw sources:
  - `raw/articles/tweet-2093212482261127618-numbered-checklist-audit-trail.md`
  - `raw/articles/tweet-2093172638063493366-five-minute-launch-only.md`
- Updated: `concepts/work-routines.md`, `concepts/task-initiation.md`, `index.md`.
- Tips: チェックリストは項目番号・項目別の合否・空欄を残して未確認を可視化し、同じ確認を再実行可能にする。着手が重い活動は「5分だけ起動して閉じる」ことを許可し、継続要求を外して入口だけ通す。
- Note: X投稿は低信頼度の個人実践であり、医療的・臨床的効果の根拠ではない。

## [2026-08-28] ingest | X ADHD practical-tip search 86
- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; candidates were deduplicated by tweet ID and checked against raw sources and the recent log.
- Created raw source: `raw/articles/tweet-2093441419050704993-exit-conditions-hyperfocus.md`.
- Updated: `concepts/hyperfocus-control.md`; `index.md` already listed this existing concept and was current as of 2026-08-28.
- Tip: 過集中へ入る前に「時間・量・行動段階」の複数の終了条件を置き、どれか一つで止まれたら成功とする。終了後には15分の余白を予定する。
- Note: X投稿は低信頼度の個人実践であり、医療的・臨床的効果の根拠ではない。投稿内の研究言及は原典照合していない。

## [2026-08-29] ingest | X ADHD practical-tip search 87
- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; candidates were deduplicated by tweet ID and checked against raw sources and recent log entries.
- Created raw sources:
  - `raw/articles/tweet-2093615514149073332-ai-photo-task-triage.md`
  - `raw/articles/tweet-2093591982216019999-failure-mode-separate-log.md`
- Updated: `concepts/task-initiation.md`, `concepts/external-memory.md`, `concepts/work-routines.md`, `index.md`.
- Tips: 写真・紙からAIに「最初の5分」「タスク／メモ」「日付・期限・行動」を限定抽出させ、推測は不明とする。失敗を一括集計せず、工程・発生段階ごとの型へ分け、型ごとに点検箇所を変える。
- Note: X投稿は低信頼度の個人実践であり、医療的・臨床的根拠ではない。画像・書類をAIに入れる場合は個人情報・機密情報を最小化し、サービスのデータ取扱いを確認する。

## [2026-08-29] ingest | X ADHD practical-tip search 88
- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; candidates were deduplicated by tweet ID and checked against raw sources and log entries.
- Created raw source: `raw/articles/tweet-2093713787690135865-notion-ai-action-buttons.md`.
- Updated: `concepts/digital-adhd-support.md`, `concepts/task-initiation.md`. `index.md` required no entry change because no page was created and it was already current as of 2026-08-29.
- Tip: タスク画面を「開始／完了／今日／明日／AI依頼」の少数ボタンへ縮約し、背景・完了条件を置いたうえでAI依頼へ進めることで、整理・選択・操作の摩擦を減らす。
- Note: X投稿は低信頼度の個人実践であり、医療的・臨床的根拠ではない。AI連携へ職場・個人・第三者の機微情報を入れすぎない。

## [2026-08-30] ingest | X ADHD practical-tip search 89
- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; candidate tweet IDs were deduplicated and checked against existing raw sources and log entries.
- Created raw source: `raw/articles/tweet-2093896497696027037-weekly-envelope-opening-window.md`.
- Updated: `concepts/task-initiation.md`, `index.md`.
- Tip: 封筒を開く・読む・対応する工程を分け、週1回などの固定した短時間枠では「開封だけ」を目的にして、書類への着手摩擦を下げる。
- Note: X投稿は低信頼度の個人実践であり、医療的・臨床的効果の根拠ではない。期限・支払いのある書類は到着時に期限を外部記憶へ登録し、固定枠を待たない。

## [2026-08-30] ingest | X ADHD practical-tip search 90
- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; candidate tweet IDs were deduplicated and checked against existing raw sources and log entries.
- Created raw source: `raw/articles/tweet-2093999960966775126-notion-ai-task-specification.md`.
- Updated: `concepts/digital-adhd-support.md`, `concepts/task-initiation.md`, `concepts/external-memory.md`. `index.md` required no entry change because no page was created and it was already current as of 2026-08-30.
- Tip: 思いつきだけを入力し、AIに背景・目的、検討の方向、必要な成果物、完了条件をタスクへ整形・登録させる。後で開いた時の「何をどこまでやるか」の再構成を減らす。
- Note: X投稿は低信頼度の個人実践であり、医療的・臨床的効果の根拠ではない。クラウドAIへ渡す記事・業務・第三者情報を最小化し、AI生成の仕様・タスク登録を本人が確認する。

## [2026-08-30] ingest | X ADHD practical-tip search 91
- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; candidate tweet IDs were deduplicated and checked against existing raw sources and log entries.
- Created raw sources:
  - `raw/articles/tweet-2093918695684964637-questify-tasks.md`
  - `raw/articles/tweet-2093987135791452312-shopping-checkpoint-read-aloud.md`
- Updated: `concepts/task-initiation.md`, `concepts/forgetfulness-countermeasures.md`, `index.md`.
- Tips: 調子のよい時にタスクをクエスト名・小さな完了条件・即時フィードバックで設計する。買い物はスマホのチェックボックスを商品投入時に切り替え、出口で残項目を音読する。
- Note: X投稿は低信頼度の個人実践であり、医療的・臨床的効果の根拠ではない。投稿内の研究言及は独立に検証していない。

## [2026-08-31] ingest | X ADHD practical-tip search 92
- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; candidate tweet IDs were deduplicated and checked against existing raw sources and log entries.
- Created raw source: `raw/articles/tweet-2094276615593234715-specific-needs-chat-instructions.md`.
- Updated: `concepts/work-routines.md`, `index.md`.
- Tip: 診断名だけでなく、困りごとと代替手段を短文で伝える。例として、口頭指示が残りにくい時はチャットで受け取り、後から確認できる形へ変える。
- Note: X投稿は低信頼度の個人実践であり、医療的・臨床的効果の根拠ではない。診断名の開示は必須ではなく、開示範囲・職場制度・相手との関係は本人が選ぶ。

## [2026-08-31] ingest | Research-watch digital CBT, EMA/JITAI, mindfulness, Cog-Fun-A, and VR review
- Reviewed 5 unprocessed machine-readable candidates from `.automation/research-watch/candidates.jsonl`.
- Accepted 5 for raw + existing page updates (score 3); created no new wiki pages.
- Created raw sources:
  - `raw/papers/damelio-2026-attexis-digital-cbt-adult-adhd-rct.md` — adult ADHD pragmatic RCT of fully self-guided digital CBT/mindfulness adjunct.
  - `raw/papers/koch-2021-e-diaries-adhd-jitai-review.md` — e-diary/EMA and just-in-time adaptive intervention review.
  - `raw/papers/mitchell-2017-mindfulness-adult-adhd-pilot-trial.md` — adult ADHD mindfulness pilot trial.
  - `raw/papers/velder-shukrun-2026-cog-fun-a-adult-adhd-case-series.md` — adult ADHD Cog-Fun-A extreme case series.
  - `raw/papers/single-2025-immersive-vr-cognitive-rehabilitation-adhd-review.md` — immersive VR cognitive rehabilitation systematic review.
- Updated wiki pages: `concepts/digital-adhd-support.md`, `concepts/cognitive-behavioural-therapy.md`, `concepts/cognitive-personal-informatics.md`, `concepts/executive-function.md`, `concepts/emotion-regulation.md`, `concepts/assistive-technology.md`, `index.md`.
- Updated automation state: `.automation/research-watch/curation-state.json`.
- Note: digital CBT/VR/mindfulness claims are source-bound evidence summaries, not personal medical advice. Cog-Fun-A is a 3-case analysis; e-diary/JITAI sources are design/research infrastructure and require privacy/monitoring cautions.

## [2026-08-31] ingest | X ADHD practical-tip search 93
- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; candidate tweet IDs were deduplicated and checked against existing raw sources and log entries.
- Created raw source: `raw/articles/tweet-2094319526531768709-ai-start-task-observation.md`.
- Updated: `concepts/task-initiation.md`. `index.md` required no entry change because no page was created and its navigation remains current.
- Tip: 「5分だけ」も始められない時は、AIに作業の細分化と最初の処理を依頼し、出力を見ながら本人が確認・参加する。業務・第三者・個人情報の入力は最小化する。
- Note: X投稿は低信頼度の個人実践であり、医療的・臨床的効果の根拠ではない。AIの出力・操作は本人が確認する。

## [2026-08-31] ingest | X ADHD practical-tip search 94
- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; candidate tweet IDs were deduplicated and checked against existing raw sources and log entries.
- Created raw source: `raw/articles/tweet-2094436315047793087-external-interruption-hyperfocus.md`.
- Updated: `concepts/hyperfocus-control.md`. `index.md` required no entry change because no page was created and its navigation remains current.
- Tip: 過集中の前に、同意のある通話・予定・確認など外部から一度中断が入る条件を設計し、切り上げ判断を環境側へ出す。
- Note: X投稿は知人についての又聞きで、低信頼度の個人実践であり、医療的・臨床的効果の根拠ではない。周囲の集中、同意、勤務ルールを損なわない範囲で扱う。

## [2026-09-01] ingest | X ADHD practical-tip search 95
- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; candidates were deduplicated by tweet ID and checked against existing raw sources and log entries.
- Created raw source: `raw/articles/tweet-2094715646240030882-repair-system-commitment.md`.
- Updated: `concepts/work-routines.md`. `index.md` required no entry change because no page was created and its navigation remains current.
- Tip: ミス後は「気をつけます」だけで閉じず、提出前チェック日時・締切前アラーム・同意済みの短い相互確認など、次回に入れた仕組みを一つ具体的に伝える。
- Note: X投稿は低信頼度の個人実践であり、医療的・臨床的効果の根拠ではない。相互確認は相手の時間・機密・職場ルールを尊重する。

## [2026-09-01] ingest | X ADHD practical-tip search 96
- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; deduplicated 82 candidate tweet IDs and checked existing raw sources and log entries.
- Created raw source: `raw/articles/tweet-2094773017733955723-action-buttons-ai-workflow.md`.
- Updated: `concepts/external-memory.md`, `concepts/digital-adhd-support.md`.
- Index: no new page was created; the existing concept entries remain current.
- Tip: タスクを記録で終わらせず、「今日／明日／開始／AI依頼／完了」を同じ画面の少数ボタンで遷移させ、背景・完了条件つきで作業・進捗表示へつなぐことで、記憶・再発見・転記の中間工程を減らす。
- Note: X投稿は低信頼度の個人実践であり、医療的・臨床的効果の根拠ではない。AI・Slack連携へ送る業務・個人・第三者情報は最小限にし、出力・送信・閲覧権限を本人が確認する。

## [2026-09-01] ingest | X ADHD practical-tip search 97
- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; candidate tweet IDs were deduplicated and checked against existing raw sources and log entries.
- Created raw source: `raw/articles/tweet-2094915706408300816-repeat-immediate-note.md`.
- Updated: `concepts/work-routines.md`. `index.md` required no entry change because no page was created and its navigation remains current.
- Tip: 口頭指示は内容・期限を復唱しながら即時に記録し、聞き違いの確認と後から参照できる外部記憶を同時に作る。
- Note: X投稿は低信頼度の個人実践であり、医療的・臨床的効果の根拠ではない。職場での記録は、許可されたメモ手段と情報管理ルールに従う。

## [2026-09-02] ingest | X ADHD practical-tip search 98
- Searches: 4 Japanese practical-tip searches across Latest and Top via bird; 75 candidate tweet IDs were deduplicated and compared with existing raw tweet sources.
- Created raw sources:
  - raw/articles/tweet-2094556336491307078-one-minute-reward-task-start.md
  - raw/articles/tweet-2093896186273071116-precommitment-external-structure.md
- Updated concept pages:
  - concepts/task-initiation.md
  - concepts/work-routines.md
- Updated index.md metadata; no page was created, so its catalog entries remain unchanged.
- Tips: 一日の最初に1分で終えられる好きな作業を置き、小さな完了から起動する。調子のよい時に締切・同意済みの約束・小さな自動化を設定して、未来の自分の意志力だけに依存しない。
- Note: X投稿は低信頼度の個人実践であり、医療的・臨床的効果の根拠ではない。相手を巻き込む約束と自動化は、負担・同意・情報管理を確認する。

## [2026-09-02] ingest | X ADHD practical-tip search 99
- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; candidate tweet IDs were deduplicated and compared with existing raw tweet sources and log entries.
- Created raw source: `raw/articles/tweet-2095178111294046677-total-time-visualization-game.md`.
- Updated concept pages: `concepts/time-management.md`, `concepts/task-initiation.md`.
- Index: no new page was created; the catalog entries remain current.
- Tip: 嫌な仕事を箇条書きに分け、各所要時間と合計を先に見える化して、終わりの不明な仕事を有限のゲームへ変える。見積もりは実測で補正する。
- Note: X投稿は低信頼度の個人実践であり、医療的・臨床的効果の根拠ではない。

## [2026-09-02] ingest | X ADHD practical-tip search 100
- Searches: 4 Japanese practical-tip searches across Latest and Top via bird; candidate tweet IDs were deduplicated and compared with existing raw tweet sources and log entries.
- Created raw source: raw/articles/tweet-2095278344183099400-ai-single-intake-now-three.md.
- Updated concept pages: concepts/digital-adhd-support.md, concepts/task-initiation.md.
- Updated index: index.md summary for digital-adhd-support.
- Tip: 用件を一つの入力口へ集め、AIに分類・5分粒度への分解をさせ、UIには「今やる3つ」だけを出して選択肢と判断コストを減らす。
- Note: X投稿は低信頼度の個人開発・実践であり、医療的・臨床的効果の根拠ではない。AI同期では業務・家族・第三者情報を最小化し、保存期間・閲覧権限を確認する。

## [2026-09-03] ingest | X ADHD practical-tip search 101
- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; deduplicated 76 candidate tweet IDs and compared candidates with existing raw tweet sources and log entries.
- Created raw source: `raw/articles/tweet-2095346052744311160-exit-ritual-two-stage-warning.md`.
- Updated: `concepts/hyperfocus-control.md`, `index.md`.
- Tip: 終了時刻をタイマーで外部化し、「あと5分」→「今終わり」の二段階予告、タブを閉じる・通知を切る・机上を一つ片づける短い終了儀式、次行動への移行をセットにする。
- Note: X投稿は低信頼度の個人実践であり、医療的・臨床的効果の根拠ではない。

## [2026-09-03] ingest | Research-watch adult EMA and raw-only child/transition/VR protocol candidates

- Reviewed 5 unprocessed candidates from `.automation/research-watch/candidates.jsonl`.
- Accepted 1 for raw + existing page updates (score 3): Murray et al. (2021), adult EMA study linking ADHD symptoms, emotional lability, and internalising symptoms.
- Accepted 4 for raw-only (score 2): child music-based occupational therapy RCT, youth online self-reflective meditation RCT, adolescence-to-adulthood transition commentary, and adult real-vs-virtual nature/VR protocol with no outcome data yet.
- Created raw sources:
  - `raw/papers/erarslan-2026-music-occupational-therapy-child-adhd-rct.md`
  - `raw/papers/lee-2026-online-self-reflective-meditation-youth-adhd-rct.md`
  - `raw/papers/murray-2021-ema-emotional-dysregulation-adult-adhd-internalising.md`
  - `raw/papers/buitelaar-2017-adhd-transition-adolescence-adulthood-commentary.md`
  - `raw/papers/zhang-2026-real-virtual-nature-adult-adhd-protocol.md`
- Updated concept/navigation/state pages:
  - `concepts/emotion-regulation.md`
  - `concepts/cognitive-personal-informatics.md`
  - `.automation/research-watch/curation-state.json`
- Note: child/youth and protocol/commentary sources were kept raw-only to avoid overgeneralising. EMA findings are source-bound and not medical advice.

## [2026-09-03] ingest | X ADHD practical-tip search 102
- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; candidates were deduplicated by tweet ID and checked against existing raw tweet sources and log entries.
- Created raw source: `raw/articles/tweet-2095384585760886934-setlog-hourly-photo-log.md`.
- Updated: `concepts/cognitive-personal-informatics.md`, `index.md`.
- Tip: 1時間ごとの通知を時間境界の合図にし、その時点の行動を素早く記録して時刻つきで振り返る。写真・行動ログは記録範囲・共有先・保持期間を限定し、他者の監視用途にしない。
- Note: X投稿は低信頼度の個人実践であり、医療的・臨床的効果の根拠ではない。

## [2026-09-04] ingest | X ADHD practical-tip search 103
- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; deduplicated candidates by tweet ID and compared them with existing raw tweet sources and log entries.
- Created raw source: `raw/articles/tweet-2095712203920007318-reduce-startup-steps-timer-cue.md`.
- Updated: `concepts/task-initiation.md`, `index.md`.
- Tip: 開始までの連続工程を数えて前日配置で削り、最初の行動を「座る」だけに近づける。開始の催促は人の声でなく固定タイマーへ置く。
- Note: X投稿は低信頼度の個人実践であり、医療的・臨床的効果の根拠ではない。

## [2026-09-04] ingest | X ADHD practical-tip search 104
- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; candidates were deduplicated by tweet ID and checked against raw tweet sources and the wiki log.
- Created raw source: `raw/articles/tweet-2095646354387374409-detailed-procedure-externalization.md`.
- Updated: `concepts/working-memory.md`, `index.md`.
- Tip: 作業手順を再開できる粒度まで外部化し、自分用メモ・引き継ぎ・AIへの依頼で「詳細な手順」を明示して中間工程の省略を減らす。
- Note: X投稿は低信頼度の個人実践であり、医学的・臨床的効果の根拠ではない。

## [2026-09-04] ingest | X ADHD practical-tip search 105
- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; candidates were deduplicated by tweet ID and checked against raw tweet sources and the wiki log.
- Created raw source: `raw/articles/tweet-2095878027540566484-reminders-checklist-ai-review.md`.
- Updated: `concepts/work-routines.md`, `index.md`.
- Tip: 失念・確認漏れ・先延ばし・情報整理を、リマインダー、チェックリスト、2日前締切、AIによる第二確認・整理へ一対一で対応づけ、注意力に頼らない。
- Note: X投稿は低信頼度の個人実践であり、医学的・臨床的効果の根拠ではない。AI入力は最小化し、出力・送信は本人が確認する。

## [2026-09-05] ingest | X ADHD practical-tip search 106
- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; candidates were deduplicated by tweet ID and checked against raw tweet sources and the wiki log.
- Created raw source: `raw/articles/tweet-2096096736410513679-nightly-cutoff-residual-review.md`.
- Updated: `concepts/work-routines.md`, `index.md`.
- Tip: 当日リストを夜の固定時刻で締め、残件は翌朝の紙へ移す。残件を工程状態で分け、同じ項目が3日続く時にだけ工程・通知・分担の仕組みを点検する。
- Note: X投稿は低信頼度の個人実践であり、医学的・臨床的効果の根拠ではない。

## [2026-09-05] ingest | X ADHD practical-tip search 107
- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; 76 candidate tweet IDs were deduplicated and compared with existing raw tweet sources and log entries.
- Created raw source:
  - `raw/articles/tweet-2096176512861089838-interruption-resumption-anchor.md`
- Updated concept pages:
  - `concepts/work-routines.md`
  - `concepts/task-resumption.md`
- Updated navigation:
  - `index.md`
- Tip: 電話当番を時間で分け、集中枠を中断されにくい場所へ置き、避けられない電話の直前には「今の行」または次操作を一行で残して作業再開の手がかりにする。職場の合意と機密情報の扱いを確認する。
- Note: X投稿は低信頼度の個人実践であり、医学的・臨床的効果の根拠ではない。

## [2026-09-05] ingest | X ADHD practical-tip search 108
- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; 136 candidate tweet IDs were deduplicated and compared with existing raw tweet sources and recent log entries.
- Created raw source:
  - `raw/articles/tweet-2096243519094698287-process-separated-workspaces.md`
- Updated concept/navigation pages:
  - `concepts/work-routines.md`
  - `index.md`
- Tip: 工程ごとに机・トレー・棚などの作業場所を分け、前工程の道具を片付けてから次へ移る切替コストと、机上で工程が混ざる状態を減らす。
- Note: X投稿は低信頼度の個人実践であり、医学的・臨床的効果の根拠ではない。投稿者の自己記載の健康情報は実践案の理解に不要なため保存しない。共有空間では占有範囲・安全・他者との合意を確認する。

## [2026-09-06] ingest | X ADHD practical-tip search 109
- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; candidates were deduplicated by tweet ID and compared with existing raw tweet sources and recent log entries.
- Created raw source:
  - `raw/articles/tweet-2096603229073359309-smart-assistant-wearable-prompts.md`
- Updated wiki pages:
  - `concepts/external-memory.md`
  - `index.md`
- Tip: Alexaやスマートウォッチに、必要な時刻だけ次の行動を具体的な音声・振動の指示として出させ、想起を端末側へ移す。通知過多を避けるため、対象と時刻は少数に絞る。
- Note: X投稿は低信頼度の個人実践であり、医学的・臨床的効果の根拠ではない。

## [2026-09-06] ingest | X ADHD practical-tip search 110
- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; 75 candidate tweet IDs were deduplicated and compared with existing raw tweet sources and recent log entries.
- Created raw sources:
  - `raw/articles/tweet-2096730096388419918-task-song-working-memory.md`
  - `raw/articles/tweet-2096728311825383505-bath-exit-cleaning-routine.md`
- Updated concept/navigation pages:
  - `concepts/external-memory.md`
  - `concepts/environment-design.md`
  - `index.md`
- Tips: 短い歌・リズムで次の行動を口ずさみ、想起を支える。入浴の出口に浴室掃除をつなぎ、重い掃除を小さな維持作業へ分割する。
- Note: X投稿は低信頼度の個人実践であり、医学的・臨床的効果の根拠ではない。浴室掃除では転倒・洗剤・同居者との分担に注意する。

## [2026-09-07] ingest | X ADHD practical-tip search 111
- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; candidates were deduplicated by tweet ID and checked against raw tweet sources and recent log entries.
- Created raw sources:
  - `raw/articles/tweet-2096796555894239274-external-watchdog-reminders.md`
  - `raw/articles/tweet-2096780493052162239-game-feedback-task-design.md`
- Updated concept/navigation pages:
  - `concepts/external-memory.md`
  - `concepts/task-initiation.md`
  - `index.md`
- Tips: 頭内の「やらなきゃ」を付箋・アラームへ移して外部の割り込みにする。作業は小さな完了、短いタイマー、完了報告への即時反応を組み合わせ、ゲームの明確なゴールとフィードバックを借りる。
- Note: X投稿は低信頼度の個人実践であり、医学的・臨床的効果の根拠ではない。通知・報告が負担になる場合は量を減らすか使わない。


## [2026-09-07] ingest | Research-watch college EMA, service access, and neurodiversity design candidates

- Reviewed 5 unprocessed candidates from `.automation/research-watch/candidates.jsonl`.
- Accepted 3 for raw + existing page updates (score 3) and 2 for raw-only (score 2); created no new wiki pages.
- Created raw sources:
  - `raw/papers/goh-2026-day-to-day-adhd-stress-college-ema.md` — college-student EMA/network study on ADHD symptoms and perceived stress
  - `raw/papers/australia-2026-adhd-assessment-treatment-access-quality.md` — service/policy argument on ADHD assessment access and diagnostic quality in Australia
  - `raw/papers/beaux-2024-guiding-empowerment-model-neurodiversity-online-higher-ed.md` — neurodiversity/online higher-education HCI design framework
  - `raw/papers/baillargeon-2024-neurodiversity-social-computing-review.md` — raw-only CSCW neurodiversity framing review
  - `raw/papers/web-barkley-parent-training-caregiver-burden-child-adhd-rct.md` — raw-only web Barkley parent-training RCT for mothers of children with ADHD
- Updated concept/navigation/state pages:
  - `concepts/cognitive-personal-informatics.md`
  - `concepts/emotion-regulation.md`
  - `concepts/diagnosis-and-management.md`
  - `concepts/public-support.md`
  - `concepts/digital-adhd-support.md`
  - `concepts/assistive-technology.md`
  - `index.md`
  - `.automation/research-watch/curation-state.json`
- Note: EMA findings are observational and source-bound; Australian service recommendations are jurisdiction-specific policy arguments; HCI/neurodiversity design sources are not clinical efficacy evidence.

## [2026-09-07] ingest | X practical ADHD tips: visual transition timer and waiting-time task line

- Searched X with both Latest and Top products; deduplicated results and skipped generic, medical, hostile, or already-ingested posts.
- Created raw sources:
  - `raw/articles/tweet-2097086508268437838-visual-timer-transition.md` — a household experience using a Time Timer's shrinking color area to show a child the remaining 10 minutes before a transition.
  - `raw/articles/tweet-2097047045827854683-waiting-time-single-task-line.md` — a workplace practice splitting cooling/soaking waits into time-stamped, short follow-up tasks so the worker need not retain the pending step.
- Updated:
  - `concepts/time-management.md`
  - `concepts/work-routines.md`
  - `index.md`
- Note: both sources are public individual experiences, retained as low-confidence practical examples rather than medical or clinical evidence; workplace safety, hygiene, and equipment procedures take precedence.

## [2026-09-08] ingest | X ADHD practical-tip search 112
- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; 77 unique tweet IDs were deduplicated and checked against existing raw tweet sources and log entries.
- Created raw source:
  - `raw/articles/tweet-2097176422943269130-sixty-point-work-boundaries.md`
- Updated concept/navigation pages:
  - `concepts/work-routines.md`
  - `index.md`
- Tip: 朝10分で当日の対象を絞り、イレギュラー用の余白と終業時刻を先に固定して、微調整の無限化・休息の圧迫を防ぐ。
- Note: X投稿は低信頼度の個人実践であり、医学的・臨床的効果の根拠ではない。余白や終業時刻は職場の締切・安全・労務ルールに合わせる。

## [2026-09-09] ingest | X ADHD practical-tip search 113
- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; 73 unique tweet IDs were deduplicated and checked against existing raw tweet sources and log entries.
- Created raw source:
  - `raw/articles/tweet-2097448673500090516-next-morning-one-task.md`
- Updated concept/navigation pages:
  - `concepts/task-initiation.md`
  - `index.md`
- Tip: 就寝前に翌朝の最初の一件だけを書き、順番待ちのタスクを朝の視界から分離して、優先順位決定の負荷を先送りしない。
- Note: X投稿は低信頼度の個人実践であり、医学的・臨床的効果の根拠ではない。

## [2026-09-09] ingest | X ADHD practical-tip search 114
- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; results were deduplicated and checked against existing raw tweet sources and log entries.
- Created raw source:
  - `raw/articles/tweet-2097555987599409210-shopping-choice-constraint.md`
- Updated concept page:
  - `concepts/impulsivity-countermeasures.md`
- Navigation: `index.md` was reviewed; no page was created or removed, so its current 2026-09-09 catalog required no content change.
- Tip: 普段使いの買い物先を、予定外の商品を見続けにくい小規模店などへ寄せ、購入候補と比較の入口を物理的に絞る。
- Note: X投稿は低信頼度の個人実践であり、医学的・経済的効果の根拠ではない。必要品の入手性、価格、移動負担を確認する。

## [2026-09-09] ingest | X ADHD practical-tip search 115
- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; candidates were deduplicated by tweet ID and checked against existing raw tweet sources and log entries.
- Created raw source:
  - `raw/articles/tweet-2097596147644973231-cleaning-exit-boundary.md`
- Updated concept/navigation pages:
  - `concepts/environment-design.md`
  - `index.md` reviewed; the existing `[[environment-design]]` catalog entry remains valid and no page was created or removed.
- Tip: 掃除は開始前に範囲・15分の終了時刻・脱線した場所のメモ先を決め、タイマーで途中でも終える。大掃除化を注意力ではなく境界条件で止める。
- Note: X投稿は低信頼度の個人実践であり、医学的・臨床的効果の根拠ではない。

## [2026-09-09] ingest | X ADHD practical-tip search 116
- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; tweet IDs were deduplicated and checked against existing raw sources and log entries.
- Created raw source:
  - `raw/articles/tweet-2097590989254778998-work-structure-five-scaffolds.md`
- Updated concept/navigation pages:
  - `concepts/work-routines.md`
  - `index.md`
- Tip: 中断の多い職場では、指示を一度に詰め込まない、作業を見える化する、優先順位と順番を固定する、ミス後の復旧手順を用意することで、注意力への要求を仕事の構造へ移す。
- Note: X投稿は低信頼度の個人実践であり、医学的・臨床的効果の根拠ではない。職場の安全、業務品質、就業規則を優先する。
## [2026-09-10] ingest | Research-watch short-form video engagement trap

- Reviewed 5 unprocessed candidates from `.automation/research-watch/candidates.jsonl`.
- Accepted 1 for raw + existing page update (score 3): Misirlic et al. (2026), “Quantifying the Engagement Trap: Impact of Short-form Video Recommender Systems on Users with ADHD”.
- Marked 4 low-priority/duplicate candidates as state-only: already-ingested arXiv neurodiversity demographics, pictogram reading support, cognitive personal informatics workshop; broad Global Burden of Disease mental-disorder burden paper.
- Created raw source:
  - `raw/papers/misirlic-2026-engagement-trap-short-form-video-adhd.md`
- Updated concept/navigation/state pages:
  - `concepts/digital-interruptions.md`
  - `index.md`
  - `.automation/research-watch/curation-state.json`
- Note: short-form video findings are self-reported survey evidence, not clinical advice. Proposed design features were hypothetical and should be treated as accessibility design candidates, not proven interventions.

## [2026-09-10] ingest | X ADHD practical-tip search 117
- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; candidates were deduplicated by tweet ID and checked against existing raw tweet sources and log entries.
- Created raw sources:
  - `raw/articles/tweet-2097922517012807747-bag-dedicated-spares.md`
  - `raw/articles/tweet-2098019180717150590-ai-report-omission-check.md`
- Updated concept/navigation pages:
  - `concepts/forgetfulness-countermeasures.md`
  - `concepts/work-routines.md`
  - `index.md` reviewed; no page was created or removed, and its catalog was already current on 2026-09-10.
- Tip summaries:
  - 通勤バッグ用の充電器・イヤホンは取り出さず、自宅用を別にして、持ち出し・戻し・探索の工程を消す。
  - 報告書の仮文をAIに要約させ、「誰が・いつ・何を・どうしたか」の抜けを第二確認する。ただし機密・個人情報は入力せず、最終確認は本人が行う。
- Note: X投稿は低信頼度の個人実践であり、医学的・臨床的効果の根拠ではない。AI利用は業務の情報管理規則を優先する。

## [2026-09-10] ingest | X ADHD practical-tip search 118
- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; candidates were deduplicated by tweet ID and checked against existing raw tweet sources and log entries.
- Created raw source:
  - `raw/articles/tweet-2098012610939551918-recommended-tab-blocker.md`
- Updated concept/navigation pages:
  - `concepts/digital-interruptions.md`
  - `index.md` reviewed; the existing `[[digital-interruptions]]` catalog entry remains current because no page was created or removed.
- Tip: Xのおすすめタブを隠す／閲覧前に別行動を挟む拡張機能で、無限スクロールの入口へ摩擦を置く。
- Note: X投稿は低信頼度の個人実践であり、医学的・臨床的効果の根拠ではない。拡張機能は権限・データ収集・提供元を確認してから使う。

## [2026-09-11] ingest | X ADHD practical-tip search 119
- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; candidates were deduplicated by tweet ID and checked against existing raw tweet sources and log entries.
- Created raw sources:
  - `raw/articles/tweet-2098248383131742565-body-doubling-call-start.md`
  - `raw/articles/tweet-2098236586634698991-automate-small-recurring-work.md`
- Updated concept/navigation pages:
  - `concepts/task-initiation.md`
  - `concepts/work-routines.md`
  - `index.md`
- Tip summaries:
  - 片付け・洗濯・外出の前に、同意を得た相手との通話を先につなぎ、人の存在を着手の外部合図にする。
  - 大きな自動化ではなく、時刻・場所・手順が固定された反復工程を、当日中に置換できる小単位から自動化する。
- Note: X投稿は低信頼度の個人実践であり、医学的・臨床的効果の根拠ではない。通話時のプライバシー、自動化の安全・品質・情報管理を優先する。

## [2026-09-11] ingest | X ADHD practical-tip search 120
- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; 74 results were deduplicated by tweet ID, then checked against existing raw tweet sources and log entries.
- Created raw sources:
  - `raw/articles/tweet-2098377263515611607-memo-workflow-design.md`
  - `raw/articles/tweet-2098305680851738724-work-system-q-and-a.md`
- Updated concept/navigation pages:
  - `concepts/external-memory.md`
  - `concepts/work-routines.md`
  - `index.md`
- Tip summaries:
  - メモを取ること自体で終えず、受け取り・記録・見返し・実行のどこで詰まるかを分け、一項目ずつの伝達、文書併用、共有メモ、見返し時刻で運用を組む。
  - 気が散る端末を視界外へ置き、最初の一つ・固定手順・都度参照するマニュアル・極小の開始単位・戻り先を組み合わせ、仕事を意志でなく仕組みで回す。
- Note: X投稿は低信頼度の個人実践であり、医学的・臨床的効果の根拠ではない。職場の安全、品質、就業規則、録音・共有時の同意と情報管理を優先する。

## [2026-09-11] ingest | X ADHD practical-tip search 121
- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; 76 results were deduplicated by tweet ID and checked against existing raw tweet sources and recent log entries.
- Created raw source:
  - `raw/articles/tweet-2098427170293174738-work-rotation-visible-schedule.md`
- Updated concept/navigation pages:
  - `concepts/work-routines.md`
  - `index.md` reviewed; the existing `[[work-routines]]` catalog entry remains current because no page was created or removed.
- Tip: 短い時間ごとの作業ローテーションと事前掲示の配置表で、飽きへの対処と次の工程・準備の外部化を組み合わせる。
- Note: X投稿は低信頼度の個人実践であり、医学的・臨床的効果の根拠ではない。勤務の安全、休憩、健康配慮、配置変更は職場の規則と管理者・専門職の判断を優先する。


## [2026-09-12] ingest | X ADHD practical-tip search 122
- Searches: 4 Japanese practical-tip searches across Latest and Top via bird; 72 results were deduplicated by tweet ID and checked against existing raw tweet sources and recent log entries.
- Created raw source:
  - raw/articles/tweet-2098787980903366929-bathroom-body-doubling.md
- Updated concept/navigation pages:
  - concepts/body-doubling.md
  - index.md
- Tip: 入浴などの開始が重い生活動作を、同意した相手と「今から始める」のDMで同時開始し、内容を共有せずに同席感だけを借りる。
- Note: X投稿は低信頼度の個人実践であり、医学的・臨床的効果の根拠ではない。相手の同意、映像・音声・私生活情報を共有しないことを優先する。

## [2026-09-13] ingest | X ADHD practical-tip search 123
- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; candidates were deduplicated by tweet ID and checked against existing raw tweet sources and log entries.
- Created raw source:
  - `raw/articles/tweet-2098723132941140012-calendar-commitment-deadline.md`
- Updated concept/navigation pages:
  - `concepts/work-routines.md`
  - `index.md` reviewed; the existing `[[work-routines]]` catalog entry remains current because no page was created or removed.
- Tip: 口約束で終えず、その場でカレンダーへ入れ、必要な相手を巻き込んだ締切に変換して、記憶と後日の意欲に頼らない。
- Note: X投稿は低信頼度の個人実践であり、医学的・臨床的効果の根拠ではない。相手を巻き込む範囲、通知、個人・業務情報の扱いは本人の同意と職場規則を優先する。

## [2026-09-13] ingest | X ADHD practical-tip search 124
- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; results were deduplicated by tweet ID and checked against existing raw tweet sources and log entries.
- Created raw source:
  - `raw/articles/tweet-2099112005122904219-failure-system-repair.md`
- Updated concept/navigation pages:
  - `concepts/work-routines.md`
  - `index.md`
- Tip: ミスを人格評価で反すうせず、失敗の型に対応する外部支えを一つだけ置く（確認漏れならチェックリスト、遅刻なら着替え開始アラーム）。対策が決まったら振り返りを終える。
- Note: X投稿は低信頼度の個人実践であり、医学的・臨床的効果の根拠ではない。


## [2026-09-14] ingest | X ADHD practical-tip search 125
- Searches: 4 Japanese practical-tip searches across Latest and Top via bird; results were deduplicated by tweet ID and checked against existing raw tweet sources and log entries.
- Created raw source:
  - raw/articles/tweet-2099081656707527123-accountability-practice-community.md
- Updated concept/navigation pages:
  - concepts/body-doubling.md
  - index.md
- Tip: 「定期的な会話・最小限の進捗確認・質問先・同じく実践する人・手を動かす予定」を組にして、1対1の伴走または実践型コミュニティから継続の外部構造を借りる。共有範囲・頻度・費用・離脱方法は先に決め、監視にしない。
- Note: X投稿は低信頼度の個人実践であり、医学的・臨床的効果の根拠ではない。

## [2026-09-14] ingest | X ADHD practical-tip search 126
- Searches: 4 Japanese practical-tip searches across Latest and Top via bird; 80 results were deduplicated to 77 tweet IDs and checked against existing raw tweet sources and log entries.
- Created raw source:
  - raw/articles/tweet-1207620544314499079-action-bundling.md
- Updated concept/navigation pages:
  - concepts/environment-design.md
  - index.md reviewed; the existing [[environment-design]] catalog entry remains current because no page was created or removed.
- Tip: 給水など既に動ける行動に、ゴミを一つ持つような小タスクを一つだけ束ね、別途の開始判断を減らす。
- Note: X投稿は低信頼度の個人実践であり、医学的・臨床的効果の根拠ではない。

## [2026-09-14] ingest | X ADHD practical-tip search 127
- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; 80 results were deduplicated to 76 tweet IDs and checked against existing raw tweet sources and log entries.
- Created raw source:
  - `raw/articles/tweet-2099467139925381507-work-brief-clarification.md`
- Updated concept/navigation pages:
  - `concepts/work-routines.md`
  - `index.md` reviewed; the existing catalog entry remains current because no page was created or removed.
- Tip: 曖昧な仕事依頼は着手前に「誰が読むか・何を決めるか・どのくらいの量か」の3点だけ確認し、目的・読み手・分量を外部化する。
- Note: X投稿は低信頼度の個人実践であり、医学的・臨床的効果の根拠ではない。


## [2026-09-15] ingest | X ADHD practical-tip search 128
- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; 79 results were deduplicated to 73 tweet IDs and checked against existing raw tweet sources and log entries.
- Created raw source:
  - `raw/articles/tweet-1740389109255020660-subject-zip-file.md`
- Updated concept/navigation pages:
  - `concepts/forgetfulness-countermeasures.md`
  - `index.md`
- Tip: 教科ごとにジッパーファイルを一つ用意し、教科書・ノート・配布プリントを同居させる。保管先と出し入れの工程を一単位にして、プリントの紛失を減らす学生生活の個人実践。
- Note: X投稿は低信頼度の個人実践であり、医学的・臨床的効果の根拠ではない。

## [2026-09-15] ingest | X ADHD practical-tip search 129
- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; results were deduplicated by tweet ID and checked against existing raw tweet sources and recent log entries.
- Created raw source:
  - `raw/articles/tweet-2099711846999851500-intra-day-deadlines.md`
- Updated concept/navigation pages:
  - `concepts/time-management.md`
  - `index.md` reviewed; its existing [[time-management]] entry and current date remain accurate, so no catalog text change was needed.
- Tip: ジムや事務などの日中の固定予定を先に時間ブロックし、その予定までに一つの作業を終える短い締切を複数作る。長時間だらだら続ける代わりに、外部の予定で終了境界を置く個人実践。
- Note: X投稿は低信頼度の個人実践であり、医学的・臨床的効果の根拠ではない。

## [2026-09-15] ingest | X ADHD practical-tip search 130
- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; 80 results were deduplicated to 77 tweet IDs and checked against existing raw tweet sources and recent log entries.
- Created raw sources:
  - `raw/articles/tweet-2099803252510646601-compassionate-progress-checkins.md`
  - `raw/articles/tweet-2099828632717795561-ai-output-noun.md`
- Updated concept pages:
  - `concepts/task-initiation.md`
  - `concepts/digital-adhd-support.md`
- Navigation: `index.md` reviewed; it already has the current date and lists both updated concept pages, so no catalog text change was needed.
- Tips:
  - 最終締切だけでなく、合意した中間締切と責めない進捗確認を置き、着手のきっかけを外部化する。
  - AIを開く前に、その回で残す成果物を「比較表」など一つの名詞で決め、選択肢の増加によるフリーズを抑える。
- Note: X投稿は低信頼度の個人実践であり、医学的・臨床的効果の根拠ではない。

## [2026-09-16] ingest | X ADHD practical-tip search 131
- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; results were deduplicated by tweet ID and checked against existing raw tweet sources and recent log entries.
- Created raw sources:
  - `raw/articles/tweet-2099974128094629924-one-action-storage-decisions.md`
  - `raw/articles/tweet-2099844764455915801-tasque-single-task-course.md`
- Updated concept/navigation pages:
  - `concepts/environment-design.md`
  - `concepts/task-initiation.md`
  - `index.md`
- Tips:
  - 物量、定位置、収納の操作数をまとめて減らし、片付けで毎回必要になる判断を減らす。
  - タスクを順番付きのコースにして一件ずつ進め、同時に扱う対象と選択肢を制限する。
- Note: X投稿は低信頼度の個人実践／開発中ツールの投稿であり、医学的・臨床的効果の根拠ではない。

## [2026-09-16] ingest | X ADHD practical-tip search 132
- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; deduplicated by tweet ID and checked against existing raw tweet sources and recent log entries.
- Created raw source:
  - `raw/articles/tweet-2100027391599124957-timer-start-is-complete.md`
- Updated concept/navigation pages:
  - `concepts/task-initiation.md`
  - `index.md`
- Tip: 作業完了ではなくタイマー開始ボタンを今回の完了条件にして、着手直前の抵抗を極小化する。
- Note: X投稿は低信頼度の個人実践であり、医学的・臨床的効果の根拠ではない。

## [2026-09-16] ingest | X ADHD practical-tip search 133
- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; results were deduplicated by tweet ID and checked against existing raw tweet sources and recent log entries.
- Created raw sources:
  - `raw/articles/tweet-2100199521862971514-visible-timer-basket-clear-storage.md`
  - `raw/articles/tweet-2100199522286641337-hooks-keyreel-spares-notes-laundry-net.md`
- Updated concept pages:
  - `concepts/environment-design.md`
  - `concepts/external-memory.md`
  - `concepts/time-management.md`
- Navigation: `index.md` reviewed; existing catalog entries already cover the updated concepts, so no catalog text change was needed.
- Tips:
  - 回して残量が見えるタイマー、透明収納、放り込みかごで、時間・物・分類を頭で保持しない。
  - フック、キーリール、場所別ケーブル、出口の大判付箋、洗濯ネットで、探す・忘れる・畳む工程を物理的に減らす。
- Note: X投稿は低信頼度の個人実践であり、医学的・臨床的効果の根拠ではない。

## [2026-09-16] ingest | X ADHD practical-tip search 134
- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; deduplicated candidates by tweet ID and checked against existing raw tweet sources and log entries.
- Created raw source:
  - `raw/articles/tweet-2099762658509742550-file-spine-alignment-check.md`
- Updated concept/navigation pages:
  - `concepts/careless-mistake-countermeasures.md`
  - `index.md`
- Tip: 紙ファイルの背表紙をまたぐ一本線を確認用の外部手がかりにし、戻し間違い・ファイル欠落を棚の見た目で検知する。
- Note: X投稿は低信頼度の個人実践であり、医学的・臨床的効果の根拠ではない。

## [2026-09-17] ingest | X ADHD practical-tip search 135
- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; results were deduplicated by tweet ID and checked against existing raw tweet sources and recent log entries.
- Created raw source:
  - `raw/articles/tweet-2100163865195774193-priority-time-block-choice.md`
- Updated concept/navigation pages:
  - `concepts/time-management.md`
  - `index.md`
- Tip: 締切がないが大切な活動には定時枠を先に確保し、その枠の具体的な活動には選択の余地を残す。
- Note: X投稿は動画紹介を含む低信頼度の実践情報として保存し、医学的・臨床的効果の根拠としては扱わない。

## [2026-09-17] ingest | X ADHD practical-tip search 136
- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; candidates were deduplicated by tweet ID and checked against existing raw tweet sources and recent log entries.
- Created raw source:
  - `raw/articles/tweet-2100450302587756727-camera-checklist-app.md`
- Updated concept/navigation pages:
  - `concepts/forgetfulness-countermeasures.md`
  - `concepts/external-memory.md`
  - `index.md` reviewed; its existing catalog entries cover the updated concepts and the date is already current.
- Tip: 出発前に持ち物をカメラへ見せ、リストとの照合を使うことで、「持ったはず」という記憶ではなく実物提示で確認する。
- Note: X投稿上の製品紹介に基づく低信頼度の実践候補であり、アプリの精度・データ取扱いと医学的・臨床的効果は未検証。

## [2026-09-17] ingest | Research-watch low-score OTMP/EMA and raw-only background candidates

- Reviewed 5 unprocessed machine-readable candidates from `.automation/research-watch/candidates.jsonl`; all had low `score_hint`, so curation stayed conservative.
- Accepted 2 for raw + existing page updates (score 3):
  - `pubmed:42521366` — school-based Organizational Skills Training-Tier 2 subgroup/mediation RCT; updated `concepts/time-management.md`.
  - `pubmed:24827866` — EMA of smoking antecedents/consequences in adults with ADHD; updated `concepts/cognitive-personal-informatics.md`.
- Accepted 3 as raw-only background sources (score 2):
  - `pubmed:42275393` — HOPS organization/time-management/planning protocol for youth.
  - `pubmed:36200275` — broad technology and mental health assessment/treatment review.
  - `arxiv:2508.09680v1` — autistic software-engineering employment pathways systematic review.
- Created raw sources:
  - `raw/papers/nissley-tsiopinis-2026-school-ost-t2-organizational-skills.md`
  - `raw/papers/mitchell-2014-ema-smoking-adults-adhd.md`
  - `raw/papers/langberg-2026-hops-organization-planning-youth-protocol.md`
  - `raw/papers/harvey-2022-technology-mental-health-review.md`
  - `raw/papers/patlolla-2025-inclusive-employment-pathways-autistic-software-engineering.md`
- Updated wiki/state files:
  - `.automation/research-watch/curation-state.json`
  - `concepts/cognitive-personal-informatics.md`
  - `concepts/time-management.md`
  - `log.md`
- Note: child/school and smoking/substance-use findings are source-bound, not medical advice; raw-only background sources were not promoted into wiki prose to avoid scope creep.

## [2026-09-18] ingest | X/Twitter ADHD practical routine thread

- Searched Japanese practical ADHD posts with both `Latest` and `Top`; deduplicated tweet IDs and skipped generic, medical, and already-ingested posts.
- Created raw source:
  - `raw/articles/tweet-2100745448470581531-externalize-daily-routine-thread.md`
- Updated concept/navigation pages:
  - `concepts/forgetfulness-countermeasures.md`
  - `concepts/time-management.md`
  - `concepts/task-initiation.md`
  - `concepts/environment-design.md`
  - `index.md`
- Tip: 必需品を一体化・一ポーチ化して持ち替えを一回にし、タスクは発生時に即入力、朝に順番化、予定は一回だけの直前アラーム、見つけやすさ・こぼれにくさを道具の仕様へ移す。
- Note: 公開Xスレッド由来の低信頼度な当事者実践メモであり、医療的エビデンスや個別助言ではない。

## [2026-09-18] ingest | X ADHD practical-tip search 137
- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; results were deduplicated by tweet ID and checked against existing raw tweet sources and recent log entries.
- Created raw sources:
  - `raw/articles/tweet-2100945829511242141-work-failsafe-layers.md`
  - `raw/articles/tweet-2100876468205350915-early-arrival-forced-workspace.md`
- Updated concept/navigation pages:
  - `concepts/work-routines.md`
  - `concepts/waiting-mode.md`
  - `index.md` reviewed; its existing catalog entries cover the updated concepts and already carry the current date, so no catalog text change was needed.
- Tips:
  - 仕事のミスは注意の反復ではなく、時刻固定・アラーム・チェックリスト・完了記録・必要時の相互確認という工程別の防御層へ変える。
  - 予定前の待機で止まりやすい時は、十分早く現地近くへ移動し、待機場所の制約を短い作業枠として使う。
- Note: X投稿は低信頼度の個人／実務実践であり、医学的・臨床的効果の根拠ではない。職場の安全・品質・機密・役割分担、移動時の安全と体力を優先する。

## [2026-09-19] ingest | X/Twitter ADHD practical-tip search 138
- Searches: 4 Japanese practical-tip searches across `Latest` and `Top`; deduplicated tweet IDs and checked against existing raw sources and log entries.
- Created raw sources:
  - `raw/articles/tweet-2101098958066235676-holding-box-scheduled-review.md`
  - `raw/articles/tweet-2100887835536728329-ai-forgetfulness-planning-prompt.md`
- Updated concept/navigation pages:
  - `concepts/environment-design.md`
  - `concepts/forgetfulness-countermeasures.md`
  - `index.md`
- Tips:
  - 片付けの判断で止まる物は保留箱へ移し、投入日とカレンダー上の見直し日をセットにする。
  - 予定別の忘れ物対策をAIへ整理させる時は、重要物に絞った短いリストにし、入力情報と生成内容を利用者が確認する。
- Note: X投稿は低信頼度の個人／実務実践であり、医学的・臨床的効果の根拠ではない。AI利用時は第三者・予定情報の最小化と結果確認を優先する。

## [2026-09-19] ingest | X/Twitter ADHD practical-tip search 139
- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; deduplicated tweet IDs and checked against existing raw sources and recent log entries.
- Created raw source:
  - `raw/articles/tweet-2101257651875385502-five-minute-research-cutoff.md`
- Updated concept page:
  - `concepts/task-initiation.md`
- Navigation: `index.md` was reviewed; it already listed the updated concept and had the current date, but its binary detection prevented a safe targeted catalog-summary edit.
- Tip: 下調べや比較で止まりやすい時は、最初の5分だけを可視タイマーで区切り、終了を実作業へ移る合図にする。安全・品質・法令順守に必要な確認は短縮しない。
- Note: X投稿は低信頼度の個人実践であり、医学的・臨床的効果の根拠ではない。

## [2026-09-19] ingest | X/Twitter ADHD practical-tip search 140
- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; deduplicated tweet IDs and checked against existing raw sources and recent log entries.
- Created raw source:
  - `raw/articles/tweet-2101389739467358289-parroting-processing-buffer.md`
- Updated concept page:
  - `concepts/relationships.md`
- Navigation: `index.md` was reviewed; it already lists `[[relationships]]`, carries the current date, and its one-line description already covers the page's practical communication content, so no catalog text change was needed.
- Tip: 突然の呼びかけで理解が追いつかない時は、反射的な聞き返しを短いオウム返しに置き換え、確認と数秒の処理待ちを同時につくる。
- Note: X投稿は低信頼度の個人実践であり、医学的・臨床的効果の根拠ではない。重要な依頼や聞き取れない内容は改めて確認する。

## [2026-09-20] ingest | X/Twitter ADHD practical-tip search 141
- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; deduplicated tweet IDs and checked candidates against existing raw sources and log entries.
- Created raw sources:
  - `raw/articles/tweet-2101476437824094313-fridge-photo-shopping-list.md`
  - `raw/articles/tweet-2101415020555071755-waiting-mode-scheduled-chain.md`
- Updated concept/navigation pages:
  - `concepts/external-memory.md`
  - `index.md`
- Tips:
  - 文字の買い物リストを見ない場合、出発前の冷蔵庫写真を店で見て不足品を照合する。
  - 予定前の待機で止まりやすい場合、重い予定の前後を考えなくてよい固定タスクで連結して一日の流れを作る。
- Note: X投稿は低信頼度の個人／実務実践であり、医学的・臨床的効果の根拠ではない。予定連鎖は費用、体力、移動安全、予定変更への余白を確認して使う。

## [2026-09-20] ingest | X/Twitter ADHD practical-tip search 142
- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; deduplicated tweet IDs and checked candidates against existing raw sources and log entries.
- Created raw source:
  - `raw/articles/tweet-2101446239904739716-written-instructions-immediate-note.md`
- Updated concept page:
  - `concepts/working-memory.md`
- Navigation: `index.md` was reviewed; it already lists `[[working-memory]]` and carries the current date. A targeted catalog edit was not applied because the file is detected as binary, avoiding an unsafe whole-file rewrite.
- Tip: 複数の口頭指示は、チャット等の文面でもらうか、その場で短くメモして、後から確認できる記録にする。
- Note: X投稿は低信頼度の個人実践であり、医学的・臨床的効果の根拠ではない。投稿内の認知機能に関する一般化や数値は採用していない。

## [2026-09-20] ingest | X/Twitter ADHD practical-tip search 143
- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; deduplicated tweet IDs and checked candidates against existing raw sources and recent log entries.
- Created raw source:
  - `raw/articles/tweet-2101634940576350210-keyword-notes-immediate-reconstruction.md`
- Updated concept page:
  - `concepts/working-memory.md`
- Navigation: `index.md` was reviewed; it already lists `[[working-memory]]` and has the current date. It remains binary-detected, so no unsafe whole-file or targeted edit was made.
- Tip: 会話中は文章で整えずに単語だけを記録し、終了直後の約30秒で行動項目・確認事項へ補う。
- Note: X投稿は低信頼度の個人実践であり、医学的・臨床的効果の根拠ではない。投稿の認知機能に関する数値・一般化と登録導線は採用していない。重要な内容は文面確認または正式記録を優先する。

## [2026-09-20] ingest | X/Twitter ADHD practical-tip search 144
- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; candidates were deduplicated by tweet ID and checked against existing raw sources and log entries.
- Created raw source:
  - `raw/articles/tweet-1798367137691767210-background-video-morning-prep.md`
- Updated concept/navigation pages:
  - `concepts/task-initiation.md`
  - `index.md`
- Tip: 朝の支度で始められない時、内容に没入しない程度の一定の背景動画・音声を開始儀式にし、支度へ入る抵抗を下げる。音が注意を奪う場合や安全確認が要る場面には使わない。
- Note: X投稿は低信頼度の個人実践であり、医学的・臨床的効果の根拠ではない。

## [2026-09-21] ingest | X/Twitter ADHD practical-tip search 145
- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; candidates were deduplicated by tweet ID and checked against existing raw sources and log entries.
- Created raw source:
  - `raw/articles/tweet-2101574868051562964-start-switch-resumption-plus-one.md`
- Updated concept page:
  - `concepts/task-initiation.md`
- Navigation: `index.md` was reviewed but remains binary-detected, so no unsafe whole-file or targeted catalog edit was made; it already lists `[[task-initiation]]`.
- Tip: 固定の開始儀式で重い仕事への入口を作り、中断時は再開地点を一行残し、積み上がる雑務は「発生分＋一つ」だけ処理して少しずつ減らす。
- Note: X投稿は低信頼度の個人実践であり、医学的・臨床的効果の根拠ではない。優先順位・安全・締切が必要な作業には、適切な手順を優先する。

## [2026-09-21] ingest | Research-watch AI copresence for developers with ADHD

- Reviewed 5 unprocessed candidates from `.automation/research-watch/candidates.jsonl`.
- Accepted 1 for raw + existing page updates (score 3); skipped/state-only 4 low-fit candidates.
- Created raw source:
  - `raw/papers/pimenova-2026-ai-copresence-developers-adhd.md` — Pimenova et al. (2026), "Two's a Crowd: Human and AI-Based Copresence for Developers with ADHD".
- Updated concept/navigation/state files:
  - `concepts/body-doubling.md`
  - `concepts/digital-adhd-support.md`
  - `concepts/work-routines.md`
  - `concepts/task-initiation.md`
  - `index.md`
  - `.automation/research-watch/curation-state.json`
- Skipped/state-only: `pubmed:41955613`, `pubmed:41621352`, `pubmed:42147856`, `arxiv:2506.00142v1`.
- Note: AI copresence findings are qualitative HCI/software-work evidence, not clinical treatment evidence. Privacy, workplace confidentiality, and human verification boundaries were kept explicit.

## [2026-09-21] ingest | X/Twitter ADHD practical-tip search 146
- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; candidates were deduplicated by tweet ID and checked against existing raw sources and recent log entries.
- Created raw source:
  - `raw/articles/tweet-2101869056492024174-multimodal-document-review.md`
- Updated concept/navigation pages:
  - `concepts/careless-mistake-countermeasures.md`
  - `index.md`
- Tip: 文書・メールの検品は、時間を空ける／表示を変える／読み上げる／数字・日付・宛名・添付だけの短いリストを使う、と別経路に分ける。重要文書は守秘・権限を守った相互レビューを追加する。
- Note: X投稿は低信頼度の個人実践であり、医学的・臨床的効果の根拠ではない。機密情報を読み上げサービスや第三者へ渡さず、組織のレビュー手順・期限を優先する。

## [2026-09-21] ingest | X/Twitter ADHD practical-tip search 147
- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; candidates were deduplicated by tweet ID and checked against existing raw sources and recent log entries.
- Created raw sources:
  - `raw/articles/tweet-2101993844363428297-completion-time-declaration.md`
  - `raw/articles/tweet-1785314213579358457-sticker-checklist.md`
  - `raw/articles/tweet-1785316048423780680-completed-tasks-bold-mark.md`
- Updated concept/navigation pages:
  - `concepts/work-routines.md`
  - `concepts/task-initiation.md`
  - `concepts/external-memory.md`
  - `index.md`
- Tips: 完璧主義で止まりやすい仕事には完了時刻を先に宣言して終了条件にする。付箋型チェックリストでは、完了項目を太いマーカーで消して進捗の累積を見える化する。
- Note: X投稿は低信頼度の個人実践であり、医学的・臨床的効果の根拠ではない。公式締切・品質・安全確認を省略せず、投稿の短縮URLは未展開のまま保存した。

## [2026-09-21] ingest | X/Twitter ADHD practical-tip search 148
- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; candidates were deduplicated by tweet ID and checked against existing raw sources and recent log entries.
- Created raw source:
  - `raw/articles/tweet-2101946280499195997-three-turn-day.md`
- Updated concept pages:
  - `concepts/time-management.md`
  - `concepts/work-routines.md`
- Navigation: `index.md` was reviewed; it already lists both concepts and is dated 2026-09-21. Its binary detection prevented a safe targeted catalog-summary edit, so no unsafe whole-file rewrite was made.
- Tip: 一日を朝・昼・夜など3区画に先に分け、実働目標を2区画だけに限定する。終わりが見える有限の作業枠にし、残りは休息・生活・予備として残す。
- Note: X投稿は低信頼度の個人実践であり、医学的・臨床的効果の根拠ではない。勤務・休憩・安全上の制約を優先し、休息を削る用途にはしない。

## [2026-09-22] ingest | X/Twitter ADHD practical-tip search 149
- Searches: 4 Japanese practical-tip searches across Latest and Top via bird; candidates were deduplicated by tweet ID and checked against existing raw sources and recent log entries.
- Created raw source:
  - raw/articles/tweet-2102224363311247676-output-quality-gate-monitoring.md
- Updated concept/navigation pages:
  - concepts/work-routines.md
  - index.md
- Tip: 予定枠で出力がない時は、成果物がないのか、成果物はあるが検品・承認済みの印がないのかを分けて記録し、最初に欠けた工程を点検する。
- Note: X投稿は低信頼度の個人実践であり、医学的・臨床的効果の根拠ではない。品質・安全・承認の正式手順を優先する。

## [2026-09-22] ingest | X/Twitter ADHD practical-tip search 150
- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; candidates were deduplicated by tweet ID and checked against existing raw sources and recent log entries.
- Created raw source:
  - `raw/articles/tweet-2102231421649821933-study-physical-lock-sprints-location.md`
- Updated concept/navigation pages:
  - `concepts/task-initiation.md`
  - `index.md`
- Tip: 学習を図解へ置き換え、端末の物理的制約、30分の短い学習枠、期間ごとの場所替えを組み合わせて、着手・注意維持の条件を環境側へ移す。
- Note: X投稿は低信頼度の個人実践であり、医学的・臨床的効果の根拠ではない。端末制約は本人の同意、必要な連絡手段、安全、プライバシーを優先する。

## [2026-09-22] ingest | X/Twitter ADHD practical-tip search 151
- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; candidates were deduplicated by tweet ID and checked against existing raw sources and recent log entries.
- Created raw sources:
  - `raw/articles/tweet-2102381451782263236-specification-external-memory.md`
  - `raw/articles/tweet-2102371115855155680-transit-alarm-focus-fire-timer.md`
- Updated concept pages:
  - `concepts/external-memory.md`
  - `concepts/time-management.md`
- Navigation: `index.md` was reviewed; it already lists both concept pages. It remains binary-detected by the file editor, so no unsafe whole-file rewrite was made.
- Tips:
  - 仕事では背景・目的・次の作業・完了条件を仕様書へ残し、脱線後も文脈を頭から復元せず再開する。
  - 乗り過ごし対策は降車2駅前のアラーム、移動中の調べ物の遮断、火気開始時のタイマーを組み合わせる。火気は通常の安全手順と安全機能を優先する。
- Note: X投稿は低信頼度の個人実践であり、医学的・臨床的効果の根拠ではない。

## [2026-09-22] ingest | X/Twitter ADHD practical-tip search 152
- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; 79 unique tweet IDs were deduplicated and checked against existing raw tweet files.
- Created raw sources:
  - `raw/articles/tweet-2102323500656857376-ten-task-initiation-tips.md`
  - `raw/articles/tweet-2102354471778931115-five-parenting-environment-settings.md`
- Updated concept pages:
  - `concepts/task-initiation.md`
  - `concepts/environment-design.md`
- Navigation: `index.md` was reviewed. No new page was created, and it already catalogs both updated concepts; the file remains binary-detected by editor tools, so no unsafe whole-file rewrite was made.
- Tips:
  - 着手は最初の一手を極小化し、前日の途中停止・既存習慣への接続・終了時刻／退出条件／低い初稿品質を先に決めて、開始を長時間や完璧さから切り離す。
  - 子どもの家庭内の摩擦は、一動作の大きな受け皿、声かけの代わりの音の合図、帰宅後のクールダウン、ゲーム終了の移行儀式、10分だけの宿題枠へ環境側から移す。
- Note: X投稿は低信頼度の個人・事業者由来の実践であり、医学的・臨床的効果の根拠ではない。家庭向けの工夫は本人の感覚特性、年齢、学校要件、同意、安全を優先する。

## [2026-09-23] ingest | X/Twitter ADHD practical-tip search 153
- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; candidates were deduplicated by tweet ID and checked against existing raw sources and recent log entries.
- Created raw source:
  - `raw/articles/tweet-2102585706229240143-iphone-notion-shortcuts-capture.md`
- Updated concept page:
  - `concepts/external-memory.md`
- Navigation: `index.md` was reviewed. No new page was created, and the updated concept is already cataloged; the file remains binary-detected by editor tools, so no unsafe whole-file rewrite was made.
- Tip: iPhoneのAppleショートカットに出るNotion提案を入口にし、思いついたタスクを数秒で直接ToDoへ投入して、捕捉の手数を下げる。設定手順・動作は未検証で、入力する情報と同期・共有範囲を確認する。
- Note: X投稿は低信頼度の個人実践であり、医学的・臨床的効果の根拠ではない。

## [2026-09-23] ingest | X/Twitter ADHD practical-tip search 154
- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; candidates were deduplicated by tweet ID and checked against existing raw sources and recent log entries.
- Created raw source:
  - `raw/articles/tweet-2102646718852378628-commute-idling-task-start.md`
- Updated concept/navigation pages:
  - `concepts/task-initiation.md`
  - `index.md`
- Tip: 作業場所に着いてから始める内容を選ばず、出勤・移動・散歩などの短い移行時間に最初の一手を決める「アイドリング」を固定し、着席時の選択・起動コストを下げる。
- Note: X投稿は低信頼度の個人実践であり、医学的・臨床的効果の根拠ではない。通勤・移動を増やす推奨ではなく、着手前の選択を既存の移行時間へ移す設計として扱う。

## [2026-09-24] ingest | X/Twitter ADHD practical-tip search 155

- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; candidates were deduplicated by tweet ID and checked against existing raw tweet files and recent log entries.
- Created raw sources:
  - `raw/articles/tweet-2102943914110120051-naggie-annoying-reminder-app.md`
  - `raw/articles/tweet-2102894528755896541-automation-retry-reversible.md`
  - `raw/articles/tweet-2102679171751362671-job-structure-fit-checklist.md`
  - `raw/articles/tweet-2102717111227576616-sleep-environment-parenting-thread.md`
- Updated concept/navigation pages:
  - `concepts/external-memory.md`
  - `concepts/work-routines.md`
  - `concepts/sleep.md`
  - `concepts/parenting.md`
  - `index.md`
- Tips:
  - 絶対に忘れたくない予定は、時間になると通知カードを出し、見逃す・放置すると3〜10分間隔で再通知が来る Windows 用リマインダーアプリ（Naggie）の製品紹介。予定を覚える負荷を再通知へ移す。
  - 自動化が止まったらログから真因を時刻つきで特定し、再試行（3回・10分間隔）を足して、元へ戻せる設定にする。
  - 仕事の構造との相性をチェックリスト（頼まれ事・裁量・複数案件・ミスが信用問題等11項目）で自己点検し、7個以上で相性見直しの目安にする。
  - 発達特性のある子の睡眠環境は、就寝約90分前の38〜40度ぬるめ入浴、体重10%前後で顔を覆わない重みブランケット、寝る前の確認・反省会をチェックリスト・指さし・固定ルーティンへ引き算する。
- Note: X投稿は低信頼度の個人実践・製品紹介であり、医学的・臨床的効果の根拠ではない。自動化は停止方法・通知・責任・データ取扱いを運用前に決め、睡眠の持続的な困難や服薬との関係は専門職へ相談する。

## [2026-09-24] ingest | X/Twitter ADHDパワー系ソリューション定期検索 156
- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; candidates were deduplicated by tweet ID and checked against existing raw sources and recent log entries.
- Created raw sources:
  - `raw/articles/tweet-2102733271448854685-konjac-brain-load-calibration.md`（開始ラインを「気軽にやれる範疇」へ下げ、余裕なら増やし、きつくなったら全力で減らす。積んで崩して崩れなかった部分だけを拾う）
  - `raw/articles/tweet-2102965445599142338-pen-in-hand-start.md`（スマホの代わりに常にペンを握り、仕事の最初の身体動作を開始前に済ませる）
- Updated concept pages:
  - `concepts/self-experimentation.md`（負荷を逐次調整する新節）
  - `concepts/task-initiation.md`（道具を先に握る着手ハック）
- Updated navigation: `index.md`（self-experimentation 要約を更新）
- Tips:
  - 開始ラインを「気軽にやれる範疇」まで下げ、余裕が出たら増やし、きつくなったら全力で減らす。堅固な構造を組まず、崩れずに残った部分だけを拾う。
  - 脱線先のスマホを持つ手を作業道具（ペン）を持つ手へ置き換え、仕事の最初の身体動作を開始前に済ませる。
- Note: X投稿は低信頼度の個人実践であり、医学的・臨床的根拠ではない。

## [2026-09-24] ingest | X/Twitter ADHDパワー系ソリューション定期検索 157

- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; candidates were deduplicated by tweet ID and checked against existing raw tweet files and recent log entries.
- Created raw sources:
  - `raw/articles/tweet-2103146318223007779-reset-compulsion.md`（リセット癖：24時間ルール・部分リセット・再開最小化）
  - `raw/articles/tweet-2103116700963225858-dopamine-menu.md`（ドーパミン・メニュー）
  - `raw/articles/tweet-2103109949022773264-waiting-mode-timer.md`（待機モード：アラームまで他事OK）
  - `raw/articles/tweet-2103109457664471301-sixty-percent-first.md`（まず6割で通す）
  - `raw/articles/tweet-2103109173965942993-thirty-min-before-sleep.md`（寝る前30分確保）
  - `raw/articles/tweet-2102744799677964439-unstable-rotation.md`（不安定なまま回す）
- Created concept page:
  - `concepts/reset-compulsion.md`
- Updated concept/navigation pages:
  - `concepts/task-initiation.md`（ドーパミン・メニュー）
  - `concepts/waiting-mode.md`（アラームまで他事OK＋身体を動かす）
  - `concepts/all-or-nothing-thinking.md`（完璧にする順番を後ろへずらす）
  - `concepts/sleep.md`（寝る前30分の確保）
  - `concepts/self-experimentation.md`（不安定なまま回す）
  - `index.md`（reset-compulsion 追加、総ページ数 52）
- Tips:
  - リセットしたい衝動を維持コストと刺激低下の緊急回避と捉え、24時間ルール・部分リセット・仕組みの入れ替え・再開ハードル最小化でリセット前のコストを下げる。
  - 一日をコース料理に見立て、前菜（1分スクワット）→メイン（没入）→サイド（雑務×Podcast）→デザート（SNS15分）→スペシャル（長期の楽しみ）で着手・退屈・報酬を段階に分ける。
  - 待機モードは「アラームまで他事OK」と許可し、無理やりでも体を動かす。
  - 完璧主義は「まず6割で最後まで通す」で、完璧にする順番を後ろへずらす。
  - 寝る前30分を「何もしなくていい時間」として先に確保し、就寝へ移る。
  - 「毎日整える」を逆転させ、思い出した日に爆速・午後始動・1個徹底・変化を許す習慣で不安定なまま回す。
- Note: X投稿は低信頼度の個人実践であり、医学的・臨床的根拠ではない。

## [2026-09-24] ingest | X/Twitter ADHDパワー系ソリューション定期検索 158

- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; candidates were deduplicated by tweet ID and checked against existing raw tweet files and recent log entries.
- Created raw sources:
  - `raw/articles/tweet-1876056692011757803-wrong-power-solutions.md`（「借りるくらいなら買う」などの間違ったパワー系ソリューションの失敗形）
  - `raw/articles/tweet-2103046963679678855-fixed-scaffold-free-content.md`（土台だけ固定して中身は自由）
  - `raw/articles/tweet-2101493494153875812-waiting-mode-bundle-day.md`（予定を同じ日にまとめて空白の日を作る）
- Updated concept pages:
  - `concepts/all-or-nothing-thinking.md`（パワー系ソリューションの失敗形の節を追加）
  - `concepts/impulsivity-countermeasures.md`（極端なパワー系解決が逆効果になる型を自覚する節を追加）
  - `concepts/environment-design.md`（土台固定・中身自由の生活設計を追加）
  - `concepts/waiting-mode.md`（予定を同じ日にまとめる型を追加）
- Navigation: index.md は新規ページ追加なし（総ページ数 52 のまま）。
- Tips:
  - 「借りるくらいなら買う」「貸すくらいならあげる」「迷うくらいなら全部やらない」など、白黒思考が強い解決策として誤学習された極端策は、選択肢・人間関係・時間・持ち物を失わせる失敗形。
  - 起床時刻・仕事の順番・定位置の席など「土台」だけ固定し、中身は毎日自由にすると、ルーティン崩れの不安と刺激不足を両立できる。
  - 予定の前後が使えなくなる待機モード対策として、予定を同じ日にまとめて空白の日を丸ごと作る。
- Note: X投稿は低信頼度の個人実践であり、医学的・臨床的根拠ではない。

## [2026-09-25] ingest | X/Twitter ADHDパワー系ソリューション定期検索 159

- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; 70 unique tweet IDs were deduplicated by tweet ID and checked against existing raw sources and log entries.
- Created raw sources:
  - `raw/articles/tweet-1975766626399367189-uninteresting-video-work-bgm.md`
  - `raw/articles/tweet-1992934100684996865-event-trigger-prospective-memory.md`
  - `raw/articles/tweet-2103319553325285384-smallest-item-priority-paralysis.md`
  - `raw/articles/tweet-2103329897854689607-verify-actual-execution.md`
- Updated concept pages:
  - `concepts/task-initiation.md`（興味のない内容を流して適度に脳を奪う）
  - `concepts/prospective-memory.md`（出来事トリガーへの組み替え）
  - `concepts/executive-function.md`（優先度づけフリーズ時は最小の一手）
  - `concepts/work-routines.md`（予定ではなく実測で確認）
- Navigation: `index.md` date bump（新規ページなし、総ページ数 52 のまま）。
- Tips:
  - 興味のない人文系の対談動画を作業用BGMに流し、適度に脳のリソースを奪うことで着手の心理的抵抗を下げる。
  - 時間ベースの「19時に◯◯する」を、出来事トリガー（皿と薬を並べる、PC起動でメール自動表示、玄関の「明日の自分ボックス」）へ組み替える。
  - 全部が最優先に感じて固まる時は、一番小さい作業を最初の一手にする。
  - 予定表ではなく実測（実際に実行・配信されたか）で確認する仕組みを持つ。
- Note: X投稿は低信頼度の個人実践であり、医学的・臨床的根拠ではない。

## [2026-09-25] ingest | X/Twitter ADHDパワー系ソリューション定期検索 160

- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; 77 unique tweet IDs deduplicated by ID and checked against existing raw sources (382 files) and log entries.
- Created raw sources:
  - `raw/articles/tweet-2103421807252693465-routine-margin-mental-rehearsal.md`（日課の組み直し＝余白＋頭の中での手順リハーサル）
  - `raw/articles/tweet-2103416802370081210-people-drop-paper-visible.md`（「人は抜ける」前提で紙と視界へ残す）
  - `raw/articles/tweet-2103378974101704728-ten-minute-night-note.md`（寝る前10分の整理ノート）
  - `raw/articles/tweet-1927179918279868672-stop-and-go-game.md`（幼児の抑制を育てるストップ＆ゴーゲーム）
  - `raw/articles/tweet-1740340412177596822-plush-on-remote.md`（リモコンにぬいぐるみ）
  - `raw/articles/tweet-2025394259176931463-medical-first-then-hacks.md`（まず医療、その上でライフハック）
- Updated concept pages:
  - `concepts/time-management.md`（新しい日課の余白＋メンタルリハーサル）
  - `concepts/external-memory.md`（人は抜ける前提の紙と視界／寝る前10分整理ノート）
  - `concepts/parenting.md`（ストップ＆ゴーゲーム）
  - `concepts/forgetfulness-countermeasures.md`（リモコンにぬいぐるみ）
  - `concepts/medication.md`（まず医療、その上でライフハック）
- Navigation: `index.md` は変更なし（新規ページなし、総ページ数 52 のまま、日付も同日のため据え置き）。
- Tips:
  - 生活の大きな変化で日課を組み直す時は、予定の間に空白（切り替え時間）を設け、余白を取れない場合は始める前に新しい日課を頭の中で数回たどって手順を飛ばさない。
  - 「人は抜ける」を前面に置き、一度の口頭説明で終わらせず紙にもする・目にも入るようにする。
  - 寝る前10分の「整理ノート」で今日やったこと・明日やること各3つを書き、未完了の山による夜の焦りを外へ出す。
  - 「ストップ＆ゴーゲーム」（赤/青カードで歩く・止まる）で幼児の抑制を遊びで練習する。
  - リモコンにぬいぐるみを付けて大きく・目立たせ、失くしにくくする。
  - ライフハックを集める前にまず適切な医療を受け、その上でライフハックが効く。
- Note: X投稿は低信頼度の個人実践であり、医学的・臨床的根拠ではない。

## [2026-09-25] ingest | X/Twitter ADHDパワー系ソリューション定期検索 161

- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; 74 unique tweet IDs deduplicated by ID and checked against existing raw sources (443 tweet IDs).
- Created raw sources:
  - `raw/articles/tweet-2102689427919389064-template-chores-routines.md`（家事・ルーティンをテンプレ化して「気疲れ」を減らす）
  - `raw/articles/tweet-1740365098630406505-greet-everyone-face-memory.md`（顔を覚えられない→全員ににこやかに挨拶）
  - `raw/articles/tweet-1276770061278040065-vocalize-ahhh-start.md`（「あーー」と発声して先延ばしタスクへ着手）
  - `raw/articles/tweet-2103462218515763458-three-time-tactics-teacher.md`（時間可視化＋準備の予定＋予想vs実測）
  - `raw/articles/tweet-2103467303815835681-return-signal-before-going-out.md`（外出前に「帰る合図」を先に決める）
  - `raw/articles/tweet-2103352546983334272-automation-stop-detection.md`（自動化は「止まったとき」まで設計）
  - `raw/articles/tweet-2103363871356735724-stopping-mechanism-visibility.md`（止める仕組みには「止まった理由が見える仕組み」も）
  - `raw/articles/tweet-2102911012953542709-money-tech-buy-duplicates.md`（お金とテクノロジーで苦手を解決）
  - `raw/articles/tweet-2004140473657839653-reverse-countdown-alarm-gemini.md`（逆算アラーム＋1.5倍バッファ、Gemini生成）
- Updated concept pages:
  - `concepts/environment-design.md`（反復作業のテンプレ化／外出の退出条件を先置き）
  - `concepts/time-management.md`（準備の予定／逆算アラーム）
  - `concepts/task-initiation.md`（あーー発声の高エンゲージメント実例）
  - `concepts/work-routines.md`（自動化の停止検知／止める仕組みの可視化）
  - `concepts/relationships.md`（顔認識を挨拶で迂回）
  - `concepts/forgetfulness-countermeasures.md`（お金とテクノロジー）
- Navigation: `index.md` は変更なし（新規ページなし、総ページ数 52 のまま）。
- Tips:
  - 家事・ルーティーンワークをテンプレ化し、考えずに回せる型へ固定して「気疲れ」を減らす。
  - 人の顔が覚えられないなら、すれ違う人全員ににこやかに挨拶して認識を不要にする。
  - 先延ばしの嫌な行動は声に出して「あーー」と言いながらやると着手できる。
  - 予定の前に「準備の予定」（例: 18時半から準備）を入れ、時間は残量タイマー／アナログ時計で可視化する。
  - 衝動で出かけるのは許しつつ、「イヤホン外したら帰る」など退出条件を先に決める。
  - 自動化は「完全に止まったら通知する」まで設計し、静かな停止に誰も気づけない状態を避ける。
  - メガネが毎朝見つからないなら同じものを3つ持ち、なくしたら躊躇せず買い直す。
- Note: X投稿は低信頼度の個人実践であり、医学的・臨床的根拠ではない。

## [2026-09-28] ingest | X/Twitter ADHDパワー系ソリューション定期検索 162

- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; 75 unique tweet IDs deduplicated by ID and checked against existing raw sources (397 tweet IDs).
- Created raw sources:
  - `raw/articles/tweet-2104321010485047685-morning-sns-first-stimulus-design.md`（朝イチの最初の刺激をSNSより先に設計）
  - `raw/articles/tweet-2104337792256131089-verbal-request-slack.md`（口頭依頼は「Slackで送ってもらっていい？」）
  - `raw/articles/tweet-2104352639437939000-folding-umbrella-always-packed.md`（折り畳み傘を常時リュックへ）
  - `raw/articles/tweet-2104195787618128263-five-more-minutes-timer-first.md`（夜の「あと5分」前にタイマー先押し）
  - `raw/articles/tweet-2104103795693330463-short-deadline-before-free-time.md`（自由時間より短い締切を先に）
  - `raw/articles/tweet-2104103772020785195-external-pressure-ignition-fuel.md`（起動の燃料は外から来る締切と強制力）
  - `raw/articles/tweet-2104231375872385332-rumination-move-body-distance.md`（反芻は体を動かす・環境から離れる）
  - `raw/articles/tweet-2104376626582876236-start-from-what-bugs-you.md`（気になったものから着手・シングルタスク）
  - `raw/articles/tweet-2104162574262730874-auto-timer-cooker-replacement.md`（自動タイマー付き調理器具へ買い替え）
  - `raw/articles/tweet-2104342517147914618-job-strength-weakness-ratio.md`（得意:不得意 2:8→6:4 の職選び）
- Updated concept pages:
  - `concepts/forgetfulness-countermeasures.md`（折り畳み傘常時リュック）
  - `concepts/external-memory.md`（口頭依頼を文字で受け取る）
  - `concepts/environment-design.md`（朝イチ刺激設計・自動タイマー調理器具）
  - `concepts/time-management.md`（夜あと5分タイマー・短い締切）
  - `concepts/task-initiation.md`（短い締切・外圧が起動燃料・気になったものから着手）
  - `concepts/rumination.md`（反芻の実践節を新設）
  - `concepts/work-routines.md`（得意不得意6:4の職選び）
- Navigation: `index.md` は変更なし（新規ページなし、総ページ数 52 のまま）。
- Tips:
  - 朝イチでSNSを開くと「刺激を追うモード」に入るため、SNSより先にカーテンを開ける・水を飲む・机の上を1か所だけ片付ける、といった低刺激の動作から始める。
  - 廊下ですれ違いざまの口頭依頼は消えるため、「Slackで送ってもらっていい？」を口癖にし、口頭の依頼は受け取っていない扱いにする。
  - 傘を忘れる前提で、晴れの日でも折り畳み傘を常時リュックへ入れておき、乾かしたら即リュックへ戻す。
  - 夜の「あと5分」が伸びるなら、言う前にタイマーを先に押し、鳴ったら途中でも一度立つ。
  - 時間があるほど動けなくなる前提で、長い自由時間より30分後に人と会う約束のような短い締切を先に置く。起動の燃料はやる気ではなく外から来る締切と強制力。
  - 反芻は体を動かして一時的に途切れさせ、反芻を引き起こす環境・人から離れて頻度を減らす。
  - 優先順位づけが回らないなら、気になったものから順にシングルタスクで仕留める。
  - 自動タイマー付きの調理器具へ買い替え、火の見守りという注意負荷を器具へ逃がす。
  - 職選びは得意:不得意の業務比重を2:8から6:4へ変え、不得意は対策で補う。
- Note: X投稿は低信頼度の個人実践であり、医学的・臨床的根拠ではない。

## [2026-09-28] ingest | X/Twitter ADHDパワー系ソリューション定期検索 163

- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; 78 unique tweet IDs deduplicated by ID and checked against existing raw sources and log entries. Skipped already-ingested tweets, English-only content, generic empathy/diagnosis discourse, memes, medical/diet/supplement claims without reliable source, self-promotion without workflow detail, duplicate tactics, and posts exposing unnecessary personal detail.
- Created raw sources:
  - `raw/articles/tweet-2104168172861477285-ten-home-environment-settings-child.md`（発達特性のある子の家庭環境づくり10選：カオティック・ゾーン／分解専用箱／ホワイトノイズ／フィジット／色分け／パーソナルテント／失敗展示ボード／体を動かす道具／何もない壁／朝の高照度光）
  - `raw/articles/tweet-2104416154156757381-reduce-start-count-minimize-breaks.md`（開始コストが高い→開始回数を減らし休憩を最小化）
  - `raw/articles/tweet-2104403630514401455-defer-decide-when-first.md`（後回しにするなら「いつやるか」だけ先に決める）
  - `raw/articles/tweet-2104454734690275467-ai-close-tasks-small-units.md`（AIにはタスクを小さい単位でCloseを優先）
  - `raw/articles/tweet-2104453799155020171-ai-delegation-open-loops.md`（AI委任は未完了タスクを増やす諸刃の剣）
  - `raw/articles/tweet-2104405737455628559-choose-materials-by-trait.md`（通信教育は特性で教材を選ぶ）
  - `raw/articles/tweet-2102210266557735127-hide-comparison-targets-hyperfocus.md`（上の比較対象を視界から消す）
  - `raw/articles/tweet-2103241252368269445-time-measurement-hyperfocus-trigger.md`（時間を測る競技性で着手、時間感覚は掴めない）
  - `raw/articles/tweet-2104463501582291175-adhd-weaknesses-ai-strengths.md`（ADHDの苦手＝AIの得意）
- Updated concept pages:
  - `concepts/environment-design.md`
  - `concepts/parenting.md`
  - `concepts/sleep.md`
  - `concepts/attention-control.md`
  - `concepts/task-initiation.md`
  - `concepts/hyperfocus-control.md`
  - `concepts/digital-adhd-support.md`
  - `concepts/work-routines.md`
  - `concepts/external-memory.md`
  - `concepts/time-management.md`
- Updated navigation: `index.md` date bump（新規ページなし、総ページ数 52 のまま）。
- Note: X投稿は低信頼度の当事者実践であり、医学的・臨床的根拠ではない。発達特性のある子の環境づくり10選は事業者アカウント（オンライン運動教室の宣伝を含む）由来の情報で個別検証はしていない。「上の比較対象を視界から消す」は競争的・攻撃的な表現を含むため慎重に扱った。クラウドAI利用は入力の最小化と本人確認を前提とした。

## [2026-09-28] ingest | ADHD Research Watch curation（NZ成人ADHDケア経路）

- Accepted (score 3): `pubmed:42784829` — ニュージーランド（アオテアロア）で2026年2月から家庭医・ナースプラクティショナーによる成人ADHDへの刺激薬処方開始が認められた制度変更を、公平性・診断品質・費用・持続可能性から検討する政策論。
  - Created: `raw/papers/lillis-2026-adhd-care-pathways-aotearoa-nz.md`
  - Updated: `concepts/public-support.md`（アクセスと質を同時に設計する）、`concepts/diagnosis-and-management.md`（アクセス拡大と診断品質の両立）
- Skipped:
  - `pubmed:41887460`（ADHD子育ての編集記事、2ページ論説で新規性が薄い）score 1
  - `pubmed:42789617`（一般向けCBTレビュー、ADHDは補助的治療の一項目）score 0
  - `pubmed:42788194`（韓国の医療用麻薬利用の薬剤疫学研究、ADHD支援と無関係）score 0
- Navigation: `index.md` 変更なし（新規ページなし、総ページ数 52 のまま）。
- Note: 政策論・制度論であり、個別診断・処方の代替ではない。国・制度差に注意。

## [2026-09-28] ingest | X/Twitter ADHDパワー系ソリューション定期検索 164

- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; 62 unique tweet IDs deduplicated by ID and checked against existing raw sources (416 tweet IDs). Skipped already-ingested tweets, English-only content, generic empathy/diagnosis discourse, memes, medication/diagnosis discourse, self-promotion without workflow detail, duplicate tactics（AI外部脳・選択排除・最小タスク着手など既存カバー済み）, and posts exposing unnecessary personal detail.
- Created raw sources:
  - `raw/articles/tweet-2104529361433223224-audiobook-plus-paper-dual-input-reading.md`（音声＋紙の二重入力読書）
  - `raw/articles/tweet-2104568076301689180-subject-batching-weekly-not-parallel.md`（科目を週単位でまとめる）
  - `raw/articles/tweet-2104569477711241337-family-shared-calendar-indirect-prompt.md`（家族共有カレンダー＋間接的声かけ）
- Updated concept pages:
  - `concepts/attention-control.md`（音声＋紙の二重入力読書／科目の週単位ブロック化）
  - `concepts/parenting.md`（共有カレンダー＋「チェックした？」の間接的声かけ）
  - `concepts/external-memory.md`（家族共有カレンダーで確認を習慣化）
- Navigation: `index.md` 要約を2件微更新（新規ページなし、総ページ数 52 のまま）。
- Tips:
  - 読書中に視線が泳ぐなら、Audible（音声）を流しながら同じ紙の本を開いて読むと、一方の入力が途切れても文章摂取が続く。
  - 短いスパンでの切り替えが苦手なら、複数科目を並行ローテーションせず1科目を週単位でまとめて回す。
  - 家族共有カレンダー＋個人別カラーで、直接指示する代わりに「チェックした？〜があった気がする」と問いかけて本人が確認するルーティンを育てる。
- Note: X投稿は低信頼度の当事者実践であり、医学的・臨床的根拠ではない。

## [2026-09-28] ingest | X/Twitter ADHDパワー系ソリューション定期検索 165

- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; 74 unique tweet IDs deduplicated by ID, 59 not yet ingested. Evaluated against selection criteria. Skipped English-only content, memes, diagnosis/medication discourse, self-promotion without workflow detail, duplicate tactics（AI外部脳・選択排除・最小タスク着手・移動1.5倍見積もり・手に持たない等は既存カバー済み）, posts without actionable detail, and one anti-diagnosis misinformation post (1877854412934406310).
- Created raw source:
  - `raw/articles/tweet-1743926787309289837-dialogue-vs-lecture-background-sound.md`（背景音・動画を「対談／講義」で目的別に使い分ける、CB連投スレッド）
- Updated concept pages:
  - `concepts/task-initiation.md`（対談は第三者同士で意識が持っていかれず、講義は話者に引き付けられてストレス、という背景音の形式による使い分け＋選定基準「広告なし・長時間・意味不明」）
  - `concepts/attention-control.md`（静かすぎる環境で妄想が始まる人へ、あえて音を足す）
  - `concepts/sleep.md`（眠れぬ夜に講義形式の専門的な話で意識を「強制終了」させて入眠へつなげる）
- Navigation: `index.md` 変更なし（新規ページなし、総ページ数 52 のまま）。
- Tips:
  - 静かな環境では妄想が始まって集中が続かないタイプは、喫茶店か、家では「広告なし・長時間・程よく意味不明」な公的機関の人文系の対談を流して環境を作る。
  - 対談は会話が第三者同士で完結するため意識が持っていかれないが、講義形式（放送大学など）は話者が自分に語りかけていると脳が認識して引き付けられ、逆にストレスになる、という使い分け。
  - 眠れぬ夜には、ワーキングメモリへの負荷が大きい講義形式を流して意識を「強制終了」させ、睡眠へつなげる。
- Note: X投稿は低信頼度の当事者実践であり、医学的・臨床的根拠ではない。音・動画が注意を奪う人や安全確認が必要な場面では使わない。

## [2026-09-29] ingest | X/Twitter ADHDパワー系ソリューション定期検索 166

- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; 75 unique tweet IDs deduplicated by ID, 57 not yet ingested; checked against 420 existing raw sources/log IDs. Skipped English-only content, memes, astrology, diagnosis/medication discourse, self-promotion without workflow detail, duplicate tactics（毎日同じ服の選択排除・AI外部脳・最小タスク着手・GPSタグ・「気合いでなく仕組み化」等は既存カバー済み）, posts without actionable detail, and unsourced medical claims.
- Created raw sources:
  - `raw/articles/tweet-2104700180411064405-virtual-desktop-per-task.md`（案件ごとに仮想デスクトップを分け、切り替えてもウィンドウを閉じずに文脈を残す）
  - `raw/articles/tweet-2104699597956534762-careless-mistake-three-step-review.md`（印→原因を1つ言葉にする→次の見直しは1か所の3手順）
  - `raw/articles/tweet-2104746374151676297-engine-stages-light-task-ladder.md`（軽いタスクから徐々に負荷を上げる「エンジンの段階」）
  - `raw/articles/tweet-1971025987644371400-parenting-acceptance-structure-agreement.md`（依存予防の「受容×構造×合意」と年齢別ルーティン）
  - `raw/articles/tweet-1992196380790812991-time-blindness-research-meta-analysis.md`（時間盲のメタ分析知見と3対策）
- Updated concept pages:
  - `concepts/task-resumption.md`（仮想デスクトップで案件ごとに文脈を残す）
  - `concepts/careless-mistake-countermeasures.md`（最小3手順の見直しループ）
  - `concepts/task-initiation.md`（エンジンの段階＝負荷を段階的に上げる暖機運転）
  - `concepts/parenting.md`（依存予防の「受容×構造×合意」と年齢別ノースマホ・ルーティン）
  - `concepts/time-management.md`（時間盲のメタ分析知見で見える化・5分刻み・二重化締切を位置づけ）
- Navigation: `index.md` date bump（新規ページなし、総ページ数 52 のまま）。
- Note: X投稿は低信頼度の当事者実践であり、医学的・臨床的根拠ではない。足立匡基（@adachi_psy）の2投稿は専門家アカウントで研究知見に言及するが、依存予防スレッドは個別書誌が未提示で、時間盲スレッドは本文に書誌を記載。いずれも主張の引用は一次文献で確認する。

## [2026-09-29] ingest | X/Twitter ADHDパワー系ソリューション定期検索 167

- Searches: 4 Japanese practical-tip searches across `Latest` and `Top` via bird; 79 unique tweet IDs deduplicated by ID and checked against 425 existing raw sources/log IDs. Skipped already-ingested tweets, English-only content, memes, PR/書籍販促, diagnosis/medication discourse, astrology, self-promotion without workflow detail, duplicate tactics（スマホ物理除去・選択排除・AI外部脳・最小タスク着手・仕組み化等は既存カバー済み）, and posts without actionable detail.
- Created raw sources:
  - `raw/articles/tweet-2104813423322145235-note-write-for-future-recall.md`（メモは「あとから思い出せるように」誰と・いつ・何をするかまで具体的に書く）
  - `raw/articles/tweet-2104778742958793026-single-task-delegation-partner.md`（パートナーの家事マルチタスクを引き受け、本人はシングルタスクに集中）
  - `raw/articles/tweet-2104848655161475283-buffer-resources-good-periods.md`（動ける時期に作り置きの食事と報告できる仕事の成果を先に貯めるバッファ設計）
- Updated concept pages:
  - `concepts/external-memory.md`（メモをあとから思い出せるように書く）
  - `concepts/relationships.md`（マルチタスクを外してシングルタスクへ絞る役割設計）
  - `concepts/energy-management.md`（動ける時期に資源を前倒しで貯めるバッファ設計）
- Navigation: `index.md` 変更なし（新規ページなし、総ページ数 52 のまま）。
- Tips:
  - メモは「忘れないため」でなく「あとから思い出せるように」書く。「誰と・いつ・何をするのか」まで具体的に書く。
  - ADHD傾向のあるパートナーには家事というマルチタスクを引き受け、本人には自室の片付けというシングルタスクだけに集中させる。
  - やる気が出ない時期に備え、動ける時に作り置きの食事と報告できる仕事の成果を先に貯めておく。
- Note: X投稿は低信頼度の当事者実践であり、医学的・臨床的根拠ではない。メモ具体化は発達障害カウンセラーアカウント、役割設計は配偶者、バッファ設計は自己啓発系当事者アカウントの単一投稿で、いずれも個別検証はしていない。

## [2026-10-07] ingest | Reddit ADHD / ADHD_Programmers / ADHDers 定期レビュー

- Reviewed: 36 candidates（r/ADHD 12、r/ADHD_Programmers 12、r/ADHDers 12）。医療用量・診断主張・危機/私的体験・ミーム・宣伝・既存手法の重複を除外し、個人名・ユーザー名・コメントの個別叙述は保存しなかった。
- Accepted: 1（score 3）。長いAI生成仕様を読み直す負荷を減らす、冒頭の決定要約・確認箇所の固定、短縮/図/読み上げ等の選択肢。単一Redditスレッド由来の低信頼度な生活実践であり、臨床的主張ではない。
- Created raw: `raw/articles/reddit-1wzq3pf-dyslexia-agent-output-review-2026.md`
- Updated: `entities/i-have-adhd.md`（Reddit由来・信頼度 low と明示）、`index.md`（更新日）
- State: `.automation/reddit-watch/state.json` に36件すべてのレビュー済みID、成功時刻、サブレディット別 reviewed/accepted/skipped 集計を記録。
- Source: https://www.reddit.com/r/ADHD_Programmers/comments/1wzq3pf/dyslexia_agentic_engineering_tips_for_reading/
