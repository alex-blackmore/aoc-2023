#!/usr/bin/env python3
import itertools as it

STEPS = 130
GARDEN, ROCK, START = '.', '#', 'S'
DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def adjacent(garden, y, x):
    result = []
    for dy, dx in DIRECTIONS:
        if y + dy in range(len(garden)) and x + dx in range(len(garden[0])):
            result.append((y + dy, x + dx))
    return result

def explore(desert, elves):
    new_elves = set()
    for elf in elves:
        for y, x in adjacent(desert, *elf):
            if desert[y][x] in [GARDEN, START]:
                new_elves.add((y, x)) 
    return new_elves

with open("input.txt") as file:
    desert = [list(line) for line in file.read().strip().split("\n")]
    elves = set([(y, x) for y, x in it.product(range(len(desert)), range(len(desert[0]))) if desert[y][x] == 'S'])
    for _ in range(STEPS):
        elves = explore(desert, elves)
    print(len(elves))