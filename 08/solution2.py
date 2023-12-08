#!/usr/bin/env python3
import re
import functools as ft
import math as m

cur_nodes = []
node_map = {}
node_tracker = {}
counter = 1

def loop(instructions):
    global cur_nodes, node_map, counter
    for direction in instructions: 
        for i in range(len(cur_nodes)):
            cur_nodes[i] = node_map[cur_nodes[i]][0] if direction == 'L' else node_map[cur_nodes[i]][1]
            if cur_nodes[i][2] == 'Z' and not node_tracker[cur_nodes[i]]: 
                node_tracker[cur_nodes[i]] = counter
        counter += 1

def concat_map(mapping, elem):
    mapping[elem[0]] = [elem[1], elem[2]]
    return mapping

with open("input.txt") as file:
    instructions, _, *nodes = file.read().strip().split("\n")
    nodes = list(map(lambda x : re.sub(r'([A-Z]+) = \(([A-Z]+), ([A-Z]+)\)', r'\1 \2 \3', x).split(), nodes))
    nodes = ft.reduce(lambda x, y : concat_map(x, y), nodes, node_map)
    cur_nodes = [node for node in nodes if node[2] == 'A']
    for node in nodes: 
        if node[2] == 'Z': node_tracker[node] = None
    while any(map(lambda k : node_tracker[k] == None, node_tracker)): loop(instructions)
    print(m.lcm(*node_tracker.values()))
