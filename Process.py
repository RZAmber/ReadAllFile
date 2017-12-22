#! /usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author:Xiuzhu
@file:Process.py
@time:2017/12/21 14:28
"""


import os
import fnmatch
import natsort
import codecs
allFileNum = 0


def printPath(level,path):
    global allFileNum

    dirList = []
    fileList = []
    files = fnmatch.filter(os.listdir(path),'*.txt')
    files = natsort.natsorted(files)
    dirList.append(str(level))
    for f in files:
        if(os.path.isdir(path +'/' + f)):
            if(f[0] == '.'):
                pass
            else:
                dirList.append(f)
        if(os.path.isfile(path + '/' + f)):
            fileList.append(f)

    i_dl = 0
    for dl in dirList:
        if (i_dl == 0):
            i_dl = i_dl + 1
        else:
            print('-' * (int(dirList[0])),dl)
            printPath((int(dirList[0]) +1), path +'/' + dl)

    for fl in fileList:
        print('-' *(int(dirList[0])),fl)
        allFileNum = allFileNum+1

    return fileList

if __name__ == "__main__":
    fileList = printPath(1, r'D:\pycharm\Rd_File\test\goottext')
    print(fileList)
    f = codecs.open('good.txt','a',encoding = 'utf-8')
    for file in fileList:
        content = []
        file_now = 'test/goottext' + '/' + files
        all_line = codecs.open(file_now, 'r',encoding = 'gbk',errors = 'ignore').read().strip().split()
        print(all_line)

        f.write(' '.join(all_line) + '\n')
    f.close
