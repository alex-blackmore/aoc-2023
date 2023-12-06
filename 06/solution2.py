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
    time = int(ft.reduce(lambda x, y : x + y, filter(str.isdigit, lines[0].split(':')[1].strip())))
    record = int(ft.reduce(lambda x, y : x + y, filter(str.isdigit, lines[1].split(':')[1].strip())))
    print(count_sols(time, record))