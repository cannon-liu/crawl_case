#!/usr/bin/env python3
#-*- coding:utf-8 -*-

__author__ = 'cannon-liu'

'''
create 2017.07.23

create write/read   txt
create write/read   csv
create write/read   json
create write/read   excel,文件格式只能是xls，xlsx会有问题
'''

import os
import csv
import json
import xlwt
import xlrd
import xlutils
from xlutils.copy import copy





class WrFile(object):
    def __init__(self):
        pass

    def write_txt(self,filename,items):
        f=open(filename,'a')
        for item in items:
            f.write(item + '\n')
        f.close()



    def read_txt(self,filename):
        f=open(filename,'r')
        for eachLine in f.readlines():
            #pass
            print(eachLine)
        f.close()


    def write_csv(self,filename,items):
        with open(filename,'a',newline='\n') as f:
            # dialect为打开csv文件的方式，默认是excel，delimiter="\t"参数指写入的时候的分隔符
            csvwriter = csv.writer(f, dialect=("excel"))
            # csv文件插入一行数据，把下面列表中的每一项放入一个单元格（可以用循环插入多行）
            for item in items:
                #newlines = ['a','1','2']
                newlines = list(item)
                #csvwriter.writerow(newlines)
                csvwriter.writerow(newlines)


    def read_csv(self,filename):
        ''''''
        with open(filename,'r') as f:
            csvreader = csv.reader(f)
            for line in csvreader:
                #pass
                print(line)

    '''往EXCEl单元格写内容，每次写一行sheet:页签名称；row：行内容列表；rowIndex：行索引;'''
    '''xlwt只能创建一个全新的excel文件,追加读写需要用到xlutils模块'''
    '''
    xlwt.Workbook() #创建工作簿
    cell_overwrite_ok参数表示能否覆盖，不改为True，可能报错
    write_merge(x, x + m, y, w + n, string, sytle)  表示合并单元格写入，如果m或者n=0,则表示单格写入

    '''

    def write_excel(self,filename):
        #style = xlwt.easyxf('font: bold 1')   easyxf代表了可以对excel的操作
        book = xlwt.Workbook(encoding='utf8',style_compression=0)
        sheet = book.add_sheet('haha',cell_overwrite_ok=True)
        #sheet = book.add_sheet('haha')
        sheet.write(1,1,'刘')
        sheet.write(1, 1, '100')
        book.save(filename)

    '''
    # 打开文件
    workbook = xlrd.open_workbook(r'F:\demo.xlsx')
    # 获取所有sheet
    print workbook.sheet_names() # [u'sheet1', u'sheet2']
    sheet2_name = workbook.sheet_names()[1]

    # 根据sheet索引或者名称获取sheet内容
    sheet2 = workbook.sheet_by_index(1) # sheet索引从0开始
    sheet2 = workbook.sheet_by_name('sheet2')

    # sheet的名称，行数，列数
    print sheet2.name,sheet2.nrows,sheet2.ncols

    # 获取整行和整列的值（数组）
    rows = sheet2.row_values(3) # 获取第四行内容
    cols = sheet2.col_values(2) # 获取第三列内容
    print rows
    print cols

    # 获取单元格内容
    print sheet2.cell(1,0).value.encode('utf-8')
    print sheet2.cell_value(1,0).encode('utf-8')
    print sheet2.row(1)[0].value.encode('utf-8')

    # 获取单元格内容的数据类型
    print sheet2.cell(1,0).ctype
    '''
    def read_excel(self,filename):
        excel = xlrd.open_workbook(filename)
        sheet = excel.sheet_by_index(0)  # sheet索引从0开始
        print(sheet.name)
        print(sheet.nrows)
        print(sheet.ncols)

    '''
     #用wlrd提供的方法读取一个excel文件,
     #用wlrd提供的方法获得现在已有的行数和列数，分别是sheet对象的nrows，ncols
     #用xlutils提供的copy方法将xlrd的对象转化为xlwt的对象,from xlutils.copy import copy
     #用xlwt对象的方法获得要操作的sheet
    '''
    def add_excel(self,filename):
        rexcel = xlrd.open_workbook(filename)  # 用wlrd提供的方法读取一个excel文件
        rows = rexcel.sheets()[0].nrows  # 用wlrd提供的方法获得现在已有的行数
        excel = copy(rexcel)  # 用xlutils提供的copy方法将xlrd的对象转化为xlwt的对象
        table = excel.get_sheet(0)  # 用xlwt对象的方法获得要操作的sheet
        print("*********************************")
        values = ["1", "2", "3"]
        row = rows
        for value in values:
            table.write(row, 0, value)  # xlwt对象的写方法，参数分别是行、列、值
            table.write(row, 1, "haha")
            table.write(row, 2, "lala")
            row += 1
        excel.save(filename)  # xlwt对象的保存方法，这时便覆盖掉了原来的excel



    def write_json(self,filename,item):     #item是对象
        with open(filename,'a', encoding='utf-8') as fp:
            line = json.dumps(dict(item),ensure_ascii=False)+'\n'

            fp.write(line)

        #对于多个{}，需要通过[{},{}]列表形式隔离，否则load(fp)会decode 报错
        #对于单个{}的文件，load(fp)能正常读取，千万不要写fp.read()，否则load(fp)也会decode 报错

    def read_json(self,filename):
        with open(filename,'r',encoding='utf-8') as fp:
            file = json.load(fp)
            print(file)





if __name__ == '__main__' :
    #write_txt('hello.txt')
    #read_txt('gonglv.txt')
    #write_csv('hello.csv')
    #read_csv('hello.csv')

    # wr.read_json('test2.json')
    wr = WrFile()
    wr.write_excel('./log/现在的.xlsx')
    #wr.add_excel('./log/现在的.xls')
    #wr.read_excel('./log/现在的.xls')
    # items = [['a',1,2],['b',3.4]]
    # wr.write_csv('./log/hello.csv',items)
    # wr.read_csv('./log/hello.csv')
