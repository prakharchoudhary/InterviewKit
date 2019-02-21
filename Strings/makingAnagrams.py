#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the makeAnagram function below.


def makeAnagram(a, b):
    count = 0
    c = Counter()
    for i, item in enumerate(a):
        if item in c.keys():
            c[item] += 1
        else:
            c[item] = 1
    for j, item in enumerate(b):
        if item in c.keys():
            c[item] -= 1
        else:
            c[item] = -1

    for key, val in c.items():
        if val != 0:
            count += abs(val)
    return count

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    print(res)

    # fptr.write(str(res) + '\n')

    # fptr.close()
