# You get a list of words, already sorted in an unknown language's dictionary order.
# Letters in that language are English letters, but their order may not be a-z.
# Return one string: the letters in an order that matches the dictionary.
# If the words contradict each other, return "".
# You only need one valid order, not every possible order.

words = ["wrt", "wrf", "er", "ett", "rftt"]
# words = ["z", "x", "z"]
# words = ["a", "z", "x", "z"]
# expected: "wertf"
# (any order that does not break the dictionary is fine if more than one works)

def ordered_string(words):
    links = {}
    left = 0
    right = 1
    in_left = 0
    in_right = 0
    expected = ""
    depends = {}
    taken = []
    unique_letters = ""

    while right < len(words):
        while in_left in range(len(words[left])) and in_right in range(len(words[right])):
            if words[left][in_left] != words[right][in_right]:
                if words[right][in_right] not in links:
                    links[words[right][in_right]] = []
                links[words[right][in_right]].append(words[left][in_left])
                break
            in_left = in_left + 1
            in_right = in_right + 1
        in_left = 0
        in_right = 0
        left = left + 1
        right = right + 1
    print(links)
    idx = 0

    while idx < len(words):
        for k in range(len(words[idx])):
            print("word is:", words[idx][k])
            if words[idx][k] not in unique_letters:
                unique_letters =  unique_letters + words[idx][k]

            if words[idx][k] not in links:
                if words[idx][k] not in expected:
                    expected = expected + words[idx][k]
                    taken.append(words[idx][k])
            else:
                allowed = True
                for x in links[words[idx][k]]:
                    print("links of:", words[idx][k], "is:", x)
                    if x not in expected:
                        print("x not in expected")
                        allowed =  False
                        if x not in depends:
                            depends[x] = []
                        if words[idx][k] not in depends[x]:
                            depends[x].append(words[idx][k])
                if allowed:
                    if words[idx][k] not in expected:
                        expected = expected + words[idx][k]
                        taken.append(words[idx][k])
            while taken:
                if taken[0] in depends:
                    for x in depends[taken[0]]:
                        links[x].remove(taken[0])
                        if len(links[x]) == 0:
                            if x not in expected:
                                expected = expected + x
                                taken.append(x)
                taken.pop(0)
            print("depends:", depends)
            print("link:" , links)
            print("expected:", expected)
        idx = idx + 1
    
    if len(unique_letters) == len(expected):
        return expected
    else:
        return ""

print("returned:", ordered_string(words))