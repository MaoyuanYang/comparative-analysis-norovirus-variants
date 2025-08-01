import pandas as pd

# ['Sydney', 'New_Orleans', 'Den_Haag']
CapsidSubtype = 'Den_Haag'
SeqFile = open('data/' + 'VP1-' + CapsidSubtype + '.fasta', 'r')
ComparedFile = open('data/' + CapsidSubtype + '/compared.fas', 'r')
# SeqFile = open('data/' + CapsidSubtype + '/' + CapsidSubtype + '.fas', 'r')
# ComparedFile = open('data/' + CapsidSubtype + '/compared.fas', 'r')
seqs = []
ComparedFile.readline()
comparedSeq = ComparedFile.readline().replace('\n', '')
line = SeqFile.readline()
row = []
data = []
while line:
    if '>' not in line:
        seqs.append(line.replace('\n', ''))
    line = SeqFile.readline()

seqLen = len(seqs[0])

for p in range(seqLen):
    row.append(p + 1)
data.append(row)
row = []

# for p in range(seqLen):
#     if comparedSeq[p] == '-':
#         row.append(1)
#     else:
#         row.append(0)
# data.append(row)
# row = []

for seq in seqs:
    for p in range(seqLen):
        if seq[p] == '-':
            row.append(1)
        else:
            row.append(0)
    data.append(row)
    row = []
e = pd.DataFrame(data)
e.to_excel(CapsidSubtype + '-result-vp1.xlsx')
