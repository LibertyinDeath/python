#======================================
# File Name: waranpeace.py
# Author: Jewelry Zhu
# mail: jewelryzhu@v4user.com
# Created Time: 六  1/20 13:37:59 2018
#====================================
#!/usr/bin/python3
# -*- coding: utf-8 -*-


#首先抓取整个页面，然后创建一个BeautifulSoup对象

from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html,"lxml")

# 然后我们通过BeautifulSoup对象用findAll函数抽取只包含在<span class="green"></span>标签里面的文字，这样就会得到一个人物名称的Python列表（findAll是一个非常灵活的函数，我们会经常遇到它）

namelist = bsObj.findAll("span",{"class":"green"})
print("打印namelist的长度")
print(len(namelist))
print("打印namelist")
print(namelist)
for name in namelist:
    print(name.get_text())


# get_text()会把你正在处理的html文档中的所有标签都清除掉，然后返回一个只包含文字的字符串
print("打印包含the prince 的namelist的长度")
namelist1 = bsObj.findAll(text="the prince")
print(len(namelist1))
print("打印所有关键字为text的标签")
ALLText = bsObj.findAll(id="text")
print(ALLText[0].get_text())
