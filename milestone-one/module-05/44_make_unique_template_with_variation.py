
import random


person = ['Monali', 'England']


name = person[0]
location = person[1]

sentence_one_group = [
    f'This is {name}',
    f'{name} is my name',
    f'My name is {name}'
]


sentence_two_group = [
    f'I live in {location}',
    f'I reside in {location}',
    f'I was raised in {location}',
    f'{location} is place where i reside',
]


sentence_one = random.choice(sentence_one_group)

# print(sentence_one)


sentence_two = random.choice(sentence_two_group)

# print(sentence_two)

paragraph = f'{sentence_one}. {sentence_two}'

print(paragraph)
