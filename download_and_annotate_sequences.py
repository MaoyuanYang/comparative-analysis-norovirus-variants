# 根据分型网站所得结果，从NCBI下载序列文件，并将序列的相关信息注释到文件名中

import re
from Bio import Entrez
import pandas as pd

# 正则表达式规则
pattern = re.compile('P[0-9]+|PNA[0-9]+')
s = ''

# email参数，这样如果遇到什么问题，NCBI可以通过邮件联系到你，在过度使用的情况下，NCBI会在封锁用户访问E-utilities之前尝试通过用户提供的邮件地址联系
Entrez.email = 'xxx'

# 分型网站结果
sheet = pd.read_excel('xxx')

gb = ''
fasta = ''
country = ''
data = ''
name = ''
c = 0
p = ''  # P分型
G = ''  # G分型
for i in range(13797):
    name = sheet.loc[i]['name']
    polymerase_type = sheet.loc[i]['polymerase type']
    capsid_type = sheet.loc[i]['capsid type']
    if pd.isna(polymerase_type) or polymerase_type == 'Could not assign':
        p = 'unknown'
    else:
        s = str(polymerase_type)
        p = pattern.search(s).group(0)
    if pd.isna(capsid_type) or capsid_type == 'Could not assign':
        g = 'unknown'
    else:
        g = str(capsid_type)
    sequence_type = g + '[' + p + ']'

    handle_fasta = Entrez.efetch(db="nucleotide", id=name, rettype="fasta", retmode="text")
    fasta = handle_fasta.read()
    handle_genbank = Entrez.efetch(db="nucleotide", id=name, rettype="gb", retmode="text")
    gb = handle_genbank.read()
    if 'country' not in str(gb):
        country = 'unknown'
    if 'collection_date' not in str(gb):
        data = 'unknown'
    gb = gb.split('\n')
    for line in gb:
        if 'country=' in line:
            line = line.split('"')
            country = line[1]
    for line in gb:
        if 'collection_date=' in line:
            line = line.split('"')
            data = line[1]
    country = country.replace(':', '_')
    data = data.replace('-', '_')
    country = country.replace('/', '_')
    data = data.replace('/', '_')
    path = './result/' + '/' + str(name) + '-' + sequence_type + '-' + country + '-' + data + '.fasta'
    path = path.replace('\\', '_')
    path = path.replace(':', '_')
    path = path.replace('*', '_')
    path = path.replace('?', '_')
    path = path.replace('"', '_')
    path = path.replace('>', '_')
    path = path.replace('<', '_')
    path = path.replace('|', '_')
    f = open(path, 'w')
    f.write(fasta)
    f.close()
    print('进度：' + str(i + 1) + '/' + '13797')
    print(path)
