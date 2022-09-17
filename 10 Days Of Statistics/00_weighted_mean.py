#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'weightedMean' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY X
#  2. INTEGER_ARRAY W
#




def weightedMean(X, W):
    xw_sum = 0
    for i in range(len(X)):
        xw_sum += X[i] * W[i]
    weighted_mean = xw_sum/sum(W)
    print(round(weighted_mean, 1))

if __name__ == '__main__':
    # n = int(input().strip())

    # vals = list(map(int, input().rstrip().split()))

    # weights = list(map(int, input().rstrip().split()))

    vals = [1, 2, 3]
    weights = [5, 6, 7]

    weightedMean(vals, weights)
