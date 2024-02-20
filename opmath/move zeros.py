def move(arr):
    result = []
    zeros = 0

    for i in arr:
        if i == 0 and type(i) != bool:
            zeros += 1
        else:
            result.append(i)
    return f"{result}, zeros: {zeros}"



