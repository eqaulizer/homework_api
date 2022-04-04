from src.Figure import Figure


class Square(Figure):
    def __init__(self, a: float):
        self.a = a
        if self.check_create_figure():
            self.name = 'Square'
            self.perimeter = self._perimeter()
            self.area = self._area()

    def _perimeter(self):
        return self.a * 4

    def _area(self):
        return self.a ** 2

    def check_create_figure(self):
        if self._check_side_type(self.a):
            if self._check_is_more_than_zero(self.a):
                return True

        raise ValueError(f"a={self.a} Square side set incorrectly")
