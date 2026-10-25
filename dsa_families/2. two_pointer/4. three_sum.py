nums = [-1, 0, 1, 2, -1, -4]

def three_sum(nums: list):

    # output: 
    # 1. list of list of integers
    # 2. each inner list = one valid triplet

    # valid triplet
    # 1. a + b + C == 0
    # 2. no dublicate triplet (order inside triplet doesn't matter, values can't be same in two triplets)
    # 3. each value in triplet can come from different index/position

    length = len(nums) - 1

    L = 0
    M = 1
    R = 2

    output = []

    temp_list = []

    while (L <= length-2):

        sum_of_triplet = nums[L] + nums[M] + nums[R]

        if sum_of_triplet == 0:
            temp_list.append(nums[L])
            temp_list.append(nums[M])
            temp_list.append(nums[R])
            print("temp_list:", temp_list)
            temp_list.sort()
            print("sorted_temp_list:", temp_list)
            if output.count(temp_list) == 0:
                output.append(temp_list)
            print("output:", output)
            # new list/box
            temp_list = []
        
        if R == length:
            if M == (length - 1):
                L = L + 1
                M = L + 1
                R = L + 2
            else:
                M = M + 1
                R = M + 1

        elif R < length:
            R = R + 1
        
    return output

def three_sum_optimized(nums: list):

    output = []
    seen = set()
    temp_list = []

    nums.sort()
    print(nums)

    length = len(nums) - 1

    L = 0
    M = L + 1
    R = length

    while (L <= length-2):

        target = -(nums[L])
        print("target:", target)

        if L > 0 and (nums[L] == nums[L-1]):
            print("L is same as previous")

        else:
            while (M < R):

                sum = nums[M] + nums[R]

                if sum == target:
                    temp_list.append(nums[L])
                    temp_list.append(nums[M])
                    temp_list.append(nums[R])
                    temp_list.sort()
                    key = tuple(temp_list)
                    if key not in seen:
                        seen.add(key)
                        output.append(temp_list)
                        print("output:",output)
                    temp_list = []
                    M = M + 1
                    R = R - 1
                    # if (M < R) and (nums[M] == nums[M-1]):
                    while (M < R) and (nums[M] == nums[M-1]):
                        M = M + 1

                    # if (M < R) and (nums[R] == nums[R+1]):
                    while (M < R) and (nums[R] == nums[R+1]):
                        R = R - 1


                elif sum < target:
                    M = M + 1
                else:
                    R = R - 1
        
        L = L + 1
        M = L + 1
        R = length
        print("L:", L)

    return output


print(three_sum_optimized(nums))