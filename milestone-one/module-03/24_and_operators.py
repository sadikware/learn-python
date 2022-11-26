

mark = int(input('Enter Your Mark: '))


if mark >= 80 and mark <= 100:
    print('A+')

elif mark >= 70 and mark <= 79:
    print('A')

elif mark < 69 and mark >= 0:
    print('You are failed')
else:
    print('Invalid Number')
