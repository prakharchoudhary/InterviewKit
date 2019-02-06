import math
import os
import random
import re
import sys

# Complete the rotLeft function below.


def rotLeft(a, d):
    d = d % len(a)
    new_arr = [0 for i in a]
    for i, item in enumerate(a):
        if i - d < 0:
            new_arr[len(a) + (i - d)] = a[i]
        else:
            new_arr[i - d] = a[i]
    return new_arr


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    print(result)

    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
