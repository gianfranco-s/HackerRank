#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def quartiles(arr):
    '''
    odd number of data points: do not include the median (the central value in the ordered list) in either half (returns 3 quartiles)
    even number of data points: split this data set exactly in half (returns 2 quartiles)
    '''
    arr.sort()
    def calc_median(arr):
        mid = len(arr) // 2  # Floor division
        median = (arr[mid] + arr[~mid]) / 2  # ~mid is the same as -mid-1
            ## Given a 5-element array:
            # [  0 |  1 |  2 |  3 |  4 ]  # Index
            # [  9 ,  5 ,  7 ,  1 ,  3 ]  # Value
            # arr[mid] would be arr[2] = 7

            # Using negative indexes:
            # [ -5 | -4 | -3 | -2 | -1 ]  # Index
            # [  9 ,  5 ,  7 ,  1 ,  3 ]  # Value
            # arr[~mid] would be arr[-2-1] = 7

            ## Given a 6-element array:
            # [  0 |  1 |  2 |  3 |  4 |  5 ]  # Index
            # [  9 ,  5 ,  7 ,  1 ,  3 ,  8 ]  # Value
            # arr[mid] would be arr[3] = 1

            # Using negative indexes:
            # [ -6 | -5 | -4 | -3 | -2 | -1 ]  # Index
            # [  9 ,  5 ,  7 ,  1 ,  3 ,  8 ]  # Value
            # arr[~mid] would be arr[-3-1] = 7
        return median
    
    mid = len(arr) // 2
    
    if len(arr) % 2 != 0:
        lower = arr[:mid]
        Q1 = calc_median(lower)
        Q2 = arr[mid]
        
        upper = arr[mid+1:]
        Q3 = calc_median(upper)
        
        quartiles_list = [Q1, Q2, Q3]

    else:

        lower = arr[:mid]
        Q1 = calc_median(lower)
        
        Q2 = calc_median(arr)

        upper = arr[mid:]
        Q3 = calc_median(upper)
        
        quartiles_list = [Q1, Q2, Q3]

    # Possible one-liners
    mid = len(arr) / 2
    # quartiles_list = [calc_median(arr[:int(mid)]), calc_median(arr), calc_median(arr[math.ceil(mid):])]
    # quartiles_list = list(map(calc_median, [arr[:int(mid)], arr, arr[math.ceil(mid):]]))
    # quartiles_list = [calc_median(e) for e in (arr[:int(mid)], arr, arr[math.ceil(mid):])]
    
    print(quartiles_list)
    return quartiles_list

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input().strip())

    # data = list(map(int, input().rstrip().split()))

    arr = '3 7 8 5 12 14 21 13 18'
    # arr = '3 7 8 5 12 14 21 15 18 14'
    
    
    data = [int(e) for e in arr.split()]
    
    # data = [7, 15, 36, 39, 40, 41]
    # data = [1, 3, 3, 4, 5, 6, 6, 7, 8, 8]
    res = quartiles(data)

    # fptr.write('\n'.join(map(str, res)))
    # fptr.write('\n')

    # fptr.close()
