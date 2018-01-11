#======================================
# File Name: lagou-address.py
# Author: Jewelry Zhu
# mail: jewelryzhu@v4user.com
# Created Time: 日  1/ 7 22:11:04 2018
#====================================
#!/usr/bin/python3
# -*- coding: utf-8 -*-

import codecs
import urllib
import re
from lxml import etree
import requests
import xlsxwriter
import time
def getHtml(num):                               #定义解析url成可分析数据的函数
    url ="http://hotel.elong.com/%s.html"%num   #格式化url，%s为替换变量
    page = requests.get(url)
    html = page.text
    return html
s = u''  #u表示读取中文
f = codecs.open("elong-address1.txt",'w','utf-8')    #创建并打开txt文档

f.write(s)
f.write(str(list))

for i in range(50206000,50210000):              #设置变量值域
    html_str=getHtml(i)
    html = etree.HTML(html_str)                 #解析xml文本
    result =    html.xpath('/html/body/div[3]/div/div[1]/div[1]/p/span[1]/text()')#解析xpath，进行定位
    for i in result:    #写入txt文件
        f.write(i)  

f.close()               #关闭txt文件
