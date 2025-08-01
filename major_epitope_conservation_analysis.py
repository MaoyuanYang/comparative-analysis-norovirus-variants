import operator
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
data = []
ratio = []
AaDistribution = {}
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
    vp1.readline()
    ComparedSeq = vp1.readline()
    line = f.readline()
    while line:
        if '>' not in line:
            seqs.append(line.replace('\n', ''))
        line = f.readline()
    SeqNum = len(seqs) + 1
    seqs.append(ComparedSeq)
    for po in site:
        i = po - 1
        for seq in seqs:
            if seq[i] in AaDistribution.keys():
                AaDistribution[seq[i]] = AaDistribution[seq[i]] + 1
            else:
                AaDistribution[seq[i]] = 1
        maxAa = max(AaDistribution.items(), key=operator.itemgetter(1))[1]
        print(maxAa)
        AaDistribution = {}
        ratio.append(maxAa / (SeqNum + 1))
    data.append(ratio)
    ratio = []

print(data)

CapsidSubtype_list = ['Sydney', 'Den_Haag', 'New_Orleans', 'Apeldoorn', 'Camberwell', 'Farmington_Hills', 'Hunter',
                      'Osaka', 'US', 'Yerseke']
plt.figure(figsize=(10, 10))
plt.imshow(data, cmap='magma')  
plt.xticks(range(len(site)), site, rotation=60)
plt.yticks(range(len(CapsidSubtype_list)), CapsidSubtype_list)
plt.colorbar(shrink=0.6)
# plt.savefig('热力图.png')
plt.show()
