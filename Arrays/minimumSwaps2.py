import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.


def swapFor(arr, i):
    global swapCount
    while i != arr[i]:
        tempa = arr[i]
        tempb = arr[arr[i]]
        arr[i] = tempb
        arr[tempa] = tempa
        swapCount += 1
    return arr


def minimumSwaps(arr):
    global swapCount
    arr = [i - 1 for i in arr]
    # print(arr)
    while True:
        for idx, item in enumerate(arr):
            if item == idx:
                continue
            else:
                arr = swapFor(arr, idx)
        break
    return swapCount


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    swapCount = 0

    res = minimumSwaps(arr)

    print(res)

    # fptr.write(str(res) + '\n')

    # fptr.close()
