import math
import os
import random
import re
import sys
from collections import Counter

# Complete the isValid function below.


def isValid(s):
    c = Counter(s)
    d = Counter()
    for k, v in c.items():
        if v in d.keys():
            d[v].append(k)
        else:
            d[v] = [k]
    elem_in_d = list(d.keys())
    if len(elem_in_d) == 1:
        return "YES"
    if len(elem_in_d) > 2:
        return "NO"
    if abs(elem_in_d[0] - elem_in_d[1]) > 1:
        if min(elem_in_d) == 1 and len(d[min(elem_in_d)]) == 1:
            return "YES"
        return "NO"
    if len(d[elem_in_d[0]]) == 1 or len(d[elem_in_d[1]]) == 1:
        return "YES"
    return "NO"

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    print(result)

    # fptr.write(result + '\n')

    # fptr.close()
