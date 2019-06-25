#!/usr/bin/python
#-*- coding:utf8 -*-
import json
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
import time, datetime

f = file("/home/youxia/shared/h5/h5.txt")
s = json.load(f)
f.close
# print s
# print s[0].keys()
# print s["hits"]["hits"][0]["_source"].keys()
# print len(s["hits"]["hits"])

# arr = []
# for a in s["hits"]["hits"]:
    # arr.append(a["_source"])
def tsconvert(x):
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(x/1000))

# 20190607
def tscompare(x):
    day = x.split(" ")[0]
    hour = x.split(" ")[1].split(":")[0]
    return (day == "2019-06-22" and int(hour) >= 13) or (day == "2019-06-23" and int(hour) <=12)

df = pd.DataFrame(s)
print "数据总条目数：%d" % len(df)

df['time'] = df['time'].apply(tsconvert)

df = df[df['time'].apply(tscompare)]
print "按时期筛选后条目数：%d" % len(df)

df = df[df['status'] == 7]
print "status==7条目数：%d" % len(df)
df = df.drop_duplicates(["aid"])
print "用户去重后条目数：%d" % len(df)

df = df[df['activeTime'] < 24 * 60 * 60]
df = df[df['activeTime'] > 0]
print "去掉存活时间为０后条目数：%d" % len(df)
df = df[df['clientTime'] > 0]
print "去掉展示时间为０后条目数：%d" % len(df)
# df = df[df['clientTime'] <= 3 * 60]
# print "去掉展示时间大于1分钟后条目数：%d" % len(df)
alluser = len(df)
# print df.head()
# print df.tail()

# print df['showCount'].value_counts()
# print df['pid'].value_counts()
alltime = df['clientTime'].sum()
allshow = df['showCount'].sum()

#print alltime
#print allshow
if allshow != 0:
    print "平均展示次数，次：%d" % (allshow/alluser)
    print "展示平均时长，秒：%d" % (alltime/allshow)

print "展示时长区间分布(共3次):"
#设置切分区域
listBins = [0, 30, 60, 90, 120, 150, 300, 10000]
#设置切分后对应标签
listLabels = ['0~30','31~60','61~90','91~120','121~150','151~300','301~']
#利用pd.cut进行数据离散化切分
"""
pandas.cut(x,bins,right=True,labels=None,retbins=False,precision=3,include_lowest=False)
x:需要切分的数据
bins:切分区域
right : 是否包含右端点默认True，包含
labels:对应标签，用标记来代替返回的bins，若不在该序列中，则返回NaN
retbins:是否返回间距bins
precision:精度
include_lowest:是否包含左端点，默认False，不包含
"""
df['fenzu'] = pd.cut(df['clientTime'], bins=listBins, labels=listLabels, include_lowest=True)

print df['fenzu'].value_counts()

print "平均用户展示时长，秒：%d" % (alltime/alluser)
print "平均用户可用内存，KB：%d" % (df['ram'].sum()/alluser)
print "平均被杀次数：%d" % (df['idChange'].sum()/alluser)
print "平均存活时间，小时：%d" % (df['activeTime'].sum()/alluser/60)


# ts = pd.Series(df['fenzu'].values)
# ts = ts[ts > 300]
# print ts.head()
# ts = ts[ts < 200]
# plt.plot(ts,'bo-')
# plt.show()
