#!/usr/bin/python3
"""
Module for calculating the minimum number of operations
to reach n 'H' characters.
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in exactly n H
    characters in the file.

    Args:
        n (int): The target number of H characters.

    Returns:
        int: The minimum number of operations (Copy All and Paste).
             Returns 0 if n is impossible to achieve (n <= 1).
    """
    if not isinstance(n, int) or n <= 1:
        return 0

    operations = 0
    divisor = 2
    # Find the sum of prime factors
    temp_n = n  # Use a temporary variable for calculations
    while divisor * divisor <= temp_n:
        if temp_n % divisor == 0:
            operations += divisor
            temp_n //= divisor
        else:
            divisor += 1
    # If temp_n is still > 1, it must be a prime factor itself
    if temp_n > 1:
        operations += temp_n

    return operations
