def binary_search(arr, elm):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (high + low) // 2
        val = arr[mid]
        if val == elm:
            return mid, arr
        elif val < elm:
            low = mid + 1
        else:
            high = mid - 1

    return "Not Found!"



