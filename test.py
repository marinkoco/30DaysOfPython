# Get user input using input(“Enter your age: ”). 
# If user is 18 or older, give feedback: You are old enough to drive. 
# If below 18 give feedback to wait for the missing amount of years.
age = int(input('Enter your age: '))
driving_age = 18
if driving_age - age <= 0:
    print('You are old enough to learn to drive.')
else:
    print ('You need', abs(age-driving_age), 'more years to learn to drive.')