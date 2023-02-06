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

def gradingStudents(Students_Mark):
    # Write your code here
    
    # Write your code here
    Rounded_Mark = []
    for grade in Students_Mark:
        if grade < 38:
            Rounded_Mark.append(grade)
        else:
            diff = 5 - (grade % 5)
            if diff == 0:
                Rounded_Mark.append(grade)
            elif diff >=3:
                Rounded_Mark.append(grade)
            else:
               Rounded_Marks.append(grade+diff)
    return Rounded_Mark


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
        
      
