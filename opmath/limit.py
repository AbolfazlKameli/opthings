def limit(arr, miin=None, maax=None):
    if len(arr) == 0:
        return arr

    if miin is None:
        miin = min(arr)
    if maax is None:
        maax = max(arr)

    return [y for y in arr if miin < y < maax]



