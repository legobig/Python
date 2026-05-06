from math import sqrt
def f(x):
    """
    Возвращает список делителей числа x без 1 и самого числа.

    >>> f(10)
    [2, 5]

    >>> f(16)
    [2, 4, 8]

    >>> f(13)
    []

    """
    a = []
    for i in range(2, int(sqrt(x))+1):
        if x % i == 0:
            a.append(i)
            a.append(x // i)
    return sorted(set(a))


for x in range(174457, 174505 + 1):
    if len(f(x)) == 2:
        print(*f(x))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
