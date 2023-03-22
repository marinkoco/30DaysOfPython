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
for key, value in person['address'].items():
    if key == 'street':
        print(key + ':', value)


for i in range(1,8):
    print('#' * i)

for i in range(1,8):
    print('#' * 8)

for i in range(0,11):
    print(i, 'x', i, '=', i*i)

# Use for loop to iterate from 0 to 100 and print the sum of all numbers.
total = 0
for i in range(101):
    total = total + i
print(total)