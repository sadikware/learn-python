# Escape Character

# print('I\'m Sadik. What\'s your name?')

# New Line and Tab

"""
    “It matters not how strait the gate,
        How charged with punishments the scroll,
    I am the master of my fate,
        I am the captain of my soul.”
"""


# print('\"It matters not how strait the gate,\n \tHow charged with punishments the scroll,\n I am the master of my fate, \n\tI am the captain of my soul.\"')


# Formatted String f'This is String'
# Dynamic Variable in String


"""
SGCL Job Circular 2022 published on the official websites www.sgcl.gov.bd. Sundarban Gas Company Limited job circular 2022 one of the best govt job circular in Bangladesh. The www.sgcl.gov.bd job circular 2022 will be best for those who want to get government jobs in BD. The Sundarban Gas Company Limited SGCL has issued a job circular for the posts of doctor, and others.

"""

# company_avv = input('Enter Company Avv: ')
# company_name = input('Enter Company name: ')
# year = int(input('Enter Published Year: '))
# website = input('Enter Website: ')
# job_type = input('Enter Job Type: ')
# job_role = input('Enter Job Role: ')


# paragraph = f'{company_avv} Job Circular {year} published on the official websites {website}. {company_name} job circular {year} one of the best {job_type} job circular in Bangladesh. The {website} job circular {year} will be best for those who want to get {job_type} jobs in BD. The {company_name} {company_avv} has issued a job circular for the posts of {job_role}, and others.'

# print(paragraph)


# Comaprison Operator - ==, !=, >, <, >=, <=

# If Else Elif

budget_bdt = int(input('Enter Your Budget (BDT): '))

if budget_bdt >= 80000:
    processor = 'Intel Core i5 12gen'
    ram = '8GB DDR4 3200Mhz'
    ssd = '512GB NVme'
    display = '15.6" inch'
    print(
        f'This Pc Processor{processor}. Here {ram} and {ssd}. This Pc  {display} LCD Soft Display Always attract Users.')

elif budget_bdt >= 60000:
    processor = 'Intel Core i5 11gen'
    ram = '8GB DDR4 3200Mhz'
    ssd = '256GB NVme'
    display = '14" inch'
    print(
        f'This Pc Processor {processor}. Here {ram} and {ssd}. This Pc  {display} LCD Soft Display Always attract Users.')

else:
    print('You should go buy a Used High Config Laptop.')

# Nested If
