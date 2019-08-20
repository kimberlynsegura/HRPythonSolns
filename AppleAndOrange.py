import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    a_house = 0
    b_house = 0

    for i in range(len(apples)):
        apples[i] = apples[i] + a
        if apples[i] >= s and apples[i] <= t:
            a_house += 1

    for j in range(len(oranges)):
        oranges[j] = oranges[j] + b
        if oranges[j] >= s and oranges[j] <= t:
            b_house += 1

    return a_house, b_house



if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
