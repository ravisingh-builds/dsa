# Drill 1
# n = how many numbers in nums
# Name the time of work() in terms of n.
# Do not write the answer in this file.

n = 5
nums = list(range(n))

def work(nums):
    total = 0
    for i in nums:
        for j in nums:
            total += i + j
    return total

print(work(nums))
