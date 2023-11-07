"""
Advent of Code 2022 Day 03
https://adventofcode.com/2022/day/3
AUTHOR: Alex Nazareth
DATE:   November 2023
Short description:
 - Input text list, each row is a string of characters, case sensitive.
 - Each row represents a rucksack with 2 compartments, each character represents an item.
 - First half of characters are in compartment 1, second half in compartment 2. 
 - Each rucksack has exactly 1 item appearing in both compartments.
 - Item priorities: {a-z: 1-26, A-Z: 27-52}.
 - Part 1: Return sum of duplicate items in compartments 1 and 2 in each rucksack.
 - Part 2: Return sum of badge priorities, 1 unique badge per 3 rows.
"""

import pandas as pd


def part1(data):
    runsum = 0
    for rucksack in data.loc[:,0]:
        num_items = int(len(rucksack))
        # find the duplicate item by finding the intersection of the two compartments
        # - pop an item out since there is guaranteed to be only one duplicate
        repeat_item = set(rucksack[:num_items//2]).intersection(set(rucksack[num_items//2:])).pop()
        runsum = runsum + get_priority(repeat_item)
    return runsum

def part2(data):
    runsum = 0
    i = 0
    while i < len(data) - 2:
        badge_char = set(data.loc[i,:][0]) & set(data.loc[i+1,:][0]) & set(data.loc[i+2,:][0])
        badge_char = badge_char.pop()
        runsum = runsum + get_priority(badge_char)
        i = i + 3
    return runsum

def get_priority(item_char):
    # ascii value of 'a' is 97, 'z' is 122, 'A' is 65, 'Z' is 90
    deduction = 96 if item_char.islower() else 38
    return ord(item_char) - deduction

if __name__=="__main__":
    
    infile = 'input.txt'
    indata = pd.read_csv(infile, header=None, skip_blank_lines=False)

    print("Part 1: Sum of repeat item priorities is " + str(part1(indata)))
    print("Part 2: Sum of badge priorities is " + str(part2(indata)))