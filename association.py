import pandas as pd
import itertools

INITIAL_RANGE = 1
FINAL_RANGE = 8

data = pd.read_csv(
    'datasets/processed association data - data for association rules.csv')
minimum_support_count = 2
records = []

for i in range(0, len(data)):
    records.append([str(data.values[i, j])
                   for j in range(INITIAL_RANGE, FINAL_RANGE)])
items = sorted(
    [item for sublist in records for item in sublist if item != 'nan'])


def stage_1(items, minimum_support_count):
    c1 = {i: items.count(i) for i in items}
    l1 = {}
    for key, value in c1.items():
        if value >= minimum_support_count:
            l1[key] = value

    return c1, l1


c1, l1 = stage_1(items, minimum_support_count)

print(c1, l1)
