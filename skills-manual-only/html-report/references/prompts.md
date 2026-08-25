# HTML report prompts by scenario

Prompt library for the `html-report` skill, drawn from Anthropic's [Using Claude Code: The unreasonable effectiveness of HTML](https://claude.com/blog/using-claude-code-the-unreasonable-effectiveness-of-html) (Thariq Shihipar, May 2026). Each branch lists what it is for and the prompts to follow. Swap the bracketed subject for the actual one. Prompts marked ✏️ come from the article nearly verbatim; the rest are the patterns the article names.

## Planning, exploration, and specs

A rich canvas for diving into a problem: brainstorm options, expand into mockups, then write an implementation plan.

Use for: exploring ways to implement something; experimenting with multiple visual designs at once; turning a problem into a web of reference files for a later implementation session.

✏️ "I'm not sure what direction to take the [onboarding screen]. Generate 6 distinctly different approaches—vary layout, tone, and density—and lay them out as a single HTML file in a grid so I can compare them side by side. Label each with the tradeoff it's making."

✏️ "Create a thorough implementation plan in an HTML file; be sure to make some mockups, show data flow, and add important code snippets I might want to review. Make it easy to read and digest."

## Code review and understanding

Render diffs, annotations, flowcharts, and modules so code becomes readable.

Use for: writing a PR; reviewing a PR; explaining a topic in code to someone unfamiliar with it.

✏️ "Help me review this PR by creating an HTML artifact that describes it. I'm not very familiar with the [streaming/backpressure] logic, so focus on that. Render the actual diff with inline margin annotations, color-code findings by severity, and whatever else might be needed to convey the concept well."

## Design and prototypes

Sketch a design in HTML even when the end surface is not HTML; prototype interactions with knobs and sliders.

Use for: design system artifacts; adjusting components; visualizing component libraries; prototyping animations and interactions.

✏️ "I want to prototype a new [checkout button]; when clicked it does a [play animation] and then turns [purple] quickly. Create an HTML file with several sliders and options for me to try different options on this animation, and give me a copy button to copy the parameters that worked well."

## Reports, research, and learning

Synthesize information across sources into a readable report, explainer, deck, or slideshow; use SVG for diagrams.

Use for: feature summarizations; explainers; weekly status reports; incident reports; SVG illustrations, flowcharts, and technical diagrams.

✏️ "I don't understand how our [rate limiter] actually works. Read the relevant code and produce a single HTML explainer page: a diagram of the [token-bucket] flow, the 3–4 key code snippets annotated, and a 'gotchas' section at the bottom. Optimize it for someone reading it once."

## Custom editing interfaces

A throwaway editor purpose-built for one piece of data: not a product, a single HTML file for exactly what you're working on. Always end with an export — a copy button that turns what you did in the UI back into something you can paste into the agent or commit to a file.

Use for: reordering, triaging, or bucketing anything (tickets, test cases, feedback); editing structured config (feature flags, env vars, JSON/YAML with constraints); tuning prompts, templates, or copy with live preview; curating datasets (approve/reject rows, tag, export); annotating a document, transcript, or diff; picking values that are painful to express in text (colors, easing curves, crop regions, cron schedules, regexes).

✏️ "I need to reprioritize these 30 [Linear tickets]. Make me an HTML file with each ticket as a draggable card across Now / Next / Later / Cut columns. Pre-sort them by your best guess. Add a 'copy as Markdown' button that exports the final ordering with a one-line rationale per bucket."

✏️ "Here's our [feature flag] config. Build a form-based editor for it; group flags by area, show dependencies between them, warn me if I enable a flag whose prerequisite is off. Add a 'copy diff' button that gives me just the changed keys."

✏️ "I'm tuning this [system prompt]. Make a side-by-side editor: editable prompt on the left with the variable slots highlighted, three sample inputs on the right that re-render the filled template live. Add a character/token counter and a copy button."
