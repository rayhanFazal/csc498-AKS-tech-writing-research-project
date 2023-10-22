import sys

def main(n):
    """
    The main function which will run the AKS algorithm on the given input n. It will use
    helper functions for each of the steps in the algorithm. This function will output
    either PRIME or COMPOSITE.
    """
    # Step 1:

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
    """
    pass

def get_smallest_r(n):
    """
    This function computes the smallest r such that the order of n mod r is greater than log^2(n).
    """
    pass

if __name__ == '__main__':
    main(sys.argv[1]) # Will output PRIME or COMPOSITE
