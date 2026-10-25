# dsa_2p_find_pair_2 — revision note

Paired with `dsa_2p_find_pair_2.py`.  
**Problem studied:** Container With Most Water (not two-sum). Filename follows this folder’s `dsa_2p_*` pattern.

**For a later AI:** This note is the complete-search stage only. Do **not** teach a faster skip/two-pointer trick unless the user writes `spoil the solution`. Coach from `.cursor/skills/dsa-socratic-coach/`.

**Revision mode:** Ask **one** question from “Quiz (pain-point order)” at a time. Do not dump the quiz. If they miss, teach that one mix-up using their wording below — then ask if they want the next question. Expected answers are for the AI, not to paste first.

---

## Status (locked)

Correct method: score **every** pair `L < R`, keep a max bucket.  
Example: `height = [1, 8, 6, 2, 5, 4, 8, 3, 7]` → **49**.  
Tiny check table: `height = [1, 8, 6, 2]` → max **6** (pair `1,2`).

Not done yet: a proven way to skip pairs.

---

## Contract (understand before code)

| Piece | Locked meaning |
| --- | --- |
| Input | A **list of numbers**. Index = wall position. Value = height. Not “the picture.” |
| One container | **Any two** walls. Not only neighbors. |
| Output | **One number** = water of the **best** pair. Not the two indices. Not a sum of all pairs. |
| Water of one pair | Two steps: `width = R - L`, then `water = shorter_height * width`. Grouping matters: not `height * R - L`. |
| Shorter wall | Water height is capped by the **smaller** of the two walls. |
| Walls in between | Other **candidate pairs**, not extra walls of *this* container. |
| Do not sort | Height is tied to index. Sorting would break width. |

Verbs in the problem: *pick two*, *maximum*. That means **compare** pairs, do **not add** them all.

---

## Mental models (how not to get lost)

1. **Story vs contract** — `def solve(???)` takes data (the list), not the diagram.
2. **One unit first** — define water for **one** pair before thinking about max.
3. **Extra rules** — if the problem didn’t write it (adjacent, add every pair, lock tallest, lock last index), it is a guess.
4. **Complete search** — if you cannot prove a pair is safe to ignore, score it.
5. **Cost** — `n` = `len(height)`. Rows = pairs = `n(n-1)/2`.
6. **Interview path** — correct complete search first; fewer rows only with a proof.

Google grades this **path**, not a LeetCode title.

---

## Method you implemented

Jobs **per pair** (two separate `if`s is fine):

1. Score: `shorter`, `width`, `water`; if `water > max_water`, replace the bucket.
2. Move to the **next** pair. Do not mix move into the water `if`.

How `L`/`R` must walk (complete table):

- Start `L = 0`, `R = 1`.
- If `R` is not at the last index: `R += 1` (same `L`, next right wall).
- If `R` is at the last index: `L += 1` **and** `R = L + 1` (new left wall; `R` must start just right of new `L`, or you skip pairs like `(1,2)`).

Loop condition: `L` must actually change, or `while L < last_index` never ends.

---

## Loop bugs you already found (revision traps)

| Mistake | What went wrong |
| --- | --- |
| `R = L + 1` **inside** every loop | Only neighbors. Adjacent extra-rule. |
| Move `L` but leave `R` at the end | Miss pairs that don’t touch the last wall. |
| Increment `i` but never `L = i` | `L` stuck; infinite loop. |
| `while L < R` with `R` growing | Stop condition fights the search. |
| `from math import small` | No such function. Use builtin `min`. |
| `print("L": j)` | Syntax error; `j` never existed. |
| `else: ValueError(...)` | Does nothing without `raise`. Leftover of `R == last` / `R < last` is `R > last`, not “L > R”. Dead if moves are right. |
| Define `max_water` but never `print(max_water(height))` | Function never runs. |

---

## Complexity (this method)

- **Time** = number of steps ≈ number of pairs = `n(n-1)/2`.  
  Drop `-1` and `/2` **only when naming the shape** → **`O(n²)` time**.
- **Extra space** = memory **you** allocate, **apart from** input `height`.  
  A few variables that do not grow with `n` → **`O(1)` extra space**.  
  `O(1)` means **constant**, not “one list” and not “zero.”

### Big-O, in the words that finally clicked

- `n` = input size (how many heights). **Not** the work.
- **Work** = how many steps (one table row = one step).
- `O(...)` = **name of the shape** of work as `n` grows. Not a new formula.
- Exact count `n(n-1)/2` → ignore `-1` and `/2` for the name → `n*n` → write `O(n²)`.
- Doubling `n` (10 → 20) made pairs 45 → 190 (**about 4×**). That is a **check** that the name `n²` is right. Do **not** write `O(4)` or `O(n⁴)`. The `4` is `2×2` from `(2n)×(2n)`.
- One extra list of length `n` → **`O(n)` extra space**, not `O(2)`. Two such lists still `O(n)` (drop the constant).
- Extra space **can** be `O(n²)` if you allocate an `n×n` grid. This water code does not.

Other interview shapes exist (`O(1)`, `O(n)`, `O(n log n)`, …). This exercise owns **`O(n²)` time**.

---

## Interview script (say this)

> I’ll score every pair `L < R`. Water is `min(height[L], height[R]) * (R - L)`. I keep a max.  
> Time `O(n²)`, extra space `O(1)`.  
> If `n` is huge (e.g. `10^5` = 100,000 walls), this is many pairs. I’d need a skip rule I can prove.

`10^5` is a **constraint** (imagine a large `n`). It is not computed from the 4-wall table.

---

## What to code-review next time

- Does every `L < R` appear (compare to the 6-row table for `n=4`)?
- Water `if` only updates the bucket.
- After `L` moves, is `R` reset to `L+1`?
- Return one number; call the function to print it.

---

## Pain points from this chat

These are the mix-ups that actually happened. Quiz these first; they will fail here before they fail on a new problem.

| # | What they mixed up | What “got it” sounds like |
| --- | --- | --- |
| 1 | Story vs data. Said input was “vertical lines” or pass `i`. | Input is the **list of heights**. `i` is a loop label, not the function argument. |
| 2 | Extra rules: only adjacent pairs; **add** all containers. | Any two indices. **Compare**, don’t add. Verbs: pick / maximum. |
| 3 | Formula grouping: `height * R - L`. | Two steps: `width = R - L`, then `water = shorter * width`. Pair `(1,8)` with heights `8` and `7` → width `7`, water `49` for **that pair only**. |
| 4 | Hero index: lock last wall, or lock tallest. | That skips pairs. Complete search visits **every** `L < R`. |
| 5 | “Lock” meant a code variable. `10^5` felt calculated. | Lock = keep the idea. `10^5` = “imagine 100,000 items” (constraint), not from the 4-wall table. |
| 6 | `n` vs rows. | `n` = walls. Rows = pairs = `n(n-1)/2`. `n=4→6`, `n=5→10`, `n=6→15`, `n=7→21`. |
| 7 | Two `if`s; water `if` vs move `if`. | Score and move are **two jobs**. Water `if` only updates the bucket. |
| 8 | Loop: `R = L+1` every iteration; `L` never assigned; `R` stuck at end when `L` moves. | After last `R`: `L += 1` **and** `R = L+1`. Trace `[1,8,6,2]` must include `(1,2)`. |
| 9 | `math.small`; `print("L": j)`; never called the function. | `min(...)`. Call `print(max_water(height))`. |
| 10 | **Work** vs **`n`**. Thought `n` is the step count. | `n` = input size. Work = steps (table rows). `O(...)` names how work grows when `n` grows. |
| 11 | `2*n = 4*steps`. Thought 4× means `O(n⁴)` or `O(4)`. | `n×n` comes from **pair count** `n(n-1)/2`, not from the 4. Drop `-1` and `/2` **only to name** `O(n²)`. 4× is a **check**: `(2n)×(2n) = 4×(n×n)`. |
| 12 | Extra space: “not used”; `O(2)` for one more list; `O(1)` = one list. | Extra = **apart from input**. Few variables → `O(1)` = **constant**, not “one list”. New list of length `n` → `O(n)` extra, not `O(2)`. |

---

## Quiz (pain-point order)

Ask one at a time. After they answer, mark hit/miss against **Expect**. Do not skip to skip-rules.

**Q1.** What do you pass into `def max_water(???)` — the picture, index `i`, or what type of data? What is one slot?

**Expect:** A list of numbers. Index = position, value = height of that wall.

**Q2.** Does the problem ask you to add water from every pair, and only neighbors?

**Expect:** No. Any two walls. Output is the **max** of those waters (compare).

**Q3.** Write water for one pair as two lines. Then compute walls at index `1` (height `8`) and `8` (height `7`).

**Expect:** `width = 8-1 = 7`; `water = 7*7 = 49`. That is one pair, not yet the problem answer unless it wins the compare.

**Q4.** You sort `height` to make two-pointers easier. Allowed? Why?

**Expect:** No. Width needs the original indices.

**Q5.** What does `n` mean vs what does `n(n-1)/2` mean? How many rows for `n=4` and `n=6`?

**Expect:** `n` = walls. The formula = pairs/steps. 6 and 15.

**Q6.** What is `10^5` in an interview constraint?

**Expect:** 100,000. A size limit they might give. Not computed from the tiny example.

**Q7.** In the loop, can the water `if` also move `L`/`R`? When `R` hits the last index, what two updates are required?

**Expect:** No — water `if` only updates max. Then `L += 1` and `R = L+1`.

**Q8.** On `[1,8,6,2]`, if after `L=0` you leave `R` at the last index, which table row do you miss?

**Expect:** `(1,2)` (water 6). That was the max on that tiny input.

**Q9.** What is work? Is `n` the work? Why is this method `O(n²)` time — from the 4×, or from the pair formula?

**Expect:** Work = steps. `n` is input size, not work. `O(n²)` is the **name** of `n(n-1)/2` after dropping `-1` and `/2`. The 4× (10→20 walls, 45→190 pairs) is only a check, not the source. Not `O(4)`, not `O(n⁴)`, not `2n = 4*steps`.

**Q10.** Time and extra space of **this** code? If you add one new list of length `n`, extra space becomes what — `O(2)` or `O(n)`? What does the `1` in `O(1)` mean?

**Expect:** `O(n²)` time, `O(1)` extra. New list → `O(n)` extra. `1` = constant (does not grow with `n`), not “one list” and not “zero.” Input `height` is not extra.

**Q11 (interview line).** Say time and extra space in one sentence, then what you would tell Google if `n` is huge.

**Expect:** `O(n²)` time, `O(1)` extra space. Complete search may be too many pairs; I’d need a skip I can prove. Do not demand they name the faster algorithm.

---

## Breakthrough — optimized method (self-derived)

You reached this by proof, not by memorizing a name. Your own words:

1. First I was doing scoring each pair.
2. Then I found, the smaller wall in a widest pair, will be the max water cap.
3. So I scored that pair.
4. And skipped all other pairs with that smaller wall.

Restated with the skip-rule from earlier in this doc:

- Start widest: `L = 0`, `R = last index`. Score it.
- The **shorter** of the two walls in the current pair is the cap. Every closer pair that **still uses that same wall** has shorter ≤ this cap and smaller width → already proven to lose (see "Skip vs a scored pair" below). So that wall is **finished** — retire it by moving that side inward by one.
- The **other** wall is still unproven — keep it, score the new pair against it.
- Repeat until `L` and `R` meet.

This visits only `n` pairs total (each pointer moves at most `n-1` times), not `n(n-1)/2`.

**Code (locked correct):** `max_water_optimized` in `dsa_2p_find_pair_2.py`. Traced on `[1,8,6,2]`: `(0,3)→L=1`, `(1,3)→R=2`, `(1,2)→R=1`, stop. Max `6`. On the full 9-element array: reaches `49`.

### Complexity of the optimized method

- Time: each of `L`, `R` moves inward at most `n-1` times total, one pair scored per step → **`O(n)`** time (down from `O(n²)`).
- Extra space: still only a few variables → **`O(1)`**.

### The proof, precisely (say this in an interview)

Whichever side (`L` or `R`) holds the **smaller** height in the current pair is the cap for every pair that still includes it. Moving the *other* side closer can only shrink width while the cap stays the same or drops — so any such pair is already proven to lose against the one just scored (same-or-worse cap + smaller width, from the "Skip vs a scored pair" rule above). So it's safe to stop considering that wall entirely and move it inward. The taller wall might still pair better with something further in, so it stays.

### Leftover cleanup (not urgent)

Unused imports in the file: `from ast import And`, `from operator import index`, `from turtle import width`, `from unittest import skip`. `width`/`index` also shadow local variable names (harmless here, but confusing). Remove when convenient.

---

## Quiz — optimized method (ask after the O(n²) quiz is solid)

**Q12.** In the optimized loop, which pointer moves and why — always `L`, always `R`, or whichever side held the smaller height?

**Expect:** Whichever index held the smaller height. Never a fixed side.

**Q13.** Why is it safe to never re-visit a wall once its side has been moved past?

**Expect:** Every pair that would reuse that wall with a closer partner has a cap ≤ the one just scored and a smaller width — proven to lose, from the skip-rule.

**Q14.** Time and extra space of the optimized method, and why time dropped from the complete search?

**Expect:** `O(n)` time, `O(1)` extra space. Each pointer moves inward at most `n-1` times total instead of scoring `n(n-1)/2` pairs.

**Q15 (interview line).** State the full answer as you would to an interviewer: approach, proof in one sentence, time, space.

**Expect:** Two pointers from both ends, move the side with the smaller height inward each step because that side cannot form a better pair with anything closer than what's already been scored. `O(n)` time, `O(1)` extra space.
