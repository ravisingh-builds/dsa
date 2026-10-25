# You get a list of integers and an integer k.
# Among every run of exactly k neighbors in a row, find the largest sum.
# Return that sum (one number).

nums = [2, 1, 5, 1, 3, 2]
k = 3
# expected: 9
# (2+1+5=8, 1+5+1=7, 5+1+3=9, 1+3+2=6)

# v1 breaks when all sums are -ve

def largest_sum_v1(nums: list, k: int):
	left = 0
	mid = 0
	right = k - 1
	largest_sum = 0
	sum = 0
	
	while right < len(nums):
		while	mid <= right:
			sum = sum + nums[mid]
			mid =  mid + 1
		if largest_sum < sum:
			largest_sum = sum
		sum = 0
		left = left + 1
		mid = left
		right = left + (k-1)
	
	return largest_sum

# v2: handles when sums are -ve

def largest_sum_v2(nums: list, k: int):
	left = 0
	mid = 0
	right = k - 1
	largest_sum = 0
	sum = 0
	
	while right < len(nums):
		while	mid <= right:
			sum = sum + nums[mid]
			mid =  mid + 1
		if left == 0:
			largest_sum = sum
		elif largest_sum < sum:
			largest_sum = sum
		sum = 0
		left = left + 1
		mid = left
		right = left + (k-1)
	
	return largest_sum

# skip rule: first run adds k slots; later runs subtract the value that left, add the new right
def largest_sum_v3(nums: list, k: int):
    # n < k: no run of k — ask the interviewer; do not assume 0
    if len(nums) < k:
        return None
    left = 0
    right = k - 1
    mid = 0
    window_sum = 0
    while mid <= right:
        window_sum = window_sum + nums[mid]
        mid = mid + 1
    largest_sum = window_sum
    left = 1
    right = left + (k - 1)
    while right < len(nums):
        window_sum = window_sum - nums[left - 1] + nums[right]
        if largest_sum < window_sum:
            largest_sum = window_sum
        left = left + 1
        right = left + (k - 1)
    return largest_sum


#print(largest_sum_v2(nums, k))
#print(largest_sum_v3(list(nums), k))
#print(largest_sum_v3([-5, -1, -2], 2))

def largest_sum_v4(nums: list, k: int):
	if len(nums) < k:
		return None 
	left = 0
	mid = 0
	right = k - 1
	sum = 0

	while mid <= right:
		sum = sum + nums[mid]
		mid =  mid + 1

	print("sum:", sum)
	largest_sum = sum
	left = 1
	right = right + 1

	while right < len(nums):
		sum = sum - nums[(left - 1)] + nums[right]
		print("sum2:", sum)
		if largest_sum < sum:
			largest_sum = sum
		left = left + 1
		right = right + 1
	return largest_sum

print(largest_sum_v4([5, 3, 1], k = 1))