#!/usr/bin/env python3
import itertools as it
import sys 

sys.setrecursionlimit(10000)

STEPS = 26501365
GARDEN, ROCK, START = '.', '#', 'S'
DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
EVEN, ODD = 0, 1

def opposite(parity):
    if parity == EVEN: return ODD
    return EVEN

def is_corner(size, point_of_entry):
    y, x = point_of_entry
    if y in [0, size - 1] and x in [0, size - 1] : return True
    return False

def count(behaviour, parity=None, steps=None):
    total = 0
    for node in behaviour:
        if parity != None and behaviour[node][0] != parity: continue
        if steps != None and behaviour[node][1] > steps: continue
        total += 1
    return total

def area_by_parity(radius):
    p1, p2 = (radius - 1) // 2, radius // 2
    return (p1 * 2 + 1) ** 2, (p2 * 2) ** 2

def parity(num):
    return num % 2

def step(parity, count):
    return (ODD, count + 1) if parity == EVEN else (EVEN, count + 1)

def adjacent(desert, y, x):
    for dy, dx in DIRECTIONS:
        if y + dy in range(len(desert)) and x + dx in range(len(desert[0])):
            yield (y + dy, x + dx)

def walkable(desert, y, x):
    return desert[y][x] in [GARDEN, START]

def mark_behaviour(behaviour, desert, elf):
    queue = [elf]
    while queue:
        elf, queue = queue[0], queue[1:]
        for adjacent_elf in adjacent(desert, *elf):
            if walkable(desert, *adjacent_elf) and adjacent_elf not in behaviour:
                behaviour[adjacent_elf] = step(*behaviour[elf])
                queue.append(adjacent_elf)

with open("input.txt") as file:
    desert = [list(line) for line in file.read().strip().split("\n")]
    width = len(desert[0])
    height = len(desert)
    size = width
    start = [(y, x) for y, x in it.product(range(width), range(height)) if desert[y][x] == 'S'][0]

    base_behaviour = {}
    base_behaviour[start] = (EVEN, 0)
    mark_behaviour(base_behaviour, desert, start)

    points_of_entry = list(it.product([0, height // 2, height - 1], [0, width // 2, width - 1]))
    points_of_entry.remove((height // 2, width // 2))

    entry_behaviours = {}
    for point_of_entry in points_of_entry:
        entry_behaviours[point_of_entry] = {}
        entry_behaviours[point_of_entry][point_of_entry] = (EVEN, 0)
        mark_behaviour(entry_behaviours[point_of_entry], desert, point_of_entry)

    radius = STEPS // size
    remainder = STEPS % size

    base_parity = parity(STEPS)
    alternate_parity = opposite(base_parity)

    base_parity_maps, alternate_parity_maps = area_by_parity(radius)
    base_parity_total = count(base_behaviour, parity=base_parity)
    alternate_parity_total = count(base_behaviour, parity=alternate_parity)

    print(base_parity_maps, base_parity_total)
    print(alternate_parity_maps, alternate_parity_total)

    corner_entry_maps_big = (radius - 1)
    corner_entry_maps_small = radius

    point_of_entry_totals_big = {}
    point_of_entry_totals_small = {}

    for point_of_entry in points_of_entry:
        steps = remainder + size - 1 if is_corner(size, point_of_entry) else remainder + size // 2 - 1
        point_of_entry_totals_big[point_of_entry] = count(entry_behaviours[point_of_entry], parity=opposite(parity(radius)), steps=steps)
        if is_corner(size, point_of_entry):
            point_of_entry_totals_small[point_of_entry] = count(entry_behaviours[point_of_entry], parity=parity(radius), steps=remainder - 1)

    total = 0
    total += base_parity_maps * base_parity_total
    total += alternate_parity_maps * alternate_parity_total
    for point_of_entry in points_of_entry:
        if is_corner(size, point_of_entry):
            total += corner_entry_maps_big * point_of_entry_totals_big[point_of_entry]
            total += corner_entry_maps_small * point_of_entry_totals_small[point_of_entry]
        else:
            total += point_of_entry_totals_big[point_of_entry]
    
    print(total)
    print(628206330073385)