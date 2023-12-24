#!/usr/bin/env python3
import itertools as it
import sys 

sys.setrecursionlimit(10000)

STEPS = 64
GARDEN, ROCK, START = '.', '#', 'S'
DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
EVEN, ODD = 0, 1

def count(behaviour, parity=None, steps=None):
    total = 0
    for node in behaviour:
        if parity != None and behaviour[node][0] != parity: continue
        if steps != None and behaviour[node][1] > steps: continue
        total += 1
    return total

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
    width = range(len(desert[0]))
    height = range(len(desert))
    start = [(y, x) for y, x in it.product(width, height) if desert[y][x] == 'S'][0]
    behaviour = {}
    behaviour[start] = (EVEN, 0)
    mark_behaviour(behaviour, desert, start)
    print(count(behaviour, parity=parity(STEPS), steps=STEPS))