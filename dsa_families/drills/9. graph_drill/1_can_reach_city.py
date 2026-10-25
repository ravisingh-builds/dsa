# There are n cities, numbered 0 through n - 1.
# You get a list of roads. Each road joins two cities and can be walked in either direction.
# You start at city src and want city dst.
# Return whether you can get there.
# If src and dst are the same city, the answer is true.

# n = 3
# roads = [[0, 1], [1, 2]]
# src = 0
# dst = 2
# expected: True

# n = 3
# roads = [[0, 1], [1, 2]]
# src = 0
# dst = 0
# expected: True

#n = 4
#roads = [[0, 1], [1, 2], [2, 3]]
#src = 0
#dst = 3
#expected: True

n = 4
roads = [[0,1], [0, 2], [1, 3], [2, 3]]
src = 0
dst = 3

#n = 3
#roads = [[0, 1], [1, 2]]
#src = 0
#dst = 2


def can_reach(n, roads, src, dst):
    links = {}
    idx = 0
    seen = set()
    pile = []
    expected = False
    # for a, b in roads:
    while idx < len(roads):
        a = roads[idx][0]
        b = roads[idx][1]
        if a not in links:
            links[a] = []
        if b not in links[a]:
            links[a].append(b)
        if b not in links:
            links[b] = []
        if a not in links[b]:
            links[b].append(a)
        idx = idx + 1
    # same src and dest are same city
    if src == dst:
        return True
    # if no roads
    if len(roads) == 0:
        return False
    pile.append(src)
    while pile:
        city = pile.pop(0)
        if city not in seen:
            if city in links:
                if dst in links[city]:
                    return True
                    break
                else:
                    for k in links[city]:
                        pile.append(k)
                seen.add(city)
    return False

# optimized function is O(r) whereas non-optimized one is O(r^2) on time complexity scale.
# two important changes are -
# pop(0) is removed from pop(). Why?
# link has sets instead of list.
def can_reach_optimized(n, roads, src, dst):
    links = {}
    seen = set()
    pile = []
    expected = False
    # links
    for a, b in roads:
        if a not in links:
            links[a] = set()
        if b not in links[a]:
            links[a].add(b)
        if b not in links:
            links[b] = set()
        if a not in links[b]:
            links[b].add(a)
    # no road
    if len(roads) == 0:
        return False
    # src and dest are same city
    if src == dst:
        return True
    # 
    pile.append(src)
    while pile:
        city = pile.pop()
        if city not in seen:
            if city in links:
                if dst in links[city]:
                    return True
                    break
                else:
                    for k in links[city]:
                        pile.append(k)
                seen.add(city)
    return False

print(can_reach(n, roads, src, dst))