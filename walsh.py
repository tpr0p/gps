"""A module to compute walsh code matrices."""
from functools import reduce
import numpy as np

def is_power2(n):
    """Determine if n is a power of 2."""
    # Method for other numbers 
    if n == 0:
        return True

    # If there is only one occurence of '1' in the binary representation
    # of n, then it is a power of 2.
    bin_str = bin(n)
    one_detected = False
    for char in bin_str:
        if char == '1':
            # If '1' has already been detected, then '1' occurs more than once.
            if one_detected:
                return False
            else:
                one_detected = True
        else:
            continue
    
    if one_detected:
        return True
    else:
        return False

def ones(n):
    """Return the square matrix n x n, where n is a power of 2
    and each entry is 1.
    """
    if not is_power2(n):
        raise ValueError("The function \'ones\' only accepts inputs that "
                         "are powers of 2.")
    if n == 0:
        raise ValueError("This droid does not know how to build a 0 x 0 matrix.")

    # The 2 x 2 ones matrix.
    two = np.matrix([[1, 1], [1, 1]])

    if n == 2:
        return two
    else:
        return reduce(np.kron, [two for _ in range(int(log2(n)))])

def walsh(n):
    """Return the Nth walsh matrix."""
    if not (n == 1 or is_power2(n)):
        raise ValueError("A walsh matrix must have 1 row or n rows "
                         "where n is a power of 2.")

    # Base Case
    if n == 1:
        return np.matrix([[0]])
    
    else:
        base = walsh(int(n/2))
        base_xor = base ^ 1
        mask1 = np.matrix([[1, 1],[1, 0]])
        mask2 = np.matrix([[0, 0],[0, 1]])
        return np.kron(mask1, base) + np.kron(mask2, base_xor)

if __name__ == "__main__":
    pass
