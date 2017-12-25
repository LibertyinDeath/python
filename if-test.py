#!/usr/bin/env python
# -*- coding: utf-8 -*-

age = int(input("请输入你的年龄"))
print("")
if age<0:
    print("傻逼，输错了")
elif age < 14:
    print("太小了，再见")
elif age >28:
    print("太大了")
else:
    print ("你就是我的菜")
