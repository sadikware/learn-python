person_one = ['Moris', 'male', 'australia',
              '29th January 1998', 'moris@jon.com', '01-714-4567']


person_two = ['Monali', 'female', 'england',
              '29th March 1958', 'monali@engl.com', '33-722-3532']


person = [['Moris', 'male', 'australia', '29th January 1998', 'moris@jon.com', '01-714-4567'],

          ['Monali', 'female', 'england', '29th March 1958',
              'monali@engl.com', '33-722-3532'],

          ['Smith', 'male', 'Norway', '23th April 1938',
              'smith@norw.com', '43-543-3535'],

          ['James', 'male', 'Finland', '11th May 1878',
              'james@finl.com', '99-111-6543'],

          ['Candy', 'female', 'Ireland', '17th May 1777', 'candy@irel.com', '22-111-6522']]

# print(person[1][1])

# Moris is born in Australia . His date of birth 29th January 1998. He is available at moris@jon.com and phone no is 01-714-4567


i = 0

while i < len(person):
    single_person = person[i]

    # print(single_person)

    name = single_person[0]
    gender = single_person[1]
    country = single_person[2]
    dob = single_person[3]
    email = single_person[4]
    phone = single_person[5]

    if gender == 'male':
        relative = 'His'
        pronoun = 'He'

    elif gender == 'female':
        relative = 'Her'
        pronoun = 'She'

    sentence = f'{name} is born in {country} . {relative} date of birth {dob}. {pronoun} is available at {email} and phone no is {phone}'

    print(sentence)

    i = i+1
