from src.Figure import Figure


class Rectangle(Figure):
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b
        if self.check_create_figure():
            self.name = 'Rectangle'
            self.perimeter = self._perimeter()
            self.area = self._area()

    def _perimeter(self):
        return 2 * (self.a + self.b)

    def _area(self):
        return self.a * self.b

    def check_create_figure(self):
        if self._check_side_type(self.a) and self._check_side_type(self.b):
            if self._check_is_more_than_zero(self.a) and self._check_is_more_than_zero(self.b):
                return True

        raise ValueError(f"a={self.a}, b={self.b} One of the sides of the rectangle is set incorrectly")
