#!/usr/bin/env python3
import functools as ft
def hash(cur, new):
    return ((cur + ord(new)) * 17) % 256

with open("input.txt") as file:
    codes = [list(x) for x in file.read().split(",")]
    print(sum([ft.reduce(hash, code, 0) for code in codes]))