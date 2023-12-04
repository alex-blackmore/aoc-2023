#!/usr/bin/env python3
import functools as ft
import itertools as it

ns = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
check = [-1, 1, 0]

def valid(lines, i, nu):
    bad = ns + ['.']
    for j in nu:
        for c1 in check:
            for c2 in check:
                if lines[i + c1][j + c2] not in bad: return True
    return False

def numbers(lines, i):
    line = lines[i]
    digits = list(filter(lambda x : x[1] in ns, enumerate(line)))
    nums = []
    for di, _ in digits:
        if nums == []: nums = [[di]]
        elif nums[-1][-1] != di - 1: nums.append([di])
        else: nums[-1].append(di)
    nums = filter(ft.partial(valid, lines, i), nums)
    return sum(map(lambda xs : int("".join(map(lambda x : lines[i][x], xs))), nums))

with open("input.txt") as file:
    lines = file.read().strip().split("\n")
    lines = ['.' * len(lines[0])]\
        + list(map(lambda x : '.' + x + '.', lines))\
        + ['.' * len(lines[0])]
    print(sum(map(ft.partial(numbers, lines), range(len(lines)))))