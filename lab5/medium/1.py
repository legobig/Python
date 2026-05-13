import pytest
from main import gen

def test_gen_same_seed():
    """Одинаковый seed -> одинаковая последовательность"""
    g1 = gen(10)
    g2 = gen(10)

    seq1 = [next(g1) for i in range(5)]
    seq2 = [next(g2) for i in range(5)]

    assert seq1 == seq2

def test_gen_different_seed():
    """Разные seed -> разные последовательности"""
    g1 = gen(10)
    g2 = gen(20)

    seq1 = [next(g1) for i in range(5)]
    seq2 = [next(g2) for i in range(5)]

    assert seq1 != seq2


def test_gen_first_value():
    """Проверка первого значения по формуле"""
    a = 1103515245
    c = 12345
    m = 2**32
    seed = 10

    expected = (a * seed + c) % m

    g = gen(seed)
    assert next(g) == expected





