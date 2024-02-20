def first_oc(arr, elm):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if low == high:
            break
        if arr[mid] < elm:
            low = mid + 1
        else:
            high = mid

    if arr[low] == elm:
        return f"first occurrence of {arr[low]} at index {low}"
