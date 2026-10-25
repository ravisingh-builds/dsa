# Valid Palindrome
# A phrase is a palindrome if, after you ignore case and drop every
# character that is not a letter or a digit, it reads the same
# forward and backward.
# Return True or False.



s = "A man, a plan, a canal: Panama"
# expected: True
# "Panama" alone is False (p vs a)

# brute force: it shows i wasn't aware that -
# 1. string have their own indices
# 2. I can skip an index if it's not alnum
def palindrome(s: str):

    new_s = []
    for i in s:
        if i.isalnum():
            new_s.append(i.lower())

    print(new_s)

    i = 0
    j = len(new_s) - 1

    while (i < j):

        if new_s[i] == new_s[j]:
            i = i + 1
            j = j - 1

        else:
            return False
    
    return True


def palindrome_optimized_v1(s: str):

    left_index = 0
    right_index = len(s) - 1

    while (left_index < right_index):

        if not s[left_index].isalnum() and not s[right_index].isalnum():
            left_index = left_index + 1
            right_index = right_index - 1
        
        elif not s[right_index].isalnum():
            right_index = right_index - 1

        elif not s[left_index].isalnum():
            left_index = left_index + 1

        if s[left_index].lower() == s[right_index].lower():
            left_index = left_index + 1
            right_index = right_index - 1
        else:
            return False
    
    return True


def palindrome_optimized_v2(s: str):

    left_index = 0
    right_index = len(s) - 1

    while (left_index < right_index):

        if s[left_index].isalnum() and s[right_index].isalnum():
            if s[left_index].lower() == s[right_index].lower():
                left_index = left_index + 1
                right_index = right_index - 1
            else:
                return False

        else:  
            if not s[left_index].isalnum():
                left_index = left_index + 1
            if not s[right_index].isalnum():
                right_index = right_index - 1
                
    return True


def palindrome_optimized_v3(s: str):
    # Same O(1) method as v2. One job per loop turn (if / elif / else).
    left_index = 0
    right_index = len(s) - 1

    while left_index < right_index:
        if not s[left_index].isalnum():
            left_index = left_index + 1
        elif not s[right_index].isalnum():
            right_index = right_index - 1
        elif s[left_index].lower() != s[right_index].lower():
            return False
        else:
            left_index = left_index + 1
            right_index = right_index - 1

    return True


def palindrome_optimized_v4(s: str):
    # Same method. Inner while = "skip until ready" (what v2's ifs were doing one step at a time).
    # A for-loop is not a better fit: the two ends jump by different amounts.
    left_index = 0
    right_index = len(s) - 1

    while left_index < right_index:
        while left_index < right_index and not s[left_index].isalnum():
            left_index = left_index + 1
        while left_index < right_index and not s[right_index].isalnum():
            right_index = right_index - 1
        if left_index < right_index:
            if s[left_index].lower() != s[right_index].lower():
                return False
            left_index = left_index + 1
            right_index = right_index - 1

    return True


print(palindrome_optimized_v3(s))
print(palindrome_optimized_v4(s))
