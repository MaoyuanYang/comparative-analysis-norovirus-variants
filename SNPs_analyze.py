import os
from matplotlib import pyplot as plt
import matplotlib
import pandas as pd

# ['Sydney', 'New_Orleans', 'Den_Haag']
CapsidSubtype = 'Sydney'
SeqFile = open('data/' + CapsidSubtype + '/' + CapsidSubtype + '.fas', 'r')
ComparedFile = open('data/' + CapsidSubtype + '/compared.fas', 'r')
seqs = []
ratio = []
num = 0
gapNum = 0
data = {}
ComparedFile.readline()
ComparedSeq = ComparedFile.readline()
line = SeqFile.readline()
while line:
    if '>' not in line:
        seqs.append(line.replace('\n', ''))
    line = SeqFile.readline()
SeqLen = len(ComparedSeq)
seqNum = len(seqs)
x = []
for i in range(SeqLen):
    for seq in seqs:
        if seq[i] != '-' and ComparedSeq[i] != '-':
            if seq[i] != ComparedSeq[i]:
                num = num + 1
        else:
            gapNum = gapNum + 1
    if gapNum < seqNum:
        if 0.99 > num / (seqNum - gapNum) > 0.01:
            ratio.append(num / (seqNum - gapNum))
        else:
            ratio.append(0)
    else:
        ratio.append(0)
    x.append(i + 1)
    gapNum = 0
    num = 0

data = {'site': x, 'mutation rate': ratio}
# df = pd.DataFrame(data)
# df.to_excel(CapsidSubtype + '_snp.xlsx')

js = 0
for r in ratio:
    if r > 0:
        js = js + 1
print(js)
