---
source_url: https://github.com/ayghri/i-have-adhd
ingested: 2026-07-22
sha256: 73192e3f166e64b47f295f413b00e7204aa31265b1d82c86d6d1a22bb725c03d
---

# i-have-adhd repository

Source: https://github.com/ayghri/i-have-adhd
Captured: 2026-07-22
Commit inspected: ccce9e793a0d9fa008e9fb42199c39463f73a70a
License: MIT
Primary language: Python
Repository description: A skill for your coding agent to stop it from burying the answer. ADHD-friendly output.
GitHub topics: adhd, claude-code-plugin, claude-skills, developer-tools, productivity
Stars at capture: 7507
Forks at capture: 321

## What the repository is

`i-have-adhd` is an agent skill/plugin that changes coding-agent responses into an ADHD-friendly output style. It is not a clinical ADHD tool. It is a communication and developer-tooling project: make the answer easier to act on by leading with the next action, numbering steps, suppressing tangents, and making progress visible.

The README summarizes the goal as: "A skill for your coding assistant that stops it from burying the answer. Action first. Steps numbered. No \"Hope this helps!\""

## Supported agent surfaces

The repository includes installation paths or plugin metadata for multiple coding agents and editors:

- Claude Code via plugin marketplace commands and `/i-have-adhd`.
- Codex via plugin marketplace commands and `$i-have-adhd`.
- Zed via Agent Skills import from URL or copying the skill folder.
- Hermes via `hermes skills install ayghri/i-have-adhd/skills/i-have-adhd`.
- Gemini, Cursor, Antigravity, and other skill/plugin-compatible harnesses via included metadata and instructions.

## Core rules from the skill

The skill file states that output should be shaped for a reader with ADHD, not merely shortened. Its ten rules are:

1. Lead with the next action.
2. Number multi-step tasks.
3. End with one concrete next action.
4. Suppress tangents.
5. Restate state every turn.
6. Give specific time estimates.
7. Make completed work visible.
8. Use a matter-of-fact tone for errors.
9. Cap lists at 5 items.
10. No preamble, no recap, no closing pleasantries.

The skill also has explicit exceptions: explain fully when asked, confirm before destructive actions, stop after repeated debugging failures and name the doubtful assumption, ask a short question when ambiguity is real, and let harness/system constraints win when they conflict with the output style.

## Always-on behavior

The Claude Code install path includes an optional always-on mode. A SessionStart hook reads `$CLAUDE_CONFIG_DIR/.i-have-adhd-always` or `~/.claude/.i-have-adhd-always`. If the flag exists, it injects the skill body at session start. The hook is designed not to block session start; failures exit without throwing.

For Codex, Zed, Hermes, and other systems, the install guide suggests putting a shorter always-on rule block in the relevant `AGENTS.md` or persona configuration.

## Evaluation support

The repository includes an `evals/` directory with cases, a rubric, and `scripts/run_evals.py`. The rubric scores response quality across correctness, autonomy, actionability, safety, and concision. It emphasizes blind comparison, isolated runner configuration, pinned models, budget tracking, and a release gate where the candidate must improve weighted score without blocking correctness or safety regressions.

## ADHD wiki interpretation

For this wiki, the important pattern is ADHD-aware information design for agent output. The tool encodes practical accessibility defaults: reduce working-memory load, reduce start friction, keep the next action visible, make progress explicit, and avoid low-value social wrapping. It belongs near external memory, task initiation, executive function, work routines, and assistive technology.

This is a software/project source, not medical evidence. It should not be treated as proof that a particular style improves ADHD symptoms. It is useful as an implementation example of ADHD-informed output design in coding agents.
