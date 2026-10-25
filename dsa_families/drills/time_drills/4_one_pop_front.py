# Drill 4
# k = how many cities are in pile
# Name the time of one_pop() in terms of k.
# One call only.
# Do not write the answer in this file.

k = 4
pile = [0, 1, 2, 3]


def one_pop(pile):
    pile.pop(0)
    return pile


print(one_pop(pile))
