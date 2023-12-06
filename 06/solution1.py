#!/usr/bin/env python3
import math as m
import functools as ft
def count_sols(duration, record):
    minhold = (duration - m.sqrt((duration ** 2) - (4 * record))) / 2
    maxhold = (duration + m.sqrt((duration ** 2) - (4 * record))) / 2
    adjust = 0
    if minhold == m.floor(minhold): adjust -= 1
    if maxhold == m.floor(maxhold): adjust -= 1
    return (m.floor(maxhold) - m.ceil(minhold) + 1 + adjust)

with open("input.txt") as file:
    lines = file.read().strip().split("\n")
    times = list(map(int, lines[0].split(':')[1].strip().split()))
    records = list(map(int, lines[1].split(':')[1].strip().split()))
    races = list(zip(times, records))
    print(ft.reduce(lambda x, y : x * y, map(lambda x : count_sols(*x), races), 1))