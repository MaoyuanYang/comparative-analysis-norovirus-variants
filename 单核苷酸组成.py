import pandas as pd
# ['Sydney', 'Den_Haag', 'New_Orleans', 'Apeldoorn', 'Camberwell', 'Farmington_Hills', 'Hunter', 'Osaka', 'US95_96',
# 'Yerseke']
data = {'CapsidSubtype': ['Sydney', 'Den_Haag', 'New_Orleans', 'Apeldoorn', 'Camberwell', 'Farmington_Hills', 'Hunter',
                          'Osaka', 'US95_96', 'Yerseke'], 'a': [], 't': [], 'c': [], 'g': [], '-': []}
for CapsidSubtype in ['Sydney', 'Den_Haag', 'New_Orleans', 'Apeldoorn', 'Camberwell', 'Farmington_Hills', 'Hunter',
                      'Osaka', 'US95_96', 'Yerseke']:
    a = 0
    t = 0
    c = 0
    g = 0
    gap = 0
    file = open('../snp/data/rna/VP1-GII.4_' + CapsidSubtype + '-rename.fasta', 'r')
    line = file.readline()
    while line:
        if '>' not in line:
            for base in line:
                if base == 'a':
                    a = a + 1
                if base == 't':
                    t = t + 1
                if base == 'c':
                    c = c + 1
                if base == 'g':
                    g = g + 1
                if base == '-':
                    gap = gap + 1
        line = file.readline()
    data['a'].append(a/(a+t+c+g+gap))
    data['t'].append(t/(a+t+c+g+gap))
    data['c'].append(c/(a+t+c+g+gap))
    data['g'].append(g/(a+t+c+g+gap))
    data['-'].append(gap/(a+t+c+g+gap))
e = pd.DataFrame(data)
e.to_excel('result-ratio.xlsx')