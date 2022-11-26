
person_one = ['Moris', 'male', 'australia',
              '29th January 1998', 'moris@jon.com', '01-714-4567']


person_two = ['Jordan', 'male', 'england',
              '29th March 1958', 'jordan@engl.com', '33-722-3532']

gender = person_one[1]

if gender == 'male':
    relative = 'His'
    pronoun = 'He'

else:
    relative = 'Her'
    pronoun = 'She'


sentence = f'{person_one[0]} is born in {person_one[2].title()} . {relative} date of birth {person_one[3]}. {pronoun} is available at {person_one[4]} and phone no is {person_one[5]}'


print(sentence)
