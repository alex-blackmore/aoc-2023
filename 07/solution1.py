#!/usr/bin/env python3
import itertools as it

sort_val = { '0': 'Y', '1': 'X', '2': 'W', '3': 'V', '4': 'U', '5': 'T', '6': 'S', '7': 'R', '8': 'F', '9': 'E', 'T': 'D', 'J': 'C', 'Q': 'B', 'K': 'A', 'A': '0'}

def get_class(hand):
    groups = list(map(lambda x : list(x[1]), it.groupby(sorted(hand))))
    match(len(groups)):
        case 1: return 1
        case 2: return 2 if any(map(lambda g : len(g) == 4, groups)) else 3
        case 3: return 4 if any(map(lambda g : len(g) == 3, groups)) else 5
        case 4: return 6
        case _: return 7

def pre_sort(hand):
    return list(map(lambda x : sort_val[x], hand))

with open("input.txt") as file:
    lines = file.read().strip().split("\n")
    plays = list(map(lambda x : (x.split()[0], int(x.split()[1])), lines))
    plays.sort(key=lambda x : pre_sort(x[0]))
    plays.sort(key=lambda p : get_class(p[0]))
    nums = range(len(plays), 0, -1)
    print(sum(map(lambda x : x[0] * x[1][1], zip(nums, plays))))