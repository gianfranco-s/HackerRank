#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'interQuartile' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY freqs
#




def interQuartile(values, freqs):
    S = []
    
    # for i in range(len(values)):
    #     S += [values[i] for e in range(freqs[i])]
    
    # More pythonic code:
    for value,freq in zip(values, freqs):
        S += [value for e in range(freq)]
    S.sort()

    def calc_median(data):
        n = len(data)
        return (data[n//2] + data[~(n//2)]) / 2
    
    N = len(S)
    quartiles_list = [calc_median(S[:N//2]), calc_median(S), calc_median(S[(N+1)//2:])]

    print(quartiles_list[2] - quartiles_list[0])

if __name__ == '__main__':

    # Test code #1
    val = [6, 12, 8, 10, 20, 16]
    freq = [5, 4, 3, 2, 1, 5]

    # Test code #2
    val = [1, 2, 3]
    freq = [3, 2, 1]
    interQuartile(val, freq)
