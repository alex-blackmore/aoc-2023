#!/usr/bin/env python3
from functools import reduce, cache
from itertools import groupby

def calibration(s):
    n = list(filter(lambda x : x in ["0","1","2","3","4","5","6","7","8","9"], s))
    return int(n[0] + n[-1])

with open("input.txt") as file:
    lines = file.read().split("\n")[:-1]
    print(sum(list(map(calibration, lines))))