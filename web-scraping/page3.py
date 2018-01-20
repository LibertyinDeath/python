#======================================
# File Name: page3.py
# Author: Jewelry Zhu
# mail: jewelryzhu@v4user.com
# Created Time: 六  1/20 14:50:44 2018
#====================================
#!/usr/bin/python3
# -*- coding: utf-8 -*-


from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html,"lxml")

print("打印子标签")
for child in bsObj.find("table",{"id":"giftList"}).children:
    print(child)
    
print("打印兄弟标签")

for sibling in bsObj.find("table",{"id":"giftList"}).tr.next_siblings:
    print(sibling)


print("打印父标签")

print(bsObj.find("img",{"src":"../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())
