#!/usr/bin/env python3
import re
import itertools as it

LOWER_BOUND = 200000000000000
UPPER_BOUND = 400000000000000

def intersection(hailstone1, hailstone2):
    x1, y1, _, dx1, dy1, _ = hailstone1
    x2, y2, _, dx2, dy2, _ = hailstone2 
    gradient1 = dy1 / dx1
    gradient2 = dy2 / dx2
    if gradient1 == gradient2: return False
    x = (y2 - y1 + x1 * (gradient1) - x2 * (gradient2)) / (gradient1 - gradient2)
    y = (gradient1) * (x - x1) + y1
    time1 = (x - x1) / dx1
    time2 = (x - x2) / dx2
    if time1 < 0 or time2 < 0: return False
    if y < LOWER_BOUND or y > UPPER_BOUND: return False
    if x < LOWER_BOUND or x > UPPER_BOUND: return False
    return True

with open("input.txt") as file:
    hailstones = [[int(x) for x in re.findall('-?\d+', line)] for line in file.read().strip().split("\n")]
    print(len([pair for pair in it.combinations(hailstones, 2) if intersection(*pair)]))