import math

import pytest

from app.main import perform_calculation


@pytest.mark.parametrize(
    "a,b,op,expected",
    [
        (1, 2, "+", 3),
        (5, 3, "-", 2),
        (4, 2.5, "*", 10),
        (5, 2, "/", 2.5),
    ],
)
def test_basic_operations(a, b, op, expected):
    assert perform_calculation(a, b, op) == pytest.approx(expected)


def test_division_by_zero():
    with pytest.raises(ValueError):
        perform_calculation(1, 0, "/")


def test_unsupported_operation():
    with pytest.raises(ValueError):
        perform_calculation(1, 2, "%")

