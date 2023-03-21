# Dictionaries
# A dictionary is a collection of unordered, modifiable(mutable) paired (key: value) data type.

# Creating a Dictionary
# The dictionary below shows that a value could be any data types:string, boolean, list, tuple, set or a dictionary.
person = {
    'first_name': 'Ivan',
    'last_name': 'Marinkovic',
    'age': 250,
    'country': 'Serbia',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# Dictionary Length
# It checks the number of 'key: value' pairs in the dictionary.

person = {
    'first_name': 'Ivan',
    'last_name': 'Marinkovic',
    'age': 250,
    'country': 'Serbia',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
print(len(person))  # 7

# Accessing Dictionary Items
# We can access Dictionary items by referring to its key name.

person = {
    'first_name': 'Ivan',
    'last_name': 'Marinkovic',
    'age': 250,
    'country': 'Serbia',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
print(person['first_name'])  # Ivan
print(person['country'])    # Marinkovic
# ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person['skills'])
print(person['skills'][0])  # JavaScript
print(person['address']['street'])  # Space street
print(person['city'])       # Error

# Accessing an item by key name raises an error if the key does not exist.
# To avoid this error first we have to check if a key exist or we can use the get method.
# The get method returns None, which is a NoneType object data type, if the key does not exist.

person = {
    'first_name': 'Ivan',
    'last_name': 'Marinkovic',
    'age': 250,
    'country': 'Serbia',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
print(person.get('first_name'))  # Ivan
print(person.get('country'))    # Serbia
# ['HTML','CSS','JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person.get('skills'))
print(person.get('city'))   # None
print(person.get('address', {}).get('street'))  # Space street

# Adding Items to a Dictionary
person = {
    'first_name': 'Ivan',
    'last_name': 'Marinkovic',
    'age': 250,
    'country': 'Serbia',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
person['job_title'] = 'Instructor'
person['skills'].append('HTML')
person['address']['phone'] = "000-xxx"
print(person)

# Modifying Items in a Dictionary
person = {
    'first_name': 'Ivan',
    'last_name': 'Marinkovic',
    'age': 250,
    'country': 'Serbia',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
person['first_name'] = 'Johnny'
person['age'] = 252
person['address']['zipcode'] = '02220'
print(person)

# Checking Keys in a Dictionary
# We use the in operator to check if a key exist in a dictionary
# Removing Key and Value Pairs from a Dictionary
# pop(key): removes the item with the specified key name:
# popitem(): removes the last item
# del: removes an item with specified key name
person = {
    'first_name': 'Ivan',
    'last_name': 'Marinkovic',
    'age': 250,
    'country': 'Serbia',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
person.pop('first_name')        # Removes the firstname item
person['address'].pop('street')
# or
del person['address']['street']
person.popitem()                # Removes the address item
del person['is_married']        # Removes the is_married item

# Changing Dictionary to a List of Items
# The items() method changes dictionary to a list of tuples.
person = {
    'first_name': 'Ivan',
    'last_name': 'Marinkovic',
    'age': 250,
    'country': 'Serbia',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
print(person.items())

# Clearing a Dictionary
# If we don't want the items in a dictionary we can clear them using clear() method
print(person.clear())

# Deleting a Dictionary
# If we do not use the dictionary we can delete it completely
del person

# Copy a Dictionary
# We can copy a dictionary using a copy() method. Using copy we can avoid mutation of the original dictionary.
person_copy = person.copy()

# Getting Dictionary Keys as a List
# The keys() method gives us all the keys of a a dictionary as a list.
values = person.values()
print(values)
