import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.


# def minimumBribes(q):
#     minBribes = 0
#     diff = [0] * len(q)

#     for idx, item in enumerate(q):
#         # print("q[%d] : %d" % (idx, item))
#         diff[idx] = item - (idx + 1)
#     print(diff)

#     for idx, item in enumerate(diff):
#         minBribes += math.ceil(item / 2)

#     if minBribes > len(q):
#         print("too chaotic")
#         return

#     print(minBribes)

def minimumBribes(q):
    minBribes = 0
    # ensuring the values match 0 indexing(not required
    # but makes comparision easy)
    q = [i - 1 for i in q]

    for idx, item in enumerate(q):
        # if the difference is greater than 2;
        # it means the value has been swapped
        # more than twice which is not allowed
        if (item - idx) > 2:
            print("Too chaotic")
            return

        # now we look at how many times an item has been bribed;
        # we must remember that anyone who has bribed an item can't be any further than
        # 1 position than the value's original position. So we can how many of those
        # positions in queue contain a number larger than item.
        # Hence we will look look from (item-1) to (idx-1).
        for j in range(max(item - 1, 0), idx):
            if q[j] > item:
                minBribes += 1
    print(minBribes)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))
        minimumBribes(q)
