"""
Author: Mr128Bit
Date:   03.05.23

This script is a Python implementation of the Pollard-Rho algorithm for factorizing a given integer into its prime factors. 
The script first applies the Sieve of Eratosthenes to find all prime numbers up to the square root of the given number, 
and then divides the number by each prime number found to check for divisibility.
If the number is still greater than 1 after division by all prime numbers, the Pollard-Rho method is applied to find the remaining prime factors. 
The script provides an efficient and effective way to factorize large integers into their prime factors, making it useful for cryptographic purposes.
"""

import math
import random
import sys

def pollard_rho(n):
    """
    This function implements the Pollard-Rho method for factorizing a given integer n.

    Args:
    n (int): The integer to be factorized.

    Returns:
    A list of prime factors of n.

    Example:
    >>> pollard_rho(15)
    [3, 5]
    """

    # initalise variables
    x = 2
    y = 2
    d = 1

    # implement Pollard-Rho-Method for factorizing n
    while d == 1:
        x = (x*x + 1) % n
        y = (y*y + 1) % n
        y = (y*y + 1) % n
        d = math.gcd(abs(x-y), n)

    # When a prime factor was found, recursively continue factorization
    if d != n:
        return factorize(d) + factorize(n//d)

    # if no prime factor was found return n
    return [n]

def factorize(n):
    """
    Factorize a given integer into prime factors using the sieve of Eratosthenes and the Pollard-Rho method.

    Args:
    n (int): An integer to be factorized.

    Returns:
    List[int] or str: A list of prime factors of the given integer, or an error message if the factorization is not unique.

    """

    orig_n = n
    factors = []
    limit = int(math.sqrt(n))
    
    # apply sieve of eratosthenes to find prime numbers up to the root of n
    primes = sieve_of_eratosthenes(limit)

    # Divide n by each prime number found
    for p in primes:
        while n % p == 0:
            factors.append(p)
            n //= p
        if n == 1:
            break

    # If n is still greater than 1, apply Pollard Rho method
    if n > 1:
        factors += pollard_rho(n)

    if len(factors) == 2:
        return factors
    else:
        return "Fehler: Die Zahl hat keine eindeutige Faktorisierung in 2 Primzahlen."

def sieve_of_eratosthenes(n):
    """
    Find all prime numbers up to the input integer n using the Sieve of Eratosthenes.

    Args:
        n (int): The upper limit of the prime numbers to find.

    Returns:
        list of int: The prime numbers up to n.
    """
    # Generate a list of n booleans that are initially set to true.
    sieve = [True] * (n+1)

    # 0 and 1 are no prime numbers
    sieve[0] = sieve[1] = False

    for i in range(2, int(math.sqrt(n))+1):
        if sieve[i]:
            # Mark all multiples of i as not prime
            for j in range(i*i, n+1, i):
                sieve[j] = False

    # Extract the list of prime numbers from the sieve
    primes = []
    for i in range(2, n+1):
        if sieve[i]:
            primes.append(i)

    return primes

if __name__ == "__main__":

    args = sys.argv
    number = None

    try:
        number = int(args[1])

        if number > 1:
            factors = factorize(number)
            print(factors)
        else:
            print("Please submit a valid number")
        
    except ValueError:
        print("Please submit a valid number")
        exit(1)
