miles = int(input('William, how many miles would you like converted to kilometers: '))
if miles >= 0.0:
    far = int(input('What is the temperature: '))
    if far <= 1000.0:
        gal = float(input('How many gallons: '))
        if gal >= 0.0:
            pounds = float(input('How many pounds: '))
            if pounds >= 0.0:
                inches= float(input('How many inches: '))
                if inches >= 0.0:
                  kilos = miles*1.6
                  cels = (far-32)*5/9
                  liters = gal*3.9
                  kilograms = pounds*.45
                  centi = inches*2.54
                  print(miles,' miles is equal to ', str(kilos), 'kilometers')
                  print(far, ' fahrenheit is equal to ', str(cels), 'celsius')
                  print(gal,' gallons is equal to ', str(liters), 'liters')
                  print(pounds,' pounds is equal to ', str(kilograms), 'kilograms')
                  print(inches,' inches is equal to ', str(centi), 'centimeters')
                else: print('Incorrect value, terminating program.')
            else: print('No negative weight, terminating program.')
        else: print('No negative volume, terminating program.')
    else: print("That's too hot, terminating program.")
else: print('No negative distance, terminating program.')


