# Unseen range variants. Answers stay out of this file.
# Do one letter at a time in chat.

# A. These two look similar. What does each print? (empty is allowed)
print("A1", list(range(5, 2)))
print("A2", list(range(5, 2, -1)))

# B. Inclusive-looking stop: does 9 print? What is the last number?
print("B", list(range(1, 10, 3)))

# C. Negatives. What prints?
print("C", list(range(-2, 3)))

# D. A range object can be indexed like a list. What is last?
r = range(1, 10, 3)
print("D", r[-1])

# E. Membership: no loop. True or False?
print("E", 8 in range(0, 10, 2))

# F. Crash or numbers? If crash, which argument is illegal?
# print("F", list(range(0, 5, 0)))

# G. Write ONE range(...) that prints: 7, 4, 1
# (type it in chat, do not fill here)
