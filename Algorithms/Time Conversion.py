#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    AM_PM = s[-2:]
    #print(AM_PM)
    s = s[:8]
    hh, mm, ss = [int(x) for x in s.split(":")]
    #print(mm)
    if AM_PM == 'PM' and hh != 12:
        return('{:02}:{:02}:{:02}'.format(hh+12, mm, ss))
    elif AM_PM == 'AM' and hh == 12:
        return('{:02}:{:02}:{:02}'.format(0, mm, ss))
    else:
        return('{:02}:{:02}:{:02}'.format(hh, mm, ss))
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
