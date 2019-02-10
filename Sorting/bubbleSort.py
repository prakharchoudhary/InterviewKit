import math
import os
import random
import re
import sys

# Complete the countSwaps function below.


def countSwaps(a):
    swapCount = 0
    for i in range(len(a)):
        f = len(a)
        for j in range(f - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapCount += 1
        f -= 1
    print("Array is sorted in %d swaps.\nFirst Element: %d\nLast Element: %d" % (
        swapCount, a[0], a[len(a) - 1]))


if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
