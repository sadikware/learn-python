
# String Concatanation


# first_name = "Sadik"
# last_name = "Rahman"


# full_name = first_name + ' ' + last_name
# print(full_name)


# full_name = first_name * 3

# print(full_name)


# name = input("Enter Your Name: ")
# age = input("Enter Your Age: ")
# height = input("Enter Your Height: ")

# desc = "My Name is " + name + ". I am " + \
#     age + " years old. I am " + height + " Inch"

# print("Hello", desc)


# Job Templates

"""

Bangladesh Red Crescent Society job circular 2022 has been published 12 Nov 2022 by authority on their official website www.bdrcs.org. Bangladesh Red Crescent Society job circular 2022 offering new job vacancy as a volunteer at their office. Bangladesh Red Crescent Society (BDRCS) are looking for new job holder.You can get all important information regarding Bangladesh Red Crescent Society BDRCS career opportunity. So lets check the BD Red Crescent Society BDRCS job circular 2022 and apply now.

"""


# institution_name = 'Bangladesh Red Crescent Society'
# published_date = '12 Nov 2022'
# website = 'www.bdrcs.org'
# institution_avv = "BDRCS"
# position = 'volunteer'

institution_name = input('Enter Your Institution Name: ')
published_date = input('Enter Your Published Date: ')
website = input('Enter Your Institution Website: ')
institution_avv = input('Enter Your Institution Avvreviation: ')
position = input('Enter Your Job Position: ')


first_line = institution_name + \
    ' job circular 2022 has been published on ' + published_date + \
    ' by authority on their official website ' + website + '. '

second_line = institution_name + \
    ' job circular 2022 offering new job vacancy as a ' + \
    position + ' at their office. '


third_line = institution_name + \
    ' (' + institution_avv + ') are looking for new job holder. You can get all important information regarding ' + \
    institution_name + ' career opportunity.'


print(first_line + second_line + third_line)
