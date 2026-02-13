# Derivative of a function (simple polynomial)
def derivative(coeffs):
    """
    coeffs: list of coefficients of polynomial starting from highest degree
    Example: 3x^2 + 2x + 1 => [3,2,1]
    Returns: list of coefficients of derivative
    """
    n = len(coeffs)
    return [coeffs[i] * (n-i-1) for i in range(n-1)]

# Evaluate polynomial at x
def evaluate_poly(coeffs, x):
    return sum(coeffs[i] * x**(len(coeffs)-i-1) for i in range(len(coeffs)))

# Definite integral using simple Riemann sum
def definite_integral(func, a, b, n=1000):
    dx = (b-a)/n
    return sum(func(a + i*dx) * dx for i in range(n))

