#
# argument_parameters.py
# @author bulbasaur
# @description 


#在函数内部，实参被赋给称作形参(parameters) 的变量。

# @created 2020-03-15T17:00:22.550Z+08:00
# @last-modified 2020-03-15T17:20:00.181Z+08:00
#

import math
# the 'bruce' is a parameters
#将实参赋给名为bruce 的形参。当函数被调用的时候，它会打印形参（无论它是什么）的值两次。
def print_twice(bruce):
    print(bruce)
    print(bruce)

print_twice('Spam')

print('\n')

print_twice(42)

print('\n')

# We can use any types of variables to be the arguments in this function
print_twice('Spam ' * 4)    # 在函数被调用之前，实参会先进行计算
print('\n')
print_twice(math.cos(math.pi))

print('\n')

# Use pure variable be the arguments
michael = 'Eric, the half a bee.'
print_twice(michael)


print('\n')
print('--------------------')
print('\n')



# Both arguments and parameters are local, just exist in the func
def cat_twice(part1, part2):
    cat = part1 + part2
    print_twice(cat)


# This func accept two argumetns, concatenates(拼接) them and print the results twices
line1 = 'Bing tiddle '
line2 = 'tiddle bang '
# call the function
cat_twice(line1, line2)
