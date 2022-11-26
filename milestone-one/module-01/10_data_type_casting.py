# Currency Converter

usd = input('Enter Your USD Amount:')

print(type(usd))

usd_number = float(usd)
print(type(usd_number))

exchange_rate = 98.34

bdt = usd_number * exchange_rate

print(usd, 'is equal to', bdt, 'bdt.')
