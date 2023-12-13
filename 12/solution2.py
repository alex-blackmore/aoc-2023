#!/usr/bin/env python3
import functools as ft

@ft.cache
def solve(start, s, r, springs, records):
    # base cases
    if r >= len(records): 
        return 1 if not any(map(lambda x : x == '#', springs[s:])) else 0

    if s >= len(springs): 
        return 0

    # can't use    
    if s + records[r] > len(springs): 
        return 0

    for i in range(s, s + records[r]):
        if springs[i] == '.':
            for j in range(s, i):
                if springs[j] == '#':
                    return 0
            return solve(True, i + 1, r, springs, records)

    if s + records[r] < len(springs) and springs[s + records[r]] == '#':
        # must place but cannot 
        if springs[s] == '#': return 0
        return solve(True, s + 1, r, springs, records)

    if not start: 
        # must use but can't
        return solve(True, s + 1, r, springs, records)

    # must use
    if springs[s] == '#': 
        return solve(False, s + records[r], r + 1, springs, records)

    # may use
    return solve(False, s + records[r], r + 1, springs, records) + solve(True, s + 1, r, springs, records)

def unfold(problem):
    return (((problem[0] + ("?",)) * 5)[:-1], problem[1] * 5)

with open("input.txt") as file:
    problems = [(tuple(x.split()[0]), tuple(map(int, x.split()[1].split(',')))) for x in file.read().strip().split("\n")]
    problems = list(map(unfold, problems))
    print(sum(map(lambda ps : solve(True, 0, 0, *ps), problems)))
