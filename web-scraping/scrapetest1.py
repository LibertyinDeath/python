#======================================
# File Name: scrapetest1.py
# Author: Jewelry Zhu
# mail: jewelryzhu@v4user.com
# Created Time: 五  1/19 00:06:30 2018
#====================================
#!/usr/bin/python3
# -*- coding: utf-8 -*-


from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/page1.html")

bsObj = BeautifulSoup(html.read())

print(bsObj.h1)
