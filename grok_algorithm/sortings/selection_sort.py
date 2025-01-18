"""
Selection sort algorithm.
"""


def find_biggest(array: list) -> int:
    if not array:
        return 0

    biggest_index = 0
    biggest = array[0]

    for i in range(1, len(array)):
        if array[i] > biggest:
            biggest = array[i]
            biggest_index = i
    return biggest_index


def selection_sort(array: list) -> list:
    new_array = []
    for i in range(len(array)):
        biggest_index = find_biggest(array)
        new_array.append(array.pop(biggest_index))
    return new_array


print(selection_sort([5, 3, 6, 2, 10]))
