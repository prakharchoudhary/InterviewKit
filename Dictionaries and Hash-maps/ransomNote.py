import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.


def checkMagazine(magazine, note):
    vocab = {}

    for i in magazine:
        if i not in vocab.keys():
            vocab[i] = 1
        else:
            vocab[i] += 1
    # print(vocab)

    for i in note:
        if i not in vocab or vocab[i] == 0:
            print("No")
            return
        else:
            vocab[i] -= 1
    print("Yes")

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
