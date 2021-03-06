import math
import os
import random
import re
import sys

# Complete the countInversions function below.


def sort_pair(arr0, arr1):
    if len(arr0) > len(arr1):
        return arr1, arr0
    else:
        return arr0, arr1


def merge(arr0, arr1):
    inversions = 0
    result = []
    i0 = 0
    i1 = 0
    len0 = len(arr0)
    len1 = len(arr1)
    while len0 > i0 and len1 > i1:
        if arr0[i0] <= arr1[i1]:
            result.append(arr0[i0])
            i0 += 1
        else:
            inversions += len0 - i0
            result.append(arr1[i1])
            i1 += 1

    if len0 == i0:
        result += arr1[i1:]
    elif len1 == i1:
        result += arr0[i0:]

    return result, inversions


def sort(arr):
    length = len(arr)
    mid = length // 2
    if length >= 2:
        sorted_0, counts_0 = sort(arr[:mid])
        sorted_1, counts_1 = sort(arr[mid:])
        result, counts = merge(sorted_0, sorted_1)
        return result, counts + counts_0 + counts_1
    else:
        return arr, 0


def countInversions(a):
    final_array, inversions = sort(a)
    return inversions

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

        print(result)

        # fptr.write(str(result) + '\n')

    # fptr.close()
