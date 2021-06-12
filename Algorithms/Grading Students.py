#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    end = []
    for x in grades:
        if x < 38:
            end.append(int(x))
        else:
            if x % 5 == 3:
                end.append(int(x)+2)
            elif x % 5 == 4:
                end.append(int(x)+1)
            else:
                end.append(int(x))
    return(end)
    """if grades >= 38:
        if grades % 5 == 3:
            grades += 2
        elif grades % 5 == 4:
            grades += 1
    print(grades)"""
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
