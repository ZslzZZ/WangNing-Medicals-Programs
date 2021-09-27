import pandas as pd
import numpy as np
df = pd.read_excel('./重庆六家医院合并.xlsx')
nunumber = df.isnull().sum()
temp = pd.DataFrame(nunumber)
temp.to_excel('统计空值数量.xlsx')
for i in range(len(nunumber)):
    if nunumber[i]< (len(df)/5):
        nunumber[i] = False
    else: nunumber[i] = True
    #说明有超过5分之一的病人都没有录入数据，将舍弃该属性
for index in nunumber.index :
    if nunumber[index] == True :
        df = df.drop(index,axis =1)
#df1 = df.fillna(value = df.mode().iloc[0])  #用众数去填充空值
df1 = df.loc[:, (df != df.iloc[0]).any()] #去除所有值相同的列
df1.to_excel('空值去除后数据.xlsx',index = False)
        
