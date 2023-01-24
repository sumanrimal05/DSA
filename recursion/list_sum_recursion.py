def list_sum_recursion(list):
    # Base case
    if len(list) == 0:
        return 0
    # Recursive Function
    return list[0] + list_sum_recursion(list[1:])


print(list_sum_recursion([1, 2, 3, 4]))
