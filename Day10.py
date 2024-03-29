# Loops

# While Loop
# We use the reserved word while to make a while loop. 
# It is used to execute a block of statements repeatedly until a given condition is satisfied. 
# When the condition becomes false, the lines of code after the loop will be continued to be executed.
count = 0
while count < 5:
    print(count)
    count = count + 1
#prints from 0 to 4

# In the above while loop, the condition becomes false when count is 5. 
# That is when the loop stops. 
# If we are interested to run block of code once the condition is no longer true, we can use else.
count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)

# Break and Continue - Part 1
# Break: We use break when we like to get out of or stop the loop.
count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break
# Continue: With the continue statement we can skip the current iteration, and continue with the next:
count = 0
while count < 5:
    if count == 3:
        continue
    print(count)
    count = count + 1

# For Loop
# A for keyword is used to make a for loop, similar with other programming languages, but with some syntax differences. 
# Loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
numbers = [0,1,2,3,4,5]
for number in numbers: # number is temporary name to refer to the list's items, valid only inside this loop
    print(number)       # the numbers will be printed line by line, from 0 to 5

# For loop with string
language = 'Python'
for letter in language:
    print(letter)

for i in range(len(language)):
    print(language[i])

# For loop with tuple
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)

# For loop with dictionary Looping through a dictionary gives you the key of the dictionary.
person = {
    'first_name':'Ivan',
    'last_name':'Marinkovic',
    'age':250,
    'country':'Serbia',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02220'
    }
}
for key in person:
    print(key)

for key, value in person.items():
    print(key, value) # this way we get both keys and values printed out

# Loops in set
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)

# Break and Continue - Part 2
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        break
# Continue: We use continue when we like to skip some of the steps in the iteration of the loop.
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print("loop's end") # for short hand conditions need both if and else statements
print('outside the loop')

# The Range Function
# The range() function is used list of numbers. 
# The range(start, end, step) takes three parameters: starting, ending and increment. 
# By default it starts from 0 and the increment is 1. 
# The range sequence needs at least 1 argument (end). 
# Creating sequences using range
lst = list(range(11)) 
print(lst) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
st = set(range(1, 11))    # 2 arguments indicate start and end of the sequence, step set to default 1
print(st) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

lst = list(range(0,11,2))
print(lst) # [0, 2, 4, 6, 8, 10]
st = set(range(0,11,2))
print(st) #  {0, 2, 4, 6, 8, 10}

for number in range(11):
    print(number)   # prints 0 to 10, not including 11

# Nested For Loop
person = {
    'first_name': 'Ivan',
    'last_name': 'Marinkovic',
    'age': 250,
    'country': 'Serbia',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02220'
    }
}
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)
# or if you want to descend in and print key:value from nested json
for key, value in person['address'].items():
    if key == 'street':
        print(key + ':', value)

# For Else
# If we want to execute some message when the loop ends, we use else.
for number in range(11):
    print(number)   # prints 0 to 10, not including 11
else:
    print('The loop stops at', number)

# Pass
# In python when statement is required (after semicolon), but we don't like to execute any code there, we can write the word pass to avoid errors.
#  Also we can use it as a placeholder, for future statements.
for number in range(6):
    pass

