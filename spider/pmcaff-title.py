#======================================
# File Name: pmcaff-title.py
# Author: Jewelry Zhu
# mail: jewelryzhu@v4user.com
# Created Time: 五 12/29 16:17:10 2017
#====================================
#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

url='http://www.pmcaff.com/feed'
res = requests.get(url)
soup = BeautifulSoup(res.text,'html5lib')
text = soup.find('div',class_='news-title').h2.a.string
print(text)
