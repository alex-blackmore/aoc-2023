#!/usr/bin/env python3
import functools as ft
sum = 0
for z in [[list(map(int, h.split()))] for h in open("input.txt").read().strip().split("\n")]: 
    while any(z[-1]): z.append(list(map(lambda i : z[-1][i] - z[-1][i - 1], range(1, len(z[-1])))))
    sum += ft.reduce(lambda x, y : y + [y[-1] + x[-1]], reversed(z[:-1]), z[-1])[-1]
print(sum)