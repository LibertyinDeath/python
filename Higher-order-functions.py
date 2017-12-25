###################################################################
# File Name: test1.py
# Author: Jewelry Zhu
# mail: jewelryzhu@v4user.com
# Created Time: 四 12/21 18:42:21 2017
#=============================================================
#!/usr/bin/python3

# -*- coding: utf-8 -*-

#f = abs             将Python自带函数abs赋值给f，即变量f指向函数abs
def add(x,y,f):     #定义高阶函数add，函数中接收abs函数作为参数
    return f(x)+f(y)    #返回值为x的应变量加上y的应变量

print(add(-5,6,abs))
