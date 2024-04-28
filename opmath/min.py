def remove_min(stack):
    storage = []
    if len(stack) == 0:
        return stack

    minimum = stack.pop()
    stack.append(minimum)
    for i in range(len(stack)):
        val = stack.pop()
        if val <= minimum:
            minimum = val
        storage.append(val)

    for i in range(len(storage)):
        val = storage.pop()
        if val != minimum:
            stack.append(val)

    return stack, minimum
