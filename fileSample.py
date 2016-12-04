# coding:utf-8
import os

f = open("test001.txt")
filestate = os.stat("test001.txt")
print filestate
for line in f:
    print line,