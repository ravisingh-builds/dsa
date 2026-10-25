# You get a list of numbers (not sorted) and a target.
# Return two different indexes i, j such that nums[i] + nums[j] == target.
# There is exactly one answer. You may return the two indexes in any order.


nums = [3, 3]
target = 6
# expected: [1, 2]

def find_2_indices(nums: list, target: int):
    length = len(nums) - 1
    pair = []
    left_idx = 0
    right_idx = 1

    while left_idx < length:

        if nums[left_idx] + nums[right_idx] == target:
            pair.append(left_idx)
            pair.append(right_idx)
            return pair

        else:
            if right_idx == length:
                left_idx = left_idx + 1
                right_idx = left_idx + 1
            elif right_idx < length:
                right_idx = right_idx + 1

    return pair

#print(find_2_indices(nums, target))

def find_2_indices_v2(nums: list, target: int):

    length = len(nums) - 1
    idx = 0
    seen = {}

    while idx <= length:
        print("seen:", seen)
        need = target - nums[idx]
        if need in seen:
            return (seen[need], idx)
        else:
            seen[nums[idx]] = idx
            idx = idx + 1

print(find_2_indices_v2(nums, target))
