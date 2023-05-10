import numpy as np
import pandas as pd


def nan_num(m):
    n = 0
    for e in m:
        if np.isnan(e):
            n = n + 1
    return n


seqs = []
seqNum = 0
seqLen = 0
mutation = []
js = 0
unit_str = ''
data = {}
unitPositionA = []
unitPositionB = []
MutationRatioA = []
MutationRatioB = []
unitRatio = []
jd = 0
# ['Sydney', 'New_Orleans', 'Den_Haag']
for CapsidSubtype in ['Den_Haag']:
    seqfile = open(CapsidSubtype + '/' + CapsidSubtype + '.fas', 'r')
    compared = open(CapsidSubtype + '/' + 'compared.fas', 'r')
    compared.readline()
    comparedSeq = compared.readline().replace('\n', '')
    line = seqfile.readline()
    while line:
        if '>' not in line:
            seqs.append(line.replace('\n', ''))
        line = seqfile.readline()
    seqLen = len(comparedSeq)
    seqNum = len(seqs)
    matrix = np.zeros((int(seqNum), int(seqLen)))
    for seq in seqs:
        for p in range(seqLen):
            if comparedSeq[p] != '-' and seq[p] != '-':
                if comparedSeq[p] != seq[p]:
                    mutation.append(1)
                else:
                    mutation.append(0)
            else:
                mutation.append(np.nan)
        matrix[js] = mutation
        js = js + 1
        mutation = []
    js = 0
    seqs = []
    matrix = matrix.T
    for i in range(seqLen):
        for j in range(seqLen):
            jd = jd + 1
            if i != j:
                if 0.95 > np.sum(matrix[i] == 1) / (np.sum(matrix[i] == 1)+np.sum(matrix[i] == 0)) > 0.05 and 0.95 > np.sum(matrix[j] == 1) / (np.sum(matrix[j] == 1)+np.sum(matrix[j] == 0)) > 0.05:
                    if (np.sum((matrix[j] - matrix[i]) == 0) + nan_num(matrix[j] - matrix[i])) / seqNum >= 0.95:
                        # unit_str = unit_str + str(i) + ' & ' + str(j) + '\n'
                        unitPositionA.append(str(i + 1))
                        unitPositionB.append(str(j + 1))
                        unitRatio.append(
                            (np.sum((matrix[j] - matrix[i]) == 0) + nan_num(matrix[j] - matrix[i])) / seqNum)
                        MutationRatioA.append(np.sum(matrix[i] == 1) / (np.sum(matrix[i] == 1)+np.sum(matrix[i] == 0)))
                        MutationRatioB.append(np.sum(matrix[j] == 1) / (np.sum(matrix[j] == 1)+np.sum(matrix[j] == 0)))
            print(str(jd) + '/' + str(seqLen * seqLen) + '   进度：' + str(format(jd / (seqLen * seqLen), '.3f')))
    # print(np.sum((matrix[1]-matrix[0]) == 0))
    # print((matrix[1]-matrix[0]).tolist().count(0))
    data['unitSiteA'] = unitPositionA
    data['unitSiteB'] = unitPositionB
    data['unitRatio'] = unitRatio
    data['MutationRatioA'] = MutationRatioA
    data['MutationRatioB'] = MutationRatioB
    df = pd.DataFrame(data)
    df.to_excel('linkage-' + CapsidSubtype + '.xlsx')
    jd = 0
