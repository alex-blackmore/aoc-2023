#!/usr/bin/env python3

import itertools as it

def out_of_bounds(y, x, contraption):
    return y not in range(len(contraption)) or x not in range(len(contraption[0]))

def tick(contraption, energized, beams):
    for y, x, dy, dx in beams[:]:
        energized[y][x].append((dy, dx))
        match contraption[y][x]:
            case '.':
                beams.append((y + dy, x + dx, dy, dx))
            case '/':
                beams.append((y - dx, x - dy, -dx, -dy))
            case '\\':
                beams.append((y + dx, x + dy, dx, dy))
            case '-':
                if dy:
                    beams.append((y, x + 1, 0, 1))
                    beams.append((y, x - 1, 0 ,-1))
                else:
                    beams.append((y + dy, x + dx, dy, dx))
            case '|':
                if dx:
                    beams.append((y + 1, x, 1, 0))
                    beams.append((y - 1, x, -1, 0))
                else:
                    beams.append((y + dy, x + dx, dy, dx))

with open("input.txt") as file:
    contraption = [list(x) for x in file.read().strip().split("\n")]
    lcol = [(*x, 1, 0) for x in it.product([0], range(len(contraption)))]
    rcol = [(*x, -1, 0) for x in it.product([len(contraption[0]) - 1], range(len(contraption)))]
    urow = [(*x, 0, 1) for x in it.product(range(len(contraption[0])), [0])]
    brow = [(*x, 0, -1) for x in it.product(range(len(contraption[0])), [len(contraption) - 1])]
    s = 0
    for initbeams in lcol + rcol + urow + brow:
        energized = [[[] for _ in x] for x in contraption]
        beams = [initbeams]
        while beams: 
            tick(contraption, energized, beams)
            beams = [b for b in beams if not out_of_bounds(b[0], b[1], contraption) and (b[2], b[3]) not in energized[b[0]][b[1]]]
        if sum([len([x for x in row if x]) for row in energized]) > s:
            s = sum([len([x for x in row if x]) for row in energized]) 
    print(s)