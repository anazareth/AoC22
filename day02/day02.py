"""
Advent of Code 2022 Day 02
https://adventofcode.com/2022/day/2
AUTHOR: Alex Nazareth
DATE:   November 2023
Short description:
 - Many rounds of rock paper scissors.
 - Input text file of rows of 3 characters:
 -- First column A/B/C, second column X/Y/Z, for rock, paper, scissors.
"""

import pandas as pd


def part1():
    infile = 'input.txt'
    data = pd.read_csv(infile, header=None, skip_blank_lines=False)
    data = data[0].str.split(' ', expand=True)
    data2 = data.copy()
    data2.iloc[:,1] = data.iloc[:,1].replace({'X': 0, 'Y': 1, 'Z': 2}, regex=True)
    data2.iloc[:,0] = data.iloc[:,0].replace({'A': 0, 'B': 1, 'C': 2}, regex=True)

    data2['result'] = data2.apply(lambda x: calc_score(x[1], x[0]), axis=1)
    print(data2.head(10))

    return sum(data2['result'])

def calc_score(your_move, opp_move):
    # Rock: 0, Paper: 1, Scissors: 2
    # Game result corresponds to difference modulus 3
    # eg. Winning result for "you" (second column) is Scissors - Paper <-> 3-2 = 1,
    #   or Rock - Scissors <-> 0-2 = -2 <-> 1.
    diff = (your_move - opp_move) % 3
    # Win = 6, Lose = 0, Tie = 3, plus the value of your move:
    # Rock = 1, Paper = 2, Scissors = 3 (1 more than my encoding)
    return (3 + 3*diff) % 9 + your_move + 1
    
if __name__=="__main__":
    print("Part 1: Your total score is " + str(part1()))
    print("Part 2:")
