#!/usr/bin/env python3

def solve_col(col):
    total = 0
    dist = 0
    for i in range(len(col)):
        if col[i] == 'O':
            total += (len(col) - dist)
            dist += 1
        elif col[i] == '#':
            dist = i + 1
    return total

with open("input.txt") as file:
    platform = [list(x) for x in file.read().strip().split("\n")]
    cols = list(map(lambda i : [l[i] for l in platform], range(len(platform))))
    print(sum(map(solve_col, cols)))