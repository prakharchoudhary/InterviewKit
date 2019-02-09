#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the countTriplets function below.


def countTriplets(arr, r):
    count = 0
    r2 = Counter()
    r3 = Counter()
    for item in arr:
        if item in r3:
            count += r3[item]

        if item in r2:
            r3[item * r] += r2[item]

        r2[item * r] += 1
    return count

if __name__ == '__main__':

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    print(ans)
