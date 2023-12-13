#!/usr/bin/env python3
import functools as ft


def testvm(i, pattern):
    for line in pattern:
        for j, k in zip(range(i - 1, -1, -1), range(i, len(line))):
            if line[j] != line[k]: return False
    return True

def testhm(i, pattern):
    for j, k in zip(range(i - 1, -1, -1), range(i, len(pattern))):
        if pattern[j] != pattern[k]: return False
    return True

def solve(pattern):
    for i in range(1, len(pattern[0])): 
        if testvm(i, pattern): return i
    for i in range(1, len(pattern)): 
        if testhm(i, pattern): return i * 100

with open("input.txt") as file:
    patterns = [list(map(list, p.split("\n"))) for p in file.read().strip().split("\n\n")]
    print(sum(map(solve, patterns)))
