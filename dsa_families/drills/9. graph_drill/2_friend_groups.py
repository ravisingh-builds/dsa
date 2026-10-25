# A company has n employees, numbered 0 through n - 1.
# You get a list of friendships. Each friendship joins two employees and goes both ways.
# Two employees are in the same group if you can walk from one to the other through friendships.
# Return how many groups there are.

n = 5

friendships = []
def friend_groups(n, friendships):
    links = {}
    seen = set()
    pile = []
    groups = 0

    for a, b in friendships:
        if a not in links:
            links[a] = set()
        if b not in links[a]:
            links[a].add(b)
        
        if b not in links:
            links[b] = set()
        if a not in links[b]:
            links[b].add(a)

    for k in range(n):
        if k not in seen:
            pile.append(k)
            while pile:
                num = pile.pop()
                if num not in seen:
                    if num in links:
                        for b in links[num]:
                            pile.append(b)
                        seen.add(num)
            groups = groups + 1
    
    return groups


def friend_groups_optimized(n, friendships):
    links = {}
    for a, b in friendships:
        if a not in links:
            links[a] = set()
        if b not in links:
            links[b] = set()
        links[a].add(b)
        links[b].add(a)

    seen = set()
    groups = 0
    for k in range(n):
        if k in seen:
            continue
        groups += 1
        seen.add(k)
        pile = [k]
        while pile:
            num = pile.pop()
            if num not in links:
                continue
            for b in links[num]:
                if b not in seen:
                    seen.add(b)
                    pile.append(b)
    return groups


print(friend_groups(n, friendships))
print(friend_groups_optimized(n, friendships))
