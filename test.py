nameask = True

names = []
while nameask:
    name = input('Please enter your name: ')
    try:
        if name.lower() == 'no':
            nameask = False
        else: names.append(name)
    except:
        print('Please provide an actual name.')
    print('Type no when you are done.')

print('The names you have provided are the following: ')
for name in names:
    print(name)
