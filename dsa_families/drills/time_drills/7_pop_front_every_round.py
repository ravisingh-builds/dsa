# Drill 7
# n = how many rounds
# k = how many cities are in pile at every pop
# The popped city is put back, so the pile length stays k.
# Name the time of work() in terms of n and k.
# Do not write the answer in this file.

n = 3
k = 4
pile = [0, 1, 2, 3]


def work(pile, n):
    rounds = 0
    while rounds < n:
        city = pile.pop(0)
        pile.append(city)
        rounds += 1
    return pile


print(work(pile, n))
