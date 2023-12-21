#!/usr/bin/env python3
import itertools as it

STEPS = 26501365
# 65 + 130 + 65 + 130 = 13 TOTAL AREAS
# 65 + 130 + 65 + 130 - 1 = 5 TOTAL AREAS
# STEPS = 65 + 131 + 65 + 131
GARDEN, ROCK, START = '.', '#', 'S'
DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
UNKNOWN = -1
EVEN, ODD = 0, 1
# the number of steps taken to reach a given tile is just the manhattan distance of the 
# closest edge piece (that being corner or centre middle)
# this is true for the puzzle input due to the "window" shape of garden tiles, but is not true for the example input

# there will be a large number of tiles which can be reached with a number of remaining steps greater
# than or equal to the required steps for all tiles to be reach from the entry piece

# for these the number of plots in each parity can be trivially calculated

# there will be a small number of tiles which will be reached with a number of remaining steps less
# than the required steps for all tiles to be reached from the entry piece

# for those we need to know:

# from each of the 8 relevant edge pieces (centre side and corner),
# the number of steps taken for each garden tile to be reached

# assuming they have been reached,
# tiles with odd-odd or even-even coordinates are active on EVEN step counts
# tiles with odd-even or even-odd coordinates are active on ODD step counts

# {start_tile: {tile: steps_needed}}
# behaviour = {(5, 5): {(0, 0): -1}}

def area_by_parity(radius):
    p1, p2 = (radius - 1) // 2, radius // 2
    return (p1 * 2 + 1) ** 2, (p2 * 2) ** 2

def area(radius):
    return 4 * ((radius * (radius - 1)) // 2) + 1

def parity(y, x):
    return EVEN if y % 2 == x % 2 else ODD

def adjacent(garden, y, x):
    result = []
    for dy, dx in DIRECTIONS:
        if y + dy in range(len(garden)) and x + dx in range(len(garden[0])):
            result.append((y + dy, x + dx))
    return result

def explore(desert, elves):
    new_elves = set()
    for elf in elves:
        for y, x in adjacent(desert, *elf):
            if desert[y][x] in [GARDEN, START]:
                new_elves.add((y, x))
    return new_elves

def explore_report(desert, elves, tiles, i):
    new_elves = set()
    for elf in elves:
        for y, x in adjacent(desert, *elf):
            if desert[y][x] in [GARDEN, START]:
                new_elves.add((y, x))
                if tiles[(y, x)] == UNKNOWN:
                    tiles[(y, x)] = i

    return new_elves



with open("input.txt") as file:
    desert = [list(line) for line in file.read().strip().split("\n")]
    elves = set([(y, x) for y, x in it.product(range(len(desert)), range(len(desert[0]))) if desert[y][x] == 'S'])
    start_tiles = list(it.product([0, len(desert) // 2, len(desert) - 1], [0, len(desert[0]) // 2, len(desert[0]) - 1]))
    all_tiles = [(y, x) for y, x in it.product(range(len(desert)), range(len(desert[0]))) if desert[y][x] in [START, GARDEN]]
    
    # find reachable tiles
    print('searching reachable tiles')
    new_elves = elves
    elves = []
    i = 0
    while elves != new_elves:
        elves = new_elves
        new_elves = explore(desert, elves)
        new_elves = explore(desert, new_elves)
    reachable_tiles = list(elves.union(explore(desert, elves)))
    
    # find steps needed to reach each tile from all relevant tiles
    behaviour = {}
    for start_tile in start_tiles:
        print('finding steps needed to reach each tile from', start_tile)
        behaviour[start_tile] = {}
        for reachable_tile in reachable_tiles:
            behaviour[start_tile][reachable_tile] = UNKNOWN
        elves = set([start_tile])
        for i in it.count(1):
            elves = explore_report(desert, elves, behaviour[start_tile], i)
            if not any([x == UNKNOWN for x in behaviour[start_tile].values()]):
                break

    # from analysis of my input, the steps needed completely explore a map is 
    # equal to the distance to the furthest tile from the start tile, so we can
    # just take a single direction and we know the square shape relevant
    modified_steps = STEPS + 1
    radius = (modified_steps) // len(desert)
    leftover = (modified_steps) % len(desert)

    edge_blocks = radius * 4
    
    print('radius:', radius)
    print('edge blocks:', edge_blocks)
    
    total = 0
    other_parity_tiles, base_parity_tiles = area_by_parity(radius)

    base_parity = STEPS % 2
    other_parity = (STEPS + 1) % 2

    base_parity_count = 0
    other_parity_count = 0

    for tile in reachable_tiles:
        if parity(*tile) == base_parity:
            base_parity_count += 1
        else:
            other_parity_count += 1


    total += base_parity_count * base_parity_tiles
    total += other_parity_count * other_parity_tiles

    if radius % 2:
        desired_parity = other_parity
    else:
        desired_parity = base_parity

    print('centre blocks:', base_parity_tiles, other_parity_tiles, '=', base_parity_tiles + other_parity_tiles)
    print('parity count:', base_parity_count, other_parity_count)
    print('remaining steps:', leftover)

    print('edge areas:')
    for start_tile in start_tiles:
    # there are 4 edge tiles (the outer points) which are reached on the 
    # relevant edge piece with (leftover + 65) steps remaining
        if (start_tile[0] == len(desert) // 2\
            or start_tile[1] == len(desert) // 2)\
            and start_tile[0] != start_tile[1]:
            remaining_steps = leftover + 65
            count = 1

    # the rest of the edge tiles are reached with leftover steps 
    # remaining on the relevant corner piece
        elif start_tile[0] != len(desert) // 2 and start_tile[1] != len(desert) // 2:
            remaining_steps = leftover
            count = (edge_blocks // 4) - 1

    # the middle tile does not lie on the edge
        else:
            continue

        tiles_reached = 0

    # add to total the area of these edge blocks
        for tile in behaviour[start_tile]:
            if behaviour[start_tile][tile] <= remaining_steps and parity(*tile) == desired_parity:
                tiles_reached += 1
        print(f"\t{tiles_reached} {count}")
        total += tiles_reached * count

    print(total)
    print('expected:', 628206330073385)
    # TODO: fix me