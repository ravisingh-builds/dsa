list_of_list = [[1, 2], [2, 3], [3, 4], [5, 6], [10, 12], [10, 12], [10, 14], [10, 16]]
simple_list = [1, 2, 3, 4, 5]

def even_numbers(simple_list: list):
    even_nums = []
    for num in simple_list:
        if num%2 == 0:
            even_nums.append(num)
    
    return even_nums

print(even_numbers(simple_list))


def any_number_is_even(list_of_list):
    even_nums = {}
    for a, b in list_of_list:
        if a%2 == 0:
            even_nums[a] = b
        
    return even_nums

print(any_number_is_even(list_of_list))



# in list of list, a is the key and b's are the values
# same a's should have all bs
def key_with_all_values(list_of_list):
    notebook = {}
    for a, b in list_of_list:
        if a not in notebook:
            notebook[a] = []
        if b not in notebook[a]:
            notebook[a].append(b)
    
    return notebook

print(key_with_all_values(list_of_list))