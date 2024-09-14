#!/usr/bin/python3
"""
calculates the fewest number of operations needed to result in exactly n H characters in the file.
"""


def minOperations(n):
    """Calculate the minimum number of operations to get exactly n H's."""
    if n <= 1:
        return 0

    operations = 0
    current = 1

    # Start from 2 to find factors
    for i in range(2, n + 1):
        # While i is a factor of n
        while n % i == 0:
            operations += i  # Add the number of operations to reach i H's
            n //= i  # Reduce n by its factor
    return operations
