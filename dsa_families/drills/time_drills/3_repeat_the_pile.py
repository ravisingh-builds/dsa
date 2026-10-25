# Drill 3
# n = how many bags
# p = how many items in ALL bags together
# Name the time of work() in terms of n and/or p.
# Do not write the answer in this file.

bags = {
    0: [10, 20],
    1: [30],
    2: [],
    3: [40, 50, 60],
}
# here n = 4, p = 6

def work(bags):
    n = len(bags)
    hits = 0
    rounds_left = n
    while rounds_left > 0:
        for bag in bags:
            for item in bags[bag]:
                hits += 1
        rounds_left -= 1
    return hits

print(work(bags))
