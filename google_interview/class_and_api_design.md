# “Design this class / API” (L4 coding, not HLD)

Practice folder: **`lld_topics/`** (same idea as `dsa_topics/` for algorithms).

This is still a **coding** round. They want a **clear contract**, then **working methods**. It is **not** “design YouTube.”

## What it looks like

Interviewer: *“Design a type that can … Implement these methods.”*

Examples of the **size**: a cache with `get` / `put`; a stack that also returns min; a logger that drops repeats in 10 seconds; a router that matches a path. You write a **class** (or two), not a datacenter.

## Same ladder as DSA (45 min)

1. **Contract** — list methods: name, arguments, return type, what “not found” means.  
2. **One unit** — what one call changes in memory (one key, one timestamp).  
3. **What you store** — which list / dict / set. Say why in one sentence.  
4. **Code** the methods.  
5. **Dry run** two calls. **Edges:** empty, duplicate key, first vs second call.

Do **not** start with Kubernetes. Do **not** start coding before the method list.

## Language you need (Python)

```text
class Thing:
    def __init__(self, ...):
        ...
    def method(self, ...):
        ...
```

`self` = this object’s box. Data lives on `self.something`, not in a global.

You already practice I/O on problems. Here I/O is **the method list**.

## How to prepare (after more Python + DSA, not week 1)

**Once a week, 30–40 min, no AI:**

1. Pick **one** tiny design-as-code problem (LRU cache, min stack, “logger rate limit”).  
2. **Paper first (5 min):** write only the method signatures + what each field stores.  
3. **Then code** and dry-run two sequences of calls.  
4. Name time of `get` / `put` (`O(1)` vs `O(n)`).

Do **not** open a system-design book for this. That is L5 / another month.

## When in your 6 months

- **Months 1–2:** DSA + `range` / lists / `class` basics only.  
- **Month 3+:** one of these a week.  
- If the recruiter says *“3 coding + Googliness, no design”* — keep it light. If they say *“one LLD”* — do two of these a week for 3 weeks.

## Recruiter question

*“Is any onsite ‘design a class / API’ or only algorithm problems?”*
