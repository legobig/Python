def f(x):
    total = 0
    for i in x:
        total+=1
        print(i)
        if isinstance(i, list):
            total += f(i)
    return total
print (f([1, 2, [3, 4, [5]]]))
