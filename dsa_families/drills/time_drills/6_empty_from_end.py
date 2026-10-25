# Drill 6
# k = how many cities start in pile
# Nothing is appended.
# Name the time of work() in terms of k.
# Do not write the answer in this file.

k = 4
pile = [0, 1, 2, 3]


def work(pile):
    hits = 0
    while pile:
        pile.pop()
        hits += 1
    return hits


print(work(pile))
