#======================================
# File Name: open_test.py
# Author: Jewelry Zhu
# mail: jewelryzhu@v4user.com
# Created Time: 二 12/26 12:46:41 2017
#====================================
#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests

res = requests.get('https://github.com/timeline.json')
savefile = open('itcast.html','wb')
savefile.write(res.content)
savefile.close()
