
tries = 0
tries_left = 3
name = input('What is your name: ')
email = input('What is your email address: ')
search_char = email.find('@')
while search_char == -1:
    print('Please enter a valid email address')
    email = input('What is your email address: ')
    search_char = email.find('@')

while tries <= 3:
    miles = int(input(f'{name} how many miles would you like converted to kilometers: '))
    kilos = miles * 1.6
    while miles <= 0 and tries < 3:
        tries += 1
        tries_left -= 1
        print(f'Please enter a measurable distance, you have {tries_left} tries left.')
        miles = int(input('What is the distance: '))
    if tries_left <= 0 and miles <=0:
        print('Outside of acceptable input, you have no more attempts')
    else:
        print(f'{miles} miles is equal to {kilos:.1f} kilometers')

    far = int(input('What is the temperature: '))
    cels = (far-32)*5/9
    while far >= 1000.0 and tries < 3:
        tries += 1
        tries_left -= 1
        print(f'Please enter a reasonable temperature, you have {tries_left} tries left.')
        far = int(input('What is the temperature: '))
    if tries_left <= 0 and far >=1000.0:
        print('Outside of acceptable input, you have no more attempts')
    else: 
        print(f'{far} fahrenheit is equal to {cels:.2f} celsius')

    gal = float(input('How many gallons: '))
    liters = gal*3.9
    while gal <= 0 and tries < 3:
        tries += 1
        tries_left -= 1
        print(f'Please enter a positive volume, you have {tries_left} tries left.')
        gal = int(input('How many gallons: '))
    if tries_left <= 0 and gal <= 0:
        print('Outside of acceptable input, you have no more attempts')
    else: 
        print(f'{gal} gallons is equal to {liters:.1f} liters')

    pounds = float(input('How many pounds: '))
    kilograms = pounds*.45
    while pounds <= 0 and tries < 3:
        tries += 1
        tries_left -= 1
        print(f'Please enter a measurable weight, you have {tries_left} tries left.')
        pounds = int(input('What is the weight: '))
    if tries_left <= 0 and pounds >= 0:
        print('Outside of acceptable input, you have no more attempts')
    else: 
        print(f'{pounds} pounds is equal to {kilograms:.2f} kilograms')

    inches= float(input('How many inches: '))
    centi = inches*2.54
    while inches <= 0 and tries < 3:
        tries += 1
        tries_left -= 1
        print(f'Please enter a measurable height, you have {tries_left} tries left.')
        inches = int(input('What is the height: '))
    if tries_left <= 0 and inches <= 0:
        print('Outside of acceptable input, you have no more attempts')
    else: 
        print(f'{inches} inches is equal to {centi:.2f} centimeters')
    break

