# Drill 5 — walk a word from the right (your letter_order range)
# k is the SLOT this trip, not the step.
# First k = start. Then k = k + step. Stop is a wall: k never equals stop.
# Last letter is w[-1], not w[-n]. w[-n] is the first letter (same as w[0]).
#
# Two ranges, same pairs:
#   minus slots:  range(-1, -len(w), -1)       → k = -1, -2, ...
#   real slots:   range(len(w) - 1, 0, -1)    → k = 2, 1, ...  (for "wrt")
# When k is the right letter, w[k-1] is still inside. First letter is read as k-1, not as k.
#
# This is a PYTHON drill (consecutive letters inside ONE word).
# It is NOT dictionary order (that compares two neighbor words).
#
# Paper: for w = "wrt", list k for each range. What is depends after the loop?

w = "wrt"
depends_minus = {}
depends_slot = {}

for k in range(-1, -len(w), -1):
    if w[k] not in depends_minus:
        depends_minus[w[k]] = []
    if w[k - 1] not in depends_minus[w[k]] and w[k] != w[k - 1]:
        depends_minus[w[k]].append(w[k - 1])

for k in range(len(w) - 1, 0, -1):
    if w[k] not in depends_slot:
        depends_slot[w[k]] = []
    if w[k - 1] not in depends_slot[w[k]] and w[k] != w[k - 1]:
        depends_slot[w[k]].append(w[k - 1])

print("minus k:", list(range(-1, -len(w), -1)))
print("slot  k:", list(range(len(w) - 1, 0, -1)))
print("depends_minus:", depends_minus)
print("depends_slot: ", depends_slot)
# both should be {'t': ['r'], 'r': ['w']}
