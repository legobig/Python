from .base import Shape

class Trapez(Shape):

    def __init__(self, a, b, h):
        super().__init__("Трапеция")
        self.a = a
        self.b = b
        self.h = h

    def s(self):
        return (self.a + self.b) / 2 * self.h

    def opis_radius(self):
        return None

    def vpis_radius(self):
        return self.h / 2

    def __eq__(self, other):
        return self.s() == other.s()

    def __len__(self):
        return int(self.a + self.b + self.h)
