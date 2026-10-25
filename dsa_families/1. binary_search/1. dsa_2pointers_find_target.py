# find a number in the array

numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17]
target = 19


def find_target_in_number_list(numbers, target):
    left = 0
    right = len(numbers) - 1
 
    while left < right:

        mid = (left + right) // 2
        print("====while loop started===")
        print("left:", left)
        print("right:", right)
        print("mid:", mid)
  
        if numbers[mid] == target:
            return "found"
        
        elif numbers[mid] < target:
            print("======left is qual to mid=====")
            left = mid + 1

        elif numbers[mid] > target:
            print("====right is qual to mid========")
            right = mid - 1

    return "not found"
            
print(find_target_in_number_list(numbers, target))

    


            


