---
name: html-report
description: Build a self-contained HTML report artifact — one .html file, no build, opens anywhere — when a deliverable is too visual, spatial, or interactive for Markdown. User-invoked.
disable-model-invocation: true
---

# HTML Report

Deliver the work as a self-contained **HTML artifact**: one `.html` file with all CSS and JS inline, that opens in any browser and gets read. The point is **staying in the loop** — the reader engages with the report (scans tabs, follows diagrams, tweaks controls) instead of skimming a wall of Markdown, and you stay in the loop too because the artifact is easy to share, review, and edit through the agent.

This skill creates the report only. It changes no application code, tests, or configuration.

## Defaults

- **Self-contained.** One file; all CSS and JS inline. No build step, no CDN, no framework, no network access at view time.
- **Readable first.** A tight summary up top, then the detail in tabs, tables, grids, and SVG diagrams — never a linear prose dump.
- **User's language.** Title, sections, and copy in the user's language.
- **Output path.** `<report-name>-<YYYY-MM-DD>.html` in the working directory unless the user says otherwise.
- **Evidence.** Ground every claim in the gathered context; mark gaps as unknown instead of inventing.

Ask only when the subject, scope, or reader cannot be inferred safely. Record other uncertainty inside the report.

## Decide: HTML or Markdown?

Use HTML when the deliverable is any of:

- **Spatial** — diagrams, grids, side-by-side comparisons, annotated diffs;
- **Dense** — tables and interlocking facts, a spec too long to read as a scroll;
- **Interactive** — sliders, sorting, live preview, or a small purpose-built editor;
- **Shared** — anyone beyond you will open it; a link beats an attachment.

Use Markdown when the deliverable is a short linear note with no structure to visualize.

## Process

### 1. Frame the job

Name the reader and the one thing the report must do for them. Read the files, history, data, or sources it is about.

**Complete when:** the reader and the job are stated, and every claim you can check has a source.

### 2. Choose a branch

Load [references/prompts.md](references/prompts.md). Pick the branch that matches the job — planning and exploration, code review and understanding, design and prototypes, reports and explainers, or custom editing interfaces — take its prompt, fill the blanks with the gathered context, and follow it.

**Complete when:** the branch prompt is fully filled in and matches the reader's job.

### 3. Draft the artifact

Produce the single HTML file per the prompt. Structure it for a skim: summary on top, then tabs, cards, grids, and SVG diagrams rather than prose walls. For any interactive piece, end with an **export** — a button that copies what the user did back out as JSON, prompt, Markdown, or diff — so the loop stays closed.

**Complete when:** the file is self-contained, opens standalone, and every section the branch prompt demands exists.

### 4. Verify in the reader's shoes

Walk through the page as the target reader: does the one job get done on a single read? Are all diagrams legible, controls working, links resolving?

**Complete when:** the reader's question is answered without any other file, and the saved path is reported back.
