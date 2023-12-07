#!/usr/bin/env python3
import itertools as it

sort_val = { '0': 'Y', '1': 'X', '2': 'W', '3': 'V', '4': 'U', '5': 'T', '6': 'S', '7': 'R', '8': 'F', '9': 'E', 'T': 'D', 'J': 'Z', 'Q': 'B', 'K': 'A', 'A': '0'}

def get_class(hand):
    groups = list(map(lambda x : list(x[1]), it.groupby(sorted(hand))))
    match(len(groups)):
        case 1: return 1
        case 2: return 2 if any(map(lambda g : len(g) == 4, groups)) else 3
        case 3: return 4 if any(map(lambda g : len(g) == 3, groups)) else 5
        case 4: return 6
        case _: return 7

def j_class(hand):
    groups = list(map(lambda x : list(x[1]), it.groupby(sorted(hand))))
    normal_class = get_class(hand)
    if 'J' not in hand: 
        return normal_class
    num_j = len(list(filter(lambda g : g[0] == 'J', groups))[0]) 
    match normal_class:
        case 1: return normal_class
        case 2: return 1
        case 3: return 1
        case 4: return 2
        case 5: return 2 if num_j == 2 else 3
        case 6: return 4
        case 7: return 6

def pre_sort(hand):
    return list(map(lambda x : sort_val[x], hand))

with open("input.txt") as file:
    lines = file.read().strip().split("\n")
    plays = list(map(lambda x : (x.split()[0], int(x.split()[1])), lines))
    plays.sort(key=lambda x : pre_sort(x[0]))
    plays.sort(key=lambda p : j_class(p[0]))
    nums = range(len(plays), 0, -1)
    print(sum(map(lambda x : x[0] * x[1][1], zip(nums, plays))))