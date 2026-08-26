---
name: apple-glass-ui
description: 改进、评审或重构 Web 界面的玻璃质感、视觉层级与响应式布局时使用。克制的 Apple 风设计语言：玻璃用于导航、composer 和浮层等控制层，内容面保持稳定、高对比；复用现有技术栈，只动视觉不动行为。
disable-model-invocation: true
---

# Apple Glass UI

Create refined, lightweight, spatial interfaces without imitating Apple products literally. Treat glass as a control-layer material, not a universal card style.

## Constraints

* Preserve behavior, accessibility semantics, state management, routing, forms, shortcuts, and data flow.
* Inspect and reuse the existing design system, components, tokens, utilities, icons, and animation patterns.
* Prefer native CSS. Do not add UI, animation, glass-effect, SVG-filter, WebGL, or component dependencies unless explicitly requested.
* Treat reference sites and screenshots as evidence, not templates. Extract hierarchy, density, spatial behavior, and validation methods; do not copy brand colors, exact dimensions, breakpoints, information architecture, or component structure without a product-specific reason.
* If a missing choice would materially change the result, prefer built-in user-input tools exposed by the current agent runtime — e.g., `request_user_input`, `ask_user_question`, `ask_user`, `AskUserQuestion`.

## Surface hierarchy

### Level 0 — Content

Use opaque or nearly opaque, high-contrast surfaces for messages, reports, tables, charts, code, forms, logs, and document previews.

### Level 1 — Glass

Use restrained translucency, backdrop blur, a thin rim, and soft elevation for navigation, composers, toolbars, popovers, dialogs, and temporary interaction surfaces.

### Level 2 — Liquid accent

Reserve stronger highlight and press feedback for a few high-value actions such as Send, Run, Approve, or a selected mode. Never use it for repeated content cards.

Strong glass should occupy a small part of the page. Do not nest strong glass inside strong glass.

## Core model

Visible glass needs all four:

1. **Backdrop variation** — bounded color or shape detail directly behind the surface.
2. **Translucent material** — alpha, blur, saturation, and optional contrast.
3. **Edges and depth** — a subtle directional highlight, rim, and elevation.
4. **Spatial separation** — margin, radius, overlap, or shadow that distinguishes the surface from the page.

Blur over a flat backdrop remains visually inert. Diagnose the backdrop path before increasing blur.

## Workflow

### 1. Inspect the real interface

Read the current design tokens, global styles, shared primitives, application shell, and representative content and control surfaces. Trace existing layout, themes, interaction states, responsive rules, motion fallbacks, and component reuse before editing.

Do not begin by creating components or replacing the design system.

### 2. Define visible success

Name:

* which surfaces should read as glass while idle
* which dense surfaces must remain Level 0
* the intended intensity: subtle, clearly visible, or showcase
* one observable acceptance sentence

Capture a baseline at the real target viewport, theme, data, panel state, and zoom.

### 3. Fix hierarchy before effects

First improve spacing, alignment, width, density, typography, grouping, and control placement.

Reduce competing emphasis:

* keep one visually dominant action per local region
* use semantic color on small indicators, icons, badges, or selection rails rather than tinting whole content surfaces
* use one selected-state language across the product; keep keyboard focus independent
* make secondary process detail quiet when collapsed and clear when expanded
* let empty-state titles wrap and explain the next useful action

Glass must not hide poor layout structure.

### 4. Diagnose real layout constraints

Responsive behavior depends on the space a component receives, not a device label.

* reproduce the issue with actual sidebars, inspectors, data, theme, and zoom
* compare `clientWidth` and `scrollWidth` from the document to the first overflowing descendant
* inspect grid/flex children, form controls, long identifiers, and intrinsic minimum widths
* fix the shared constraint first with `min-width: 0`, `width: 100%`, wrapping, or parent-layout changes
* use container queries when viewport breakpoints cannot express the actual constraint

Protect the primary task when space is scarce. Collapse, overlay, or move an auxiliary inspector before squeezing conversation, code, tables, or forms below a readable width. Reuse the same panel instead of creating a second mobile-only implementation unless behavior differs.

### 5. Prove the backdrop path

Inspect the target surface and every ancestor between it and the intended light field. Look for opaque backgrounds, stacking contexts, isolation, clipping, and preference media queries. Confirm that bounded backdrop variation crosses the target surface.

If the surface samples a flat color, fix the backdrop or geometry before tuning material values.

### 6. Prototype uncertain visual changes

Temporarily apply candidate material or theme-token changes in the rendered page before editing repository files. Toggle the candidate at the same state and verify it at normal zoom in light and dark contexts.

If a trustworthy A/B comparison is unavailable, keep proven material values and implement independently verifiable hierarchy or layout improvements instead of guessing.

### 7. Implement minimally

Use this order:

```text
Existing component or token
↓
Existing style utility
↓
Native CSS
↓
One shared style after genuine repetition
↓
More complex visual techniques only when required
```

Implement one material layer at a time: shell, floating controls, then optional local light fields. Keep local fields within their nearest clipping boundary. Do not abstract a one-off style.

For deeper material and layout guidance, read `reference/ui-foundations.md`.

For chat, reasoning, tools, progress, HITL, reports, artifacts, and files, read `reference/agent-ui-patterns.md`.

### 8. Validate rendered output

Check:

* light and dark themes
* wide and narrow layouts
* optional side panels open and closed
* hover, focus, active, selected, disabled, loading, empty, and error states
* text contrast and semantic controls
* reduced motion and reduced transparency
* page-level and component-level horizontal overflow
* graceful behavior without backdrop blur

Compare baseline and result at identical states. Keep representative screenshots and layout measurements for overflow or squeezed-content fixes.

Typecheck, unit tests, builds, computed styles, and a non-`none` `backdrop-filter` are mechanism checks only. Visible before/after evidence is the visual completion gate.

## Visual character

Aim for calm, precise hierarchy, soft depth, subtle translucency, quiet separators, controlled radius, and clear typography.

Avoid neon dashboards, heavy glowing borders, excessive gradients, glass content cards, oversized blur, continuous filter animation, and decorative motion without interaction value.

## Completion criteria

* The result visibly improves hierarchy before decoration.
* Glass remains selective and recognizable while idle.
* Dense content stays stable and readable.
* The primary task remains usable at constrained widths.
* Focus and semantic states remain clear without relying on transparency or color alone.
* No unnecessary runtime dependency or parallel design system was introduced.
* Product behavior is unchanged.
