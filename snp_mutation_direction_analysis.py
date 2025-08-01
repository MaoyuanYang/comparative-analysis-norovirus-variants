import os
from matplotlib import pyplot as plt
import matplotlib
import pandas as pd
from pandas import DataFrame

excel = {'#': ['Sydney', 'Den_Haag', 'New_Orleans']}
data = {}
all = {}
for CapsidSubtype in ['Sydney', 'Den_Haag', 'New_Orleans']:
    f = open('./data/' + CapsidSubtype + '/' + CapsidSubtype + '.fas', 'r')
    compared_file = open('./data/' + CapsidSubtype + '/compared.fas', 'r')

    seqs = []
    compared_file.readline()
    ComparedSeq = compared_file.readline().replace('t', 'u')
    line = f.readline()
    while line:
        if '>' not in line:
            seqs.append(line.replace('\n', ''))
        line = f.readline()
    for seq in seqs:
        site = 0
        seq = seq.replace('t', 'u')
        while site < 1623:
            num = 0
            if seq[site] != '-' and ComparedSeq[site] != '-':
                if seq[site] != ComparedSeq[site]:
                    if str(ComparedSeq[site] + '->' + seq[site]) not in data.keys():
                        data[str(ComparedSeq[site] + '->' + seq[site])] = 1
                    else:
                        data[str(ComparedSeq[site] + '->' + seq[site])] = data[str(
                            ComparedSeq[site] + '->' + seq[site])] + 1
            site = site + 1
    all[CapsidSubtype] = data
    data = {}
l1 = list(all['Sydney'].keys())
l2 = list(all['Den_Haag'].keys())
l3 = list(all['New_Orleans'].keys())
union = list(set(sorted(l1 + l2 + l3)))

for u in union:
    excel[u] = []

for CapsidSubtype in ['Sydney', 'Den_Haag', 'New_Orleans']:
    for m in union:
        if m not in all[CapsidSubtype].keys():
            excel[m].append(0)
        else:
            excel[m].append(all[CapsidSubtype][m])

e = pd.DataFrame(excel)
e.to_excel('各变异株突变方向组成-u.xlsx')
