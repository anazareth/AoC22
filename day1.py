import pandas as pd

in_url = "https://adventofcode.com/2022/day/1/input"

data = pd.read_csv(in_url, sep="\n")

print(data[:5])
