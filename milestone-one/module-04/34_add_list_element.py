
movies = []


movies.append('Force')
movies.append('Road Sign')
movies.append('Countryside')
movies.append('King World')


# Insert Elemnent Specific Index

movies.insert(2, 'Fortune')

print(movies)


laptop_brand = []

laptop_brand.append('Asus')
laptop_brand.append('MSI')
laptop_brand.append('Dell')
laptop_brand.append('Lenovo')

laptop_brand.insert(1, 'Toshiba')


print(laptop_brand)


mobile_brand = ['Realme', 'Iphone', 'Samsung', 'Oneplus']


laptop_brand.extend(mobile_brand)

print(laptop_brand)


# Append - Add Element in last
# Insert - specific index number add element
# extend - firdt_list.extend(second_list)
