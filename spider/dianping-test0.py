#======================================
# File Name: dianping-test0.py
# Author: Jewelry Zhu
# mail: jewelryzhu@v4user.com
# Created Time: 日  1/ 7 20:28:24 2018
#====================================
#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

url='http://www.dianping.com/search/category/1/10/p50?aid=22435455%%2C59399241%%2C23999832%%2C45829550%%2C63177252%%2C24732947'
res = requests.get(url)
soup = BeautifulSoup(res.text,'html5lib')
text = soup.find('div',class_='tag-addr').span.string
print(text)
