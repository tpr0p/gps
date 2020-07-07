"""
walsh.py - This module is used to build walsh code matrices.
"""

from functools import reduce
import numpy as np

def is_power2(n):
    """
    is_power 2 - determine if n is a power of 2
    """
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

    
def walsh(n):
    """
    walsh - return the n-th walsh matrix
    """
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
