"""
algebra.py

Basic algebraic operations.
"""

def add(a, b):
    """
    Returns the sum of a and b.
    """
    return a + b


def subtract(a, b):
    """
    Returns the difference of a and b.
    """
    return a - b


def multiply(a, b):
    """
    Returns the product of a and b.
    """
    return a * b


def divide(a, b):
    """
    Returns the division of a by b.
    Raises ValueError if b is zero.
    """
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b


from algorithms import add, divide

print(add(3, 4))
print(divide(10, 2))

