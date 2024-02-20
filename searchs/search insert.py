def search_insert(array, value):
    low = 0
    high = len(array) - 1
    mid = high // 2

    while low <= high:
        if value > array[mid]:
            mid += 1
            low = mid
        else:
            mid -= 1
            high = mid

    return low
