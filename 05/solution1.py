#!/usr/bin/env python3
import functools as ft


def do_map(ms, x):
    for m in ms:
        if x in range(m[1], m[1] + m[2]):
            return x + (m[0] - m[1])
    return x

with open("input.txt") as file:
    # parse input
    lines = file.read().strip()
    seeds, rest = lines.split("seed-to-soil map:")
    seed_to_soil, rest = rest.split("soil-to-fertilizer map:")
    soil_to_fertilizer, rest = rest.split("fertilizer-to-water map:")
    fertilizer_to_water, rest = rest.split("water-to-light map:")
    water_to_light, rest = rest.split("light-to-temperature map:")
    light_to_temperature, rest = rest.split("temperature-to-humidity map:")
    temperature_to_humidity, humidity_to_location = rest.split("humidity-to-location map:")
    ms = [
        seed_to_soil, soil_to_fertilizer, fertilizer_to_water, 
        water_to_light, light_to_temperature, temperature_to_humidity, 
        humidity_to_location
        ]
    seeds = list(map(int, seeds.split(":")[1].strip().split()))

    # find solution
    for i in range(len(ms)):
        ms[i] = list(map(lambda x : list(map(int, x.split())), ms[i].strip().split("\n")))

    for m in ms:
        seeds = list(map(ft.partial(do_map, m), seeds))

    print(min(seeds))
