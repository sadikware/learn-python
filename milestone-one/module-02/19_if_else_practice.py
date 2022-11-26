# normal_body_temp = 98.6

# temp = float(input('Enter Your Body Temperature: '))


# if temp > normal_body_temp:
#     print('Please contact a Doctor.')

# else:
#     print('You should take rest.')


# Problem Practice 2


# Sadik is a developer in a tech company. He is very loyal man

# Zannat is a designer in a fashion company. She is very loyal woman

name = input('Enter Name: ')
gender = input('Enter Gender (M/F): ')


# profession , pronoun, person

if gender == 'M':
    profession = 'developer'
    pronoun = 'He'
    person = 'man'
    comapny_type = 'tech'

else:
    profession = 'designer'
    pronoun = 'She'
    person = 'woman'
    comapny_type = 'fashion'


print(f'{name} is a {profession} in a tech company. {pronoun} is very loyal {person}')
