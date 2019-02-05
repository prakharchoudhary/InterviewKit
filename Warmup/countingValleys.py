
import math
import os
import random
import re
import sys


def countingValleys(n, s):
    summ = 0
    valleyCount = 0
    valleyIn = False
    # states: 0 --> ground; 1 --> mountain; -1 --> valley
    for i in s:
        if i == 'U':
            summ += 1
        elif i == 'D':
            summ -= 1
        if summ == -1:
            if not valleyIn:
                valleyIn = True
        if summ == 0 and valleyIn == True:
            valleyCount += 1
            valleyIn = False
    return valleyCount

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
