#!/usr/bin/env python
# -*- coding:utf-8 -*-
for item in 'Python':
    print(item)

print("---------------")

for items in ["Mike", "John", "Sarah"]:
    print(items)

print("---------------")

for item2 in range(10):
    print(item2)

print("---------------")

for item3 in range(5, 10):
    print(item3)

print("--------------")

for item4 in range(5, 10, 2):
    print(item4)

print("---------------")

#Nested Loop
for x in range(4):
    for y in range(3):
        print(f'({x}, {y})')

print("---------------")

# Draw a F
numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)

print("---------------")

names = ['John', 'Mike', 'Mosh', 'Sarash', 'Mary']
print(names)
names[0] = 'Jon'
print(names[-1])
print(names[2:])
print(names[2:4])

print("---------------")

number = [3, 4, 7, 5, 2, 6]
max = number[0]
for num in number:
    if num > max:
        max = num
print(max)

print("---------------")

# Make a matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[0][1])
print("---")
# Through the array
for row in matrix:
    for item6 in row:
        print(item6)