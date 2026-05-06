import pytest

from one import f as f_rec1
from one_norec import f as f_norec1
from two import f as f_norec2
from two_rec import f as f_rec2


@pytest.mark.parametrize("data, expected", [
    ([1, 2, 3], 3),
    ([1, [2, 3]], 4),
    ([1, 2, [3, 4, [5]]], 6),
    ([], 0),
    ([[[]]], 2)
])
def test_rec1(data, expected):
    assert f_rec1(data) == expected


@pytest.mark.parametrize("data, expected", [
    ([1, 2, 3], 3),
    ([1, [2, 3]], 4),
    ([1, 2, [3, 4]], 5),
    ([], 0),
    ([[[]]], 2)
])
def test_norec1(data, expected):
    assert f_norec1(data) == expected


def test_both1():
    data = [1, 2, [3, 4, [5, 6]]]
    assert f_rec1(data) == f_norec1(data)




@pytest.mark.parametrize("n, expected", [
    (1, 1),
    (2, -1/8),
    (3, ((2 * (-1/8)) / 3) + ((1 * 1) / 4)),
])
def test_rec2(n, expected):
    assert f_rec2(n) == pytest.approx(expected)


@pytest.mark.parametrize("n, expected", [
    (1, 1),
    (2, -1/8),
    (3, ((2 * (-1/8)) / 3) + ((1 * 1) / 4)),
])
def test_norec2(n, expected):
    assert f_norec2(n) == pytest.approx(expected)

def test_both2():
    n = (3, ((2 * (-1/8)) / 3) + ((1 * 1) / 4))
    assert f_rec2(n) == f_norec2(n)


