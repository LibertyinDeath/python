#======================================
# File Name: horoscope-test.py
# Author: Jewelry Zhu
# mail: jewelryzhu@v4user.com
# Created Time: 三 12/27 12:32:08 2017
#====================================
#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

headers={        "Referer":"https://www.horoscope.com/us/horoscopes/love/horoscope-love-daily-today.aspx?sign=1&src=horo-btn-love","User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"}

url ='https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=2&src=horo-btn-sun'
res = requests.get(url)
soup = BeautifulSoup(res.text,'html5lib')
test1 = soup.find('div',class_='horoscope-content').p.string
print(test1)
