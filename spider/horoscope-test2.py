#======================================
# File Name: horoscope-test2.py
# Author: Jewelry Zhu
# mail: jewelryzhu@v4user.com
# Created Time: 三 12/27 17:01:30 2017
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
    url ="http://www.pmcaff.com/feed?sort_by=1&page=%s"%num
    page = requests.get(url)
    html = page.text
    return html
s = u'pmcaff标题：\r\n'  #u表示读取中文，\r\n为换行符
f = codecs.open("title0.txt",'w','utf-8')

f.write(s)
f.write(str(list))

for i in range(0,18):
    html_str=getHtml(i)
    html = etree.HTML(html_str)
    result = html.xpath('//*[@id="artList"]/li/div/h2/a')
    time.sleep(0.5)
    for i in result:
        f.write(i.text+'\r\n')  #\r\n为换行符

f.close()

#result = html.xpath('//*[@class="news-title"]/div')
#	date   = html.xpath('//*[@class="horoscope-content"]/p/b/text()')
#新建一个表
#workbook = xlsxwriter.Workbook('Demo1.xlsx')
#新建一个表对象
#worksheet = workbook.add_worksheet()
#row = 1
#for results in result:
#    print(results.text)
#row = 0
  #  writeExcel(results.text)
 #   row +=1
 #   time.sleep(0.5)
#workbook.close()


