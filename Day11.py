# Functions
# Declaring and Calling a Function
# When we make a function, we call it declaring a function.
# When we start using the it, we call it calling or invoking a function. 
# Function can be declared with or without parameters.
# syntax
# Declaring a function
# Function without Parameters
def generate_full_name ():
    first_name = 'Ivan'
    last_name = 'Marinkovic'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)
generate_full_name () # calling a function

def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)
add_two_numbers()

# Function Returning a Value - Part 1
# Function can also return values, if a function does not have a return statement, the value of the function is None. 
# Let us rewrite the above functions using return. 
# From now on, we get a value from a function when we call the function and print it.
def generate_full_name ():
    first_name = 'Ivan'
    last_name = 'Marinkovic'
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print(generate_full_name())

def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    return total
print(add_two_numbers())

# Function with Parameters
# In a function we can pass different data types(number, string, boolean, list, tuple, dictionary or set) as a parameter
# Single Parameter: If our function takes a parameter we should call our function with an argument
def greetings (name):
    message = name + ', welcome to Python for Everyone!'
    return message

print(greetings('Ivan'))

def add_ten(num):
    ten = 10
    return num + ten
print(add_ten(90))

def square_number(x):
    return x * x
print(square_number(2))

def area_of_circle (r):
    PI = 3.14
    area = PI * r ** 2
    return area
print(area_of_circle(10))

def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total+=i
    print(total)
sum_of_numbers(10) # 55
sum_of_numbers(100) # 5050

# Two Parameter: A function may or may not have a parameter or parameters. 
# A function may also have two or more parameters. 
# If our function takes parameters we should call it with arguments. 
# Let us check a function with two parameters:
def generate_full_name (first_name, last_name):
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print('Full Name: ', generate_full_name('Ivan','Marinkovic'))

def sum_two_numbers (num_one, num_two):
    sum = num_one + num_two
    return sum
print('Sum of two numbers: ', sum_two_numbers(1, 9))

def calculate_age (current_year, birth_year):
    age = current_year - birth_year
    return age

print('Age: ', calculate_age(2021, 1819))

def weight_of_object (mass, gravity):
    weight = str(mass * gravity)+ ' N' # the value has to be changed to a string first
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100, 9.81))

# Passing Arguments with Key and Value
# If we pass the arguments with key and value, the order of the arguments does not matter.
def print_fullname(firstname, lastname):
    space = ' '
    full_name = firstname  + space + lastname
    print(full_name)
print_fullname(firstname = 'Ivan', lastname = 'Marinkovic')

def add_two_numbers (num1, num2):
    total = num1 + num2
    return total
print(add_two_numbers(num2 = 3, num1 = 2)) # Order does not matter

# Function Returning a Value - Part 2
