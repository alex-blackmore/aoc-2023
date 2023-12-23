#!/usr/bin/env python3

import itertools as it
import sys

sys.setrecursionlimit(10000)

PATH, FOREST, SLOPE_N, SLOPE_E, SLOPE_S, SLOPE_W = '.', '#', '^', '>', 'v', '<'
SLOPES = [SLOPE_N, SLOPE_E, SLOPE_S, SLOPE_W]
DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
SLOPE_DIRECTION = {SLOPE_N: (-1, 0), SLOPE_E: (0, 1), SLOPE_S: (1, 0), SLOPE_W: (0, -1)}
NO_PATH = -1

def longest_path(adjacencies, start, end, visited):
    if start == end: return 0
    paths = []
    for node in adjacencies[start]:
        if not visited[node]:
            visited[node] = True
            path = longest_path(adjacencies, node, end, visited)
            visited[node] = False
            if path != NO_PATH:
                paths.append(path + 1)
    if paths: return max(paths)
    else: return NO_PATH

def is_walkable(forest, y, x):
    return forest[y][x] in [PATH] + SLOPES

def adjacent(forest, y, x):
    result = []
    searchable = DIRECTIONS if forest[y][x] not in SLOPES else [SLOPE_DIRECTION[forest[y][x]]]
    for dy, dx in searchable:
        if (dy + y) in range(len(forest)) and (dx + x) in range(len(forest[0])) \
                and is_walkable(forest, y + dy, x + dx):
            result.append((y + dy, x + dx))
    return result

with open("input.txt") as file:
    forest = [list(x) for x in file.read().split()]
    height = len(forest)
    width = len(forest[0])
    walkable = [(y, x) for y, x in it.product(range(height), range(width)) if is_walkable(forest, y, x)]
    adjacencies = {}
    start = (0, [x for x in range(width) if is_walkable(forest, 0, x)][0])
    end = (height - 1, [x for x in range(width) if is_walkable(forest, height - 1, x)][0])
    
    for y, x in walkable:
        adjacencies[(y, x)] = adjacent(forest, y, x)

    visited = {}
    for y, x in walkable:
        visited[(y, x)] = False
    visited[start] = True
    
    print(longest_path(adjacencies, start, end, visited))