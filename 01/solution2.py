#!/usr/bin/env python3

literal_nums = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

def calibration(s):
    n = []
    for i in range(len(s)):
        if s[i] in ["0","1","2","3","4","5","6","7","8","9"]:
            n.append(s[i])
        else:
            [n.append(literal_nums[word]) for word in literal_nums if s[i:i+len(word)] == word]
    return int(n[0] + n[-1])

with open("input.txt") as file:
    lines = file.read().split("\n")[:-1]
    print(sum(list(map(calibration, lines))))