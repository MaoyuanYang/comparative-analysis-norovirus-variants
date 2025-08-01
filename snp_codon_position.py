import os
from matplotlib import pyplot as plt
import matplotlib
import pandas as pd

# Sydney:
# ORF1:5bp-5110bp
# ORF2区：5091bp - 6713bp
# ORF3:6714bp-7519bp

# New_Orleans
# ORF1：5bp-5104bp
# ORF2:5085bp-6707bp
# ORF3:6707bp-7514bp

# Den_Haag
# ORF1：6bp-5111bp
# ORF2: 5092bp-6714bp
# ORF3: 6715bp-7521bp

CapsidSubtype = 'New_Orleans'
SeqFile = open('data/' + CapsidSubtype + '/' + CapsidSubtype + '.fas', 'r')
ComparedFile = open('data/' + CapsidSubtype + '/compared.fas', 'r')
seqs = []
ratio = []
num = 0
gapNum = 0
data = {}
ComparedFile.readline()
ComparedSeq = ComparedFile.readline().replace('\n', '')
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
            x.append(i + 1)
    gapNum = 0
    num = 0
ORF1 = {'first': 0, 'second': 0, 'third': 0}
ORF2 = {'first': 0, 'second': 0, 'third': 0}
ORF3 = {'first': 0, 'second': 0, 'third': 0}

if CapsidSubtype == 'Sydney':
    for site in x:
        if 5 <= site <= 5110:
            flag = site % 3
            if flag == 2:
                ORF1['first'] = ORF1['first'] + 1
            if flag == 0:
                ORF1['second'] = ORF1['second'] + 1
            if flag == 1:
                ORF1['third'] = ORF1['third'] + 1
        if 5091 <= site <= 6713:
            flag = site % 3
            if flag == 0:
                ORF2['first'] = ORF2['first'] + 1
            if flag == 1:
                ORF2['second'] = ORF2['second'] + 1
            if flag == 2:
                ORF2['third'] = ORF2['third'] + 1
        if 6713 <= site <= 7519:
            flag = site % 3
            if flag == 2:
                ORF3['first'] = ORF3['first'] + 1
            if flag == 0:
                ORF3['second'] = ORF3['second'] + 1
            if flag == 1:
                ORF3['third'] = ORF3['third'] + 1

if CapsidSubtype == 'Den_Haag':
    for site in x:
        if 6 <= site <= 5111:
            flag = site % 3
            if flag == 0:
                ORF1['first'] = ORF1['first'] + 1
            if flag == 1:
                ORF1['second'] = ORF1['second'] + 1
            if flag == 2:
                ORF1['third'] = ORF1['third'] + 1
        if 5092 <= site <= 6714:
            flag = site % 3
            if flag == 1:
                ORF2['first'] = ORF2['first'] + 1
            if flag == 2:
                ORF2['second'] = ORF2['second'] + 1
            if flag == 0:
                ORF2['third'] = ORF2['third'] + 1
        if 6715 <= site <= 7521:
            flag = site % 3
            if flag == 1:
                ORF3['first'] = ORF3['first'] + 1
            if flag == 2:
                ORF3['second'] = ORF3['second'] + 1
            if flag == 0:
                ORF3['third'] = ORF3['third'] + 1

if CapsidSubtype == 'New_Orleans':
    for site in x:
        if 5 <= site <= 5104:
            flag = site % 3
            if flag == 2:
                ORF1['first'] = ORF1['first'] + 1
            if flag == 0:
                ORF1['second'] = ORF1['second'] + 1
            if flag == 1:
                ORF1['third'] = ORF1['third'] + 1
        if 5085 <= site <= 6707:
            flag = site % 3
            if flag == 0:
                ORF2['first'] = ORF2['first'] + 1
            if flag == 1:
                ORF2['second'] = ORF2['second'] + 1
            if flag == 2:
                ORF2['third'] = ORF2['third'] + 1
        if 6707 <= site <= 7514:
            flag = site % 3
            if flag == 2:
                ORF3['first'] = ORF3['first'] + 1
            if flag == 0:
                ORF3['second'] = ORF3['second'] + 1
            if flag == 1:
                ORF3['third'] = ORF3['third'] + 1

print(CapsidSubtype)
print(ORF1)
print(ORF2)
print(ORF3)
