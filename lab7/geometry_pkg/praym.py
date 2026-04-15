import math
from .base import Shape

class Praym(Shape):

    def __init__(self, a, b):
        super().__init__("Прямоугольник")
        self.a = a
        self.b = b

    def s(self):
        return self.a * self.b

    def opis_radius(self):
        return math.sqrt(self.a**2 + self.b**2) / 2

    def vpis_radius(self):
        return min(self.a, self.b) / 2

    def __eq__(self, other):
        return self.s() == other.s()

    def __len__(self):
        return int(self.a + self.b)
