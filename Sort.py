import math
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 19:12:12 2016

@author: ameliawilson
"""



def swap_things(things_array, first_index, second_index):
    temp = things_array[first_index]
    things_array[first_index] = things_array[second_index]
    things_array[second_index] = temp
    
###############################################################################
# BUBBLE SORT
# Runtime: O(n^2)
###############################################################################

def bubble_sort_array(things_array):
    if len(things_array) < 2:
        return things_array
    for j in range(0, len(things_array)-1):
        for i in range(0, len(things_array)-1):
            if things_array[i] > things_array[i+1]:
                swap_things(things_array, i, i+1)
    return things_array

###############################################################################
# SELECTION SORT - essentially a linear sort
# Runtime: O(n^2)
###############################################################################
def selection_sort(things_array):
    if len(things_array) < 2:
        return things_array        
    for i in range(len(things_array)):
        smallest_idx = i                
        for j in range(i+1, len(things_array)):            
            if things_array[j] < things_array[smallest_idx]:
                smallest_idx = j
                
        swap_things(things_array, i, smallest_idx)


###############################################################################
# MERGE SORT
# Runtime: O(nlog(n))
###############################################################################
def merge_sort(things_array):
    if len(things_array) < 2:
        return things_array
    
    middle = len(things_array) // 2 #integer division
    
    left_half = things_array[:middle]
    right_half = things_array[middle:]

    merge_sort(left_half)
    merge_sort(right_half)    

    i = 0 #left index
    j = 0 #right index
    k = 0 #things_array index
    
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            things_array[k] = left_half[i]
            i += 1
        else:
            things_array[k] = right_half[j]
            j += 1
        k += 1
        
    while i < len(left_half):
        things_array[k] = left_half[i]
        i += 1
        k += 1
        
    while j < len(right_half):
        things_array[k] = right_half[j]
        j += 1
        k += 1
        
###############################################################################
# QUICK SORT
# Runtime: O(nlog(n))
###############################################################################

#------------------------------------------------------------------------------
# (A)  QUICK SORT OF STRINGS                                                  
#------------------------------------------------------------------------------
def quick_sort_string(string):
    string_array = list(string)
    start = 0
    end = len(string_array) - 1
    quick_sort_string_array(string_array, start, end) 
    return ''.join(string_array)

def quick_sort_string_array(string_array, start, end):
    if start <= end:
        i = start
        j = end
        p = start + (end - start) / 2
        while i <= j:
            while (string_array[i] < string_array[p]):
                i+=1
            while (string_array[j] > string_array[p]):
                j-=1
            if i <= j:
                exchange_string_characters(string_array, i, j)
                i+=1
                j-=1
            if start < j:
                quick_sort_string_array(string_array, start, j)
            if end > i:
                quick_sort_string_array(string_array, i, end)
    
            
def exchange_string_characters(string_array, i, j):
    temp = string_array[i]
    string_array[i] = string_array[j]
    string_array[j] = temp


#------------------------------------------------------------------------------
# (B)  QUICK SORT OF NUMBERS IN ARRAY                                                  
#------------------------------------------------------------------------------
def quick_sort_numbers(number_array):
    start = 0
    end = len(number_array) - 1
    quick_sort_number_array(number_array, start, end)
    
def quick_sort_number_array(number_array, start, end):
    if start <= end:
        i = start
        j = end
        p = start + (end - start) / 2
        while i <= j:
            while number_array[i] < number_array[p]:
                i+=1
            while number_array[j] > number_array[p]:
                j-=1
            if i <= j:
                exchange_numbers(number_array, i, j)
                i += 1
                j -= 1
            if start < j:
                quick_sort_number_array(number_array, start, j)
            if end > i:
                quick_sort_number_array(number_array, i, end)

def exchange_numbers(number_array, i, j):
    temp = number_array[i]
    number_array[i] = number_array[j]
    number_array[j] = temp

###############################################################################
# RADIX SORT
# Runtime: O(kn)
###############################################################################
def radix_sort(int_arr):
    RADIX = 10
    max_length = False
    tmp = -1
    place = 1
    
    while not max_length:

        max_length = True        
        buckets = [list() for _ in range(RADIX)]
                
        for it in int_arr:

            tmp = it / place
            buckets[tmp % RADIX].append(it)

            if max_length and tmp > 0:
                max_length = False
        
        a = 0
        for r in range(RADIX):

            b = buckets[r]
            
            for i in b:
                int_arr[a] = i
                a += 1            
        
        place *= RADIX


###############################################################################
# BUCKET SORT
# Runtime: O(n)
###############################################################################
def bucket_sort(int_arr):
    code = hash_it(int_arr) #returns [smallest_int, sqrt(len(int_arr))]
    print("code: "+str(code))    
    
    buckets = [list() for _ in range(code[1])]
    print("INITIAL buckets: "+str(buckets))    
    
    for it in int_arr:
        print("it in int_arr: "+str(it))

        x = re_hash(it, code)
        print("re_hash(it, code) = "+str(x))        
        
        buck = buckets[x]
        print("bucket at re_hash key ("+str(x)+") = "+str(buck))        
        
        buck.append(it)
        print("buck at re_hash key ("+str(x)+") after append it in int_array: "+str(buck))
        
    print("buckets AFTER hashing: "+str(buckets))
    for bucket in buckets:
        selection_sort(bucket)
    
    print("buckets AFTER sorting: "+str(buckets))
    
    idx = 0
    for b in range(len(buckets)):
        for n in buckets[b]:
            int_arr[idx] = n
            idx += 1
            
        

def hash_it(int_arr):
    it = int_arr[0]
    for i in range(1,len(int_arr)):
        if it < int_arr[i]:
            it = int_arr[i]
    result = [it, int(math.sqrt(len(int_arr)))]
    return result
    
def re_hash(i, code):
    #code[0] = smallest_int, code[1] = sqrt(len(int_arr))
    return int((i/code[0]) * (code[1] - 1))
    

###############################################################################
# (1) Sorted Merge: give 2 sorted arrays, write algorith to merge them
###############################################################################

#len(arrA) = len(arrA) + len(arrB)
#arrA is longer
#def merge_sorted_arrays(arrA, arrB, a_index = 0, b_index = 0, new_array = []):   
    
def merge_sorted_arrays(arrA, arrB):   
    a=len(arrA) - 1
    b=len(arrB) - 1
    new_array = [0 for i in range(0, len(arrA)+len(arrB))]
    n = len(new_array) - 1
    while b >= 0:    
        if a >= 0 and arrA[a] > arrB[b]:
            new_array[n] = arrA[a]
            a -= 1
        else:
            new_array[n] = arrB[b]
            b -= 1
        n -= 1
    return new_array


def main():
    '''
    test_array = [5,7,3,4,2,6]
    print("test_array before BUBBLE SORT: "+str(test_array))
    bubble_sort_array(test_array)
    print("test_array after BUBBLE SORT: "+str(test_array))
    
    test_array = [5,7,3,4,2,6]    
    print("test_array before SELECTION SORT: "+str(test_array))
    selection_sort_of_array(test_array)
    print("test_array after SELECTION SORT: "+str(test_array))

    test_array = [5,7,3,4,2,6]    
    print("test_array before MERGE SORT: "+str(test_array))
    merge_sort(test_array)
    print("test_array after MERGE SORT: "+str(test_array))
    

    arrA = [2,3,5,7,8,10,11]
    arrB = [1,4,6,9,13]
    new_array = merge_sorted_arrays(arrA, arrB)
    print("arrA = "+str(arrA))
    print("arrB = "+str(arrB))
    print("new = "+str(new_array))

    '''        
    test_array = [5,2,6,12, 100, 87, 3,4, 7,58, 13, 500]    
    print("test_array before BUCKET SORT: "+str(test_array))
    bucket_sort(test_array)
    print("test_array after BUCKET SORT: "+str(test_array))

   
        

main()