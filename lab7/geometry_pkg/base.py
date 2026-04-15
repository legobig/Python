from abc import *
class Shape(ABC):

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @abstractmethod
    def s(self):
        pass

    @abstractmethod
    def opis_radius(self):
        pass

    @abstractmethod
    def vpis_radius(self):
        pass

    def __str__(self):
        return f"Фигура: {self.name}"

    def __repr__(self):
        return f"{self.__class__.__name__}()"
