def f(i):
    if i == 1:
        return 1
    if i == 2:
        return -1/8
    
    return ((i-1) * f(i-1)) / 3 + \
           ((i-2) * f(i-2)) / 4
print(f(3))
