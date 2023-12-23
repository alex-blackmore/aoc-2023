#!/usr/bin/env python3

import itertools as it
import sys

sys.setrecursionlimit(10000)

PATH, FOREST, SLOPE_N, SLOPE_E, SLOPE_S, SLOPE_W = '.', '#', '^', '>', 'v', '<'
SLOPES = [SLOPE_N, SLOPE_E, SLOPE_S, SLOPE_W]
DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
NO_PATH = -1

def closest_junctions(junctions, node, adjacencies, visited, distance, results):
    visited[node] = True
    for adjacent_node in adjacencies[node]:
        if visited[adjacent_node]: continue
        if adjacent_node in junctions:
            results.append((adjacent_node, distance + 1))
        else:
            closest_junctions(junctions, adjacent_node, adjacencies, visited, distance + 1, results)
    return

def is_junction(node, adjacencies):
    return len(adjacencies[node]) > 2

def longest_path(adjacencies, start, end, visited):
    if start == end: return 0
    paths = []
    for node, distance in adjacencies[start]:
        if not visited[node]:
            visited[node] = True
            path = longest_path(adjacencies, node, end, visited)
            visited[node] = False
            if path != NO_PATH:
                paths.append(path + distance)
    if paths: return max(paths)
    else: return NO_PATH

def is_walkable(forest, y, x):
    return forest[y][x] in [PATH] + SLOPES

def adjacent(forest, y, x):
    result = []
    searchable = DIRECTIONS
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
    
    junctions = [(y, x) for y, x in walkable if is_junction((y, x), adjacencies)] + [start, end]

    for y, x in walkable:
        visited[(y, x)] = False

    junction_adjacencies = {}
    for junction in junctions:
        for y, x in walkable:
            visited[(y, x)] = False
        result = []
        closest_junctions(junctions, junction, adjacencies, visited, 0, result)
        junction_adjacencies[junction] = result

    for y, x in walkable:
        visited[(y, x)] = False

    print(longest_path(junction_adjacencies, start, end, visited))