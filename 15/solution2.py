#!/usr/bin/env python3
import functools as ft
import re

def hash(cur, new):
    return ((cur + ord(new)) * 17) % 256

boxes = [[] for _ in range(256)]

with open("input.txt") as file:
    for instruction in file.read().strip().split(","):
        label, protocol = re.match(r'([a-z]+)([=-][1-9]?)', instruction).groups()
        box = ft.reduce(hash, label, 0)
        match protocol[0]:
            case '-':
                boxes[box] = [x for x in boxes[box] if x[0] != label]
            case '=':
                try:
                    i = [x[0] for x in boxes[box]].index(label)
                    boxes[box][i] = (boxes[box][i][0], int(protocol[1]))
                except:
                    boxes[box].append((label, int(protocol[1])))

    print(sum([sum([bnum * lnum * lens[1] for lnum, lens in enumerate(box, 1)]) for bnum, box in enumerate(boxes, 1)]))