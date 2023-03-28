# Python Error Types
# When we write code it is common that we make a typo or some other common error. 
# If our code fails to run, the Python interpreter will display a message, containing feedback with information on where the problem occurs and the type of an error. 
# It will also sometimes gives us suggestions on a possible fix. 
# Understanding different types of errors in programming languages will help us to debug our code quickly and also it makes us better at what we do.
# 
# Let us see the most common error types one by one. First let us open our Python interactive shell. Go to your you computer terminal and write 'python'. The python interactive shell will be opened.
# 
# SyntaxError
# Example 1: SyntaxError

# >>> print 'hello world'
#   File "<stdin>", line 1
#     print 'hello world'
#                       ^
# SyntaxError: Missing parentheses in call to 'print'. Did you mean print('hello world')?

# NameError
# Example 1: NameError

# >>> print(age)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'age' is not defined

# IndexError
# Example 1: IndexError

# >>> numbers = [1, 2, 3, 4, 5]
# >>> numbers[5]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: list index out of range
# In the example above, Python raised an IndexError, because the list has only indexes from 0 to 4 , so it was out of range.

# ModuleNotFoundError
# Example 1: ModuleNotFoundError

# >>> import maths
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ModuleNotFoundError: No module named 'maths'
# In the example above, I added an extra s to math deliberately and ModuleNotFoundError was raised. Lets fix it by removing the extra s from math.

# AttributeError
# Example 1: AttributeError

# >>> import maths
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ModuleNotFoundError: No module named 'maths'
# >>> import math
# >>> math.PI
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: module 'math' has no attribute 'PI'
# Instead of pi, I tried to call a PI function from maths module. It raised an attribute error, it means, that the function does not exist in the module. Lets fix it by changing from PI to pi.

# KeyError
# Example 1: KeyError

# >>> users = {'name':'Asab', 'age':250, 'country':'Finland'}
# >>> users['name']
# 'Asab'
# >>> users['county']
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 'county'
# There was a typo in the key used to get the dictionary value. so, this is a key error.

# TypeError
# Example 1: TypeError

# >>> 4 + '3'
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# In the example above, a TypeError is raised because we cannot add a number to a string. First solution would be to convert the string to int or float. Another solution would be converting the number to a string (the result then would be '43'). 

# ImportError
# Example 1: TypeError

# >>> from math import power
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ImportError: cannot import name 'power' from 'math'
# There is no function called power in the math module, it goes with a different name: pow.
# >>> from math import pow
# >>> pow(2,3)
# 8.0

# ValueError

# >>> int('12a')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: invalid literal for int() with base 10: '12a'

# ZeroDivisionError

# >>> 1/0
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ZeroDivisionError: division by zero
