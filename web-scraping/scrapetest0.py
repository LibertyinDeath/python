#======================================
# File Name: scrapetest.py
# Author: Jewelry Zhu
# mail: jewelryzhu@v4user.com
# Created Time: 四  1/18 23:52:56 2018
#====================================
#!/usr/bin/python3
# -*- coding: utf-8 -*-


from urllib.request import urlopen

html = urlopen("http://www.baidu.com")

print(html.read())
