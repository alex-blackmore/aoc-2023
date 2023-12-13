#!/usr/bin/env python3
import functools as ft


def countvm(i, pattern):
    smudges = 0
    for line in pattern:
        for j, k in zip(range(i - 1, -1, -1), range(i, len(line))):
            if line[j] != line[k]: smudges += 1
    return smudges

def counthm(i, pattern):
    smudges = 0
    for j, k in zip(range(i - 1, -1, -1), range(i, len(pattern))):
        for x, y in zip(pattern[j], pattern[k]):
            if x != y: smudges += 1
    return smudges

def solve(pattern):
    for i in range(1, len(pattern[0])):
        if countvm(i, pattern) == 1: return i
    for i in range(1, len(pattern)):
        if counthm(i, pattern) == 1: return i * 100

with open("input.txt") as file:
    patterns = [list(map(list, p.split("\n"))) for p in file.read().strip().split("\n\n")]
    print(sum(map(solve, patterns)))
