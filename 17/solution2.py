#!/usr/bin/env python3
import itertools as it
import sys

DIRECTIONS = [(0, 1), (1, 0), (-1, 0), (0, -1)]

def init(adjacencies, node):
    y, x, (dy, dx), consec = node
    options = []
    if consec < 4: options = [(dy, dx)]
    elif consec < 10: options = [(dx, dy), (-dx, -dy), (dy, dx)]
    else: options = [(dx, dy), (-dx, -dy)]

    for (ny, nx) in options:
        if (y + ny in range(len(basegrid)) and x + nx in range(len(basegrid[0]))):
            if (ny, nx) == (dy, dx):
                adjacencies[node].append((y + ny, x + nx, (ny, nx), consec + 1))
            else:
                adjacencies[node].append((y + ny, x + nx, (ny, nx), 1))

def dijkstra(grid, adjacencies, visited, shortest, src):
    # initialise src node
    shortest[src] = 0
    # initialise nextv
    nextv = set([src])
    # first visit
    visit(grid, adjacencies, visited, shortest, src, nextv)
    # perform exploration
    while not all(visited.values()) and nextv:
        n = sorted(nextv, key=lambda potential : shortest[potential])[0]
        visit(grid, adjacencies, visited, shortest, n, nextv)

def visit(grid, adjacencies, visited, shortest, node, nextv):
    visited[node] = True
    nextv.remove(node)
    [nextv.add(x) for x in adjacencies[node] if not visited[x]]
    for adjnode in adjacencies[node]:
        if shortest[node] + grid[adjnode[0]][adjnode[1]] < shortest[adjnode]:
            shortest[adjnode] = shortest[node] + grid[adjnode[0]][adjnode[1]]

with open("input.txt") as file:
    basegrid = [[int(x) for x in row] for row in file.read().strip().split("\n")]
    adjacencies = {(0, 0, None, 0): [(0, 1, (0, 1), 1), (1, 0, (1, 0), 1)]}
    visited = {}
    shortest = {}
    for node in it.product(range(len(basegrid)), range(len(basegrid[0])), DIRECTIONS, range(1, 11)):
        adjacencies[node] = []
        init(adjacencies, node)
        visited[node] = False
        shortest[node] = sys.maxsize
    dijkstra(basegrid, adjacencies, visited, shortest, (0, 0, None, 0))
    print(min([shortest[node] for node in it.product([len(basegrid) - 1], [len(basegrid[0]) - 1], DIRECTIONS, range(1, 11)) if node[3] > 3]))
