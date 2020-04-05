#!/usr/bin/env python
# -*- coding:utf-8 -*-
numbers = [1, 2, 3]


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


point = Point(10, 20)
print(point.x)

# point1 = Point()
# point1.x = 10
# point1.y = 29
# print(point1.x)
# point1.draw()
# point2 = Point()
# point2.x = 1
# print(point2.x)

print('------------------')

class Person:
    def __init__(self, name,):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")


john = Person("John Smith")
john.talk()

bob = Person("Bob Smith")
bob.talk()