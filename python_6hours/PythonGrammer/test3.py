#!/usr/bin/env python
# -*- coding:utf-8 -*-
numbers = [5, 3, 9, 5, 4, 6]
# Add a new item
numbers.append(20)
print(numbers)
print('---------')
numbers.insert(0, 20)
print(numbers)
print('---------')
numbers.remove(5)
print(numbers)
print('---------')
# Remove the last item in the list
numbers.pop()
print('---------')
# Check the existence of an item in one list
print(numbers.index(5))   # If the result is false, the project will create an error
# OR
print(50 in numbers)
print('---------')
print(numbers.count(5))
print('---------')
# Sort the list
numbers.sort()
print(numbers)
print('---------')
numbers.clear()

print('-------------------------')

# Can not change, add or remove an item from a List
number = (1, 2, 3, 5)