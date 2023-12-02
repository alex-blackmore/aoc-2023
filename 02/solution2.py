#!/usr/bin/env python3
import functools as f
def power(s):
    min = {"red": 0, "green": 0, "blue": 0}
    nopunc = "".join([c for c in s if c not in [':', ',', ';']])
    pairs = list(zip(*[iter(nopunc.split())] * 2))[1:]
    for x in pairs: 
        if int(x[0]) > min[x[1]]: 
            min[x[1]] = int(x[0])
    return f.reduce(lambda x, y : x * int(min[y]), min, 1)

with open("input.txt") as file:
    lines = file.read().strip().split("\n")
    print(sum(map(power, lines)))