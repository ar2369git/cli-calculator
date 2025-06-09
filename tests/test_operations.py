import pytest
from calculator import operations

@pytest.mark.parametrize("x, y, expected", [
    (1, 2, 3),
    (-1, -1, -2),
    (0, 5, 5)
])
def test_add(x, y, expected):
    assert operations.add(x, y) == expected

@pytest.mark.parametrize("x, y, expected", [
    (5, 3, 2),
    (-1, -1, 0)
])
def test_subtract(x, y, expected):
    assert operations.subtract(x, y) == expected

@pytest.mark.parametrize("x, y, expected", [
    (2, 3, 6),
    (0, 10, 0)
])
def test_multiply(x, y, expected):
    assert operations.multiply(x, y) == expected

@pytest.mark.parametrize("x, y, expected", [
    (6, 2, 3),
    (10, 5, 2)
])
def test_divide(x, y, expected):
    assert operations.divide(x, y) == expected

def test_divide_by_zero():
    with pytest.raises(ValueError):
        operations.divide(5, 0)
