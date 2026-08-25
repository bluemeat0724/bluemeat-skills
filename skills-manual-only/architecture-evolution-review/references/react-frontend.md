# React Frontend Architecture Lens

Apply this lens when the inventory finds a first-party React frontend. It is optimized for React with TypeScript, Tailwind CSS, shadcn/ui, and Zustand. Preserve sound project and router conventions. Do not introduce a state, form, query, styling, or design-system dependency merely to match this lens.

These preferences shape the target architecture. Turn them into findings only when repository evidence shows unclear ownership, difficult change, contract risk, or degraded accessibility.

## Preferred Shape

Organize by business feature, with a small application shell and shared base:

```text
src/
├── app/                    # router, providers, layouts, composition
├── features/
│   └── <capability>/
│       ├── components/
│       ├── hooks/
│       ├── api/
│       ├── store/          # only when the feature needs shared client state
│       └── types.ts
├── components/ui/         # local shadcn/ui primitives
└── shared/                # small, stable, non-feature-specific code
```

Names may follow the framework. Ownership and dependency direction matter more than matching the tree.

Dependency rules:

- `app` composes features and shared providers.
- a feature owns its UI, workflows, API calls, and client state;
- one feature reaches another through a narrow public entry point, not its internal component, hook, store, or request module;
- `shared` and `components/ui` never import feature code;
- route files stay thin when the router already supplies a route convention.

Keep code near the feature that changes with it. Promote code to `shared` only after its meaning and change cadence are genuinely shared.

## State Ownership Ladder

Use the first rung that owns the state correctly:

1. derive it during render from existing inputs;
2. keep interaction state in the nearest component;
3. place shareable navigation state such as filters, pagination, tabs, and selected identifiers in the URL;
4. let an already-installed server-state/query layer own remote data and caching;
5. use a feature-scoped Zustand store for client state shared across distant components, pages, or a multi-step workflow.

Do not copy server responses into Zustand as a second source of truth. Do not build a query cache inside Zustand. Avoid an application-wide store that mixes unrelated features, generic global `isLoading`/`error` flags, whole-store subscriptions, actions that mutate another feature's internals, and persisted state without an explicit compatibility policy.

State selectors should expose the smallest stable value a component needs. Store actions own state transitions; components should not reconstruct the same transition in multiple places.

## Components, Hooks, and Effects

Keep straightforward rendering, local state, and event handling together so the component reads top to bottom. Extract a component or hook when it creates a named responsibility, isolates a cohesive effect/async workflow, or has demonstrated reuse. Do not enforce container/presenter pairs or one-file-per-tiny-component ceremony.

Calculate derived values during render. Use event handlers for user-triggered work. Use `useEffect` to synchronize with an external system such as a subscription, timer, browser API, or imperative widget—not to copy props into state, derive values, or coordinate an action that belongs in an event/use-case function.

Report hooks that hide unrelated workflows, component trees coupled through prop drilling despite an existing closer owner, duplicated state, and effects used as an implicit workflow engine when they materially obstruct change.

## Tailwind and shadcn/ui

Treat shadcn/ui components as locally owned source. Compose or edit them directly while preserving their accessibility behavior. Do not wrap every primitive in a second project-specific component layer.

Use Tailwind theme tokens, CSS variables, `cn`, and existing `cva` variants for repeated visual states. Create a higher-level component when it captures repeated business meaning or interaction, not merely a different class string. Keep feature-specific styling with its feature; keep truly global tokens in the application theme.

Preserve keyboard behavior, visible focus, semantic elements, labels, ARIA relationships, portal/dialog focus management, responsive layouts, contrast, and reduced-motion handling. Accessibility is a correctness boundary, not an optional cleanup.

## API and SSE Contracts

Centralize base URL, authentication, headers, transport errors, cancellation, and decoding in a thin typed client or an existing request layer. Feature API modules define capability-specific calls. Components do not scatter raw `fetch`, endpoint strings, status interpretation, or response casts.

Prefer types generated from the backend OpenAPI document when a reliable generation workflow already exists. Otherwise keep explicit TypeScript request/response types next to the feature and avoid building a new generator solely for architecture symmetry.

Model SSE and other event streams as discriminated unions with stable event names and payload types. Handle unknown events explicitly, define reconnect/cancellation ownership, and keep transport parsing outside presentation components.

The backend remains authoritative for validation and business rules. Frontend types protect developer-facing compatibility but do not make untrusted runtime data safe by themselves. Reuse an existing runtime validator when present; do not add one only to duplicate Pydantic rules.

## Forms and Async UI

Use native HTML constraints and simple React state for simple forms. Reuse an existing form/schema library for genuinely complex, repeated, or interdependent forms. Client validation provides timely feedback; it does not duplicate the full backend rule set.

Each async feature owns its loading, empty, failure, success, cancellation, and retry behavior near the surface that renders it. Use error boundaries for unexpected render failures, not ordinary request errors. Preserve the user's input and focus across recoverable failures where practical.

## Contract Impact Boundaries

Apply the main skill's four impact boundaries to the frontend:

1. public API and SSE types connect to backend contracts and consumers;
2. persisted browser data has an explicit schema/version and migration when its meaning changes;
3. user-visible behavior includes navigation, interaction, focus, loading/error semantics, and accessibility;
4. deployment interfaces include public environment variables, asset/base paths, build commands, and runtime hosting assumptions.

Do not preserve old frontend structure merely to avoid rewriting it. Preserve a boundary only when real users, durable browser data, backend consumers, or deployments make a break costly. A proposed break needs affected users/consumers, migration, verification, rollback, and removal of temporary compatibility code.

## React Frontend Evidence Pass

Before deciding, add this evidence to the main review ledger:

1. Map every route/page and core user flow to its owning feature and backend contracts.
2. Build first-party import direction among `app`, features, shared code, and UI primitives; identify feature cycles and leaked internals.
3. Classify important state as derived, local, URL, server-owned, or Zustand-owned; locate duplicated sources of truth and persisted-store contracts.
4. Locate raw requests, API clients, OpenAPI generation, SSE parsing, response/error mapping, and cancellation ownership.
5. Trace effect-heavy components and custom hooks to the external system or workflow they own.
6. Inspect shadcn modifications, wrapper layers, Tailwind tokens/variants, and shared components for real ownership.
7. Verify loading, empty, failure, success, retry, keyboard, focus, semantics, responsive, and reduced-motion behavior for every core flow that can be inspected.

The pass is complete when every discovered route, core flow, shared store, request/event boundary, shared component, and frontend contract boundary has a named owner or is recorded as unknown. Fold the evidence into the main report; do not append a generic React checklist.
