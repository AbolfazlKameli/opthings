def remove_min(stack):
    storage = []
    if len(stack) == 0:
        return stack

    min = stack.pop()
    stack.append(min)
    for i in range(len(stack)):
        val = stack.pop()
        if val <= min:
            min = val
        storage.append(val)

    for i in range(len(storage)):
        val = storage.pop()
        if val != min:
            stack.append(val)

    return stack, min


