
user = {
    'id': 1,
    'first_name': 'Sadik',
    'last_name': 'Rahman',
    'username': 'admin',
    'password': '123456789',
    'role': 'admin'

}


# first_name = user['first_name']
# last_name = user['last_name']

# print(first_name, last_name)


# Latest Access Way

first_name = user.get('first_name')

print(first_name)


keys = user.keys()
print(list(keys))

values = user.values()

print(list(values))
