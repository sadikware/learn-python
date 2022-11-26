# Make Simple Template From List

import random
car = ['Volvo', 'white', 'elctric', 2022]


# Volvo is the most attractive electric car in 2022. There are black and white colors are available. If the is black , you should clean it weekly. if the car is white, you should clean it daily.


company = car[0]
color = car[1]
types = car[2]
year = car[3]

if color == 'black':
    clean = 'weekly'

elif color == 'white':
    clean = 'daily'

paragraph = f'{company} is the most attractive {types} car in {year}. There are black and white colors are available. If the is {color} , you should clean it {clean}. '

# print(paragraph)


# Multiple List

bio_data = [['Arif Bin Habib', 'Author', 'Dhaka'],
            ['Arif Azad', 'Author', 'Chittagong'],
            ['Mizanur Rahman', 'PHD Holder', 'Malyesia'],
            ['Tarik Zamil', 'PHD Holder', 'Pakistan']]

i = 0

while i < len(bio_data):
    single_bio_data = bio_data[i]
    # print(single_bio_data)
    i = i+1

    name = single_bio_data[0]
    title = single_bio_data[1]
    address = single_bio_data[2]

    if title == 'Author':
        review = 'Excellent Writer'

    elif title == 'PHD Holder':
        review = 'We expect more valuable research'

    sentence = f'{name} is the best {title} in current world. He lives in {address}. Some Reviews - {review}'

    print(sentence)


# ludu game


ludu_point = [1, 2, 3, 4, 5, 6]

new_point = random.choice(ludu_point)

print('New Point:', new_point)


# Random Every Time Unique item
