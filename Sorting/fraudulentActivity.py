import math
import os
import random
import re
import sys
from collections import deque
# Complete the activityNotifications function below.


class CustomQueue:

    def __init__(self, length):
        self.freq = [0] * 201
        self.queue = deque()
        self.length = length

    def add(self, item: int):
        self.queue.append(item)
        self.freq[item] += 1
        if len(self.queue) > self.length:
            val = self.queue.popleft()
            self.freq[val] -= 1

    def median(self) -> int:
        a1 = int(self.length / 2)
        a2 = a1 + 1
        mid1 = None
        mid2 = None
        res = 0

        for idx, item in enumerate(self.freq):
            res += item
            if res >= a1 and mid1 is None:
                mid1 = idx
            if res >= a2:
                mid2 = idx
                break

        if self.length % 2 == 0:
            return (mid1 + mid2) / 2.0
        return mid2

    def __repr__(self):
        return str(self.freq)


def activityNotifications(expenditure, d):
    count = 0
    q = CustomQueue(d)
    for i in expenditure[:d]:
        q.add(i)

    for idx, item in enumerate(expenditure[d:]):
        median = q.median()
        # print(q)
        # print(median, expenditure[idx: idx + 1])
        if item >= (2 * median):
            count += 1
        q.add(item)
    return count

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    f = open('testcase.txt', 'r')

    # expenditure = list(map(int, input().rstrip().split()))

    expenditure = list(map(int, f.read().rstrip().split()))

    result = activityNotifications(expenditure, d)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
