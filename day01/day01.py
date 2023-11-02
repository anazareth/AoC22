import pandas as pd

in_url = "https://adventofcode.com/2022/day/1/input.txt"

data = pd.read_csv(in_url)

print(data[:5])
