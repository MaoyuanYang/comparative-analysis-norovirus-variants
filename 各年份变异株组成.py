import pandas as pd
import re

pattern = re.compile('[0-9]{4}')
df = pd.read_excel('./snp/GII.4_info.xlsx')
data = {}
excel = {}
capsidList = ['Sydney_2012', 'Den_Haag_2006b', 'New_Orleans_2009', 'Apeldoorn_2007', 'Asia_2003', 'Bristol_1993',
              'Cairo_2007', 'Camberwell_1994',
              'Farmington_Hills_2002', 'Hong_Kong_2019', 'Hunter_2004', 'Kaiso_2003', 'Lanzou_2002',
              'Osaka_2007', 'US95_96', 'Yerseke_2006a']
for i in range(2538):
    info = df.iloc[i].values.tolist()
    year = pattern.search(info[7]).group()
    if int(year) < 2004:
        if int(year) < 1995:
            year = 'before 1995'
        else:
            if 1995 <= int(year) < 2001:
                year = 'before 2001'
            else:
                if 2001 <= int(year) < 2004:
                    year = 'before 2004'
    capsidSubtype = info[3]
    if year not in data.keys():
        data[year] = {}
    if capsidSubtype not in data[year].keys():
        data[year][capsidSubtype] = 1
    else:
        data[year][capsidSubtype] = data[year][capsidSubtype] + 1

year_sorted = sorted(data.keys())

excel['CapsidSubtype'] = capsidList

for y in year_sorted:
    excel[y] = []
for y in year_sorted:
    for c in capsidList:
        if c not in data[y].keys():
            excel[y].append(0)
        else:
            excel[y].append(data[y][c])

e = pd.DataFrame(excel)
e.to_excel('result.xlsx')
