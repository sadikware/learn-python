# Sadik is a developer in a tech company. He is very loyal man

# Monalisa is a designer in a fashion company. She is very loyal woman

name = input('Enter Name: ')
gender = input('Enter Gender (M/F): ')


# profession , pronoun, person

if gender == 'M':
    profession = 'developer'
    pronoun = 'He'
    person = 'man'
    comapny_type = 'tech'
    print(f'{name} is a {profession} in a tech company. {pronoun} is very loyal {person}')

elif gender == 'F':
    profession = 'designer'
    pronoun = 'She'
    person = 'woman'
    comapny_type = 'fashion'
    print(f'{name} is a {profession} in a tech company. {pronoun} is very loyal {person}')


else:
    print('Person Detecting Failed')


#  ODD EVEN ZERO

number = int(input('Enter Your Number: '))

if number == 0:
    print(number, 'Number is Zero.')

elif number % 2 == 0:
    print(number, 'Number is Even.')

else:
    print(number, 'Number is Odd.')


# GPA Calculator

mark = int(input('Enter Your Mark: '))

if mark >= 80:
    print('A+')

elif mark >= 70:
    print('A')
elif mark >= 60:
    print('A-')
elif mark >= 50:
    print('B')
elif mark >= 40:
    print('C')
elif mark >= 33:
    print('D')

else:
    print('Fail')
