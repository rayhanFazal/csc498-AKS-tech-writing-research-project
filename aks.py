import sys
from math import log2, floor, gcd

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
    r = get_smallest_r(n)
    print("r is: ", r)

    # Step 3:
    if not isall_a_coprime_to_n(r, n):
        return "COMPOSITE"

    # Step 4:
    print("r is: ", r, " and n is: ", n)
    if n <= r:
        return "PRIME"

    # Step 5:
    # For this, we will need to multiply polynomials, so maybe numpy might help for that
    # We will also need to implement a helper function for modular exponentiation of polynomials
    for a in range(1, floor(sqrt(euler_totient(r)) * log2(n))):
        pass
    # Step 6:
    

########################################################################################

# HELPER FUNCTIONS:
def euler_totient(r):
    """
    This function computes Euler's totient function phi(n), which is the number of positive
    integers less than or equal to n that are relatively prime (or co-prime) to n.
    """
    count = 0
    for i in range(1, r + 1):
        if gcd(i, r) == 1:
            count += 1
    return count

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
    # This part relies on the fact that a^(log_a(b)) = b, where a and b are positive integers.
    # Notice that since the smallest possible value of a is 2, the largestt possible value of
    # b is log_2(n) because 2^log_2(n) = n. Therefore, we only need to check values of b from 2 to log_2(n),
    # and if take apply log_b to both sides of the equation n = a^b, we get a = n^(1/b), and so for each
    # value of b, we check if n^(1/b) is an integer. If it is, then n is a perfect power.

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
    # Recall from Lemma 3 in the paper that the max value of r is log_2(n)^5.
    r_max = log2(n) ** 5

    # We want order of n mod r to be greater than log^2(n), so the max value of the exponent of r is log^2(n).
    e_max = log2(n) ** 2
    exists_next_r = 1
    r = 1
    # Want to try out all values of r from 1 to r_max until we find one that works
    while exists_next_r:
        r += 1
        exists_next_r = 0
        e = 0
        while e < e_max and not exists_next_r:
            e += 1
            result = n ** e % r
            if result == 0 or result == 1:
                exists_next_r = 1
    assert r <= r_max
    return r

def isall_a_coprime_to_n(r, n):
    """
    This function checks if for all a such that 1 < a <= r, gcd(a, n) = 1.
    If this is the case, it will return 1, otherwise it will return 0.

    a is a value in [2, min(r, n)], see comments below for explanation.
    """
    # Remember that the minimum value of r is 2, however, we don't know which of r and n is smaller,
    # and so for the values of a, we will check all values from 2 to min(r, n), and we check if a is
    # co-prime to n.

    # Note: Maybe could use any() function here instead of for loop?

    for a in range(2, min(r, n)):
        if 1 < gcd(a, n) < n: # We found an a such that 1 < (a, n) < n
            return 0
    return 1

if __name__ == '__main__':
    # import doctest
    # doctest.testmod() # For testing purposes (make sure to comment out when submitting)

    print(main(int(sys.argv[1]))) # Will output PRIME or COMPOSITE
