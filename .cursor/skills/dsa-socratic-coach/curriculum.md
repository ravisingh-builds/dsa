# Curriculum — Google coding-round patterns

Agent reference. Pick **one** pattern at a time, **one** problem at a time. Never dump this file to the user — use it to decide what to suggest next.

## Order (foundation → advanced)

1. Binary Search — classic search, search in rotated sorted array, search-on-the-answer (min capacity to ship in D days, Koko eating bananas)
2. Two Pointers — pair-sum, container/water, remove duplicates in-place, merge two sorted arrays, trapping rain water, palindrome
3. Sliding Window — max sum subarray of size k, longest substring without repeating chars, minimum window substring
4. Hashing & Prefix Sums — group anagrams, subarray sum equals k, longest consecutive sequence, two-sum **indexes** (unsorted)
5. Linked Lists — reverse a list, detect a cycle, merge k sorted lists, LRU cache
6. Stacks & Queues — valid parentheses, min stack, monotonic stack (next greater element), sliding window maximum
7. Trees — traversals, validate BST, lowest common ancestor, level-order BFS
8. Heaps / Priority Queues — kth largest element, merge k sorted lists (heap variant), top k frequent elements
9. Graphs — number of islands (grid BFS/DFS), course schedule (topological sort), clone graph, union-find
10. Backtracking — subsets, permutations, N-Queens, word search
11. Dynamic Programming — climbing stairs, coin change, longest common subsequence, edit distance
12. Greedy — jump game, interval scheduling, gas station
13. Intervals — merge intervals, meeting rooms
14. Tries — implement trie, word search II
15. Math / Bit Manipulation — single number, power of two, counting bits

## Picking the next problem

- **Stay, harder:** bump constraints (bigger `n`, an extra condition), or a variant that breaks the last proof and forces a new one.
- **Advance:** move to the next pattern **not yet locked** in `dsa_families/PROGRESS.md`.
- Don't skip ahead in this order unless the user asks — earlier patterns (esp. 1–4) resurface inside later ones (e.g. binary search inside DP-on-answer problems).

## Google-specific notes (mention sparingly, only if relevant)

- Binary-search-on-the-answer shows up more at Google than at most companies.
- Grid BFS/DFS (islands, rotting oranges) is a recurring favorite.
- Problems are rarely labeled by LeetCode name — expect the same idea in unfamiliar wording.
- Two coding rounds usually means: expect one array/string-ish pattern and one graph/tree-ish pattern, medium difficulty, ~35–45 min each including discussion.
