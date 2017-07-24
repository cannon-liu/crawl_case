#!/usr/bin/env python
#-*- coding = utf-8 -*-

import os
import requests

'''
create 2017.07.23
__author__ = "cannnon-liu"

create  filedir
download img

'''


class getFile(object):
    def __init__(self):
        pass


    def save_dir(self,path,ch = False):

        file = path+'/'       #filename表示一个系列的文件夹，该系列文件都下载在此文件下
        if os.path.exists(file):
            pass
        else:
            os.makedirs(file)

        if ch:
            os.chdir(os.path.join(path, ''))  # 切换到系列目录下操作，不在脚本所在的目录

    def save_img(self,img_content,name):

        with open(str(name)+'.jpg','wb') as f:
            f.write(img_content)



if __name__ == '__main__':
    # url = 'http://xxx.jpg'   #随意选的一个网址
    #
    # user_agent = ''
    # headers = {'User_Agent': user_agent}
    # path = './log'
    # name = '无聊'
    # resp = requests.get(url, headers=headers)
    # print(resp.status_code)
    # file = getFile()
    # file.save_dir(path,ch=True)
    # file.save_img(resp.content,name)
    pass

