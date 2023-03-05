# Day 2 - 30DaysOfPython Challenge
# Variables in Python
person_info = {
   'firstname':'Ivan',
   'lastname':'Marinkovic',
   'country':'Serbia',
   'city':'Belgrade'
   }
print(person_info)

# Declaring Multiple Variable in a Line
# Printing the values stored in the variables
first_name, last_name, country, age, is_married = 'Ivan', 'Marinkovic', 'Serbia', 44, True
print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)

# Use the print() and len() built-in functions
print('Hello, World!') # The text Hello, World! is an argument
print('Hello',',', 'World','!') # it can take multiple arguments, four arguments have been passed
print(len('Hello, World!')) # it takes only one argument

# Getting user input using the input() built-in function.
first_name = input('What is your name: ')
age = input('How old are you? ')

print(first_name)
print(age)

# int to float
num_int = 10
print('num_int',num_int)         # 10
num_float = float(num_int)
print('num_float:', num_float)   # 10.0

# float to int
gravity = 9.81
print(int(gravity))             # 9

# int to str
num_int = 10
print(num_int)                  # 10
num_str = str(num_int)
print(num_str)                  # '10'

# str to int or float
num_str = '10.6'
print('num_int', int(num_str))      # 10
print('num_float', float(num_str))  # 10.6

# str to list
first_name = 'Ivan'
print(first_name)               # 'Asabeneh'
first_name_to_list = list(first_name)
print(first_name_to_list)            # ['I', 'v', 'a', 'n']