import numpy as np
import pandas as pd

# ['Sydney', 'New_Orleans', 'Den_Haag']
unitRatio = 1
CapsidSubtype = 'Sydney'
unit_dic = {}
unit = []
temp = []
# 读取数据
print('开始读取数据')
df_all = pd.read_excel('linkage-' + CapsidSubtype + '-考虑突变方向.xlsx')
df = df_all.loc[df_all['unitRatio'] >= unitRatio]
jd = 0


# 判断list_b是否包含list_a
def isInclude(list_a, list_b):
    flag = 1
    for e in list_a:
        if e not in list_b:
            flag = 0
    return flag


# 组合函数
def FindUnit(site, dic, ulist):
    list_a = []
    list_b = []
    list_a.append(site)
    list_a.append(ulist[0])
    for j in range(1, len(ulist)):
        if isInclude(list_a, dic[ulist[j]]):
            list_a.append(ulist[j])
        else:
            list_b.append(ulist[j])
    return [list_a, list_b]


# 列表去重
def Deduplication(List):
    new = []
    for elm in List:
        if elm not in new:
            new.append(elm)
    return new


siteA = df['unitSiteA'].tolist()
siteB = df['unitSiteB'].tolist()
for i in range(len(siteA)):
    unit_dic[siteA[i]] = []
for i in range(len(siteA)):
    unit_dic[siteA[i]].append(siteB[i])

print('开始组合连锁位点')
keyNum = len(unit_dic.keys())
for key in unit_dic.keys():
    jd = jd + 1
    temp = FindUnit(key, unit_dic, unit_dic[key])
    if temp[1]:
        while temp[1]:
            unit.append(sorted(temp[0]))
            temp = FindUnit(key, unit_dic, temp[1])
    else:
        unit.append(sorted(temp[0]))
    print('进度：' + str(jd) + '/' + str(keyNum) + '   ' + format(jd / keyNum, '.3f'))

unit = Deduplication(unit)

# 保存数据
print('开始保存数据')
Mutation = pd.read_excel(CapsidSubtype + '-Mutation.xlsx')
maxLen = 0
for u in unit:
    if len(u) > maxLen:
        maxLen = len(u)

matrix = []
mutationRatio = []
mutationDirection = []
mutationInfo = pd.read_excel(CapsidSubtype + '-Mutation.xlsx')
for u in unit:
    for s in u:
        info = mutationInfo.loc[mutationInfo['site'] == s].values.tolist()[0]
        mutationRatio.append(info[2])
        # mutationRatio.append(format(info[2], '.3f'))
        mutationDirection.append(info[3])
    u = u + [np.nan] * (maxLen - len(u))
    mutationRatio = mutationRatio + [np.nan] * (maxLen - len(mutationRatio))
    mutationDirection = mutationDirection + [np.nan] * (maxLen - len(mutationDirection))
    matrix.append(u)
    matrix.append(mutationRatio)
    matrix.append(mutationDirection)
    mutationRatio = []
    mutationDirection = []
matrix = np.matrix(matrix)
df = pd.DataFrame(matrix)
df.to_excel('linkage-' + CapsidSubtype + '-' + str(unitRatio) + '-考虑突变方向.xlsx')
