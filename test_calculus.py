from algorithms import derivative, integrate
import math


def test_derivative():
    f = lambda x: x**2
    assert round(derivative(f, 3), 2) == 6.00


def test_integrate():
    f = lambda x: x
    result = integrate(f, 0, 1)
    assert round(result, 2) == 0.50


def test_invalid_limits():
    import pytest
    f = lambda x: x
    with pytest.raises(ValueError):
        integrate(f, 5, 1)

