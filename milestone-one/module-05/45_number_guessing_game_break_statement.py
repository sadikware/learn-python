
# students = []

# while True:
#     name = input('Enter Student Name: ')
#     if name == 'End':
#         print(students)
#         print('Total Students: ', len(students))
#         break
#     else:
#         students.append(name)


import random

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print('Game Start and Guess a Number From 1-9')

print('*'*40)


computer_number = random.choice(numbers)

while True:
    number = int(input('What is Your Guess: '))

    if computer_number == number:
        print('Congratulations')
        break

    else:
        print('Try Again')
