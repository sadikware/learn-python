

user_1 = {
    'username': 'sadik',
    'password': '12345',
    'role': 'admin'
}

user_2 = {
    'username': 'Rahman',
    'password': 'g56gfde',
    'role': 'contributor'
}


users = [{
    'username': 'sadik',
    'password': '12345',
    'role': 'admin'
}, {
    'username': 'Rahman',
    'password': 'g56gfde',
    'role': 'contributor'
}
]


for user in users:
    # print(user['username'])
    print(user.get('username'))
