from algorithms.number_theory import gcd, lcm, is_prime, sieve_of_eratosthenes


def test_gcd():
    assert gcd(12, 18) == 6
    assert gcd(7, 5) == 1


def test_lcm():
    assert lcm(12, 18) == 36
    assert lcm(5, 7) == 35


def test_is_prime():
    assert is_prime(2) is True
    assert is_prime(17) is True
    assert is_prime(18) is False


def test_sieve():
    assert sieve_of_eratosthenes(10) == [2, 3, 5, 7]

