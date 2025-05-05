#!/usr/bin/python3
import sys

def factorial(n):
    """
    Recursively calculate the factorial of a non-negative integer.

    Function Description:
        This function uses recursion to compute the factorial of a given
        non-negative integer. The factorial of 0 is defined as 1. For all
        other positive integers, the factorial is calculated as:
        n! = n × (n-1)!

    Parameters:
        n (int): A non-negative integer whose factorial is to be computed.

    Returns:
        int: The factorial of the input integer n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Check for correct number of arguments
if len(sys.argv) != 2:
    print("Usage: ./factorial_recursive.py <non-negative integer>")
    sys.exit(1)

try:
    # Convert input to integer
    num = int(sys.argv[1])
    if num < 0:
        raise ValueError("Input must be a non-negative integer")

    # Compute and print the factorial
    result = factorial(num)
    print(result)

except ValueError as e:
    print("Error:", e)
    sys.exit(1)
