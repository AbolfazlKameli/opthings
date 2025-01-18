def binary_search(arr, elm, low, high):
    if low <= high:
        mid = (low + high) // 2
        val = arr[mid]
        if val == elm:
            return mid
        elif val < elm:
            low = mid + 1
            return binary_search(arr, elm, low, high)
        else:
            high = mid - 1
            return binary_search(arr, elm, low, high)
    return "Not Found!"
