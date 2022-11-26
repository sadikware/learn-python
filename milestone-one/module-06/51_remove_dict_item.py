

car = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 2000,
    'color': 'Black'

}


print(car.get('year'))


# Update

car.update({'color': 'Fog Blue'})

print(car)


# Remove

car.pop('color')

print(car)

car.pop('year')

print(car)
