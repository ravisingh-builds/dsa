# You get n courses, labeled 0, 1, ..., n-1.
# You also get a list of pairs. Each pair [a, b] means: to take course a, you must already have taken course b.
# Return True if you can finish all n courses, False if you cannot.


# n = 2
# prereqs = []
# expected: True
# take 0 first, then 1

# n = 2
#prereqs = [[1, 0], [0, 1]]
# expected: False

# n = 3
# prereqs = [[0, 2]]
# expected = True

#n = 4
#prereqs = [[0, 2], [0, 3]]
# expected = True

n = 3
prereqs = [[0,1], [1,2]]

#n = 1
#prereqs = [[0, 0]] 



#n = 4
#prereqs = [[1,0],[2,0],[3,1],[3,2]]

#---------------------- framework ----------------------------------------#
# Graph framework (this problem):
# 1. Dot = courses 0, 1, ..., n-1  (n is how many dots)
# 2. Take = e.g. course = 0: no pair [0, …] → take 0, mark it
#----------------------- framework --------------------------------------#

def take_all_courses(prereqs, n):
    
    not_taken = list(range(n))
    idx = 0
    taken = []
    links = {} 

    for a, b in prereqs:
        if a not in links:
            links[a] = []
        links[a].append(b)

    any_thing_taken = False

    while idx < len(not_taken) or any_thing_taken:

        if not_taken[idx] not in links:
            course = not_taken[idx]
            taken.append(course)
            any_thing_taken =  True
            not_taken.remove(course)
        else:
            all_b = links[not_taken[idx]] 
            all_b_in_taken = True
            for b in all_b:
                if b not in taken:
                    all_b_in_taken = False
            
            if all_b_in_taken:
                course = not_taken[idx]
                taken.append(course)
                any_thing_taken = True
                not_taken.remove(course)
            else:
                idx = idx + 1
        
        if idx >= len(not_taken):
            if any_thing_taken:
                idx = 0
                any_thing_taken = False

    print("taken:", taken)
    if len(taken) == n:
        return True
    else:
        return False


# Same walk, cleaner if / for. Your function above is unchanged.
def take_all_courses_clean(prereqs, n):
    not_taken = list(range(n)) # time: O(n)
    taken = []
    links = {} 
    #time: for loop: O(p)
    for a, b in prereqs:
        if a not in links:
            links[a] = []
        links[a].append(b)

    took_someone = True
    while took_someone:
        took_someone = False
        still_waiting = [] 
        print("still waiting:", still_waiting)
        
        for course in not_taken: # time: lap1 = not_taken has all n and in worst case only 1 n moved to taken, O(n)
            if course not in links: # time: O(1)
                taken.append(course)
                took_someone = True
            else:
                allowed = True
                for b in links[course]: #time: for 1 couse = 1 + (total b for a), for n course = n + p (total b for all a)
                    if b not in taken: #time: taken could be (n-1) in worst case, therefore, O(n) = np
                        allowed = False
                if allowed:
                    taken.append(course)
                    took_someone = True
                else:
                    still_waiting.append(course)
        not_taken = still_waiting

    return len(taken) == n


#print(take_all_courses(prereqs, n))
#print(take_all_courses_clean(prereqs, n))



def take_all_courses_optimized(prereqs, n):
    not_taken = list(range(n))
    taken = []
    idx = 0
    links = {}
    depends = {}
    for a, b in prereqs:
        if a not in links:
            links[a] = []
        links[a].append(b)
    print("links:", links)
    while idx < len(not_taken):
        is_taken = False
        print("idx:", idx)
        print("course:", not_taken[idx])
        if not_taken[idx] not in links: 
            taken.append(not_taken[idx])
            is_taken = True
        else:
            allowed = True
            for b in links[not_taken[idx]]: 
                if b not in taken: 
                    allowed = False
            if allowed:
                taken.append(not_taken[idx])
                is_taken = True
            else:
                for b in links[not_taken[idx]]:
                    if b not in depends:
                        depends[b] = []
                    depends[b].append(not_taken[idx])
                print("depends:", depends)
        print("is_taken:", is_taken)

        if is_taken:
            check_courses_in_depends = []
            print("not_taken_in_depends:", not_taken[idx])
            check_courses_in_depends.append(not_taken[idx])
            while check_courses_in_depends:
                if check_courses_in_depends[0] in depends:
                    for b in depends[check_courses_in_depends[0]]:
                        links[b].remove(check_courses_in_depends[0])
                        if len(links[b]) == 0: # if not links[b]
                            taken.append(b)
                            check_courses_in_depends.append(b)
                check_courses_in_depends.pop(0)
                    
                print("links:", links)

        print("taken", taken)

        idx = idx + 1

    return len(taken) == n


# Same skip as take_all_courses_optimized. Your function above is unchanged.
def take_all_courses_optimized_clean(prereqs, n):
    taken = []
    links = {}
    depends = {}
    for a, b in prereqs:
        if a not in links:
            links[a] = []
        links[a].append(b)

    for course in range(n):
        is_taken = False
        if course not in links:
            taken.append(course)
            is_taken = True
        else:
            allowed = True
            for b in links[course]:
                if b not in taken:
                    allowed = False
            if allowed:
                taken.append(course)
                is_taken = True
            else:
                for b in links[course]:
                    if b not in depends:
                        depends[b] = []
                    depends[b].append(course)

        if is_taken:
            check = [course]
            while check:
                just_taken = check.pop(0)
                if just_taken in depends:
                    for waiter in depends[just_taken]:
                        links[waiter].remove(just_taken)
                        if len(links[waiter]) == 0:
                            taken.append(waiter)
                            check.append(waiter)

    return len(taken) == n


#print(take_all_courses(prereqs, n))
#print(take_all_courses_optimized(prereqs, n))
print(take_all_courses_optimized_clean(prereqs, n))