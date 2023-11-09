"""
Advent of Code 2022 Day 06
https://adventofcode.com/2022/day/6
AUTHOR: Alex Nazareth
DATE:   November 2023
Short description:
- Find Start of Packet Marker (SPM), first group of 4 sequential different characters.
- Part 1: Find position of first character of first SPM.
- Part 2:
"""

import pandas as pd

def part1(data):
    spm_size = 4
    four_char = data[:spm_size]
    i = spm_size
    while len(set(four_char)) != 4:
        four_char = four_char[1:] + data[i]
        i += 1
    if len(set(four_char)) == spm_size:
        print(four_char)
        return i
    else:
        return -1

if __name__ == '__main__':
    infile = 'input.txt'
    # infile = 'day06\input.txt'
    indata = pd.read_csv(infile, header=None, dtype=str, skip_blank_lines=False)
    indata = indata[0][0]
    print(indata[:4])
    print(indata[4])

    print("Part 1: The result is: " + str(part1(indata)))
    # print("Part 2: The result is: " + str(part2(indata)))