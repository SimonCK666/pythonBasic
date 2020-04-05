#!/usr/bin/env python
# -*- coding:utf-8 -*-
import math

print('hello world')

print('o----')
print(' ||||')

first = 'John'
last = 'Smith'
msg = f'{first} [{last}] is a coder'
print(msg)

course = 'Python for beginners'
print(len(course))
print(course)
print(course.upper())
print(course.lower())
print(course.find('o'))
print(course.replace('beginners', 'Absolute Beginners'))
print('Python' in course)

print(10 + 18)
print(10 / 3)
print(10 % 3)
# Important Operator
print(10 ** 3)  # exponentiation
x = 10
x += 3  # --> x = x +3
print(x)
y = 10 + 3 * 2 ** 2
print(y)  # result: 22
print(round(2.33))
print(abs(-223))
print(math.ceil(2.9))    # result 3
print(math.floor(2.8))   # result 2

is_hot = False
is_cold = False
if is_hot:
    print("It's a hot day")
elif is_cold:
    print("It's a cold day")
else:
    print("It's a lovely day")
print("Enjoy your day")

price = 1000000
has_high_income = True
has_good_credit = True
has_criminal_record = False
if has_good_credit and not has_criminal_record:
    print("Eligible for loan hahaha")
if has_good_credit and has_high_income:
    print("Eligible for loan")
    if has_good_credit:
        down_payment = 0.1 * price
    else:
        down_payment = 0.2 * price
print(f"Down payment: ${down_payment}")

temperature = 30
if temperature > 30:
    print("It's a hot day")
else:
    print("It's not a hot day")

name = "J"
print(len(name))
if len(name) < 3:
    print("Name must be at least 3 characters")
elif len(name) > 50:
    print("Name must be a maximum of 50 characters")
else:
    print("Name looks good")


i = 1
while i <= 5:
    print('*' * i)
    i += 1
print("Done")


secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print('You won!')
        break
else:
    print('Sorry, you failed!')


weight = int(input('Weight: '))
unit = input('(L)bs or (K)g:')
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} kilos")
else:
    converted = weight / 0.45
    print(f"You are {converted} pounds")