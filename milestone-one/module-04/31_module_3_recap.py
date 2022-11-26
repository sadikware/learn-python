# A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years or salary greater than 20000.
# Ask user for their salary and year of service and print the net bonus amount.


user_salary = int(input('Enter Salary: '))
user_service_year = float(input('Enter Service Year: '))

if user_service_year > 5 or user_salary >= 20000:
    bonus = 0.05
    net_salary = user_salary + user_salary * bonus
    print('Your Net Salary With Bonus', net_salary)

else:
    print('Your Salary', user_salary)
