"""
Advent of Code 2022 Day 02
https://adventofcode.com/2022/day/2
AUTHOR: Alex Nazareth
DATE:   November 2023
Short description:
 - Many rounds of rock paper scissors.
 - Input text file of rows of 3 characters:
 -- First column A/B/C for rock, paper, scissors.
 --- Part 1: Second column X/Y/Z for what you should play: rock, paper, scissors.
 --- Part 2: Second column X/Y/Z for desired result: loss, draw, win.
 - In both parts, return sum of score when playing according to input.
"""

import pandas as pd


def part1(data):
    # second column indicates what move you should play: X, Y, Z = rock, paper, scissors
    data = data[0].str.split(' ', expand=True)
    data2 = data.copy()
    data2.iloc[:,0] = data.iloc[:,0].replace({'A': 0, 'B': 1, 'C': 2}, regex=True)
    data2.iloc[:,1] = data.iloc[:,1].replace({'X': 0, 'Y': 1, 'Z': 2}, regex=True)

    data2['result'] = data2.apply(lambda x: calc_score(x[1], x[0]), axis=1)

    return sum(data2['result'])

def part2(data):
    # second column indicates the desired round end result: X, Y, Z = loss, draw, win
    data = data[0].str.split(' ', expand=True)
    data2 = data.copy()
    
    # my encoding: Rock: 0, Paper: 1, Scissors: 2
    data2.iloc[:,0] = data.iloc[:,0].replace({'A': 0, 'B': 1, 'C': 2}, regex=True)

    # Ex. A loss would be playing -1 compared to opponent. Eg. opponent plays rock (0),
    #  so 0 + (-1) = -1, which is 2 (modulus 3), so you should play scissors (2) to lose.
    data2.iloc[:,1] = data.iloc[:,1].replace({'X': -1, 'Y': 0, 'Z': 1}, regex=True)

    data2['score'] = data2.apply(lambda x: calc_score2(x[1], x[0]), axis=1)
    
    return sum(data2['score'])

def calc_score(your_move, opp_move):
    # Rock: 0, Paper: 1, Scissors: 2
    # Game result corresponds to difference modulus 3
    # eg. Winning result for "you" (second column) is Scissors - Paper <-> 3-2 = 1,
    #   or Rock - Scissors <-> 0-2 = -2 <-> 1.
    diff = (your_move - opp_move) % 3
    # Win = 6, Lose = 0, Tie = 3, plus the value of your move:
    # Rock = 1, Paper = 2, Scissors = 3 (1 more than my encoding)
    return (3 + 3*diff) % 9 + your_move + 1

def calc_score2(desired_rslt, opp_move):
    # opponent's move + desired result (mod 3) yields the encoding for your move, add 1 for actual value of move
    # add 0 for loss, 3 for draw, 6 for win
    return (opp_move + desired_rslt) % 3 + 1 + (3 + 3*desired_rslt)
    
if __name__=="__main__":
    
    infile = 'input.txt'
    indata = pd.read_csv(infile, header=None, skip_blank_lines=False)

    print("Part 1: Your total score is " + str(part1(indata)))
    print("Part 2: Your total score is " + str(part2(indata)))
