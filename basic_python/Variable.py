#!/usr/bin/env python
# -*- coding:utf-8 -*-

import random  # 导入随机数random模块

# python variables
a = 3   # a is of type int
b = 2.3
c = 1j  # c is of type complex
# 指定变量的数据类型
d = int(23)
e = float(4.6)
f = str("s2")
x = "Steve"  # x is of type String
y = float(a)  # 将整数转换为浮点数
z = complex(b)  # 将float转换为复数
print(x)
print(y)
print(z)
print(d)
print(e)
print(f)


def myfunc():
    global x   # global variable
    print("Python is " + x)


myfunc()


# random随机数: 显示 1 到 9 之间的随机数
print(random.randrange(1,10))