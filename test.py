try:
    name = input('Your name is: ')
    birth_year = int(input('Your birth year is: '))
    age = 2023 - birth_year
    print(f'You are {name} and your age is {age}')
except TypeError:
    print('Type error occured.')
