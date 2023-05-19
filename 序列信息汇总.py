# 将序列信息整理到excel表格中
import pandas as pd
import os
import re


# 获取路径下所有文件名
def GetAllFiles(targetDir):
    listFiles = os.listdir(targetDir)
    return listFiles


dic = {'ID': [],
       'capsid type': [],
       'capsid subtype': [],
       'polymerase type': [],
       'polymerase subtype': [],
       'location': [],
       'collection date': []}

FolderList = GetAllFiles('./')
for Folder in FolderList:
    if '.' not in Folder:
        CapsidSubtype = Folder
        SeqList = GetAllFiles('./' + Folder)
        for seq in SeqList:
            SeqID = seq.split('-')[0]
            CapsidType = seq.split('-')[1].split('[')[0]
            PolymeraseType = seq.split('-')[1].split('[')[1].split(']')[0]
            PolymeraseSubtype = ''
            location = seq.split('-')[2]
            CollectionDate = seq.split('-')[3].replace('.fasta', '')
            dic['ID'].append(SeqID)
            dic['capsid type'].append(CapsidType)
            dic['capsid subtype'].append(CapsidSubtype)
            dic['polymerase type'].append(PolymeraseType)
            dic['polymerase subtype'].append(PolymeraseSubtype)
            dic['location'].append(location)
            dic['collection date'].append(CollectionDate)

df = pd.DataFrame(dic)
df.to_excel('info.xlsx')
