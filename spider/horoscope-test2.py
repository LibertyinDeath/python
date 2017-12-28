#======================================
# File Name: horoscope-test2.py
# Author: Jewelry Zhu
# mail: jewelryzhu@v4user.com
# Created Time: 三 12/27 17:01:30 2017
#====================================
#!/usr/bin/python3
# -*- coding: utf-8 -*-

import urllib
import re
from lxml import etree
import requests

def getHtml(num):
	url = "https://www.horoscope.com/us/horoscopes/love/horoscope-archive.aspx?sign=2&laDate=201712%s"%num
	page = requests.get(url)
	html = page.read()
	return html


for i in range(10,30):
	html_str = getHtml(i)
	html = etree.HTML(html_str)
	result = html.xpath('//*[@class="horoscope-content"]/p/text()')
	date   = html.xpath('//*[@class="horoscope-content"]/p/b/text()')
	print(date[0]+result[1])
