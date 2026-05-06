from itertools import product

def count_words():
    """
    Считает количество слов длины 5 из букв 'еиймотф'
    по заданным условиям.

    >>> count_words()
    10476
    """
    p = product('еиймотф', repeat=5)
    k = 0
    for x in p:
        s=''.join(x)
        if s.count('й')<=1 and 'ий'not in s and 'йи'not in s and s[0]!='й' and s[4]!='й':
            k+=1
    return k
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(count_words())    
