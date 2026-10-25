# Hash — why a set can answer "is this here?" without walking the list
# Run this file. Python mechanics, not a DSA problem.

# --- 1. A hash is a fingerprint ---
# hash(x) is a number computed from x.
# Same value  -> same fingerprint (in one Python process).
# Different values *usually* -> different fingerprints.

print("hash of 5:        ", hash(5))
print("hash of 5 again:  ", hash(5))   # same
print("hash of (-1,0,1): ", hash((-1, 0, 1)))
print("hash of (-1,0,1): ", hash((-1, 0, 1)))   # same tuple, same fingerprint

# --- 2. How a set uses that fingerprint ---
# Mental model: a wall of numbered lockers (buckets).
# To store key:  compute hash(key) -> pick a locker -> put the key there.
# To ask "in?":  compute hash(key) -> open THAT locker. Do not walk every locker.
#
# .count() on a list = walk locker 0, 1, 2, ... until you find it (or finish).
# `key in seen`     = jump to one locker. That is why it is treated as O(1).

seen = set()
key = (-1, 0, 1)
seen.add(key)
print("key in seen?", key in seen)   # True — used the fingerprint, not a full scan

# --- 3. Why a list is not allowed ---
# The fingerprint must stay valid while the item sits in the set.
# A list can .append / .clear — the contents change, so the fingerprint would
# become a lie (set would look in the wrong locker).
#
# temp = [1, 2]
# seen.add(temp)   # TypeError: unhashable type: 'list'
# Uncomment the two lines above to see the error.

print("list is unhashable (TypeError if you seen.add(a_list))")

# tuple is frozen: no append. Fingerprint stays honest.
print("tuple is hashable:", hash((1, 2)))

# --- 4. Same values, different order = different fingerprint ---
# That is why 3sum sorts first, then tuple(...).
print("hash (-1, 0, 1):", hash((-1, 0, 1)))
print("hash (1, 0, -1):", hash((1, 0, -1)))   # different — set would treat as two keys

# --- 5. Two names, one idea ---
# tag / reference / memory address  = where an *object* lives
# hash                              = fingerprint of a *value*, used to place it in a set
# Do not mix them. hash is not the memory address of the list box.
