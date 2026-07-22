---
source_url: https://screenpipe.com/
ingested: 2026-07-22
sha256: 9b6470d6e6b372b9d6e3b906591056c750a256f9533a6d9036194e69f329e738
---

# screenpipe homepage

Source: https://screenpipe.com/
Captured: 2026-07-22

## Extracted content

screenpipe presents itself as a local-first workflow-memory product for computers. The page says it turns screen, audio, apps, and handoffs into searchable work memory and agent triggers.

The homepage has four main product demos:

1. Remember: search across screen, audio, apps, and handoffs without rebuilding context. Example prompt: "Draft my weekly update from this week's calls." The page shows "47 days of memory" as an example.
2. Act: background agents can run from events. The example "meeting-notes" pipe triggers when a meeting ends, writes a three-bullet summary, action items per person, decisions, and next steps, then saves the result locally to notes.
3. Connect: pipes can connect to apps such as Gmail, HubSpot, and Slack so automations can use them.
4. Control: privacy controls can exclude apps, windows, and URLs. The page says excluded sources are dropped before reaching disk. It also says captured content can be scrubbed on-device to remove card numbers, SSNs, and keys before saving.

The page emphasizes on-device capture and processing. It says screenpipe captures the screen 100% on-device, supports macOS, Windows, and Linux, and is open source / auditable through its GitHub repository.

For teams, the page describes local endpoint capture, MDM deployment, SSO, seat management, and on-device PII scrubbing.

## Example pipe from the page

```yaml
---
name: meeting-notes
trigger: meeting_ended
model: local
---

When a meeting ends, write:
- 3-bullet summary
- Action items per person
- Decisions + next steps

Save to ~/notes/{date}_{app}.md
```

## Notes for ADHD wiki use

- This is vendor-provided product text, not independent evidence of benefit.
- The ADHD-relevant pattern is not "screen recording" by itself. The relevant pattern is externalizing memory of work: what happened, what was said, which app was used, and what follow-up should happen.
- Continuous screen/audio capture is highly sensitive. Privacy controls, exclusion lists, on-device processing, and review of stored data are central, not optional.
