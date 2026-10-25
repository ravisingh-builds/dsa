# You get a list of integers. Move every 0 to the end.
# The other numbers stay in the same order.
# Change the list in place (do not return a new list).


nums = [0, 1, 0, 3, 12]
# expected: [1, 3, 12, 0, 0]

def move_zeros(nums: int):
    length = len(nums) - 1
    left = 0
    right = 1
    while right <= length:
        if nums[left] == 0 and nums[right] != 0:
            nums[left] = nums[right]
            nums[right] = 0
            left = left + 1
            right = right + 1
        elif nums[left] == 0 and nums[right] == 0:
            right = right + 1
        else:
            left = left + 1
            right = right + 1
    return nums

def move_zeros_v2(nums):
    # landing = next seat for a non-zero. read = slot we look at.
    landing = 0
    read = 0
    while read < len(nums):
        if nums[read] != 0:
            nums[landing], nums[read] = nums[read], nums[landing]
            landing = landing + 1
        read = read + 1
    return nums


print(move_zeros(list(nums)))
print(move_zeros_v2(list(nums)))

