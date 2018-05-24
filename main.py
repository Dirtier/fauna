import pandas as pd

df = pd.read_excel('VAWV-Total.xlsx')

# list of unique caves in data frame
cave_set = sorted(set(df['Cave']))

# list of species found in each cave
caves = dict()

# rows in data frame associated with each cave
caves_detailed = dict()

for cave in cave_set:
    caves[cave] = list(df.loc[df['Cave'] == cave]['Species'])
    caves_detailed[cave] = df.loc[df['Cave'] == cave]

print(caves)
print(caves_detailed)
