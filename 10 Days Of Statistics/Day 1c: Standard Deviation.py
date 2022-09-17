#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stdDev' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def stdDev(arr):
    mu = sum(arr)/len(arr)  # mean
    sqd_dist = []
    for el in arr:
        sqd_dist.append((el - mu)**2)
    standard_dev = math.sqrt(sum(sqd_dist) / len(arr))
    print(round(standard_dev, 1))

if __name__ == '__main__':
    # n = int(input().strip())

    # vals = list(map(int, input().rstrip().split()))

    vals = [2, 5, 2, 7, 4]
    vals = [10, 40, 30, 50, 20]
    stdDev(vals)
