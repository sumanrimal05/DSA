def maximum_number_recursion(list):
    # Base Case
    if len(list) == 1:
        return list[0]
    # Recursion
    else:
        max_value = maximum_number_recursion(list[1:])
        return max_value if max_value > list[0] else list[0]


max_item_list = maximum_number_recursion([1, 4, 2, 78, 45, 89, 3])
print("The maximum number in the list is :", max_item_list)
