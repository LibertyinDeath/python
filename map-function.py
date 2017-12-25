#======================================
# File Name: map-function.py
# Author: Jewelry Zhu
# mail: jewelryzhu@v4user.com
# Created Time: 一 12/25 22:09:35 2017
#====================================
#!/usr/bin/python3
# -*- coding: utf-8 -*-

#map函数接收两个参数，一个是函数，一个是iterator（迭代器），map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回

def f(x):
    return x*x

r = map(f,[1,2,3,4,5,6,7,8,9])

print(list(r))

#其作用等同于

L = []
for n in [1,2,3,4,5,6,7,8,9]:
    L.append(f(n))

print(L)

#但是只使用循环并不能看出“把f(x)作用在list的每一个元素并把结果生成一个新的list”

#map还可以计算任意复杂的函数，比如把这个list所有的数字转为字符串

print(list(map(str,[1,2,3,4,5,6,7,8,9])))


