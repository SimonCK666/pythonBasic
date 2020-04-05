#
# condition.py
# @author bulbasaur
# @description 
# @created 2020-03-25T21:00:11.834Z+08:00
# @last-modified 2020-03-25T22:36:06.261Z+08:00
#

if x > 0:
    print('x is positive')

# 语句体中可出现的语句数目没有限制，但是至少得有一个。有时候，一条语句都没有的
# 语句体也是有用的（通常是为你还没写的代码占一个位子）。这种情况下，你可以使用
# pass 语句，它什么也不做
if x < 0:
    pass     # TODO: need to handle negative values


# "二选一执行" (alternative execution)
if x % 2 == 0:
    print('x is even')
else:
    print('x is odd')


# 链式条件(chained conditional)
if x < y:
    print('x is less than y')
# elif是“else if’’ 的缩写。同样地，这里只有一个分支会被执行。elif 语句的数目没有限制
elif x > y:
    print('x is greater than y')
else:
    print('x and y are equal')



# 嵌套条件(nested condi-tionals)
if x == y :
    print ( ' x andy are equ al ' )
else :
    if x < y :
        print ( ' x is less thany ' )
    else :
        print ( ' x is g r e a t e r thany ' )
