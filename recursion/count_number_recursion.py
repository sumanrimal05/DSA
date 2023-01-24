def count_number_recursion(list):
    # Base case
    if len(list) == 1:
        return 1

    # Recursion
    return 1 + count_number_recursion(list[1:])


print(count_number_recursion([1, 2, 3, 4, 5, 6, 7, 8, 9]))
