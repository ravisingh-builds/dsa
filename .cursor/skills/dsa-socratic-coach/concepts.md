# Concept ladder — agent only

Feed **one** concept per turn. Do not paste this file to the user. Ask after each: Did you get this? Want the next concept?

---

## 1. Story vs contract

The diagram is not the function.

User must write:

- **In:** type + what one slot means
- **Out:** type + what `print` shows

If they say “vertical lines” / “the graph” / “i”: they named the story or a loop variable. Ask: what do you pass into `def solve(???)`? Can that object look up the value at any index?

Do not tell them “array of heights” until they say a list/array of numbers themselves.

---

## 2. One unit

Before max/min/count, define the quantity for **one** unit (one pair, one window, one state).

Ask only what that unit needs (two measurements? a height cap?). If they skip grouping (`a * b - c`), make them write two steps, then one tiny numeric example.

Do not give a search plan.

---

## 3. Extra rules

People invent: adjacent only, add every unit, lock the tallest, lock the last index, must sort.

Ask them to quote the **verbs** in the problem (*pick*, *maximum*, *return*). If a rule isn’t in the problem, it’s a guess.

Do not say which invented rule is the right algorithm.

---

## 4. Complete search

If they cannot prove a unit is safe to ignore, they must score it.

First correct method: every valid unit, one bucket for the best.

Unstick: 4-element table, every unit, circle the max. Confirm the table. Call this a real solution.

---

## 5. Cost

`n` = size of input. Rows = how many units they score.

Let them compute `n=5`, `n=6` from the `n=4` pattern. Then: same method on huge `n` is more calculations, not a new formula.

`10^5` means “imagine 100,000 items” (a constraint), not a number from their table.

---

## 6. Interview path

Order: (1) complete + bucket, (2) *then* fewer units, only with a proof.

Script they should own: “I’ll score every unit and keep a max. About `n²/2` work. If `n` is huge I need a skip rule.”

A skip without “this unit cannot beat the bucket” is a guess. Google grades that sentence.

---

## 7. Skip rule (still no answer)

Only after 1–6. Question: which units can you **prove** cannot beat the bucket?

They must name what they skip and why. If they lock one hero index, ask them to write one unit that lock never visits, and whether that unit can win.

Never name two-pointers, sliding window, binary search, or the move. If they reach a correct proof in their own words, say the proof is sound — do not upgrade it into a textbook name unless they ask what the pattern is called.

---

## 8. Edge cases

A proof that works on one example must be re-checked against inputs that break assumptions the example didn't have.

Give **one** boundary case at a time (from the problem's real constraints, e.g. LeetCode's stated `n` range): smallest valid `n`, all-equal values, already-sorted/reverse-sorted, duplicates. Ask them to trace their existing code by hand — no new code yet.

Teach the split: does this input change the **answer** (a real bug) or just add **redundant but still-correct** work (an efficiency note, not a bug)? Those are different findings — don't let them conflate "extra step" with "wrong."

If an edge case falls outside the problem's stated constraints (e.g. `n=0` when constraints say `n≥2`), say so — not every theoretical input needs hardening.
