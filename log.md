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

