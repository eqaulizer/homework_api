import pytest

from src.Rectangle import Rectangle
from src.Square import Square


@pytest.mark.parametrize('a', [5, 40.5])
def test_figure_name_positive(a):
    square = Square(a)
    assert square.name == 'Square'


@pytest.mark.parametrize('a', [0, -5.5])
def test_figure_name_negative(a):
    try:
        square = Square(a)
        assert square.name is None
    except ValueError as error:
        assert f"a={a} Square side set incorrectly" in error.args


@pytest.mark.parametrize('a, area', [(10, 100), (10.5, 110.25)])
def test_area_positive(a, area):
    square = Square(a)
    assert round(square.area, 2) == round(area, 2)


@pytest.mark.parametrize('a', [0, -10.5])
def test_area_negative(a):
    try:
        square = Square(a)
        assert square.area is None
    except ValueError as error:
        assert f"a={a} Square side set incorrectly" in error.args


@pytest.mark.parametrize('a, perimeter', [(10, 40), (10.5, 42)])
def test_perimeter_positive(a, perimeter):
    square = Square(a)
    assert square.perimeter == perimeter


@pytest.mark.parametrize('a', [-10, 0])
def test_perimeter_negative(a):
    try:
        square = Square(a)
        assert square.perimeter is None
    except ValueError as error:
        assert f"a={a} Square side set incorrectly" in error.args


@pytest.mark.parametrize('a, rectangle_side_a, rectangle_side_b, area_sum', [(10, 20, 15, 400),
                                                                             (10.5, 12.5, 15.6, 305.25)])
def test_add_area_rectangle_positive(a, rectangle_side_a, rectangle_side_b, area_sum):
    square = Square(a)
    assert round(square.add_area(Rectangle(rectangle_side_a, rectangle_side_b)), 2) == round(area_sum, 2)


@pytest.mark.parametrize('figure', [8, 'str', 0, None])
def test_add_area_negative(figure):
    square = Square(40)
    try:
        square.add_area(figure)
        pytest.fail('Incorrect result for negative test')
    except ValueError as error:
        assert 'Wrong figure class' in error.args
