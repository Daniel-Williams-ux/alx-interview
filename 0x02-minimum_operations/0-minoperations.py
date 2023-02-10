#!/usr/bin/python3
""" Minimum Operations"""
import sys


def minOperations(n):
    """Given a number n, write a method that calculates
       the fewest number of operations needed to
       result in exactly n H characters in the file."""
    """Initial state"""
    op = 0
    min_op = 2
    """Iterate for the remaining numbers"""
    while n > 1:
        while n % min_op == 0:
            op += min_op
            n /= min_op
        """Obtaining the number by adding 1"""
        min_op += 1
    return op
