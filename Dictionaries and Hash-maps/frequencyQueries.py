import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the freqQuery function below.


def freqQuery(queries):
    count = defaultdict(int)
    data = defaultdict(int)
    output = []
    for idx, item in enumerate(queries):
        if item[0] == 1:
            count[data[item[1]]] -= 1
            data[item[1]] += 1
            count[data[item[1]]] += 1

        elif item[0] == 2:
            if data[item[1]] > 0:
                count[data[item[1]]] -= 1
                data[item[1]] -= 1
                count[data[item[1]]] += 1

        elif item[0] == 3:
            if count[item[1]] > 0:
                output.append(1)
            else:
                output.append(0)
    return output

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    print(ans)

    # fptr.write('\n'.join(map(str, ans)))
    # fptr.write('\n')

    # fptr.close()
