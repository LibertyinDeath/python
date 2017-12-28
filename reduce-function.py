#======================================
# File Name: reduce-function.py
# Author: Jewelry Zhu
# mail: jewelryzhu@v4user.com
# Created Time: 一 12/25 22:25:01 2017
#====================================
#!/usr/bin/python3
# -*- coding: utf-8 -*-

#reduce把一个函数作用在一个序列[x1,x2,x3,...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是
#reduce(f,[x1,x2,x3,x4]) = f(f(f(x1,x2),x3),x4)

#以对一个序列求和为例进行实现

from functools import reduce

def add(x,y):
    return x+y

print(reduce(add,[1,2,3,4,7,9]))

# 这里的求和用处不大，但是如果想要将[1,3,5,7,9]变换为13579这个数呢？

def fn(x,y):
    return x*10+y

print(reduce(fn,[1,3,5,7,9]))

#这个例子本身没太大用处，可以配合map，将str转为int，下面这个函数的意思是将字符串转化为数字的list，然后再通过fn函数将他们合到一起

def char2num(s):
    digits = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    return digits[s]
#print(char2num('13579'))
print(list(map(char2num,'13579')))
print(reduce(fn,map(char2num,'13579')))

#练习：利用map函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写

#首先定义一个转换后面的变成小写字母的

def up2low(s):
    if(s.isupper):
        s = s.lower()
    return s

def link1(x,y):
    return x+y

print(list(map(up2low,'MichAEl')))


print(reduce(link1,(map(up2low,'Michael'))))


def normalize(name):
#    print(name[1:])
#    reduce(link1,(map(up2low,name[1:])))
    if(name[0].islower):
        #name[0]=name[0].upper()

        return name[0].upper()+reduce(link1,(map(up2low,name[1:])))
    else:
        return name[0]+reduce(link1,(map(up2low,name[1:])))
print(normalize('micHAEl'))
