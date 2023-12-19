#!/usr/bin/env python3

import sys

TODIR = {
    0: 'R',
    1: 'D',
    2: 'L',
    3: 'U'
}

DIR = {
    'R' : (0, 1),
    'U': (-1, 0),
    'L': (0, -1),
    'D': (1, 0)
}

def dig(direction, distance, corners):
    y, x = corners[-1]
    dy, dx = DIR[direction]
    dy *= distance
    dx *= distance
    corners.append((y + dy, x + dx))

# vertical intervals are between any "corner" (ie the y value of each corner)

# each interval contains a series of rectangles for which we may sum the area
# first we must calculate the "complicated lines", that being the first and last in the interval
# all other lines in the interval are identical and will require only a single calculation

# all vertical and horizontal lines that intersect y level
def is_edge(y, x, lines):
    for (y1, x1), (y2, x2) in lines:
        if y >= min(y1, y2) and y <= max(y1, y2):
            if x >= min(x1, x2) and x <= max(x1, x2):
                return True
    return False

def intersects(y, lines):
    ret = []
    for (y1, x1), (y2, x2) in lines:
        if y >= min(y1, y2) and y <= max(y1, y2):
            ret.append(((y1, x1), (y2, x2)))
    return ret

def leftx(line):
    return min(line[0][1], line[1][1])

def area(interval, lines):
    y = interval[0]
    s = 0
    i_lines = intersects(y, lines)
    
    # bottom line
    toggles = []
    for line in sorted(i_lines, key=leftx):
        y1, x1 = line[0]
        y2, x2 = line[1]
        # normal line
        if y > min(y1, y2) and y < max(y1, y2) :
            toggles.append(x1)
        # horizontal line intersection
        elif y1 == y2:
            if is_edge(y1 + 1, x1, lines) and is_edge(y2 - 1, x2, lines):
                toggles.append(min(x1, x2) if len(toggles) % 2 else max(x1, x2))
            elif is_edge(y1 - 1, x1, lines) and is_edge(y2 + 1, x2, lines):
                toggles.append(min(x1, x2) if len(toggles) % 2 else max(x1, x2))
            elif len(toggles) % 2:
                toggles.append(min(x1, x2))
                toggles.append(max(x1, x2))

    # maths
    if len(toggles) % 2:
        toggles.append(toggles[-1])
    s += sum([toggles[i + 1] - toggles[i] - 1 for i in range(len(toggles))[::2]])

    # middle lines
    y += 1
    if y == interval[1]: return s

    toggles = []
    for line in sorted(i_lines, key=leftx):
        y1, x1 = line[0]
        y2, x2 = line[1]
        if y > min(y1, y2) and y < max(y1, y2):
            toggles.append(x1)

    # maths
    s += sum([toggles[i + 1] - toggles[i] - 1 for i in range(len(toggles))[::2]]) * (interval[1] - interval[0] - 1)

    return s

with open("input.txt") as file:

    instructions = [("".join(l.split("#")[1].split(')')[0][0:5]), l.split("#")[1].split(')')[0][5]) for l in file.read().strip().split("\n")]
    instructions = [(TODIR[int(i[1])], int(i[0], 16)) for i in instructions] 
    corners = [(0, 0)]
    [dig(*x, corners) for x in instructions]
    ymin = min([d[0] for d in corners])
    xmin = min([d[1] for d in corners])
    corners = [(d[0] - ymin, d[1] - xmin) for d in corners]
    ymax = max([d[0] for d in corners])
    xmax = max([d[1] for d in corners])
    intervals = [(t1[0], t2[0]) for t1, t2 in zip(sorted(corners), sorted(corners)[1:]) if t1[0] != t2[0]]
    lines = list(zip(corners, corners[1:]))
    s = 0
    for interval in intervals: 
        s += area(interval, lines)
    for (y1, x1), (y2, x2) in lines:
        s += abs(y1 - y2) + abs(x1 - x2) - 1
    s += len(corners) - 1
    print(s)