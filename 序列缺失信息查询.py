# 进一步查找缺失的注释信息

import os
import re
import pandas as pd
from Bio import Entrez

# 邮箱
Entrez.email = 'xxx.com'
CountryPattern = re.compile('[A-Z]+')


# 获取路径下所有文件名
def GetAllFiles(targetDir):
    listFiles = os.listdir(targetDir)
    return listFiles


# 查找国家
def GetCountry(SequenceID):
    flag = 0
    country = ''
    handle_genbank = Entrez.efetch(db="nucleotide", id=SequenceID, rettype="gb", retmode="text")
    gb = handle_genbank.read()
    if 'organism' not in gb:
        flag = 0
    else:
        gb = gb.split('/organism=')
        organism = gb[1].split('"')[1].replace('\n', '')
        for word in organism.split('/'):
            if word.replace('"', '').isupper():
                if 'GII' not in word:
                    flag = 1
                    country = word
    if flag == 1:
        return country
    if flag == 0:
        return 'could not find'


# 查找时间
def GetTime(SequenceID):
    flag = 0
    time = ''
    handle_genbank = Entrez.efetch(db="nucleotide", id=SequenceID, rettype="gb", retmode="text")
    gb = handle_genbank.read()
    if 'organism' not in gb:
        flag = 0
    else:
        gb = gb.split('/organism=')
        organism = gb[1].split('"')[1].replace('\n', '')
        for word in organism.split('/'):
            if word.isdigit() and 1000 < int(word) < 3000:
                flag = 1
                time = word
    if flag == 1:
        return time
    if flag == 0:
        return 'could not find'


# 查找G分型
def GetGIIType(SequenceID):
    flag = 0
    GIIType = ''
    handle_genbank = Entrez.efetch(db="nucleotide", id=SequenceID, rettype="gb", retmode="text")
    gb = handle_genbank.read()
    if '"genotype' in gb:
        gb = gb.split('/note=')
        genotype = gb[1].split('"')[1].replace('\n', '').replace('genotype:', '').replace(' ', '')
        return genotype
    else:
        if 'organism' not in gb:
            flag = 0
        else:
            gb = gb.split('/organism=')
            organism = gb[1].split('"')[1].replace('\n', '')
            for word in organism.split('/'):
                if 'GI' in word:
                    flag = 1
                    GIIType = word
        if flag == 1:
            return GIIType
        if flag == 0:
            return 'could not find'


GenoType = ''
country = ''
time = ''
sequences = GetAllFiles('./result/sequence')
for sequence in sequences:
    info = sequence.split('-')
    print(info)
    sequenceID = info[0]
    GenoType = info[1]
    country = info[2]
    time = info[3].replace('.fasta', '')
    if 'unknown' in sequence:
        print('正在判断', str(sequenceID))
        if info[1].split('[')[0] == 'unknown':
            print('判断G型别:')
            GIIType = GetGIIType(sequenceID)
            if GIIType == 'could not find':
                print('G型别无法判断')
            else:
                GenoType = GIIType + '[' + info[1].split('[')[1]
                print('G型别为', GenoType)
        if info[2] == 'unknown':
            print('判断来源国家：')
            if GetCountry(sequenceID) == 'could not find':
                print('无法判断来源国家')
            else:
                country = GetCountry(sequenceID)
                print('来源国家为：', country)
        if info[3].replace('.fasta', '') == 'unknown':
            print('查询收集时间：')
            if GetTime(sequenceID) == 'could not find':
                print('无法查找到收集时间')
            else:
                time = GetTime(sequenceID)
                print('收集时间为：', time)
        print('正在修改文件名')
        os.rename('./result/sequence/' + str(sequence),
                  './result/sequence/' + str(sequenceID) + '-' + GenoType.replace('/', ',').replace(':',
                                                                                                    '').replace('-',
                                                                                                                '.') + '-' + country + '-' + time +
                  '.fasta')
        print(str(sequence) + '\n' + '-->' + str(sequenceID) + '-' + GenoType.replace('/',
                                                                                      ',').replace(':', '').replace('-',
                                                                                                                    '.') + '-' + country + '-' + time + '.fasta')
        print('---------------------------------------------------')

df = pd.read_excel('./data/information.xlsx')
for sequence in sequences:
    word = sequence.split('-')
    InfoList = df.loc[df['name'] == word[0]].values.tolist()[0]
    if pd.isna(InfoList[4]):
        PSubtype = '_unknown'
    else:
        PSubtype = '_' + InfoList[4]
        if InfoList[4] == 'Could not assign':
            PSubtype = '_unknown'
    if pd.isna(InfoList[6]):
        GSubtype = '_unknown'
    else:
        GSubtype = '_' + InfoList[6]
        if InfoList[6] == 'Could not assign':
            GSubtype = '_unknown'

    NewSequence = word[0] + '-' + word[1].split('[')[0] + GSubtype + '[' + word[1].split('[')[1].replace(']',
                                                                                                         '') + PSubtype + ']-' + \
                  word[2] + '-' + word[3]
    os.rename('./result/sequence/' + str(sequence), './result/sequence/' + str(NewSequence))
