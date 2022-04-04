import math

from src.Figure import Figure


class Circle(Figure):
    def __init__(self, radius: float):
        self.radius = radius
        if self.check_create_figure():
            self.name = 'Circle'
            self.perimeter = self._perimeter()
            self.area = self._area()

    def _perimeter(self):
        return 2 * math.pi * self.radius

    def _area(self):
        return math.pi * (self.radius ** 2)

    def check_create_figure(self):
        if self._check_side_type(self.radius):
            if self._check_is_more_than_zero(self.radius):
                return True

        raise ValueError(f"{self.radius} Incorrect value specified for radius")
