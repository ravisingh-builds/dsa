# LLD Progress

Not HLD. Not DSA walk-patterns. Two lists in this file: **how to learn LLD** (order from the LLD 101 roadmap) and **lld_google_interview** (one type you code).  
Legend: 🔒 locked · 🟡 in progress · ⬜ not started

**Start:** after more Python + a few more DSA locks, unless a recruiter says class/API. How to run a Google class/API problem: [google_interview/class_and_api_design.md](../google_interview/class_and_api_design.md).

**Two round shapes (same skill):** machine coding = running in-memory demo, 90–120 min, no internet. Whiteboard = class diagram, interfaces, pseudocode, 45–60 min, expect interruptions. Working code is the entry ticket for machine coding. Readable, one-job classes and edge cases are the pass.

---

## Learning order

Do these in sequence. A pattern named before phase 3 is memorizing.

| # | Phase | Status | What “locked” means |
|---|----------------------------|--------|---------------------|
| 1 | OOP mechanics              | ⬜ | Class, object, `__init__`, class vs instance data, override. A small class from a blank file. |
| 2 | Four pillars as boundaries | ⬜ | Encapsulation, abstraction, inheritance, polymorphism. Say what the caller may touch, and what stays hidden. |
| 3 | Relationships              | ⬜ | Label the problem association, aggregation, or composition before you name classes. |
| 4 | SOLID                      | ⬜ | Split one god class and name the letter you applied. |
| 5 | Interface vs abstraction   | ⬜ | Interface = behavior contract. Abstract type = shared blueprint (`Vehicle` → car / bike / truck). |
| 6 | Patterns, three buckets    | ⬜ | Use one only when it shortens the design. Say why the neighbor pattern is the wrong tool. |
| 7 | UML                        | ⬜ | Class diagram plus one sequence (book seat → pay → ticket). |
| 8 | Problems, then a mock      | ⬜ | Paper model, in-memory code, a demo you can run, then one new requirement. |
| 9 | Concurrency                | ⬜ later | Threads. Uber, Walmart, Flipkart lean on this. After 1–8. |

### Relationships (phase 3)

One question: if the parent disappears, does the child still make sense?

| # | Kind | Status | Picture |
|---|-------------|----|---------|
| 1 | Association | ⬜ | Both live alone. Teacher and student. Vehicle and parking spot (car exists before park and after leave). |
| 2 | Aggregation | ⬜ | Whole holds parts; parts survive. Library and books. Splitwise group and users. Movie outlives one theater. |
| 3 | Composition | ⬜ | Part dies with the whole. House and room. Screen and seat. Lot and level. Board and cell. Machine and slots. |

### SOLID (phase 4)

| # | Letter | Status | One line |
|---|--------|--------|----------|
| 1 | S — single responsibility | ⬜ | One class, one reason to change. User, repository, and email service are three classes. |
| 2 | O — open/closed           | ⬜ | New behavior is a new class. The old class stays. |
| 3 | L — Liskov                | ⬜ | A child stands in for its parent. The caller does not break. |
| 4 | I — interface segregation | ⬜ | Small interfaces. No method the caller never uses. |
| 5 | D — dependency inversion  | ⬜ | High-level code depends on an abstraction, so the concrete piece can be swapped. |

### Patterns (phase 6) — creational, then structural, then behavioral

| # | Bucket | Status | Know these, from a problem |
|---|--------|--------|----------------------------|
| 1 | Creational — how objects are born | ⬜ | Singleton (one config / pool). Factory (vehicle, notification channel). Builder (booking: snacks, discount, seat prefs filled step by step). |
| 2 | Structural — how objects are wired | ⬜ | Adapter (two plugs that do not match). Decorator (add-on at runtime: topping, caramel). |
| 3 | Behavioral — how objects decide | ⬜ | Strategy (nearest elevator / entry / exit). Observer. State. |

---

## Seven steps (every practice row)

1. Clarify (spots per vehicle, floors, hold-before-pay, currencies, double booking).
2. Nouns, then drop the ones that are fields (price lives on booking, seat number lives on seat).
3. Who owns whom, and which relationship, and one-to-one or one-to-many.
4. Classes: fields, methods, interfaces.
5. SOLID on the simple version.
6. A pattern only if the demo already works.
7. Edges: cancel, hold, payment fail, timeout.

Paper only, five apps on your phone, steps 1–3, before coding any of the ladder.

---

## Practice ladder

Start here. Ride-hailing is last.

| # | Problem | Relationship to spot | Status |
|---|---------|----------------------|--------|
| 1 | Library | Aggregation: library and books | ⬜ |
| 2 | Movie booking | Composition: screen and seat. Edges: hold, cancel, payment fail | ⬜ |
| 3 | Parking lot | Association: vehicle and spot. Composition: lot and level. Strategy for allocation. | ⬜ |
| 4 | Splitwise | Aggregation: group and users. Currency is a clarification. | ⬜ |
| 5 | Vending machine | Composition: machine and slots. Then state. | ⬜ |
| 6 | Ride-hailing or food delivery | After 1–5 | ⬜ later |

---

## lld_google_interview

Google L4 “design this class / API” is a **coding** round: method list, what you store, working methods, cost of `get` / `put`. It is not “design YouTube,” and it is not the parking-lot ladder above. Cadence once this track is open: 30–40 min, paper signatures first. See [class_and_api_design.md](../google_interview/class_and_api_design.md).

### Themes

| # | Theme | Status | Meaning |
|---|--------|--------|---------|
| 1 | Contract first (method list + what you store) | ⬜ | Paper signatures before code |
| 2 | Stateful object (`class` / `self`) | ⬜ | Data lives on the instance |
| 3 | Time of `get` / `put` named | ⬜ | `O(1)` vs `O(n)` for each method |

### Problems

| # | Problem | Folder | Status |
|---|---------|--------|--------|
| 1 | Min stack | `min_stack/` | ⬜ |
| 2 | LRU cache | `lru_cache/` | ⬜ |
| 3 | Logger rate limit (10s) | | ⬜ |

**In the room:** requirements first, one job per class, a reason for every pattern, think out loud, finish one class before the next, end machine coding with a demo.

**Next:** don’t open either list until sketch HLD #1 is done this week **and** DSA for the week is done. When this track opens, Google problems start at min stack. The learning order starts at phase 1, then relationships, before any practice-ladder code.
