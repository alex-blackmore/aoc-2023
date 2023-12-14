#!/usr/bin/env python3

def rotate(platform):
    return list(map(lambda i : list(reversed([l[i] for l in platform])), range(len(platform))))

def cycle(platform):
    for i in range(4):
        platform = rotate(platform)
        platform = list(map(roll, platform))
    return platform

def roll(line):
    rcopy = list(reversed(line))
    newline = []
    for i in range(len(rcopy)):
        if rcopy[i] == 'O':
            newline.append('O')
        if rcopy[i] == '#':
            newline.extend(['.'] * (i - len(newline)))
            newline.append('#')
    newline.extend(['.'] * (len(rcopy) - len(newline)))
    return list(reversed(newline))

def solve_col(col):
    return sum([len(col) - i for i in range(len(col)) if col[i] == 'O'])

def hash(platform):
    return "\n".join(map("".join, platform))

with open("input.txt") as file:
    platform = [list(x) for x in file.read().strip().split("\n")]
    # gather data
    history = {}
    history[hash(platform)] = [0]
    for i in range(1000):
        platform = cycle(platform)
        if hash(platform) in history:
            history[hash(platform)].append(i + 1)
        else:
            history[hash(platform)] = [i + 1]

    # extrapolate
    for pattern in history:
        if len(history[pattern]) >= 3:
            if not (1000000000 - history[pattern][0]) % (history[pattern][1] - history[pattern][0]):
                platform = list(map(list, pattern.split("\n")))

    cols = list(map(lambda i : [l[i] for l in platform], range(len(platform))))
    print(sum(map(solve_col, cols)))