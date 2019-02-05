import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.


def jumpingOnClouds(c):
    currentPos = 0
    moves = 0
    while not currentPos == len(c) - 1:
        if currentPos + 2 < len(c) and c[currentPos + 2] != 1:
            currentPos += 2
            moves += 1
        else:
            currentPos += 1
            moves += 1
    return moves


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
