#======================================
# File Name: filter-test.py
# Author: Jewelry Zhu
# mail: jewelryzhu@v4user.com
# Created Time: 四 12/28 14:15:23 2017
#====================================
#!/usr/bin/python3
# -*- coding: utf-8 -*-

#filter的作用是把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
def is_odd(n):
    return n%2 == 1  #如果为偶数，则1

print(list(filter(is_odd,[1,2,4,5,6,9,10,15])))

#把一个序列中的空字符串删掉：

def not_empty(s):
    return s and s.strip()

print(list(filter(not_empty,['A','','B',None,'C',' '])))
