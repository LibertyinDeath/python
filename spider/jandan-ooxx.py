#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
res = requests.get('http://jandan.net/ooxx')
html = BeautifulSoup(res.text,"lxml")
for index, each in enumerate(html.select('#commentlist row  img')):
    with open('{}.jpg'.format(index), 'wb') as jpg:
        ijpg.write(requests.get(each.attrs['src'], stream=True).content)
