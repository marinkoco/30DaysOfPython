def find_even_numbers(n):
    evens = []
    for i in range(n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens
print(find_even_numbers(10))

def suma_nums(*nums):
    total = 0
    for i in nums:
        total += i
    return total
print(suma_nums(2,3,5))

def generate_groups (team,*args):
    print(team)
    for i in args:
        print(i)
print(generate_groups('Team-1','Ivan','Brook','David','Eyob'))

# Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(x, y):
    return x+y
print(add_two_numbers(4,3))

# Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. 
# Check if all the list items are number types. 
# If not do give a reasonable feedback.
def add_all_nums(*args):
    if all(isinstance(arg,(int,float)) for arg in args):
        return sum(args)
    else:
        return 'Error: All arguments should be numeric'
print(add_all_nums(2,3,4,5))

# Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(month):
    Autumn = ['september', 'october', 'november']
    Summer = ['jun', 'july', 'august']
    Winter = ['december', 'january', 'february']
    Spring = ['march', 'april', 'may']
    if month in Autumn:
        print(month, 'belongs to', 'Autumn')
    elif month in Summer:
        print(month, 'belongs to', 'Summer')
    elif month in Winter:
        print((month, 'belongs to', 'Winter'))
    else:
        print((month, 'belongs to', 'Spring'))
check_season('july')

# Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(list):
    list=['i','v','a','n']
    for l in list:
        print(l)
print_list(list)  

# Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
def reverse_list(arr):
    reversed_arr = []
    for i in range(len(arr)-1, -1, -1):
        reversed_arr.append(arr[i])
    return reversed_arr
arr=[1,2,3,5,6]
reverse_list(arr)

#test change


