from math import *

def s(a, b, c):
    s1 = (a + b + c) / 2
    return sqrt(s1 * (s1 - a) * (s1 - b) * (s1 - c))

def opis_radius(a, b, c):
    S = s(a, b, c)
    return (a * b * c) / (4 * S)

def vpis_radius(a, b, c):
    s1 = (a + b + c) / 2
    S = s(a, b, c)
    return S / s1
