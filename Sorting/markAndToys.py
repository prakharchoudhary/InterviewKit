import math
import os
import random
import re
import sys
from itertools import accumulate

# Complete the maximumToys function below.


def maximumToys(prices, k):
    count = 0
    sorted_prices = sorted(prices)
    cummulative = list(accumulate(sorted_prices))
    for i in cummulative:
        if i > k:
            break
        count += 1
    return count

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
