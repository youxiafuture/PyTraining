# -*- coding:utf8 -*-
# !/usr/bin/python

import json
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
import time, datetime

def listall(datas):
    for data in datas:
        print data['msg']

alipay = "com.eg.android.AlipayGphone"
wechat = "com.tencent.mm"
mobqq = "com.tencent.mobileqq"
jdapp = "com.jingdong.app.mall"
taobao = "com.taobao.taobao"
meituan = "com.sankuai.meituan"
tmbao = "com.tmall.wireless"
ele = "me.ele"
douyin = "com.ss.android.ugc.aweme"
cheer = 'com.ss.android.article.video' #'com.kipling.cheerfour'

filename2 = "sdk2.json"
filename3 = "sdk3.json"
with open(filename3) as f:
    inapp_list = json.load(f)

msg_list = [inapp for inapp in inapp_list['data'] if inapp.has_key('status') and inapp['status'] == 10 and len(inapp['msg']) != 0]
print msg_list.__len__()

msg_list2 = [msg for msg in msg_list if cheer in msg['msg']]
print msg_list2.__len__()
# listall(msg_list2)
# listall(msg_list)

