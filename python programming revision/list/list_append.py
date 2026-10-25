nums = [-1, 0, 1, 2, 4]

output_list = []

temp_list = []

temp_list.append(nums[0])
print("temp_list:", temp_list)

output_list.append(temp_list)
print("output_list:", output_list)

temp_list.append(nums[4])
print("temp_list:", temp_list)
print("output_list:", output_list)

# note, a temp_list is appended to output
# a list is mutuable i.e. new values can be added in a list, old ones can be deleted
# any change in the temp_list will be reflected in the output list as it contains the address of temp_list