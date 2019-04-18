import pandas as pd

path = "./data/costs.csv"

file = open(path, newline="")
df = pd.read_csv(file)

print("October Average\n", df.loc[1:31].mean())
print("\n")
print("November Average\n", df.loc[32:].mean())

df