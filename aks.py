import sys
from math import log2, floor

def main(n):
    """
    The main function which will run the AKS algorithm on the given input n. It will use
    helper functions for each of the steps in the algorithm. This function will output
    either PRIME or COMPOSITE.
    """
    # Step 1:
    if is_perfect_power(n):
        return "COMPOSITE"

    # Step 2:

    # Step 3:

    # Step 4:

    # Step 5:

    # Step 6:
    pass

########################################################################################

# HELPER FUNCTIONS:
def euler_totient(r):
    """
    This function computes Euler's totient function phi(n), which is the number of positive
    integers less than or equal to n that are relatively prime (or co-prime) to n.
    """
    pass

def is_perfect_power(n):
    """
    This function checks if n is a perfect power. In other words, it checks if n = a^b,
    where a is a positive integer and b is a positive integer greater than 1. 
    If that is the case, it will return 1 (meaning True). 
    Otherwise, it will return 0 (meaning False).

    >>> is_perfect_power(1)
    1
    >>> is_perfect_power(2)
    0
    >>> is_perfect_power(4)
    1
    >>> is_perfect_power(8)
    1
    >>> is_perfect_power(9)
    1
    >>> is_perfect_power(64)
    1
    >>> is_perfect_power(81)
    1
    >>> is_perfect_power(100)
    1
    >>> is_perfect_power(199)
    0
    >>> is_perfect_power(243)
    1
    """
    # This part relies on the fact that x^(log_x(y)) = y, where x and y are positive integers.
    # Notice that since the smallest possible value of a is 2, the smallest possible value of
    # b is log_2(n) because 2^log_2(n) = n. Therefore, we only need to check values of b from 2 to log_2(n)

    if n == 1: return 1

    for b in range(2, floor(log2(n) + 1)):
        a = n ** (1 / b) # We get this by taking the bth on both sides of the equation n = a^b and solving for a
        if a.is_integer():
            return 1
    return 0

def get_smallest_r(n):
    """
    This function computes the smallest r such that the order of n mod r is greater than log^2(n).
    """
    pass

if __name__ == '__main__':
    import doctest
    doctest.testmod() # For testing purposes (make sure to comment out when submitting)

    # main(sys.argv[1]) # Will output PRIME or COMPOSITE
