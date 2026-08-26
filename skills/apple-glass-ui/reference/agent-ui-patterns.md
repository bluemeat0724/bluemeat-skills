# Apple Glass UI — Agent Interface Patterns

Agent interfaces should present conversation, execution, interaction, and results as distinct layers. Glass belongs mainly to the outer control layer.

## 1. Surface mapping

| Element | Default surface |
| --- | --- |
| User message | Level 0 |
| Assistant response | Level 0 |
| Reasoning | Level 0, visually subdued |
| Tool lifecycle and result | Level 0, compact semantic state |
| Progress | Level 0, stable and quiet |
| HITL container | Level 1 |
| Approval action | Level 2 |
| Chart, table, report, artifact content | Level 0 |
| Artifact toolbar | Level 1; selected primary action may be Level 2 |
| Sidebar and popover | Level 1 |
| Composer | Strong Level 1 |
| Send or Run | Level 2 |
| Debug timeline and raw payload inspector | Level 0, dense and readable |

## 2. Conversation

User messages should be compact, high contrast, and clearly owned. Long assistant responses should behave like documents with strong typography and minimal container decoration.

Do not turn every message into a glass bubble.

## 3. Reasoning

Reasoning is secondary process information. Keep it subdued, compact, and collapsible. While streaming, update a stable container; after completion, reduce its visual weight when collapsed.

Do not animate every token or give reasoning the same emphasis as the final answer.

## 4. Tool activity

Represent lifecycle explicitly:

```text
queued → preparing → running → completed
                              ↘ failed or cancelled
```

Show a compact semantic label and status. Streamed arguments should not flash partial raw data in the primary conversation. Technical arguments and payloads may be expandable or live in a dedicated debug surface.

Group consecutive low-level operations when users benefit from understanding one higher-level task. Do not force all tool results into one generic card: search results, tables, charts, files, validation, and forms need representations suited to their meaning.

## 5. HITL and approvals

HITL is more important than ordinary tool activity. Use a Level 1 container with an obvious purpose, required fields, local validation, keyboard access, and one clear primary action. Keep fields themselves stable rather than glassy.

Approval actions may use Level 2. Dangerous actions must communicate risk with text or icon meaning, not translucency or color alone.

## 6. Progress and subagents

Progress should be persistent, compact, stateful, and non-distracting. Prefer one stable checklist or activity group over many spinners and shimmer effects.

Subagents normally appear as execution structure, not duplicated chat participants. Allow expansion when they produce meaningful independent outputs.

## 7. Charts, tables, reports, and artifacts

Charts, tables, code, reports, and artifact content are Level 0 surfaces. Optimize reading, scanning, and numeric alignment. Their compact toolbars may use glass.

Artifact layouts may place conversation beside a viewer when enough width exists. When space is constrained, preserve the primary task and move or overlay the secondary pane.

## 8. Files and citations

File rows should communicate type, name, state, size when useful, and available actions. Keep them solid with subtle hover feedback.

Citations should remain compact. A temporary source preview may use Level 1 glass; avoid permanent large source cards after every paragraph.

## 9. Composer

The composer is one of the strongest persistent glass candidates. Preserve multiline growth, attachments, tool or mode state, a clearly primary Send action, and a stable loading layout.

Tool selection should open a compact popover; selected tools may become chips. Do not turn the composer into a dense toolbar.

Follow the product's existing in-flow or floating layout instead of imposing one.

## 10. Empty and error states

Empty states should say:

```text
What is absent
Why that matters here
What the user can do next
```

Allow titles to wrap. Keep at most one visually primary action; put secondary help in text or a link.

Errors should be explicit and local, with clear recovery. Avoid heavy red glass backgrounds.

## 11. Streaming and event architecture

Streaming should update stable semantic objects rather than creating a card for every transport event. Avoid flashing backgrounds, repeated skeleton replacement, and composer movement.

Prefer a separation such as:

```text
Transport event
↓
Semantic UI event
↓
State
↓
Renderer
```

Reuse an equivalent architecture when one exists. Do not introduce a second dispatcher or renderer registry merely to support visual changes.

## 12. Visual priority

Highest:

```text
required user interaction
final answer
critical error
primary result
```

Medium:

```text
artifact
chart
HITL context
task progress
```

Low:

```text
reasoning
technical tool details
raw arguments
debug metadata
```

Keep one high-emphasis action per local region. Destructive actions may stay outline or text treatments until confirmation.

Use one selected-state pattern across lists and keep it independent from `focus-visible`. Use semantic colors in small areas such as icons, status dots, badges, or a narrow selection rail, paired with text or icon meaning.

## 13. Final review

* Chat is not a collection of glass bubbles.
* Reasoning is visually secondary.
* Tool activity exposes meaningful lifecycle states.
* Raw payloads do not dominate the primary workflow, while dedicated debug views remain readable.
* HITL is obviously interactive.
* Charts, tables, code, reports, and artifacts stay stable and legible.
* Composer is the strongest persistent glass surface.
* Streaming does not create layout instability.
* Primary content remains readable when secondary panels are open.
* Interaction states remain accessible.
* No unnecessary dependency or duplicate architecture was introduced.
