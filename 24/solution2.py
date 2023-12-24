#!/usr/bin/env python3
import re
import itertools as it

# given an intital position, is it possible to test whether some velocity exists so that all hailstones can be striked?
# yes. given the closest and second closest hailstone's velocity, there is only one potential velocity

# probably not possible to brute force

# if any two lines from the input intersect, then they define a plane on which my throw my lie
# if any other two lines intersect on a different plane then they fully define the throw as the intersection of two planes

def cross(a, b):
    c = [a[1]*b[2] - a[2]*b[1],
         a[2]*b[0] - a[0]*b[2],
         a[0]*b[1] - a[1]*b[0]]

    return c

def intersection(hailstone1, hailstone2):
    normal = cross(hailstone1[3:], hailstone2[3:])
    point = hailstone1[:3]
    x, y, z = hailstone2[:3]
    result = normal[0] * (point[0] - x) + normal[1] * (point[1] - y) + normal[2] * (normal[2] - z)
    if result != 0:
        return False
    return True

def parallel(hailstone1, hailstone2):
    dx1, dy1, dz1 = hailstone1[3:]
    dx2, dy2, dz2 = hailstone2[3:]
    return dx1 / dx2 == dy1 / dy2 and  dy1 / dy2 == dz1 / dz2

with open("input.txt") as file:
    hailstones = [[int(x) for x in re.findall('-?\d+', line)] for line in file.read().strip().split("\n")]
    for pair in it.combinations(hailstones, 2):
        if intersection(*pair):
            print(pair)
        if parallel(*pair):
            print(pair)