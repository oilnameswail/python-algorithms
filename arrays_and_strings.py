import re
import sys

'''
Practicing Array and String manipulation/algorithms
Source of some problems:  Cracking The Coding Interview
'''

def main():
    '''
    strings = ['cat', 'doggie', 'apathy', 'aAb']
    single_string_methods = ['set_unique_chars_in_string', 'algorithm_hash_unique_chars_in_string', \
               'algorithm_ascii_unique_chars_in_string', 'quick_sort_string']
    for method in single_string_methods:    
        test_method(method, strings)  
    double_string_methods = ['permutation_by_sort','permutation_by_char_counts']
    double_strings = ['cat,act', 'cat,dog', 'cats,caat']
    for method in double_string_methods:    
        test_method(method, double_strings)  

    test_method('URLify', ['Mr John Smith   ,13'])    
    
    one_way_test_strings = ['cat,cats', 'cats,hats', 'hat,that', 'hat,heat', 'cat,hats', 'cats,thats']
    test_method('one_away', one_way_test_strings)
    test_method('one_away_in_one', one_way_test_strings)

    test_method('compress_string', ['aabcccccaaa'])
    '''
    #create_4x4_matrix()
    #rotate_nxn_matrix_90_degrees()
    
    zero_matrix()
    
def test_method(method, strings_test):
    thismodule = sys.modules[__name__]
    header = ['METHOD', 'TEST', 'RESULT']
    method_to_execute = getattr(thismodule, method)    
    result = []    
    for string_test in strings_test:
        if len(string_test.split(',')) > 1:
            string_test_split = string_test.split(',')
            result.append([method, string_test_split, method_to_execute(*string_test_split)])
        else: result.append([method, string_test, method_to_execute(string_test)])
    print_results(header, 40, result)
        
def print_results(header, width, results):
    print_header(header, width)
    for row in results:
        print_table(row, width)

def print_header(header, width):
    longwidth = width * 3
    print '=' * longwidth    
    for title in header:
        print '{:{width}}'.format('| '+title, width=width),
    print
    print '=' * longwidth
    
def print_table(row, width):
    longwidth = width * 3  
    for item in row:
        print '{:{width}}'.format('| '+str(item), width=width),
    print 
    print '-' * longwidth
    
    

###############################################################################
# (1) Is Unique: Implement an algorithm to determine if a string has all      #
#     unique characters. What if you cannot use additional data structures?   #
###############################################################################

def set_unique_chars_in_string(string):
    char_set = set(string)
    if len(char_set) == len(string):
        return True
    return False
        
def algorithm_hash_unique_chars_in_string(string):
    char_dict = {}    
    for i in range(0, len(string)):
        char_dict[string[i]] = i
    if len(char_dict) == len(string):
        return True
    return False

def algorithm_ascii_unique_chars_in_string(string):
    if(len(string) > 128):
        return False
    bit_chars = {}
    for i in range(0, len(string)):
        val = ord(string[i])        
        try:
            if bit_chars[val]:
                return False
        except KeyError:
            bit_chars[val] = True
    return True
        
    
    

###############################################################################
# (2) Check Permutation: Given 2 strings, write a method to decide if one is  #
#     a permutation of the other.                                             #
###############################################################################
def permutation_by_sort(string1, string2):
    if len(string1) != len(string2):
        return False
    #return quick_sort_string(string1) == quick_sort_string(string2)
    return sorted(string1) == sorted(string2)

def permutation_by_char_counts(string1, string2):
    if len(string1) != len(string2):
        return False
    letter_count = {}
    for char in string1:
        try:
            count = letter_count[char] + 1
            letter_count[char] = count
        except KeyError:
            letter_count[char] = 1
    for char in string2:
        try:
            count = letter_count[char] - 1
            letter_count[char] = count
        except KeyError:
            letter_count[char] = 1
    counts = list(set(letter_count.values()))    
    if len(counts) > 1:
        return False
    
    elif counts[0] != 0:
        return False    
    return True
    
    
###############################################################################
# (3) URLify: Write a method to replace all spaces in a string with '%20'.    #
#     You may assume that the string has sufficient space at the end to hold  #
#     the additional characters, and that you are given the "true" length of  #
#     the string. (Note: If implementing in Java, please use a character      #
#     array so that you can perform this operation in place.)                 #
###############################################################################

def URLify(string, tru_len):
    char_array = list(string)
    tru_len = int(tru_len)
    replacement = '%20'
    for i in reversed(range(0, tru_len)):
        if char_array[i] == ' ':
            char_array[i] = replacement    
    return ''.join(char_array)
    
###############################################################################
# (4) Palindrome Permutation: Given a string, write a function to check if it #
#     is a permutation of a palindrome. A palindrome is a word or phrase that #
#     is the same backwards and forwards. A permutation is a rearrangement of #
#     letters. The palindrome does not need to be limited to just dictionary  #
#     words.                                                                  #
#     - to decide if a a string is a permutation of a palindrome, we need to  #
#       know if it can be written such that it's the same bw & fw             #
#     - written bw & fw:                                                      #
#       -- even # of characters: 1/2 on one side, 1/2 on other                #
#       -- at most 1 'odd' character in the middle                            # 
#     - strings of even length must have even character counts                #
#     - strings of odd length must have 1 odd character count                 #
###############################################################################
def permutation_of_palindrome(string):
    white_space = re.compile(r'\s+')   
    trimmed_string = white_space.sub('', string)
    odd_count = 0
    char_count_map = {}
    for i in range(0, len(trimmed_string)):
        if char_count_map.has_key(trimmed_string[i]):
                char_count_map[trimmed_string[i]] = char_count_map[trimmed_string[i]] + 1
        else:
            char_count_map[trimmed_string[i]] = 1

    for count in char_count_map.itervalues():
        if count % 2 != 0:
            odd_count += 1
    
    if len(trimmed_string) % 2 == 0 and odd_count != 0:
        return False
    elif len(trimmed_string) % 2 != 0 and odd_count != 1:
        return False
    return True
     
###############################################################################
# (5) One Away: There are 3 types of edits that can be performed on strings:  #
#     insert a character, remove a character, replace a character. Given 2    #
#     strings, write a function to check if they are 1 edit (or 0 edits) away #
############################################################################### 
def one_away(string1, string2):
    if abs(len(string1) - len(string2)) > 1:
        return False
    elif abs(len(string1) - len(string2)) == 1:
        if len(string1) < len(string2):
            return one_away_edit(string1, string2)
        elif len(string1) > len(string2):
            return one_away_edit(string2, string1)
    else: #len(string1) == len(string2):
        return one_away_replace(string1, string2)

def one_away_edit(shorter, longer):
    shorter_index = 0
    longer_index = 0
    while shorter_index < len(shorter) and longer_index < len(longer):
        if shorter[shorter_index] != longer[longer_index]:
            if shorter_index != longer_index:
                return False
            longer_index += 1
        else:
            shorter_index += 1
            longer_index += 1
    return True
        

def one_away_replace(string1, string2):
    already_found_difference = False
    for i in range(0, len(string1)):
        if string1[i] != string2[i]:
           if already_found_difference:
               return False
           already_found_difference = True
    return True
   
   
def one_away_in_one(string1, string2):
    if abs(len(string1) - len(string2)) > 1:
        return False
    else:
        shorter = string1 if len(string1) < len(string2) else string2
        longer = string2 if shorter == string1 else string1
        found_difference = False
        shorter_index = 0
        longer_index = 0
        while shorter_index < len(shorter) and longer_index < len(longer):
            if shorter[shorter_index] != longer[longer_index]:
                if found_difference:
                    return False
                found_difference = True
                longer_index += 1
                if len(shorter) == len(longer):
                    shorter_index += 1
            else:
                shorter_index+=1
                longer_index += 1                    
    return True
    
###############################################################################
# (6) String Compression: Implement a method to perform basic string          #
#     compression using the counts of repeated characters. For example, the   #
#     string aabcccccaaa would become a2b1c5a3. If the compressed string      #
#     would not become smaller than the original string, your method should   #
#     return the original string. You can assume the string only has          #
#     uppercase and lowercase letters.                                        #
###############################################################################    
def compress_string(string):
    compressed_string = ''
    consecutive_count = 0
    for i in range(0, len(string)):
        consecutive_count +=1
        if i + 1 >= len(string) or string[i] != string[i+1]:
            compressed_string += string[i]+str(consecutive_count)
            consecutive_count = 0
    if len(compressed_string) >= string:
        return string
    else:
        return compressed_string
    

###############################################################################
# (7) Rotate Matix: Given an image represented by an NxN matrix, where each   #
#     pixel in the image is 4 bytes, write a method to rotate the image by 90 #
#     degrees. Can you do this in place?                                      #
###############################################################################  
def create_4x4_matrix():
    rows, cols = 4, 4 
    #matrix[x][y]    
    matrix = [[0 for x in range(cols)] for y in range(rows)]

    #1st col: x = 0, y = 0 -> 3
    matrix[0][0] = 'A-1'#'A-00'
    matrix[0][1] = 'A-2'#'A-01'
    matrix[0][2] = 'A-3'#A-02'
    matrix[0][3] = 'A-4'#'A-03'
    #2nd col: x = 1, y = 0 -> 3
    matrix[1][0] = 'B-1'#'B-10'
    matrix[1][1] = 'B-2'#'B-11'
    matrix[1][2] = 'B-3'#'B-12'
    matrix[1][3] = 'B-4'#'B-13'    
    #3rd col: x = 2, y = 0 -> 3
    matrix[2][0] = 'C-1'#'C-20'
    matrix[2][1] = 'C-2'#'C-21'
    matrix[2][2] = 'C-3'#'C-22'
    matrix[2][3] = 'C-4'#'C-23'    
    #4th col: x = 3, y = 0 -> 3
    matrix[3][0] = 'D-1'#'D-30'
    matrix[3][1] = 'D-2'#'D-31'
    matrix[3][2] = 'D-3'#'D-32'
    matrix[3][3] = 'D-4'#'D-33'

    
    print('--MATRIX:-------------')

    for y in range(rows):
        print('  '.join(matrix[x][y] for x in range(cols)))

    print('----------------------')
    
    return matrix
    

def rotate_nxn_matrix_90_degrees():
    matrix = create_4x4_matrix()
    rows = []
    cols = []
    
        
    for y in range(0,4):
        rows.append([matrix[x][y] for x in range(0,4)])
    
    for x in range(0,4):
        cols.append([matrix[x][y] for y in range(0,4)])

    '''
    print('--ROWS:---------------')    
    for row in rows:
        print(str(row))
    print('--COLUMNS:------------')        
    for col in cols:
        print(str(col))            
    print('----------------------')
    '''
    #rotate 90 degrees: put reversed first row in first column, reversed second row in second col...
    new_cols = []    
    for row in rows:
        #print("row: "+str(row))
        new_row = []
        for r in reversed(range(len(row))):
            new_row.append(row[r])
        new_cols.append(new_row)

    '''
    print('--NEW COLUMNS:--------')        
    for new_col in new_cols:
        print(str(new_col))
    '''
       
    for x in range(0,4):
        column = new_cols[x]
        for y in range(0,4):
            matrix[x][y] = column[y]
            
    
    print('--NEW MATRIX:---------')     
    for y in range(0,4):
        print('  '.join(matrix[x][y] for x in range(0,4)))
    print('----------------------')

    
            
    
        

###############################################################################
# (8) Zero Matix: Write an algorithm such that if an element in an MxN matrix #
#     is 0, its entire row and column are set to 0.                           #
############################################################################### 
def create_ones_matrix():
    row,col = 4,4
    matrix = [[1 for x in range(row)] for y in range(col)]
    
    print('--[ MATRIX of 1\'s: ]-----------')    
    for y in range(row):
        print('  '.join(str(matrix[x][y]) for x in range(col)))
    print('-------------------------------')
    return matrix


def zero_matrix():
    matrix = create_ones_matrix()
    #zero 0,0 out:
    matrix[1][1] = 0
    print('--[ MATRIX with (0,0) = 0 ]----')    
    for y in range(4):
        print('  '.join(str(matrix[x][y]) for x in range(4)))
    print('-------------------------------')
    
    #find the zero:
    zero_point = None
    for y in range(4):
        for x in range(4):
            if matrix[x][y] == 0:
                zero_point = (x,y)
    
    print("zero_point: "+str(zero_point))
    
    zero_x = zero_point[0]
    zero_y = zero_point[1]
    for x in range(4):
        if x == zero_x:
            for y in range(4):
                matrix[x][y] = 0
    for y in range(4):
        if y == zero_y:
            for x in range(4):
                matrix[x][y] = 0
                
    print('--[ ZERO MATRIX ]--------------')    
    for y in range(4):
        print('  '.join(str(matrix[x][y]) for x in range(4)))
    print('-------------------------------')
    

###############################################################################
# (9) String Rotation: Assume you have a method isSubstring which checks if   #
#     one word is a substring of the other. Given 2 strings, s1 and s2, write #
#     code to check if s2 is a rotation of s1 using only one call to          #
#     isSubstring (e.g., 'waterbottle' is a rotation of 'erbottlewat')        #
###############################################################################  





###############################################################################
# (A)  QUICK SORT OF STRINGS                                                  #
###############################################################################

def quick_sort_string(string):
    string_array = list(string)
    start = 0;
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


main()
