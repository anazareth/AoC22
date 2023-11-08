"""
Advent of Code 2022 Day 05
https://adventofcode.com/2022/day/5
AUTHOR: Alex Nazareth
DATE:   November 2023
Short description:
- Find final state of crate stacks given initial state and series of moves.
- Part 1: Crane can only move one crate at a time.
- Part 2: Crane can move multiple crates at a time (all crates from one move, ie one row).
"""

import pandas as pd
import numpy as np
import regex as re

def main(crates, moves, is_part1=True):
    crates2 = crates.transpose()
    stacks = []
    for i, stack in crates2.iterrows():
        rev_stack = stack.tolist()
        rev_stack.reverse()
        rev_stack = [i for i in rev_stack if i!=' ']
        stacks.append(rev_stack)

    for move in moves:
        qty, source, target = re.split(r'move ([0-9]+) from ([0-9]) to ([0-9])', move)[1:-1]
        qty, source, target = int(qty), int(source)-1, int(target)-1
        if is_part1:
            for _ in range(qty):
                stacks[target].append(stacks[source].pop())
        else:
            stacks[target].extend(stacks[source][-qty:])
            stacks[source] = stacks[source][:-qty]
    print(stacks)
    return ''.join([s[-1:][0] for s in stacks])


if __name__=='__main__':
    infile = 'input.txt'
    
    indata = pd.read_csv(infile, header=None, dtype=str, skip_blank_lines=False)
    blank_row = np.where(pd.isnull(indata))[0][0]
    df = indata.loc[:blank_row-2,:]
    df2 = df.copy()
    for i, row in df2.iterrows():
        df2.loc[i,0] = ['|' if i%4==3 else c for i, c in enumerate(row[0])]
    df3 = pd.DataFrame(df2[0].tolist(), index= df2.index)
    crate_start_pos = df3[[4*i+1 for i in range(9)]]
    crate_start_pos.columns = [i for i in range(9)]
    move_sequence = indata.loc[blank_row+1:,0].to_list()

    print("Part 1: The top crates are: " + str(main(crate_start_pos, move_sequence)))
    print("Part 2: The top crates are: " + str(main(crate_start_pos, move_sequence, False)))


