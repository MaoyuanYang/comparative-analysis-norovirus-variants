import os
from matplotlib import pyplot as plt
import matplotlib
import pandas as pd
from pandas import DataFrame

# ['Sydney', 'New_Orleans', 'Den_Haag']
CapsidSubtype = 'Sydney'
seqs = []
data = {}
num = 0
MutationDirection = {}
MutationDirection_str = ''
MutationDirection_list = []
MutationRatio = 0
MutationRatio_list = []
position = []

File = './' + CapsidSubtype + '/' + CapsidSubtype + '.fas'
ComparedFile = './' + CapsidSubtype + '/' + 'compared.fas'
f = open(File, 'r')
compared = open(ComparedFile, 'r')

compared.readline()
ComparedSeq = compared.readline().replace('\n', '')
line = f.readline()
while line:
    if '>' not in line:
        seqs.append(line.replace('\n', ''))
    line = f.readline()
SeqNum = len(seqs)
SeqLen = len(ComparedSeq)
gapNum = 0
for i in range(SeqLen):
    for seq in seqs:
        if seq[i] != '-' and ComparedSeq[i] != '-':
            if seq[i] != ComparedSeq[i]:
                num = num + 1
                if ComparedSeq[i] + '——>' + seq[i] not in MutationDirection.keys():
                    MutationDirection[ComparedSeq[i] + '——>' + seq[i]] = 1
                else:
                    MutationDirection[ComparedSeq[i] + '——>' + seq[i]] = MutationDirection[
                                                                             ComparedSeq[i] + '——>' + seq[i]] + 1
        else:
            gapNum = gapNum + 1
    # MutationRatio = num / SeqNum
    if gapNum != SeqNum:
        MutationRatio = num / (SeqNum - gapNum)
    else:
        MutationRatio = 0
    for key in MutationDirection.keys():
        MutationDirection_str = MutationDirection_str + str(key) + ':' + str(MutationDirection[key]) + '\n'
    MutationDirection_list.append(MutationDirection_str)
    MutationRatio_list.append(MutationRatio)
    MutationRatio = 0
    num = 0
    gapNum = 0
    MutationDirection = {}
    MutationDirection_str = ''

for p in range(SeqLen):
    position.append(p + 1)

data['site'] = position
data['MutationRatio'] = MutationRatio_list
data['MutationDirection'] = MutationDirection_list

df = pd.DataFrame(data)

df.to_excel(CapsidSubtype + '-Mutation.xlsx')
