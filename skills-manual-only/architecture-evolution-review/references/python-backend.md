# Python Backend Architecture Lens

Apply this lens when the inventory finds a first-party Python backend. It is optimized for FastAPI, Pydantic v2, pydantic-settings, and SQLAlchemy 2.x, but judge a sound existing stack on its own merits. These preferences shape the target architecture; they become findings only when code evidence shows change friction, unsafe coupling, or contract risk.

## Preferred Shape

Organize first by business capability, then by responsibility inside each capability:

```text
app/
├── main.py                 # composition root and lifespan
├── settings.py             # the single Settings root
├── shared/                 # small, stable, jointly owned concepts only
└── <capability>/
    ├── api/                # FastAPI routes and HTTP/SSE mapping
    ├── application/        # use cases, transactions, ports
    ├── domain/             # rules, invariants, state transitions
    └── infrastructure/     # SQLAlchemy and external adapters
```

Names may differ. Responsibilities and dependency direction matter more than matching this tree.

Allowed source dependencies:

| Source | May depend on |
|---|---|
| `domain` | domain code and Python/Pydantic primitives needed for invariants |
| `application` | its domain and narrow ports owned by the application/domain |
| `api` | application entry points and transport contract models |
| `infrastructure` | domain/application contracts that its adapters implement |
| composition root | every concrete component needed to assemble the service |

Capability A calls Capability B through B's public application entry point or documented contract. It does not import B's route, ORM model, repository implementation, session, or private service. The composition root is the intentional exception that knows concrete implementations.

## Objects and Functions

Prefer an object when it owns cohesive state, lifecycle, resources, injected dependencies, or a stable module responsibility. Typical objects include application services/use cases, gateways, repositories, resource clients, registries, and `Settings`.

Prefer a function for stateless calculation, conversion, parsing, and validation. Favor composition over inheritance.

Treat these as evidence of weak encapsulation when they obstruct change:

- a god service with unrelated reasons to change;
- state or resources hidden in module globals;
- static-only utility classes;
- objects that merely rename one function call;
- constructors with dependencies unrelated to most methods;
- base classes used only to share a few helpers;
- an interface paired with one implementation and no real boundary need.

Use `Protocol` for a genuine external or replaceable boundary, or where isolation from infrastructure materially improves the application layer. Do not mirror every concrete class with a protocol.

## Settings

Prefer one immutable root `Settings` based on `pydantic-settings`, created once at the composition root and injected where needed. Nested groups such as database, auth, and integrations are still one root. Application code does not scatter `os.getenv`, environment reads, `.env` parsing, or alternate settings singletons.

Classify every setting:

- **Required:** secrets, production database and queue endpoints, authentication/security controls, and settings whose fallback could corrupt or expose data. Missing or invalid values fail startup.
- **Fallback-capable:** ordinary tuning and optional features with a safe, documented default. Missing values use the default; invalid values may fall back only through the centralized loader and must emit a redacted startup warning.

Environment variables drive deployment-specific values. Defaults are visible in the model, not duplicated in callers. Never log secret values. Report multiple configuration sources, import-time environment reads, mutable settings, and silent fallback of required settings as boundary problems.

## Pydantic Model Boundaries

Model all data that crosses a meaningful boundary. This includes requests, responses, error payloads, SSE events, capability catalogs, application commands/results, and external integration payloads. Prefer explicit models and discriminated unions over `dict[str, Any]`, magic strings, or ad hoc serialization.

Keep semantic roles distinct:

- transport models define HTTP/SSE compatibility;
- application/domain models express use-case intent and invariants;
- SQLAlchemy models define persistence;
- integration models describe external provider contracts.

Reuse a type only when its meaning, lifecycle, and compatibility policy are genuinely the same. An ORM model is not an API response by convenience, and a request model is not a domain entity merely because its fields match today. Mapping code is worthwhile when it protects a real contract boundary; avoid ceremonial copies between identical internal shapes.

Inspect validators and serialization for hidden I/O, business workflows, lossy conversions, permissive unknown fields at trust boundaries, and accidental exposure of private ORM fields.

## FastAPI Boundary and Dependency Injection

Keep routes thin: validate transport input, invoke one application entry point, and map the result to the transport contract. Authorization may live at the transport boundary; business permission rules belong with the use case/domain rule they protect.

FastAPI `Depends`, `Request`, `Response`, `HTTPException`, status codes, and framework middleware types stop at `api` or composition code. Assemble request-scoped objects there, then use explicit constructor injection inside the application. Avoid service locators and mutable global dependency registries.

Own long-lived engines, pools, HTTP clients, and registries in application lifespan. Do not recreate them per request. Keep blocking calls off the event loop; use async only where the call path performs concurrent I/O rather than as a universal style rule.

## Transactions and Persistence

The application use case owns the transaction boundary. A route never commits, rolls back, queries an ORM session, or returns an ORM object as its contract.

Use Repository/UoW when aggregates, multi-step writes, multiple persistence operations, or infrastructure isolation justify them. For simple CRUD, one cohesive data-access object is enough; do not stack repository interface, implementation, and UoW by ceremony.

Keep database invariants in database constraints and migrations. Keep business invariants in the domain/application owner. Check that session lifetime, commit/rollback ownership, lazy loading, and exception conversion remain inside the persistence boundary.

## Error Direction

Domain/application code exposes semantic failures independent of HTTP and SQLAlchemy. Infrastructure adapters catch provider/driver errors when they can add context or translate them into an application-understood failure. API-level handlers map semantic failures to stable Pydantic error responses.

Report framework exceptions crossing inward, driver exceptions leaking outward, broad catches that erase causes, and multiple routes independently mapping the same application failure.

## Contract Impact Boundaries

Inventory these four boundaries:

1. public APIs, including HTTP and SSE payload/event semantics;
2. persisted data, including schema meaning and migration compatibility;
3. user-visible behavior;
4. deployment interfaces, including environment variables, commands, ports, health behavior, and process topology.

They do not justify retaining a worse internal design. Preserve one only when real consumers, durable data, user expectations, or deployment requirements make a break costly. Otherwise redesign it directly. A break must state the benefit, affected consumers/data/deployments, migration, verification, rollback, and removal date for any compatibility code.

## Python Backend Evidence Pass

Before deciding, add this evidence to the main review ledger:

1. Map every route, worker, CLI, scheduler, and lifespan hook to its application entry point.
2. Build the first-party import direction between capabilities and responsibilities; identify cycles and inward dependencies on frameworks/infrastructure.
3. Locate every environment read and settings instance; classify each setting as required or fallback-capable.
4. Classify Pydantic, domain, ORM, SSE, and integration models by semantic role; record accidental cross-layer reuse and unmodeled dictionaries.
5. Identify session/resource lifetime, transaction owner, and exception translation for every write flow.
6. Trace each contract boundary to its defining model/schema/configuration and any real consumers, compatibility test, or migration.

The pass is complete when every discovered entry point, settings source, model family, write transaction, long-lived resource, and contract boundary is owned by a named layer or recorded as unknown. Fold the evidence into the main report sections; do not append a generic Python best-practices checklist.
