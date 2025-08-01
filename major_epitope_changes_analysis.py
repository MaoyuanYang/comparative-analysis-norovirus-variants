import os
from matplotlib import pyplot as plt
import matplotlib
import pandas as pd
from pandas import DataFrame

siteA = [294, 295, 296, 297, 298, 368, 372, 373]
siteB = [333, 389]
siteC = [339, 340, 341, 375, 376, 377, 378]
siteD = [393, 394, 395, 396, 397]
siteE = [407, 411, 412, 413, 414]
siteG = [352, 355, 356, 357, 359, 364]
siteH = [309, 310]
site = siteA + siteB + siteC + siteD + siteE + siteG + siteH
SeqLen = 541
SeqNum = 0
# data = {'#': ['Sydney', 'Den_Haag', 'New_Orleans', 'Apeldoorn', 'Camberwell', 'Farmington_Hills', 'Hunter',
#               'Osaka', 'US95_96', 'Yerseke']}
data = {}
AaDistribution = {}
AaDistribution_str_list = []
AaDistribution_str = ''
for m in site:
    data[m] = []

for CapsidSubtype in ['Sydney', 'Den_Haag', 'New_Orleans', 'Apeldoorn', 'Camberwell', 'Farmington_Hills', 'Hunter',
                      'Osaka', 'US95_96', 'Yerseke']:
    AaFile = 'data/SNP-VP1_GII.4_' + CapsidSubtype + '_Aa/VP1-GII.4_' + CapsidSubtype + '-Aa.fas'
    AaComparedFile = 'data/SNP-VP1_GII.4_' + CapsidSubtype + '_Aa/VP1-GII.4_' + CapsidSubtype + '-Aa-compared.fas'
    f = open(AaFile, 'r')
    vp1 = open(AaComparedFile, 'r')
    seqs = []
    j = 0
    g = 0
    position = 0
    MutationDirection = {}
    MutationDirection_str = ''
    MutationDirection_str_List = []
    ratio_list = []
    vp1.readline()
    ComparedSeq = vp1.readline()
    line = f.readline()
    while line:
        if '>' not in line:
            seqs.append(line.replace('\n', ''))
        line = f.readline()
    SeqNum = len(seqs)
    seqs.append(ComparedSeq)
    for po in site:
        MutationNum = 0
        gapNum = 0
        i = po - 1
        for seq in seqs:
            if seq[i] != ComparedSeq[i]:
                if seq[i] != '-' and ComparedSeq[i] != '-':
                    MutationNum = MutationNum + 1
                    if ComparedSeq[i] + '——>' + seq[i] in MutationDirection.keys():
                        MutationDirection[ComparedSeq[i] + '——>' + seq[i]] = MutationDirection[
                                                                                 ComparedSeq[i] + '——>' + seq[
                                                                                     i]] + 1
                    else:
                        MutationDirection[ComparedSeq[i] + '——>' + seq[i]] = 1
                else:
                    gapNum = gapNum + 1
            if seq[i] in AaDistribution.keys():
                AaDistribution[seq[i]] = AaDistribution[seq[i]] + 1
            else:
                AaDistribution[seq[i]] = 1

        ratio_list.append(MutationNum / (SeqNum - gapNum))

        MutationDirection_order = sorted(MutationDirection.items(), key=lambda x: x[1], reverse=True)
        for m in MutationDirection_order:
            if m[1] / SeqNum >= 0.01:
                MutationDirection_str = MutationDirection_str + str(m[0]) + ':' + str(m[1]) + '\n'
        if MutationDirection_str == '':
            MutationDirection_str = ComparedSeq[i]
        MutationDirection = {}
        MutationDirection_str_List.append(MutationDirection_str)
        MutationDirection_str = ''

        AaDistribution_order = sorted(AaDistribution.items(), key=lambda x: x[1], reverse=True)
        AaDistribution = {}
        for m in AaDistribution_order:
            if m[1] / (SeqNum + 1) >= 0.01:
                #     AaDistribution_str = AaDistribution_str + m[0] + ':' + str(m[1]) + '\n'
                AaDistribution_str = AaDistribution_str + m[0] + ':' + str(format(m[1] / (SeqNum + 1), '.3f')) + '\n'
        AaDistribution_str_list.append(AaDistribution_str)
        AaDistribution_str = ''
    for l in range(len(site)):
        if MutationDirection_str_List[l] == '':
            MutationDirection_str_List[l] = '-'
        data[site[l]].append(AaDistribution_str_list[l])
        data[site[l]].append(ratio_list[l])
        data[site[l]].append(MutationDirection_str_List[l])
    AaDistribution_str_list = []
    MutationDirection_str_List = []
    ratio_list = []

print(data)
result = DataFrame(data)
result.to_excel('主要抗原表位改变情况.xlsx')
