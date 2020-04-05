#!/usr/bin/env python
# -*- coding:utf-8 -*-
a = "Hello World"
print(a)

# String is an array
print(a[0])

# Slicing
print(a[2:5])  # 裁切从位置2到位置5的字符（不包括）

# Length
print(len(a))

# Method
# lower() 返回小写的字符串
print(a.lower())
# upper() 返回大写的字符串
print(a.upper())
# replace()
print(a.replace("World","Python"))


# Check String
# 检查txt中是否有短语lua
txt = "China is a great country"
x = "lua" in txt
print(x)

# Connection
age = 18
txt = "My age is {0}"   # 使用format()方法格式化变量，并将它们放在占位符 {} 所在的字符串中
print(txt.format(age))


# Boolean
print(2 > 3)
print(8 == 1)
b = 299
c = 33

if b > c:
    print("b is lager than c")
else:
    print("b is smaller than c")

# Evaluate Values and Variables
print(bool(b))