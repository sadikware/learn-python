# USER CHECKER

user_name = 'sadik'
password = '123456'


input_user_name = input('Enter Username: ')
input_password = input('Enter Password: ')

if input_user_name == user_name and input_password == password:
    print('Login Successfully')

else:
    print('Something Went Wrong')
