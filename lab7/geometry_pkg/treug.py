import math
from .base import Shape

class Treug(Shape):

    def __init__(self, a, b, c):
        super().__init__("Треугольник")
        self.a = a
        self.b = b
        self.c = c

    def s(self):
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def opis_radius(self):
        return (self.a * self.b * self.c) / (4 * self.s())

    def vpis_radius(self):
        p = (self.a + self.b + self.c) / 2
        return self.s() / p

    def __eq__(self, other):
        return self.s() == other.s()

    def __len__(self):
        return int(self.a + self.b + self.c)
