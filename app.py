import pandas as pd

path = "./data/costs.csv"

file = open(path, newline="")
df = pd.read_csv(file)

# Print averages
print("October Average\n", df.loc[1:31].mean())
print("\n")
print("November Average\n", df.loc[32:].mean())

# who used the most and the least?