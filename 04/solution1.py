#!/usr/bin/env python3

def score(line):
    [c1, c2] = line.split('|')
    c1 = c1.split(':')[1].strip().split()
    c2 = c2.strip().split()
    return round(2 ** (len(list(filter(lambda x : x in c1, c2))) - 1))

with open("input.txt") as file:
    lines = file.read().strip().split("\n")
    print(sum(map(score, lines)))