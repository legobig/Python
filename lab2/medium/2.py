def count_ones():
    """
    Считает количество единиц в двоичной записи числа.

    >>> count_ones()
    2015
    """
    s = 4**2020 + 2**2017 - 15
    b = bin(s)[2:]
    return b.count('1')


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(count_ones())
