
# user_one = ['John Doe', 26, True, 'Andaman']
user_one = ['Monalisa', 99, False, 'Nikunjo']


# print(type(user_one))

# print(len(user_one))


# Access Element

# print(user_one[0])
# print(user_one[1])
# print(user_one[2])
# print(user_one[3])

# print(user_one[-1])
# print(user_one[-2])
# print(user_one[-3])
# print(user_one[-4])


# partial_list = user_one[1:3]

# print(partial_list)


# John Doe is a man of 26 years old. he lives in Andaman


name = user_one[0]
age = user_one[1]
living_place = user_one[3]
is_male = user_one[2]


if is_male:
    pronoun = 'He'
    gender = 'Man'

else:
    pronoun = 'She'
    gender = 'Woman'

sentence = f'{name} is a {gender} of {age} years old. {pronoun} lives in {living_place}'

print(sentence)
