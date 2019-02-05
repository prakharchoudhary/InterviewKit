import math
import os
import random
import re
import sys


def repeatedString(s, n):
    n_iter = int(n / len(s))
    rem = n % len(s)
    rem_a = 0
    rem_count = 0
    a_in_iter = 0
    for i in s:
        if i == 'a':
            a_in_iter += 1
            if rem_count < rem:
                rem_a += 1
        rem_count += 1
    return n_iter * a_in_iter + rem_a

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
