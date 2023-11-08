"""
Advent of Code 2022 Day 03
https://adventofcode.com/2022/day/3
AUTHOR: Alex Nazareth
DATE:   November 2023
Short description:
- Find overlapping sections in each pair of section ranges.
"""

import pandas as pd


def part1and2(data, is_part1):
    count_redundant = 0
    for _, pair in data.iterrows():
        sec1start, sec1end = [eval(i) for i in pair[0].split('-')]
        sec2start, sec2end = [eval(i) for i in pair[1].split('-')]

        if is_part1:
            # either section is a subset of the other
            if (sec1start<=sec2start and sec1end>=sec2end) \
                or (sec2start<=sec1start and sec2end>=sec1end):
                count_redundant = count_redundant + 1
        else:
            # sections overlap
            if sec1end>=sec2start and sec1start<=sec2end:
                count_redundant = count_redundant + 1
    return count_redundant

if __name__=="__main__":
    
    infile = 'input.txt'
    indata = pd.read_csv(infile, header=None, dtype=str)

    print("Part 1: Number of fully redundant section pairs " + str(part1and2(indata, True)))
    print("Part 1: Number of overlapping section pairs " + str(part1and2(indata, False)))
