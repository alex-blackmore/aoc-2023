#!/usr/bin/env python3
import re

type_to_index = {'x': 0, 'm': 1, 'a': 2, 's': 3}

def process(part, name, rules):
    for rule in rules[name]:
        if matching(rule, part):
            result = rule.split(':')[1]
            break
    else: 
        result = rule

    if result == 'A': 
        return sum(part)
    if result == 'R': 
        return 0

    return process(part, result, rules)

def matching(rule, part):
    if len(rule) == 1 or rule[1] not in ['<', '>']: 
        return False

    if '>' in rule:
        return part[type_to_index[rule[0]]] > int(rule.split(':')[0].split('>')[1])
    else:
        return part[type_to_index[rule[0]]] < int(rule.split(':')[0].split('<')[1])

with open("input.txt") as file:
    rs, parts = file.read().split("\n\n")
    rs = [("".join(l.split('{')[0]), l.split('{')[1].strip('}').split(",")) for l in rs.strip().split("\n")]
    rules = {}
    parts = [[int(x) for x in re.findall(r'\d+',l)] for l in parts.strip().split("\n")]
    for name, r in rs: 
        rules[name] = r

    print(sum([process(part, "in", rules) for part in parts]))
