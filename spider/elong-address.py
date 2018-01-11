#======================================
# File Name: elong-address.py
# Author: Jewelry Zhu
# mail: jewelryzhu@v4user.com
# Created Time: 一  1/ 8 00:29:13 2018
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
def getHtml():
    url ="http://hotel.elong.com/shanghai/"
    page = requests.get(url)
    html = page.text
    return html
s = u'酒店地址：\r\n'  #u表示读取中文，\r\n为换行符
f = codecs.open("elong-address1.txt",'w','utf-8')

f.write(s)
f.write(str(list))

#for i in range(50000000,50201250):
html_str=getHtml()
html = etree.HTML(html_str)
result = html.xpath('//*[@class="h_item"]/div/div[2]/div[3]/p[2]/text()')
#print(result)
#    f.write(result+'\r\n')
for i in result:
    print(i)
    f.write(i+'\r\n')  #\r\n为换行符

f.close()
