from math import*
def f(x):
    a=[]
    for i in range(2,int(sqrt(x))+1):
        if x%i==0:
            a.append(i)
            a.append(x//i)
    return sorted(set(a))
for x in range(174457,174505+1):
    if len(f(x))==2:
        print(*f(x))
