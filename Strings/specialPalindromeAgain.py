import math
import os
import random
import re
import sys

# Complete the substrCount function below.


def check_palindrome(s):
    flag = 1
    first = 0
    last = len(s) - 1
    carrier = None
    # print(s)
    while first <= last:
        if s[first] != s[last]:
            flag = 0
            break
        if carrier is not None:
            if (s[first] != carrier or s[last] != carrier) and first != last:
                flag = 0
                break
        elif carrier is None:
            carrier = s[first]
        first += 1
        last -= 1
    return flag


def substrCount(n, s):
    count = 0
    for i in range(n):
        for j in range(i + 2, n + 1):
            if check_palindrome(s[i: j]):
                # print(s[i:j])
                count += 1
    count += n
    return count

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    print("*" * 200, "\n")

    result = substrCount(n, s)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
