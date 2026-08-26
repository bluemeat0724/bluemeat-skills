# Apple Glass UI — Foundations

Framework-independent guidance for restrained glass interfaces using the current product's existing frontend stack.

## 1. Map concepts onto existing tokens

Inspect the current token system before adding values. Reuse its semantic surface, text, border, status, radius, shadow, motion, overlay, and theme tokens.

| Glass concept | Map to |
| --- | --- |
| Translucency | Existing surface color with alpha |
| Blur | Existing blur scale or a restrained native CSS value |
| Rim | Existing neutral border with reduced opacity |
| Elevation | Existing shadow scale |
| Radius | Existing shape hierarchy |
| Motion | Existing duration and easing tokens |
| Theme | Existing light/dark or color-scheme mechanism |

Add a semantic token only when a repeated role cannot be expressed safely with current tokens. Do not create a parallel glass token family by default.

## 2. Basic material

A minimal native CSS surface can look like:

```css
.glass-surface {
  background: color-mix(in oklab, var(--surface) 78%, transparent);
  border: 1px solid color-mix(in oklab, var(--border) 60%, transparent);
  backdrop-filter: blur(8px) saturate(1.08);
  box-shadow: var(--elevation-medium);
}
```

The names and values are illustrative. Map them to the product's existing system and tune from rendered evidence.

The opaque fallback must remain readable. Blur is progressive enhancement, not a structural dependency.

## 3. Backdrop and local light fields

Blur cannot create detail that is absent behind the surface. A visible material needs bounded color or shape variation crossing the target.

Keep decorative light fields:

* behind glass, never above content
* inside the nearest clipping boundary
* away from long reading surfaces
* faded before the boundary
* subtle enough that the interface still reads without blur

Avoid full-screen glows that tint every content surface.

## 4. Edges and highlights

Use a thin rim, restrained inset highlight, and soft shadow. A directional pseudo-element may help, but skip it for a one-off surface unless the effect materially improves visibility.

Highlights should be perceived, not seen as white paint. Do not increase blur, alpha, border, shadow, and highlight simultaneously.

## 5. Surface types

### Content surface

Opaque or nearly opaque, high contrast, little shadow. Use for text, forms, code, data, charts, logs, and documents.

### Floating glass surface

Moderate opacity, restrained blur, clear rim, compact shadow. Use for popovers, menus, floating controls, and small temporary panels.

### Strong glass surface

Use sparingly for a composer, selected floating toolbar, or important temporary control. It may have stronger separation or highlight, but should not become a repeated card style.

## 6. Themes and transparency preferences

Tune light and dark materials separately. Dark surfaces often need a more opaque base and weaker white highlights; light surfaces need enough tonal separation to avoid becoming a white wash.

Respect the product's existing theme mechanism. Do not build a parallel theme selector system.

Provide a reduced-transparency path with solid or nearly solid surfaces and hidden decorative light fields. Information must not depend on translucency.

## 7. Controls

Keep ordinary controls in the existing component system. Reserve liquid accent treatment for one high-value action in a local region.

Selection and focus are different states:

* selection may use a soft fill and narrow indicator
* `:focus-visible` needs its own clear outline or ring
* danger needs text or icon meaning in addition to color

Avoid exaggerated hover scaling and motion that shifts surrounding layout.

## 8. Motion

Keep interaction motion short and responsive. Prefer opacity, transform, color, border, and shadow transitions.

Avoid continuously animating blur, backdrop filters, large gradients, or many shimmer effects. Respect `prefers-reduced-motion` through the existing global fallback, or add one shared fallback if none exists.

## 9. Common components

* **Composer:** may be strong Level 1 glass; preserve multiline growth, focus behavior, attachment state, and stable loading layout. It may be in-flow or floating—follow the current product.
* **Sidebar:** subtle glass with strong structural separation and a clear selected state; it should not compete with main content.
* **Popover/menu:** a good glass candidate because it is small and temporary; keep it readable over light and dark backdrops.
* **Dialog:** glass may wrap the outer shell; keep large inner content sections solid.
* **Inputs:** usually solid. Glass is most suitable for search, command palettes, composers, and floating filters.
* **Tables/charts/code:** keep the content surface solid; only surrounding controls may use glass.

Avoid nested sequences such as glass dialog → glass section → glass form → glass input.

## 10. Constraint-driven responsiveness

Device labels are proxies; available container width is the real constraint.

Diagnose from the outside in:

1. reproduce the real panel, data, theme, and zoom state
2. compare document and component `clientWidth` / `scrollWidth`
3. find the first descendant whose intrinsic minimum exceeds its parent
4. fix the shared parent or control rule before clipping local overflow

Common minimal fixes include `min-width: 0` on grid/flex children, `width: 100%` on form controls, wrapping long identifiers, aligned nested breakpoints, and container queries.

Horizontal scrolling is appropriate for inherently wide code or data, not for a page shell or ordinary form.

Set a practical readability floor for the primary task. Collapse or overlay an auxiliary panel before compressing the main content below it.

## 11. Performance and fallback

Avoid many large blurred surfaces, full-screen animated filters, blur in long scrolling lists, and filter-heavy chart containers. A few control-layer surfaces usually suffice.

Verify the interface with backdrop blur disabled. It must remain legible, spatially clear, and operable.

## 12. Review checklist

* Glass is selective and visible while idle.
* Content remains high contrast.
* Backdrop variation crosses each intended glass surface.
* Radius and shadow follow the existing product hierarchy.
* Light, dark, reduced-motion, and reduced-transparency states work.
* Focus remains independent from selection and material highlights.
* Nested layouts respond to available container width.
* The primary task remains readable with auxiliary panels open.
* Forms and page shells do not create unintended horizontal overflow.
* No unnecessary visual dependency or abstraction was introduced.
