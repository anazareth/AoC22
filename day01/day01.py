"""
Advent of Code 2022 Day 01
https://adventofcode.com/2022/day/1
AUTHOR: Alex Nazareth
DATE:   November 2023
Short description:
 - Input text list of integers, separated by \n.
 - Part 1: Return highest sum of each group of integers separated by a blank line.
 - Part 2: Return sum of top 3 highest.
"""

import pandas as pd

infile = "input.txt"

data = pd.read_csv(infile, header=None, skip_blank_lines=False)

max_cal = [0, 0, 0]
cal_count = 0
for cal in data[0]:
    if cal > 0:
        cal_count = cal_count + cal
    else:
        if cal_count>max_cal[2]:
            if cal_count>max_cal[1]:
                if cal_count>max_cal[0]:
                    max_cal.insert(0, cal_count)
                else:
                    max_cal.insert(1, cal_count)
            else:
                    max_cal.insert(2, cal_count)
            max_cal.pop()
        cal_count = 0

print(max_cal)
print(sum(max_cal))
