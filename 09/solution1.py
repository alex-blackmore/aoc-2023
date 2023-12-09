#!/usr/bin/env python3
import functools as ft

def extrapolate(sequence):
    return list(map(lambda i : sequence[i] - sequence[i - 1], range(1, len(sequence))))

def unextrapolate(known, unknown):
    return unknown + [unknown[-1] + known[-1]]

with open("input.txt") as file:
    histories = [[list(map(int, h.split()))] for h in file.read().strip().split("\n")]
    sum = 0
    for history in histories: 
        while any(history[-1]): 
            history.append(extrapolate(history[-1]))
        lr = history.pop() + [0]
        history.reverse()
        sum += ft.reduce(unextrapolate, history, lr)[-1]
    print(sum)