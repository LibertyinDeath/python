#======================================
# File Name: liepin-test.py
# Author: Jewelry Zhu
# mail: jewelryzhu@v4user.com
# Created Time: 日  1/ 7 21:54:12 2018
#====================================
#!/usr/bin/python3
# -*- coding: utf-8 -*-

#!/usr/bin/python
# -*- coding: UTF-8 -*-
# -*- coding: GBK -*-
import requests
import pymysql
db = pymysql.connect(user = 'root', password = '',host ='127.0.0.1',database = 'TESTDB')
cur=db.cursor()
#c="data-address"
#with db:
cur.execute('SELECT id FROM company2 WHERE `place` IS NULL')
IDs=cur.fetchall()
for ID in IDs:
place = ""
i=1
flag=0
r = requests.get('https://www.liepin.com/company/'+str(ID[0]))
if 'data-address' in r.content:
    f=r.content.index(c)
      #print r.content[f:f+14]
     while(1):
        place=place+r.content[f+13+i]
        if '"' == r.content[f+13+i]:
        break
    i=i+1
if place=='"':
place="未在猎聘登记地址 "
cur.execute('UPDATE company2 SET `place` = %s WHERE `id` = %s',[place[0:-1],ID[0]])
db.close()
