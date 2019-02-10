import math
import os
import random
import re
import sys
import statistics

# Complete the activityNotifications function below.


def activityNotifications(expenditure, d):
    count = 0
    for i in range(d, len(expenditure)):
        trail = expenditure[i - d: i]
        median = statistics.median(trail)
        if expenditure[i] >= 2 * median:
            count += 1
    return count

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
