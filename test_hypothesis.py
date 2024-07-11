from aks import main
from hypothesis import given, strategies as st
from sympy import isprime

# This file contains correctness tests for aks.py, you can run it with this command:
# python test_hypothesis.py

# First generate numbers for testing

SMALL_PRIMES, SMALL_COMPOSITES = [], []

LARGE_PRIMES, LARGE_COMPOSITES = [], []

# Range for smaller number
LOWER_SMALL = 2
UPPER_SMALL = 20

# Range for larger numbers
LOWER_LARGE = 50
UPPER_LARGE = 100

# Generate small prime and composite numbers in the range [LOWER_SMALL, UPPER_SMALL + 1]
for i in range(LOWER_SMALL, LOWER_LARGE + 1):
    if isprime(i):
        SMALL_PRIMES.append(i)
    else:
        SMALL_COMPOSITES.append(i)

# Generate large prime and composite numbers in the range [LOWER_LARGE, UPPER_LARGE + 1]
for i in range(LOWER_LARGE, UPPER_LARGE + 1):
    if isprime(i):
        LARGE_PRIMES.append(i)
    else:
        LARGE_COMPOSITES.append(i)


############################################# TESTS #############################################
def test_small_primes():
    """
    Test that aks.py returns the correct output for small prime numbers
    in the range [LOWER_SMALL, UPPER_SMALL + 1].
    """
    for small_prime in SMALL_PRIMES:
        assert main(small_prime) == "PRIME"

def test_small_composities():
    """
    Test that aks.py returns the correct output for small composite numbers
    in the range [LOWER_SMALL, UPPER_SMALL + 1].
    """
    for small_composite in SMALL_COMPOSITES:
        assert main(small_composite) == "COMPOSITE"

def test_large_primes():
    """
    Test that aks.py returns the correct output for large prime numbers
    in the range [LOWER_LARGE, UPPER_LARGE + 1].
    """
    for large_prime in SMALL_PRIMES:
        assert main(large_prime) == "PRIME"

def test_large_composities():
    """
    Test that aks.py returns the correct output for large composite numbers
    in the range [LOWER_LARGE, UPPER_LARGE + 1].
    """
    for large_composite in SMALL_COMPOSITES:
        assert main(large_composite) == "COMPOSITE"

@given(x=st.integers(max_value=1))
def test_num_less_than_two(x):
    """Test that a negtive integer results in being neither 
    prime nor composite.
    """
    assert main(x) == "NEITHER PRIME NOR COMPOSITE"

if __name__ == '__main__':
    import pytest
    pytest.main(['test_hypothesis.py'])