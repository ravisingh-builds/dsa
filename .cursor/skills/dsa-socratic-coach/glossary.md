# DSA Reasoning Glossary — QnA

**Scope: DSA problem-reasoning vocabulary only** (how to read a problem, what counts as "the same" answer, contract-level words). Not Python/programming mechanics — those live in [glossary-python.md](glossary-python.md).

Reusable across problems and patterns. Ask **one** entry at a time when quizzing, same as a pattern's own quiz. Add new terms here as new mix-ups surface — don't duplicate them per-problem. When the user asks for a **DSA** revision session, pull only from this file, not from `glossary-python.md`.

---

## Order vs Position

**Q: What does "order" mean, for a set of values like a triplet?**
A: The sequence you **write them down** in, left to right. `[-1, 2, -1]`, `[2, -1, -1]`, and `[-1, -1, 2]` are the **same three values** in different order.

**Q: What does "position" (or "index") mean?**
A: **Where in the original input array** a value was stored. Position `0` and position `4` can both hold the value `-1` — same value, different position.

**Q: Can two different positions hold the same value?**
A: Yes, whenever the array has duplicate values.

**Q: Does changing the order you write three already-chosen values change which positions they came from?**
A: No. Order is just how you *display* values you've already picked. The underlying positions don't change.

**Q: A problem outputs a list of values (not positions) and says "no duplicate triplets." Does order matter for deciding "duplicate"?**
A: No. `[-1, -1, 2]` and `[2, -1, -1]` count as the same triplet. Only one should appear.

**Q: Then why do brute-force loops usually enforce `i < j < k` on positions?**
A: That's a **search-mechanics** trick to avoid visiting the same **position**-combo twice (or reusing a slot) — it does **not** mean order matters in the *output*. Don't confuse "how I search" with "what counts as the same answer."

---

## Aha — dropping constants in Big-O (2k vs k)

**Aha (user’s words):** `2k` and `k` both grow in a similar way. Same idea: `2k²` and `k²` grow like `k²`. This is the nuance that was easy to miss: we drop the **constant**, not the variable that grows.

**Where it showed up:** 3Sum space — `output` is `k` unique triplets, `seen` is another `k` keys, two real boxes in memory (`~2k`). Named **`O(k)`**, not `O(2k)`. Same move as `n(n-1)/2` → `O(n²)` (drop `-1` and `/2`).

**Q: We have `output` of size `k` and `seen` of size `k`. Do we say `O(2k)` or `O(k)`? Why?**
A: Two different structures, so physically about `2k`. The **name** is `O(k)` because we drop the constant `2`. `2k` and `k` grow the same way when `k` doubles.

**Q: Do we drop `k` itself because `k` is large?**
A: No. We drop **`2`**, not `k`. Dropping `k` would mean constant space. `k` is what grows (number of unique triplets).

**Q: `2k²` vs `k²` — what do we write?**
A: **`O(k²)`**. The `2` is a constant. The `²` stays — that is the shape.

**Q: Same rule as `n(n-1)(n-2)/6` → `O(n³)`?**
A: Yes. Drop constants (`/6`) and lower terms (`-1`, `-2`). Keep the dominant product (`n×n×n`).

---

## Time — units × work (any family)

**Aha:** Last legal **index** is not the **count**. Time is not a memorized `(n-k+1)`. It is: how many **units** you score × how much work **one** unit does.

**Where it showed up:** max-sum of `k` neighbors — `(n-k+1)` starts, `k` adds each. 3Sum — last place `L`/`M`/`R` can sit (`n-3`, `n-2`, `n-1`) is not “that many triplets.”

**Q: What three questions give time, on any pattern?**
A: (1) What is **one unit** I score? (2) How many units? (count first start through last start on a tiny `n`, then `last - first + 1`.) (3) Work **per** unit (adds, compares, a scan of the rest…)? Multiply. Then name Big-O (drop constants; do **not** drop `k` if `k` is part of the input).

**Q: I know the last legal start is `n-k`. Is time `O(n-k)`?**
A: No. `n-k` is an **index**. Number of starts is `n-k+1`. Time also multiplies by work inside each start.

---

## Hunt a skip (after a correct complete search)

**Aha:** Do not stare at the whole problem for hours. Write **two neighbor units** from the walk you already run. Ask: what work did I **repeat**? What can I **prove** I already know?

**Where it showed up:** max-sum of `k` — unit 2 re-adds the middle; unique-run v1 — start `1` rebuilds the tail of start `0`.

**Q: What is the first skip-hunting move?**
A: Paper only two units that sit next to each other in *your* complete search. Circle the letters/adds that appear in **both**. Those are the candidates to skip — only if you can say why they cannot change the bucket.

---

## Compact a correct walk (v5 vs v6)

**Aha:** After the walk is correct, do not invent a new story. List what each branch **does**. Same work vs different work. Then: **when** does the same work run?

**Where it showed up:** longest unique run — v4 three doors; v5 = one shrink door + grow in `else` (next visit); v6 = shrink then grow **this** visit (no `window` name).

**Q: Two questions to compact?**
A: (1) What is the **only** different action? That stays in the `if`. (2) Does the shared action happen on the **next** visit to this letter (v5) or **before** I leave this letter (v6)? Length is `right - left + 1` once the letter is in the run — `window` is only a nickname.

---

## Graph four questions (dot / link / mark / question)

**Aha:** “This is a graph” only helps if you name four things before you walk.

**Q: What are the four questions?**
A: **Dot** — what are the things? **Link** — when does one connect to another (one-way if the problem says “before”)? **Mark** — a dot is used once. **Question** — what must the walk answer?

**Q: Islands vs course prereqs?**
A: Islands: dots = land cells, links = 4-edge, mark = `used` or stamp, question = how many new groups. Courses: dots = `0..n-1`, links = pairs, mark = taken, question = can every dot be taken?

---

## Time name (every problem)

**Aha:** Same five steps after a walk is correct. Not a new method.

**Q: How do you name time in the room?**
A: (1) Name the sizes (`n`, `p`, `k`…). (2) Work that runs **once** → **add**. (3) Repeats **one after another** (walk `n`, then `n-1`) → **add**. (4) Loop **inside** a loop → **multiply**. (5) Drop constants (`2k` → `O(k)`). Swallow a term that cannot grow faster. **Do not drop** a letter that grows (`n`, `p`, `k`).

**Q: Shop story — swallowed vs keep the faster term?**
A: You walk `p` steps to the shop, then `p n` steps inside. If `p = 10` and `n = 100`, that is `10 + 1000`. The name is the inside walk. The door-to-shop `p` is swallowed. Keep `p n` because extra customers (`n`) make only the inside walk blow up.

---

*(Add more DSA-reasoning terms below as they come up — one QnA block per term, same style. Programming-language mechanics go in `python programming revision/glossary-python.md` instead.)*
