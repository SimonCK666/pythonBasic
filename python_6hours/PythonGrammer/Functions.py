#!/usr/bin/env python
# -*- coding:utf-8 -*-


def greet_user(first_name, last_name):
    print(f"Hi {first_name} {last_name}!")
    print('Hi there!')
    print('Welcome aboard')


print("Start")
# Call the function
greet_user("John", "Mary")
print("Finish")

print('--------------')


def square(number):
    return number * number


result = square(3)
print(result)

print('----------------')

# Users' phone numbers


def phone_number(phone):
    digits_mapping = {
        "1": "One",
        "2": "Two",
        "3": "Three",
        "4": "Four"
    }
    output = ""
    for ch in phone:
        output += digits_mapping.get(ch, "!")
    return output


phone = input("Phone: ")
result = phone_number(phone)
print(result)