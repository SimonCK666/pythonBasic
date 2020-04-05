#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Dictionary is to storage the key/values
customer = {
    "name": "John Smith",
    "age ": 30,
    "is_verified": True
}
print(customer["name"])
print(customer.get("birthday", "Jan 1 2000"))


print('-------------------------------')

# Face and Feeling
message = input('>')
# Split Strings with ' '
words = message.split(' ')
print(words)



print('-------------------------------')

# Users' phone numbers
phone = input("Phone: ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!")
print(output)