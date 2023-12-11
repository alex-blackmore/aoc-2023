#!/usr/bin/env python3
import itertools as it

with open("input.txt") as file:
    universe = [list(x) for x in file.read().strip().split()]
    horiz = [i for i in range(len(universe)) if not any(map(lambda x : x != '.', universe[i]))]
    vert = [i for i in range(len(universe[0])) if not any(map(lambda x : x[i] != '.', universe))]
    galaxies = [(y, x) for y, x in it.product(range(len(universe)), range(len(universe[0]))) if universe[y][x] == '#']
    sum = 0
    for g1, g2 in it.combinations(galaxies, 2):
        sum += abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])
        sum += 999999 * len(list(filter(horiz.__contains__, range(min(g1[0], g2[0]), max(g1[0], g2[0]))))) 
        sum += 999999 * len(list(filter(vert.__contains__, range(min(g1[1], g2[1]), max(g1[1], g2[1])))))
    print(sum)