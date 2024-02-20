def last_oc(arr, elm):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if (arr[mid] == elm and mid == len(arr) - 1) or \
                (arr[mid] == elm and arr[mid + 1] > elm):
            return mid
        elif arr[mid] <= elm:
            low = mid + 1
        else:
            high = mid - 1



