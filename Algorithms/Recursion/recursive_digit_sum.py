#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the superDigit function below.
def superDigit(n, k):
    digit_sum = 0
    for i in n:
        digit_sum += int(i) * k
    return get_super_digit(str(digit_sum))


def get_super_digit(n):
    if int(n) <= 9:
        return n
    digit_sum = 0
    for i in n:
        digit_sum += int(i)
    return get_super_digit(str(digit_sum))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
