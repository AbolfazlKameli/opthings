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
