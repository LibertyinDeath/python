#======================================
# File Name: baidutest.py
# Author: Jewelry Zhu
# mail: jewelryzhu@v4user.com
# Created Time: 三 12/27 12:06:07 2017
#====================================
#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests
import urllib.request
import urllib
from bs4 import BeautifulSoup

url = 'https://www.tarot.com/daily-love-horoscope/general/2017-12-26'
res = requests.get(url)
soup = BeautifulSoup(res.text,'html5lib')
text1 = soup.find('p',class_='js-today_interp_copy').string
print(text1)
