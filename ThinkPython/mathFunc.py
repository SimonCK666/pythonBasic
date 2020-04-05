#
# mathFunc.py
# @author bulbasaur
# @description 
# @created 2020-03-15T16:31:08.301Z+08:00
# @last-modified 2020-03-15T16:45:19.955Z+08:00
#

# import statement
import math

# calculus signal_power : noise_power
signal_power = 200
noise_power = 500
ratio = signal_power / noise_power
# math include the func log to calculus the log of e is lower
decibels = 10 * math.log10(ratio)
print("The decibels are ")
print(decibels)

print('\n')

# cauculus the sin of radians
radians = 0.7
height = math.sin(radians)
print("The height is ")
print(height)


print('\n')


degrees = 45
radians = degrees / 180.0 * math.pi
math.sin(radians)
print('The radians is ')
print(radians)