phonebook = {
    'John': 1111111,
    'Jack': 2222222,
    'Jill': 3333333
    }

# write your code here
phonebook['Jake'] = 4444444
del phonebook['Jill']
# phonebook.pop('Jill')

# testing code
if "Jake" in phonebook:
    print("Jake is listed in the phonebook.")
if 'Jill' not in phonebook:
    print('Jill is not listed in the phonebook.')
