#!/usr/bin/python
#-*- coding:utf8 -*-
import json
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
import time, datetime

f = file("./h5.txt")
s = json.load(f)
f.close
# print s
print s[0].keys()
# print s["hits"]["hits"][0]["_source"].keys()
# print len(s["hits"]["hits"])

# arr = []
# for a in s["hits"]["hits"]:
    # arr.append(a["_source"])
def tsconvert(x):
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(x/1000))
def tscompare(x):
    return x.split(" ")[0] == "2019-06-06"

print "数据总条目数：%d" % len(s)

df = pd.DataFrame(s)
# print df.head()
df['time'] = df['time'].apply(tsconvert)
# print df.head()
df = df[df['time'].apply(tscompare)]
# print "按时期筛选后条目数：%d" % len(df)
# print df.head()
# IsDuplicated = df.duplicated()
df = df.drop_duplicates(["aid"])
df = df[df['status'] == 1]
print "用户去重后条目数：%d" % len(df)
# print df.head()
# df = df[df['activeTime'] < 24 * 60]
df = df[df['activeTime'] > 0]
print "去掉存活时间为０后条目数：%d" % len(df)
df = df[df['clientTime'] < 5 * 60 * 8]
df = df[df['clientTime'] > 0]
print "去掉展示时间为０后条目数：%d" % len(df)

alluser = len(df)
# print "去除status==2数据后条目数：%d" % alluser
print df.head()

# print df['showCount'].value_counts()
# print df['pid'].value_counts()
alltime = df['clientTime'].sum()
allshow = df['showCount'].sum()

print alltime
print allshow
# print "平均展示时长，秒：%d" % (alltime/allshow)
print "平均用户展示时长，秒：%d" % (alltime/alluser)

print "平均被杀次数：%d" % (df['idChange'].sum()/alluser)
print "平均存活时间，小时：%d" % (df['activeTime'].sum()/alluser/60)

ts = pd.Series(df['clientTime'].values)
# ts = ts[ts > 300]
# print ts.head()
# ts = ts[ts < 200]
# plt.plot(ts,'bo-')
# plt.show()
