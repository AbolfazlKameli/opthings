def top(arr):
    values = {}
    f_val = 0

    for i in arr:
        if i in values:
            values[i] += 1
        else:
            values[i] = 1

    f_val = max(values.values())

    result = [i for i in values.keys() if values[i] == f_val]

    return f"{result} reapeted {f_val} times"


