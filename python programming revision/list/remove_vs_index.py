# .remove(x) deletes by VALUE. .pop(i) deletes by POSITION.

not_taken = [0, 1, 2]
idx = 1
print("start:", not_taken, "idx:", idx, "slot holds:", not_taken[idx])

# WRONG if you meant "delete the course at idx":
# not_taken.remove(idx)  → deletes the number 1, which happens to match here

course = not_taken[idx]
not_taken.remove(course)
print("after remove(course):", not_taken)

# The next course slid into slot idx. Do not idx + 1.
print("same idx now holds:", not_taken[idx])
