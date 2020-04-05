#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Python Collection (Array)

# List: 有序且可更改的集合
thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist[0] = "orange"  # Change list elements
print(thislist)
print(thislist[1])  # Access List
print(thislist[-1])

# Loop Through the list
for x in thislist:
    print(x)


# Check
if "banana" in thislist:
    print("Yes")
else:
    print("No")

# Length
print(len(thislist))

# Add items
thislist.append("peach")
print(thislist)
thislist.insert(1, "peach")
print(thislist)
