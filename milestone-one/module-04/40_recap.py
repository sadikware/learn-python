# Create List
subject = ['Bangla', 'English', 'Arabic']

# Access List Element
subject[0]
subject[1]

# Change or Update List Element
subject[0] = 'Urdu'

# Add List Element
subject.append('Adding')
subject.insert(0, 'Adding 0')

# Remove List Element
subject.remove('English')
subject.pop()
subject.pop(2)

# Sort List Element
subject.sort()
subject.sort(reverse=True)

# Join List Element
name_char = ['s', 'a', 'd', 'i', 'k']
name_char = ''.join(name_char)
print(name_char)

# While Loop
i = 1
while i <= 10:
    print('Class Roll: ', i)
    i = i + 1
