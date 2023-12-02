#!/usr/bin/env python3

allowed = {"red": 12, "green": 13, "blue": 14}

def valid(s):
    nopunc = "".join([c for c in s if c not in [':', ',', ';']])
    pairs = list(zip(*[iter(nopunc.split())] * 2))[1:]
    return not any(map(lambda x : int(x[0]) > allowed[x[1]], pairs))

with open("input.txt") as file:
    lines = file.read().strip().split("\n")
    print(sum([int(l.split()[1][:-1]) for l in lines if valid(l)]))