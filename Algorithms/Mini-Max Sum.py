#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    #akhir = max(arr)
    #awal = min(arr)
    #ans=[]
    #for x in arr:
    hasil1 = sum(arr) - max(arr)
    hasil2 = sum(arr) - min (arr)
    print(str(hasil1)+" "+str(hasil2))
    

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
