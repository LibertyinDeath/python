#======================================
# File Name: dianping-test.py
# Author: Jewelry Zhu
# mail: jewelryzhu@v4user.com
# Created Time: 日  1/ 7 20:00:23 2018
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
def getHtml(num):
    url="http://www.dianping.com/search/category/1/10/p%s?aid=22435455%%2C63177252%%2C59399241%%2C23999832%%2C28425895%%2C17654577"%(num)
    page = requests.get(url)
    html = page.text
    return html
s = u'上海美食地址信息：\r\n'  #u表示读取中文，\r\n为换行符
f = codecs.open("address1.txt",'w','utf-8')

f.write(s)
f.write(str(list))

#for i in range(0,3):
html_str=getHtml(1)
html = etree.HTML(html_str)
result = html.xpath('//*[@id="shop-all-list"]/ul/li/div[2]/div[3]/span')
#print(result)
#for i in result:
#    print(i.text)
#time.sleep(0.5)
for i in result:
    print(i.text)
    f.write(i.text+'\r\n')  #\r\n为换行符

f.close()
