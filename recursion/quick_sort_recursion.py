def quick_sort(list):
    # Base Case
    if (len(list) < 2):
        return list
    # Recursion
    else:
        pivot = list[0]
        left_sub_array = [i for i in list[1:] if i < pivot]
        right_sub_array = [i for i in list[1:] if i > pivot]

        return quick_sort(left_sub_array) + [pivot] + quick_sort(right_sub_array)


print(quick_sort([1, 3, 5, 3, 7, 4, 5, 9, 0]))
