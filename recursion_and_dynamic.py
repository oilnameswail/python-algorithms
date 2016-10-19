# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 21:47:47 2016

@author: ameliawilson
"""

###############################################################################
# RECURSION AND DYNAMIC PROGRAMMING
###############################################################################



###############################################################################
# FIBONACCI
###############################################################################

#bottoms up
def iterative_fibonacci(n, fiba):
    while len(fiba) < n:        
        if len(fiba) == 0:
            fiba.append(0)
        elif len(fiba) == 1:
            fiba.append(1)
        else:
            fiba.append(fiba[len(fiba)-1]+fiba[len(fiba)-2])


def recursive_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1    
    return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)
    

#top down
def memoized_fibonacci(n):
    memo = [0 for i in range(n)]
    memoized_fibonacci_array(n-1, memo)
    return memo
    

def memoized_fibonacci_array(n, memo):     
    if n == 0:
        memo[n] = 0 
        return memo[n]
    elif n == 1:
        memo[n] = 1
        return memo[n]  
    else:
        memo[n] = memoized_fibonacci_array(n-1, memo) + memoized_fibonacci_array(n-2, memo)  
    return memo[n]


###############################################################################
# Triple Step: A child is running up a staircase with n steps and can hop
#   either 1 step, 2 steps, or 3 steps at once. Implement a method to count
#   how many possible ways the child can run up the stairs.
###############################################################################
def stair_stepper_counter(steps):
    if steps < 0:
        return 0
    elif steps == 0:
        return 1
    else:
     return stair_stepper_counter(steps-1) + stair_stepper_counter(steps-2) + stair_stepper_counter(steps-3)
        
###############################################################################
# Robot On A Grid: Imagine a robot on the upper left corner of a grid with r
#   rows and c columns. The robot can only move in two directions, right and 
#   down, but certain cells are "off limits" such that the robot cannot step 
#   on them. Design an algoirthm to find a path for the robot from the top left
#   to the bottom right.
###############################################################################

# location is a point: (y,x) or (r,c)
# ways can move: (r-1, c), (r, c-1)
def robot_path(location):
    pass



###############################################################################
# Magic Index: A magic index in an array A[1,...,n-1] is defined to be an index
#   such that A[i] = i. Given a sorted array of distinct integers, wrtie a 
#   method to find a magic index, if one exists in array A.
###############################################################################

def brute_force_find_magic_index(sorted_array):
    magic_index = None
    for i in range(len(sorted_array)-1):
        if sorted_array[i] == i:
            magic_index = i
    return magic_index
    
def better_find_magic_index(sorted_array):
    #flex info that the array is sorted
    #start at middle, decide which half to search
    return binary_search_of_magic_index(sorted_array, 0, len(sorted_array)-1)
        
def binary_search_of_magic_index(sorted_array, start, end):
    
    i = (start+end)/2
    if sorted_array[i] == i:
        return i
    elif sorted_array[i] < i:
        return binary_search_of_magic_index(sorted_array, 0, i-1)
    else:
        return binary_search_of_magic_index(sorted_array, i+1, end)


###############################################################################
# Recursive Multiply: Write a recursive function to multiply two positive 
#   integers without using the * or / operators. You can use addition, 
#   subtraction, and bit shifting, but you should minimize the number of those
#   operations.
###############################################################################

def naive_multiply(n1, n2):
    smaller = n1 if n1 < n2 else n2
    bigger = n2 if smaller is n1 else n1
    return naive_product(smaller,bigger)
    
def naive_product(small, big):
    if small == 0: return 0
    elif small == 1: return big    
    return big + naive_product(small-1, big)        


def min_product(n1, n2):
    smaller = n1 if n1 < n2 else n2
    bigger = n2 if smaller is n1 else n1
    return min_product_helper(smaller, bigger)

def min_product_helper(small, big):
        
    if small == 0: return 0
    elif small == 1: return big
    
    #compute half: if uneven, compute other half. if even, double it
    half_small = small // 2 #integer division
    half_product = min_product_helper(half_small, big)    
    if (small % 2) == 0:
        return half_product + half_product
    else:
        return half_product + half_product + big               

###############################################################################
#   Coins: Given an infinte number of Quarters, Dimes, Nickels, and Pennies,
#          write code to calculate the number of ways of representing n cents
###############################################################################

def make_change(cent_amount):
    quarter = 25
    dime = 10
    nickel= 5
    penny = 1    
    coins = [quarter, dime, nickel, penny]
    
    return make_change_helper(cent_amount, coins, 0)
    

def make_change_helper(cent_amount, coins, index):
    if index >= (len(coins) - 1):
        return 1
    coin = coins[index]
    ways = 0
    i = 0
    while i * coin <= cent_amount +1:
        amount_remaining = cent_amount - i * coin
        ways += make_change_helper(amount_remaining, coins, index+1)
        i += 1
    return ways


def main():

    n = 20

    fibi = []
    iterative_fibonacci(n, fibi)
    print("1. ITERATIVE: First "+str(n)+" fibonacci numbers = "+str(fibi))

    fibr = []
    for i in range(n):
        fibr.append(recursive_fibonacci(i))
    print("2. RECURSIVE: First "+str(n)+" fibonacci numbers = "+str(fibr))

    fibm = memoized_fibonacci(n)
    print("2. MEMOIZED: First "+str(n)+" fibonacci numbers = "+str(fibm))
    
    steps = 3
    print("possiblities: "+str(stair_stepper_counter(steps)))
    
    
    n1, n2 = 5, 3
    result = naive_multiply(n1, n2)
    print("naive mult: "+str(result))
    
    result = min_product(n1, n2)
    print("min_prod: "+str(result))



    cent_amount = 100
    print "ways: "+str(make_change(cent_amount))

main()

