#
# turtle_mypolygon.py
# @author bulbasaur
# @description 
# @created 2020-03-15T17:51:33.031Z+08:00
# @last-modified 2020-03-25T20:54:47.609Z+08:00
#

import turtle
bab = turtle.Turtle()
#print(bab)
turtle.mainloop()

# go forward
bab.fd(100)
# go left
bab.lt(90)

bab.fd(100)


# for Loop encapsulation(封装)
def sqare(t):
    t.fd(100)
    t.lt(90)

sqare(bab)


# function generalization(泛化): 为函数增加一个形参被称作泛化（generalization），因为这使得函数更通用
# Add a parameter in func sqare
def polygon(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)
    
sqare(bab, 100)



# 画任意正多边形
def polygon(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)

polygon(bab, 7, 70)        # 画了一个边长为70的七边形



# 接口设置

# 是编写接受半径r 作为形参的circle 函数。下面是一个使用polygon 画一个 50 边形的简单解法
import math
def circle(t, r):
    # 计算圆的周长
    circumference = 2 * math.pi *r
    n = 50
    length = circumference / n
    polygon(t, n, length)

# 函数的接口（interface）是一份关于如何使用该函数的总结
# 所有的文档字符串都是三重引号（triple-quoted）字符串，也被称为多行字符串，因为三重引号允许字符串超过一行。
