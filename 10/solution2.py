#!/usr/bin/env python3

gridmap = {}

def connections(gridmap, location):
    y, x = location
    next = []
    match(gridmap[location][0]):
        case '|': next.extend([(1, 0), (-1, 0)])
        case '-': next.extend([(0, 1), (0, -1)])
        case 'L': next.extend([(-1, 0), (0, 1)])
        case 'J': next.extend([(-1, 0), (0, -1)])
        case '7': next.extend([(0, -1), (1, 0)])
        case 'F': next.extend([(0, 1), (1, 0)])
        case 'S': next.extend([(0, 1), (1, 0), (-1, 0), (0, -1)])
    return [(y + new[0], x + new[1]) for new in next if (y + new[0], x + new[1]) in gridmap]

with open("input.txt") as file:
    grid = [list(x) for x in file.read().strip().split()]

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            gridmap[(y, x)] = [grid[y][x], -1]
    start = list(filter(lambda x : gridmap[x][0] == 'S', gridmap))[0]
    queue = [(gridmap, start, -1)]

    while queue:
        gridmap, location, dist = queue.pop()
        if gridmap[location][1] != -1: continue
        gridmap[location][1] = 1
        for next in connections(gridmap, location):
            if not (gridmap[location][0] == 'S' and location not in connections(gridmap, next)):
                queue.append((gridmap, next, 1))

    # one liner
    print(sum(map(lambda y : len(list(filter(lambda x : len(list(filter(lambda z : gridmap[(y, z)][1] == 1 and gridmap[(y, z)][0] in ['|', 'S', '7', 'F'], range(x)))) % 2 and gridmap[(y, x)][1] != 1, range(len(grid[0]))))), range(len(grid)))))

    # readable code
    sum = 0
    for y in range(len(grid)):
        inside = False
        for x in range(len(grid[0])):
            if gridmap[(y, x)][1] == 1:
                if gridmap[(y, x)][0] in ['F', '7', '|', 'S']:
                    inside = not inside
            elif inside:
                sum += 1

    print(sum)
