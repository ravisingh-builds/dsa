numbers = [2, 5, 8, 11, 15, 19]
target = 20


# 1-indexed
# use 1 element one time
# find indexes whose value sum is target
# sorted non-decending

def find_pair(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left < right:

        sum = numbers[left] + numbers[right]
        print("left:", left)
        print("right:", right)
        print("sum:", sum)

        if sum == target:
            return {
                "status": "found",
                "left": left,
                "right": right
            }
        
        elif sum < target:
            print("sum is less than target")
            left = left + 1

        else:
            print("sum is greater than target")
            right = right - 1

    return {
        "status": "not found",
        "left": None,
        "right": None
    }


print(find_pair(numbers, target))