#!/usr/bin/env python3

DIR = {
    'R' : (0, 1),
    'U': (-1, 0),
    'L': (0, -1),
    'D': (1, 0)
}

def dig(direction, distance, dug):
    for _ in range(distance):
        y, x = dug[-1]
        dy, dx = DIR[direction]
        dug.append((y + dy, x + dx))

with open("input.txt") as file:
    instructions = [(line.split()[0], int(line.split()[1])) for line in file.read().strip().split("\n")]
    dug = [(0, 0)]
    [dig(*x, dug) for x in instructions]
    ymin = min([d[0] for d in dug])
    xmin = min([d[1] for d in dug])
    dug = [(d[0] - ymin, d[1] - xmin) for d in dug]
    ymax = max([d[0] for d in dug])
    xmax = max([d[1] for d in dug])
    field = [['.' for _ in range(xmax + 1)] for _ in range(ymax + 1)]
    for (y, x) in dug: field[y][x] = '#'
    s = 0
    for y in range(len(field)):
        inside = False
        for x in range(len(field[0])):
            cell = field[y][x] == '#'
            right = x + 1 in range(len(field[0])) and field[y][x + 1] == '#'
            left = x - 1 in range(len(field[0])) and field[y][x - 1] == '#'
            up = y + 1 in range(len(field)) and field[y + 1][x] == '#'
            down = y - 1 in range(len(field)) and field[y - 1][x] == '#'
            if not cell and inside:
                s += 1
            elif cell:
                s += 1
                if left and up: inside = not inside
                if right and up: inside = not inside
                if up and down: inside = not inside 
    print(s)