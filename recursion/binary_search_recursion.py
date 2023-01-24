def binary_search_recursion(list, element):
    mid_index = len(list)//2
    # Base Case
    if (len(list) == 0):
        return "Item not found"
    elif (list[mid_index] == element):
        return list[mid_index]
    # Recursion
    else:
        if list[mid_index] < element:
            return binary_search_recursion(list[mid_index:], element)
        else:
            return binary_search_recursion(list[:mid_index], element)


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
value = 0

print(binary_search_recursion(my_list, value))
