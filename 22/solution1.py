#!/usr/bin/env python3
import re
import itertools as it
import functools as ft

def brick_range(brick):
    (x1, y1, z1), (x2, y2, z2) = brick
    r1 = range(min(x1, x2), max(x1, x2) + 1)
    r2 = range(min(y1, y2), max(y1, y2) + 1)
    return it.product(r1, r2)

def brick_height(brick):
    return max(brick[0][2], brick[1][2]) - min(brick[0][2], brick[1][2]) + 1

def brick_initial_height(brick):
    return max(brick[0][2], brick[1][2])

def intersected_bricks(point, bricks):
    return [brick for brick in bricks if point in brick_range(brick)]

def supporting_bricks(brick, beneath):
    return set(ft.reduce(lambda x, y : x + y, beneath[brick].values()))

def remove_conflicts(beneath, brick, conflicts):
    for conflict in conflicts:
        for point in beneath[brick]:
            if conflict in beneath[brick][point]:
                beneath[brick][point].remove(conflict)

with open("input.txt") as file:
    bricks = [(tuple(re.findall(r'\d+', line)[0:3]), tuple(re.findall(r'\d+', line)[3:6])) for line in file.read().split()]
    bricks = [(tuple([int(num) for num in start]), tuple([int(num) for num in end])) for start, end in bricks]
    beneath = {}
    height = {}

    for brick in bricks:
        beneath[brick] = {}
        for point in brick_range(brick):
            beneath[brick][point] = []
            for b in intersected_bricks(point, bricks):
                if brick_initial_height(b) < brick_initial_height(brick):
                    beneath[brick][point].append(b)

    for brick in bricks:
        conflicts = set()

        for supporting_brick in supporting_bricks(brick, beneath):
            conflicts = conflicts.union(supporting_bricks(brick, beneath).intersection(supporting_bricks(supporting_brick, beneath)))

        remove_conflicts(beneath, brick, conflicts)

    for brick in bricks:
        if supporting_bricks(brick, beneath) == set():
            height[brick] = brick_height(brick)

    while len(height) < len(bricks):
        for brick in bricks:
            if brick in height:
                continue
            
            if not all([b in height for b in supporting_bricks(brick, beneath)]):
                continue

            max_height = max([height[b] for b in supporting_bricks(brick, beneath)])

            conflicts = set()

            for b in supporting_bricks(brick, beneath):
                if height[b] != max_height:
                    conflicts.add(b)

            remove_conflicts(beneath, brick, conflicts)

            height[brick] = max_height + brick_height(brick)

    removable = bricks[:]

    for brick in bricks:
        if len(supporting_bricks(brick, beneath)) == 1:
            try: removable.remove(*supporting_bricks(brick, beneath))
            except: pass

    print(len(removable))