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


def sublist(lst1, lst2):
    return set(lst1) <= set(lst2)


def check_subset_frequency(itemset, l, n):
    if n > 1:
        subsets = list(itertools.combinations(itemset, n))
    else:
        subsets = itemset
    for iter1 in subsets:
        if not iter1 in l:
            return False
    return True


def stage_2(l1, records, minimum_support_count):
    l1 = sorted(list(l1.keys()))
    L1 = list(itertools.combinations(l1, 2))
    c2 = {}
    l2 = {}
    for iter1 in L1:
        count = 0
        for iter2 in records:
            if sublist(iter1, iter2):
                count += 1
        c2[iter1] = count
    for key, value in c2.items():
        if value >= minimum_support_count:
            if check_subset_frequency(key, l1, 1):
                l2[key] = value

    return c2, l2


c2, l2 = stage_2(l1, records, minimum_support_count)


def stage_3(l2, records, minimum_support_count):
    l2 = list(l2.keys())
    L2 = sorted(list(set([item for t in l2 for item in t])))
    L2 = list(itertools.combinations(L2, 3))
    c3 = {}
    l3 = {}
    for iter1 in L2:
        count = 0
        for iter2 in records:
            if sublist(iter1, iter2):
                count += 1
        c3[iter1] = count
    for key, value in c3.items():
        if value >= minimum_support_count:
            if check_subset_frequency(key, l2, 2):
                l3[key] = value

    return c3, l3


c3, l3 = stage_3(l2, records, minimum_support_count)

print(c3, l3)
