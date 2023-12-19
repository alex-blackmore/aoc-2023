#!/usr/bin/env python3

import re
import functools as ft

type_to_index = {'x': 0, 'm': 1, 'a': 2, 's': 3}

def map_ratings(rating, rules, name, rejected, accepted):
    remaining = rating[:]
    for rule in rules[name]:
        if is_final(rule):
            if rule == 'A':
                accepted.append(remaining)
            elif rule == 'R':
                rejected.append(remaining)
            else:
                map_ratings(remaining, rules, rule, rejected, accepted)
        else:
            result, matching, remaining = split_ratings(rule, remaining)
            if result == 'A':
                accepted.append(matching)
            elif result == 'R':
                rejected.append(matching)
            else:
                map_ratings(matching, rules, result, rejected, accepted)
        
def split_ratings(rule, rating):
    splitpoint = int(re.match(r'[xmas][<>](\d+)', rule).groups()[0])
    rtype = rule[0]
    result = rule.split(':')[1]
    matching = rating[:]
    remaining = rating[:]

    if '>' in rule:
        lower, upper = rating[type_to_index[rtype]]
        if splitpoint < lower:
            remaining[type_to_index[rtype]] = []
        elif splitpoint >= upper:
            matching[type_to_index[rtype]] = []
        else:
            remaining[type_to_index[rtype]] = [lower, splitpoint]
            matching[type_to_index[rtype]] = [splitpoint + 1, upper]
    else:
        (lower, upper) = rating[type_to_index[rtype]]
        if splitpoint > upper:
            remaining[type_to_index[rtype]] = []
        elif splitpoint <= lower:
            matching[type_to_index[rtype]] = []
        else:
            remaining[type_to_index[rtype]] = [splitpoint, upper]
            matching[type_to_index[rtype]] = [lower, splitpoint - 1]
    return result, matching, remaining

def is_final(rule):
    return '>' not in rule and '<' not in rule

with open("input.txt") as file:
    rs, _ = file.read().split("\n\n")
    rs = [("".join(l.split('{')[0]), l.split('{')[1].strip('}').split(",")) for l in rs.strip().split("\n")]
    rules = {}
    rating = [[1, 4000], [1, 4000], [1, 4000], [1, 4000]]
    rejected = []
    accepted = []
    for name, r in rs: 
        rules[name] = r

    map_ratings(rating, rules, "in", rejected, accepted)

    print(sum([ft.reduce(lambda x, y : x * y, [rng[1] - rng[0] + 1 for rng in rating]) for rating in accepted]))