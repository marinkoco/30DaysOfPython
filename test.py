def my_name():
    fname = str(input("Input First Name:"))
    lname = str(input("Input Last Name:"))
    full_name = fname + ' ' + lname
    return full_name
print(my_name())

def square(x):
    return x * x
print(square(5))

def sum_num(n):
    total = 0
    for i in range(n+1):
        total += i
    print(total)
print(sum_num(10))
