#!/usr/bin/env python3
import re
import functools as ft

cur_node = 'AAA'
node_map = {}
counter = 0

def loop(instructions):
    global cur_node, node_map, counter
    for direction in instructions: 
        cur_node = node_map[cur_node][0] if direction == 'L' else node_map[cur_node][1]
        counter += 1

def concat_map(mapping, elem):
    mapping[elem[0]] = [elem[1], elem[2]]
    return mapping

with open("input.txt") as file:
    instructions, _, *nodes = file.read().strip().split("\n")
    nodes = list(map(lambda x : re.sub(r'([A-Z]+) = \(([A-Z]+), ([A-Z]+)\)', r'\1 \2 \3', x).split(), nodes))
    nodes = ft.reduce(lambda x, y : concat_map(x, y), nodes, node_map)
    while cur_node != 'ZZZ': loop(instructions)
    print(counter)
