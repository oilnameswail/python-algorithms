# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 16:47:08 2016

@author: ameliawilson
"""

import math

###############################################################################
# PRIME GENERATOR
# generates all primes up to input parameter
###############################################################################

#------------------------------------------------------------------------------
# Prime numbers: 
#------------------------------------------------------------------------------
#    
# 1. Every positive integer can be decomposed into a product of primes.
#
#    E.g.: 84 = 2^2 * 3^1 * 5^0 * 7^1 * 11^0 * 13^0 * 17^0 * ... 
#
# 2. Divisibility law: 
#
#    In order for a number x to divide a number y (y/x or mod(y,x) = 0) 
#    all primes in x's prime factorization must be in y's prime
#    factorization.
#
#       Let x = 2^j0 * 3^j1 * 5^j2 * 7^j3 * 11^j4 * ...
#       Let y = 2^k0 * 3^k1 * 5^k2 * 7^k3 * 11^k4 * ...
#       
#       if y/x, then for all i: ji <= ki
# 
#    The greatest common divisor of x and y will be:
#
#       gcd(x,y) = 2^min(j0, k0) * 3^min(j1, k1) * 5^min(j2, k2) * ...
#
#    The least commom multiple of x and y will be:
#
#       lcm(x,y) = 2^max(j0, k0) * 3^max(j1, k1) * 5^max(j2, k2) * ...
#
#    gcd * lcm:
#       
#       gcd * lcm = 2^min(j0, k0) * 2^max(j0, k0) * 
#                   3^min(j1, k1) * 3^max(j1, k1) * 
#                   5^max(j2, k2) * 5^min(j2, k2) * ... 
#                 = 2^(min(j0, k0) + max(j0, k0)) * 
#                   3^(min(j1, k1) + max(j1, k1)) *
#                   5^(max(j2, k2) + min(j2, k2)) * ... 
#                 = 2^(j0 + k0) * 3^(j1 + k1) * 5^(j2 + k2) * ...
#                 = 2^j0 * 2^k0 * 3^j1 * 3^k1 * 5^j2 * 5^k2 * ...
#                 = xy
#
#------------------------------------------------------------------------------

# (1) See if a number is prime: iterate from 2 to n-1, 
#     checking for divisibility at each iteration:
def naive_prime_check(number):
    if number < 2:
        return False
    for i in range(2,number): #python range is exclusive 
        if number % i == 0:
            return False
    return True
    
# (2) better: don't need to check against itself, only up to sqrt(number)
#     for every even divisor, there is another number that divides the divsor;
def sqrt_prime_check(number):
    if number < 2:
        return False
    for i in range(2, math.sqrt(number)):
        if number % i == 0:
            return False
    return True

# (3) Sieve of Eratosthenes
#     hightly efficient way to generate a list of primes
#     Works by recognizing that all non-prime numbers are divisible by a 
#     prime number
def sieve_of_eratosthenes(number):
    array = [True] * (number+1)
    array[0] = array[1] = False
    
    for (i, isprime) in enumerate(array):
        if isprime:
            yield i
            for n in range(i*i, number+1, i):
                array[n] = False
                
    
def main():
    
    prime_gen = sieve_of_eratosthenes(13)
    for i in prime_gen:
        print("test: "+str(i))        
    

main()
#------------------------------------------------------------------------------
# Probability: 
#------------------------------------------------------------------------------
#
#