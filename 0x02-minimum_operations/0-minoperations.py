#!/usr/bin/python3
'''0-minoperations.py file
'''


def minOperations(n):
    ''' Implements the 0-minoperations algorithm
    Args: n
    Returns: operations
    '''
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
