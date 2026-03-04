def f(n):
    total = 0
    s = [n]

    while s:
        current = s.pop()
        for i in current:
            total += 1
            if isinstance(i, list):
                s.append(i)
    return total
print(f([1, 2, [3, 4]]))
