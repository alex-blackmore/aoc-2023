#!/usr/bin/env python3
import functools as ft
scratchie = []

def calculate(xs, x=0):
    if xs == []: return x
    for i in range(xs[0][0]):
        xs[i + 1][1] += xs[0][1]
    return calculate(xs[1:], x + xs[0][1])

def score(line):
    [c1, c2] = line.split('|')
    c1 = c1.split(':')[1].strip().split()
    c2 = c2.strip().split()
    matches = len(list(filter(lambda x : x in c1, c2)))
    scratchie.append([matches, 1])

with open("input.txt") as file:
    lines = file.read().strip().split("\n")
    for line in lines: score(line)
    print(calculate(scratchie))