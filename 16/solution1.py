#!/usr/bin/env python3

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
    energized = [[[] for _ in x] for x in contraption]
    beams = [(0, 0, 0, 1)]
    while beams: 
        tick(contraption, energized, beams)
        beams = [b for b in beams if not out_of_bounds(b[0], b[1], contraption) and (b[2], b[3]) not in energized[b[0]][b[1]]]

    print(sum([len([x for x in row if x]) for row in energized]))