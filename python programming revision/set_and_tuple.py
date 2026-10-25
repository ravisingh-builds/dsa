# Small playground: set + tuple (Python mechanics, not a DSA problem)
# Run this file. Read comments. Add to glossary-python.md when revising.

# --- tuple: fixed, hashable (can go in a set) ---
t = ( -1, 0, 1 )
print("tuple:", t)
print("same values, same tuple:", t == (-1, 0, 1))

# list -> tuple (after you sort a triplet)
temp_list = [1, -1, 0]
temp_list.sort()
key = tuple(temp_list)
print("key from sorted list:", key)   # (-1, 0, 1)

# --- set: unique items + fast "is it here?" ---
seen = set()
print("empty seen:", seen)
print("(-1, 0, 1) in seen?", key in seen)   # False

seen.add(key)
print("after add:", seen)
print("(-1, 0, 1) in seen?", key in seen)   # True

# adding the same key again does not grow the set
seen.add((-1, 0, 1))
print("after add same again:", seen)   # still one item

# --- this is the 3sum bug to avoid ---
# set()  = a *new empty* set, every time you write it
# seen   = the box you created once
print("key not in set()?", key not in set())   # always True (brand-new empty box)
print("key not in seen?", key not in seen)     # False, because we added it

# --- list cannot go in a set (not hashable) ---
# seen.add(temp_list)   # TypeError — uncomment to see
