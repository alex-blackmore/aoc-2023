#!/usr/bin/env python3
import functools as ft
import itertools as it

ns = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
check = [-1, 1, 0]

def adj(i, j):
    ret = []
    for c1 in check:
        for c2 in check:
            if c1 or c2:
                ret.append((i + c1, j + c2))
    return ret

def rangeof(lines, i, j):
    if lines[i][j] not in ns:
        return None
    l = j
    while lines[i][l] in ns: l -= 1
    l += 1
    u = j
    while lines[i][u] in ns: u += 1
    u -= 1
    return (i, l, u)

def rangetonum(lines, i, l, u):
    s = ""
    for k in range(l, u + 1): s += lines[i][k]
    return int(s)

def total(lines, i):
    ttl = 0
    gears = [x[0] for x in enumerate(lines[i]) if x[1] == "*"]
    for gear in gears:
        ranges = set()
        for cell in adj(i, gear):
            if lines[cell[0]][cell[1]] in ns and rangeof(lines, cell[0], cell[1]):
                ranges.add(rangeof(lines, cell[0], cell[1]))
        if len(ranges) == 2:
            ttl += ft.reduce(lambda x, y : x * y, map(lambda x : rangetonum(lines, *x), ranges))
    return ttl

with open("input.txt") as file:
    lines = file.read().strip().split("\n")
    lines = ['.' * len(lines[0])]\
        + list(map(lambda x : '.' + x + '.', lines))\
        + ['.' * len(lines[0])]
    print(sum(map(ft.partial(total, lines), range(len(lines)))))