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
