# DSA Progress — Google interview prep

Lives in `dsa_families/` (next to family folders). Maintained by `dsa-socratic-coach`. Problem paths below are relative to this folder.

## Status legend

- 🔒 locked — correct + optimized (if applicable) + complexity + edge cases
- 🟡 in progress
- ⬜ not started / not reviewed under this process

## Pattern definitions (how you walk)

- **Binary search:** move in a **range** (jump to `mid`, drop a half).
- **Two-pointer:** two indexes move in the **same direction** or **opposite**.
- **Sliding window:** a contiguous run. Fixed `k`: next sum = last **minus leave, plus new right**. Variable: grow `right`; on a repeat, `left` = just after the **old copy** (do not clear the run / do not restart `right`).
- **Hashing (this problem):** walk once; **notebook** `value → index`; `need in seen` is ~`O(1)`, not a rescan.
- **Graph (four questions):** **dot** (what are the things?) → **link** (when does one connect to another? one-way if the problem says “before”) → **mark** (a dot is used once) → **question** (what must the walk answer?). Grid islands: dots = land cells, links = 4-edge, mark = `used`/stamp, question = how many new groups. Course prereqs: dots = `0..n-1`, links = pairs, mark = taken, question = can every dot be taken?

---

## Pattern 1 — Binary Search (⬜)

File in folder, **not** locked under this process:

| # | File | Notes |
|---|------|--------|
| 1 | `1. binary_search/1. dsa_2pointers_find_target.py` | Mid / range walk. Needs a real lock (contract → complete search → cost → edges). |

---

## Pattern 2 — Two Pointers (🟡)

**Target this pass:** ~5 locked, then sliding window. Lifetime: more later, toward ~10.

### Covered (locked)

| # | Problem | File | What they own |
|---|---------|------|----------------|
| 3 | Container With Most Water | `2. two_pointer/3. dsa_2p_find_pair_2.py` + `docs/dsa_2p_find_pair_2.md` | Opposite ends, water = shorter × width, skip shorter wall, `O(n)` / `O(1)`, edge cases |
| 4 | 3Sum | `2. two_pointer/4. three_sum.py` + `docs/4. three_sum.md` | Fix `L` + 2Sum on rest, sort allowed (values only), `seen`+tuple, skip equal `L/M/R`, `O(n²)` time, space `O(n)` sort + `O(k)` answers (`2k` → `O(k)`) |
| 5 | Trapping Rain Water | `2. two_pointer/5. trapping_rain_water.py` | Water per bar, not one container. Complete search `O(n²)`/`O(1)`. Two walks + remember left/right tallest per index, `O(n)`/`O(n)` (`3n→O(n)`). `append` while walking backward → `reverse()` once so slot `k` is bar `k`. Edges: `n=1`, `n=2`, uphill/downhill, peak. |
| 6 | Valid Palindrome | `2. two_pointer/6. valid_palindrome.py` | Alnum+lower; `new_s` then ends `O(n)`/`O(n)`. Skip junk **in `s`**: compare only when **both** alnum, else move the junk side; `.lower()`; `O(n)`/`O(1)`. Edges: `" "`, `"A"`, `"0P"`, `"0P0"`, `".,"`, `"  a"`. `"Panama"` alone is **False**. |
| 7 | Move Zeroes | `2. two_pointer/7. move_zeroes.py` | Same-direction, write in place. v1: `left`/`right` three-branch swap, `O(n)`/`O(1)` (floor). v2: `landing` = next seat, `read` walks every slot; one `if` (`read` non-zero) then tuple-swap + `landing+1`. Same-slot swap is no-op (no wipe). `a,b=b,a` captures both values first. Edges: `[0]`, `[1]`, `[1,2,3]` (no zeros). |

**Mental models locked:** story vs contract; complete search first; extra rules; `n` vs work; Big-O drop constants; sort only if output doesn’t need original index; family = how you walk; one walk can make only one side “join”; write-down per index if you need the running max later; two fingers can be **seat** vs **read** (same pattern, named jobs); tuple-swap ≠ two copies.

### In folder, not locked under this process

| # | File | What it actually is |
|---|------|---------------------|
| 2 | `2. two_pointer/2. dsa_2pointers_find_pair.py` | Sorted pair-sum (Two Sum II). Tool 3Sum reused — worth a short lock/review, not a new flavor. |

### Left to cover (two-pointer flavors they have not locked)

| Flavor | Example problems | Why it matters |
|--------|------------------|----------------|
| Same direction / in-place | Remove duplicates | Same write-in-place family as Move Zeroes. |
| Merge | Merge two sorted arrays | Curriculum. |
| Same as 3Sum, twist | 3Sum Closest, 4Sum | After 3Sum is solid. |

**This pass:** ~5 two-pointer locks done. Sliding window: **2 locked**. Graphs started.

---

## Pattern 3 — Sliding Window (🟡)

### Covered (locked)

| # | Problem | File | What they own |
|---|---------|------|----------------|
| 1 | Max sum of k neighbors | `3. sliding_window/1. max_sum_window_k.py` | Contract: list + `k` → one number. Units = starts `0..n-k` (`n-k` is last **index**, count is `n-k+1`). v2 complete search `O(nk)`/`O(1)`; first unit **assigns** (not `largest_sum=0`). `n<k`: ask, do not assume `0`. Skip: first `k` adds, then `-` leave `+` new **right**; v4 `O(n)`/`O(1)`. Edges: all-negative, `n<k` → `None`, `k=1` (`[5,3,1]` → `5,3,1`, max `5`). |
| 2 | Longest run, no repeat char | `3. sliding_window/2. longest_no_repeat.py` | String → length; no `k`. v1 complete search `O(n³)` with string `in`. Hunt skip: two neighbor units. v2 `find`+slice `O(n²)`. Notebook `letter → last index`; stale if index `< left`. v4/v5 three-door then shrink/`else` grow. v6 same visit: shrink if in-run, then write `seen`, `right-left+1`, `right+1`; `O(n)` / `O(alphabet)`. Compact: same vs different work, then **when**. Edges: `""`→`0`, `"a"`, `"abba"`→`2`. |

**Mental models:** units × work; last index ≠ count; ask `n<k`; leave ≠ new left; hunt skip on **two neighbor units**; one `while` ≠ `O(n)`; compact = same vs different, then **when** (v5 next visit / v6 same visit).

**Leftover (window):** min window that must cover required letters. Not started.

---

## Pattern 4 — Hashing & Prefix Sums (🟡)

### Covered (locked)

| # | Problem | File | What they own |
|---|---------|------|----------------|
| 1 | Pair sum → indexes (unsorted) | `4. hashing_and_prefix/1. pair_sum_indexes.py` | Contract = **indexes**, not values (sort not free). Complete search every `i < j`, `O(n²)`/`O(1)`. Notebook: ask `need in seen` then write `seen[nums[i]]=i`. `in` ~`O(1)`, pass `O(n)` / `O(n)`. Edge `[3,3]` → `[0,1]` (ask before write). |

**Next on hashing:** prefix-sum family later (subarray sum). Not required this week.

**Two-pointer this pass:** **5 / ~5**. **Sliding window:** 2 locked. Optional later: more 2P (dups / merge), min-cover window.

---

## Pattern 9 — Graphs (🟡)

### Covered (locked)

| # | Problem | File | What they own |
|---|---------|------|----------------|
| 1 | Count islands | `9. graphs/1. count_islands.py` | Count groups, not cells. 4-edge touch. **Grid walk** every cell; **not-used-island** → `+1`, `used`, **pile**. Pile: `pop`, four edges; add neighbor only if land and not in `used`. Empty pile → walk continues. Cannot mutate input → `used` set. Time `O(n)`, space `O(n)`, `n = rows * columns`. Edges: empty/`0` lands → `0`; all land → `1`; example → `3`. Left+up only is wrong. v2: stamp `"1"`→`"0"`, no `used`. |
| 2 | Course prereqs | `9. graphs/2. course_prereqs.py` | `n` + pairs → bool. All rules live together. **Dot** = `0..n-1`, **link** = pairs, **mark** = taken, **question** = all taken? Complete walk: leftover / taken until a go takes nobody. Time `O(n² p)`, space `O(n + p)`. Skip: when you take X, only tell waiters (`depends`); inner fronts add to ≤ `n`, not `n×n`. Time `O(pn)` (`in taken` is a list). Nested: full inner list → multiply; shared pile → add. Edges: `[]` → `True`; `[[0,0]]` → `False`; cycle → `False`; chain/diamond → `True`. |
| 3 | Oranges minutes | `9. graphs/3. oranges_minutes.py` | Grid 0/1/2 → minutes or `-1`. All starting `2`s in `to_be_rotten` before the clock. One minute = `len` then that many pops; `+1` only if list still has next. Then scan leftover `1`s. Time `O(n²)` (`in` list + `pop(0)`). Space `O(n)` (`to_be_rotten`). `n = rows × columns`. Edges: example `4`; two `2`s `2`; blocked `1`s `-1`; `[[1]]` `-1`; all `2`s `0`. |
| 4 | Can you reach the city | `drills/9. graph_drill/1_can_reach_city.py` | `n` cities, roads both ways, `src` → `dst`, bool. **Dot** = cities, **link** = roads both ways, **mark** = `seen`, **question** = can you stand on `dst`? `links` both ways. Pile starts as `[src]`. `pop(0)` shifts the pile: time `O(r²)`. `pop()` is one step, and neighbor sets make `in` one step: time `O(r)`, space `O(r)`. Edges: same city → `True` (even with no roads); different cities and no roads → `False`; start city on no road → `False`; cycle and diamond covered by `seen`. |
| 5 | Friend groups | `drills/9. graph_drill/2_friend_groups.py` | `n` employees + friendships → how many groups. Links both ways in sets. One pass `0..n-1`; unseen employee starts a pile and adds one group. `pop()` is one step. Time `O(f + n)`, space `O(f + n)`. An employee with no friends is a group. Self-friendship does not remove him. Ids outside `0..n-1` are not in the contract. |

### In progress

| # | Problem | File | Where they are |
|---|---------|------|----------------|
| 6 | Letter order from sorted words | `9. graphs/4. letter_order.py` | Contract next. Google-style graph; builds on course “before” rules. |

---

## Patterns and status

| #  | Pattern                  | Status| Notes                                                               |
|----|--------------------------|-------|---------------------------------------------------------------------|
| 1  | Binary Search            | ⬜   | File `1.` in folder; not locked under this process                  |
| 2  | Two Pointers             | 🟡   | 5 locked this pass (container, 3Sum, rain, palindrome, move zeroes) |
| 3  | Sliding Window           | 🟡   | 2 locked (fixed-`k` max sum, longest unique run).                   |
| 4  | Hashing & Prefix Sums    | 🟡   | 1 locked (pair-sum indexes). Prefix sums not started.               |
| 5  | Linked Lists             | ⬜   | |
| 6  | Stacks & Queues          | ⬜   | |
| 7  | Trees                    | ⬜   | |
| 8  | Heaps / Priority Queues  | ⬜   | |
| 9  | Graphs                   | 🟡   | 5 locked (islands, course prereqs, oranges minutes, can reach, friend groups). Letter order in progress. |
| 10 | Backtracking             | ⬜   | |
| 11 | Dynamic Programming      | ⬜   | |
| 12 | Greedy                   | ⬜   | |
| 13 | Intervals                | ⬜   | |
| 14 | Tries                    | ⬜   | |
| 15 | Math / Bit Manipulation  | ⬜   | |
