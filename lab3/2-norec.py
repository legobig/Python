def f(n):
    if n == 1:
        return 1
    if n == 2:
        return -1/8
    x_pred = 1  
    x_pos = -1/8     
    for i in range(3,n+1):
        x = ((i-1)*x_pos)/3 + ((i - 2) * x_pred)/4
        x_pred=x_pos
        x_pos=x
    return x_pos
print(f(3))
