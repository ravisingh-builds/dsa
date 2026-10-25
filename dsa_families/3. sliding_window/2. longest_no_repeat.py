# You get a string.
# Find the longest run of neighbors in a row where no character appears twice.
# Return the length of that run (one number).

import string
from tkinter import RIGHT

s = "abca"
# s = "pwwkek"
# expected: 3
# ("abc" is length 3; later repeats shrink the unique run)

def longest_neighbor_v1(s: str):
    left = 0
    right = 0
    sub_string = ""
    window = 0
    largest_neighbor = 0
    while left < len(s):
        while right < len(s):
            if s[right] not in sub_string:
                sub_string = sub_string + s[right]
                print("sub_string:", sub_string)
                window = window + 1
                print("window:", window)
                right = right + 1
            else:
                break
        if window == len(s):
            largest_neighbor = window
            break
        if largest_neighbor < window:
            largest_neighbor = window
        window = 0
        sub_string = ""
        left = left + 1
        right = left

    return largest_neighbor

def longest_neighbor_v2(s: str):
    # next left = just after the old copy of s[right]; keep the rest of the run
    left = 0
    right = 0
    sub_string = ""
    largest_neighbor = 0
    while right < len(s):
        if s[right] not in sub_string:
            sub_string = sub_string + s[right]
            if largest_neighbor < len(sub_string):
                largest_neighbor = len(sub_string)
            right = right + 1
        else:
            old = sub_string.find(s[right])
            sub_string = sub_string[old + 1 :]
            left = left + old + 1
    return largest_neighbor

def longest_neighbor_v3(s: str):
    left = 0
    right = 0
    slice = ""
    window = 0
    seen = {}
    largest_neighbor = 0
    while right < len(s):
        if s[right] not in seen:
            slice = slice + s[right]
            print("slice:", slice)
            seen[s[right]] = right
            window = window + 1
            if largest_neighbor < window:
                largest_neighbor = window
            right = right + 1
        elif s[right] in seen and seen[s[right]] < left:
            slice = slice + s[right]
            print("slice:", slice)
            seen[s[right]] = right
            window = window + 1
            if largest_neighbor < window:
                largest_neighbor = window
            right = right + 1
        else:
            where_in_slice = slice.find(s[right])
            slice = slice[where_in_slice + 1 : ]
            print("slice:", slice)
            window = len(slice)
            previous_copy = seen[s[right]]
            print("previous_copy:", previous_copy)
            if previous_copy >= left:
                left = previous_copy + 1

            
    return largest_neighbor

def longest_neighbor_v4(s: str):
    left = 0
    right = 0
    seen = {}
    window = 0
    largest_neighbor = 0
    while right < len(s):
        if s[right] not in seen:
            seen[s[right]] = right
            window = window + 1
            if largest_neighbor < window:
                largest_neighbor = window
            right = right + 1
        elif s[right] in seen and seen[s[right]] < left:
            window = window + 1
            if largest_neighbor < window:
                largest_neighbor = window
            seen[s[right]] = right
            right = right + 1
        elif s[right] in seen and seen[s[right]] >= left:
            left = seen[s[right]] + 1
            window = right - left
    return largest_neighbor

def longest_neighbor_v5(s: str):
    left = 0
    right = 0
    seen = {}
    window = 0
    largest_neighbor = 0
    while right < len(s):
        if s[right] in seen and seen[s[right]] >= left:
            left = seen[s[right]] + 1
            window = right - left
        else:
            seen[s[right]] = right
            window = window + 1
            if largest_neighbor < window:
                largest_neighbor = window
            right = right + 1
    return largest_neighbor


def longest_neighbor_v6(s: str):
    # same visit: maybe shrink, then always write seen, measure, step right
    left = 0
    right = 0
    seen = {}
    largest_neighbor = 0
    while right < len(s):
        if s[right] in seen and seen[s[right]] >= left:
            left = seen[s[right]] + 1
        seen[s[right]] = right
        if largest_neighbor < (right - left + 1):
            largest_neighbor = right - left + 1
        right = right + 1
    return largest_neighbor


print(longest_neighbor_v5(s))
print(longest_neighbor_v6(s))