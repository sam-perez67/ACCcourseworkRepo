tries = 0
tries_left = 3

while tries <= 3:
    miles = int(input('William, how many miles would you like converted to kilometers: '))
    kilos = miles * 1.6
    while miles <= 0 and tries < 3:
        tries += 1
        tries_left -= 1
        print('Please enter a measurable distance, you have ', tries_left, ' tries left.')
        miles = int(input('What is the distance: '))
    if tries_left <= 0 and miles <=0:
        print('Outside of acceptable input, you have no more attempts')
    else:
        print(miles,' miles is equal to ', kilos, 'kilometers')

    far = int(input('What is the temperature: '))
    cels = (far-32)*5/9
    while far >= 1000.0 and tries < 3:
        tries += 1
        tries_left -= 1
        print('Please enter a reasonable temperature, you have ', tries_left, ' tries left.')
        far = int(input('What is the temperature: '))
    if tries_left <= 0 and far >=1000.0:
        print('Outside of acceptable input, you have no more attempts')
    else: 
        print(far, ' fahrenheit is equal to ', cels, 'celsius')

    gal = float(input('How many gallons: '))
    liters = gal*3.9
    while gal <= 0 and tries < 3:
        tries += 1
        tries_left -= 1
        print('Please enter a positive volume, you have ', tries_left, ' tries left.')
        gal = int(input('How many gallons: '))
    if tries_left <= 0 and gal <= 0:
        print('Outside of acceptable input, you have no more attempts')
    else: 
        print(gal,' gallons is equal to ', liters, 'liters')

    pounds = float(input('How many pounds: '))
    kilograms = pounds*.45
    while pounds <= 0 and tries < 3:
        tries += 1
        tries_left -= 1
        print('Please enter a measurable weight, you have ', tries_left, ' tries left.')
        pounds = int(input('What is the weight: '))
    if tries_left <= 0 and pounds >= 0:
        print('Outside of acceptable input, you have no more attempts')
    else: 
        print(pounds,' pounds is equal to ', kilograms, 'kilograms')

    inches= float(input('How many inches: '))
    centi = inches*2.54
    while inches <= 0 and tries < 3:
        tries += 1
        tries_left -= 1
        print('Please enter a measurable height, you have ', tries_left, ' tries left.')
        inches = int(input('What is the height: '))
    if tries_left <= 0 and inches <= 0:
        print('Outside of acceptable input, you have no more attempts')
    else: 
        print(inches,' inches is equal to ', centi, 'centimeters')

    break





                  
                  
                  
                  
                  

            




