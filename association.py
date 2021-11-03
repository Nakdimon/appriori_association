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


def stage_1(items, minimum_support_count):
    c1 = {i: items.count(i) for i in items}
    l1 = {}
    for key, value in c1.items():
        if value >= minimum_support_count:
            l1[key] = value

    return c1, l1


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


def stage_4(l3, records, minimum_support_count):
    l3 = list(l3.keys())
    L3 = sorted(list(set([item for t in l3 for item in t])))
    L3 = list(itertools.combinations(L3, 4))
    c4 = {}
    l4 = {}
    for iter1 in L3:
        count = 0
        for iter2 in records:
            if sublist(iter1, iter2):
                count += 1
        c4[iter1] = count
    for key, value in c4.items():
        if value >= minimum_support_count:
            if check_subset_frequency(key, l3, 3):
                l4[key] = value

    return c4, l4


def stage_5(l4, records, minimum_support_count):
    l4 = list(l4.keys())
    L4 = sorted(list(set([item for t in l4 for item in t])))
    L4 = list(itertools.combinations(L4, 5))
    c5 = {}
    l5 = {}
    for iter1 in L4:
        count = 0
        for iter2 in records:
            if sublist(iter1, iter2):
                count += 1
        c5[iter1] = count
    for key, value in c5.items():
        if value >= minimum_support_count:
            if check_subset_frequency(key, l4, 4):
                l5[key] = value

    return c5, l5


c1, l1 = stage_1(items, minimum_support_count)
c2, l2 = stage_2(l1, records, minimum_support_count)
c3, l3 = stage_3(l2, records, minimum_support_count)
c4, l4 = stage_4(l3, records, minimum_support_count)
c5, l5 = stage_5(l4, records, minimum_support_count)

print("L1 => ", l1)
print("L2 => ", l2)
print("L3 => ", l3)
print("L4 => ", l4)
print("L5 => ", l5)

itemlist = {**l1, **l2, **l3, **l4}
sets = []
for iter1 in list(l4.keys()):
    subsets = list(itertools.combinations(iter1, 2))
    sets.append(subsets)


def support_count(itemset, itemlist):
    return itemlist[itemset]


list_l4 = list(l4.keys())
for i in range(0, len(list_l4)):
    for iter1 in sets[i]:
        a = iter1
        b = set(list_l4[i]) - set(iter1)
        confidence = (support_count(
            list_l4[i], itemlist)/support_count(iter1, itemlist))*100
        print("Confidence{}->{} = ".format(a, b), confidence)
