import math
import os
import random
import re
import sys

# Complete the substrCount function below.


def substrCount(n, s):
    tuples = []
    curr = None
    count = 0

    for i in range(n):
        if s[i] == curr:
            curr += 1
        else:
            if curr is not None:
                tuples.append((curr, count))
            curr = s[i]
            count = 1
    tuples.append((curr, count))

    ans = 0

    for i in tuples:
        ans += (i[1] * (i[1] + 1)) // 2

    for i in range(1, len(tuples) - 1):
        if tuples[i - 1][0] == tuples[i + 1][0] and tuples[i][1] == 1:
            ans += min(tuples[i - 1][1], tuples[i + 1][1])
    return ans

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    # print("*" * 200, "\n")

    result = substrCount(n, s)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
