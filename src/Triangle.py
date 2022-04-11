import math

from src.Figure import Figure


class Triangle(Figure):
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c
        if self.check_create_figure():
            self.name = 'Triangle'
            self.perimeter = self._perimeter()
            self.area = self._area()

    def __semi_perimeter(self):
        return (self.a + self.b + self.c) / 2

    def _perimeter(self):
        return self.a + self.b + self.c

    def _area(self):
        p = self.__semi_perimeter()
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def check_create_figure(self):
        if self._check_side_type(self.a) and self._check_side_type(self.b) and self._check_side_type(self.c):
            if self._check_is_more_than_zero(self.a) and self._check_is_more_than_zero(
                    self.b) and self._check_is_more_than_zero(self.c):
                if self.a + self.b > self.c or self.a + self.c > self.b or self.b + self.c > self.a:
                    return True

        raise ValueError(f"a={self.a}, b={self.b}, c={self.c} One of the sides of the triangle is set incorrectly")
