def linear_search(arr, element):
    for i in range(len(arr)):
        if arr[i] == element:
            return f"the element is {arr[i]} at index {i}"
    return None
