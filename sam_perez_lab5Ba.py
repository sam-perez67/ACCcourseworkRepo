import lab5bmodule

def main():
    tries = 0
    tries_left = 3
    miles = int(input('Hello William, enter number of miles: '))
    while tries < 3 and miles <= 0:
        tries += 1
        tries_left -= 1
        print('Please enter a measurable distance, you have ', tries_left, ' tries left.')
        miles = int(input('What is the distance: '))
    if tries_left <= 0 and miles <=0:
        print('Outside of acceptable input, you have no more attempts')
    else:
        lab5bmodule.milesToKm(miles)
    tries = 0
    tries_left = 3
    far = int(input('What is the temperature: '))
    while far >= 1000.0 and tries < 3:
        tries += 1
        tries_left -= 1
        print('Please enter a reasonable temperature, you have ', tries_left, ' tries left.')
        far = int(input('What is the temperature: '))
    if tries_left <= 0 and far >=1000.0:
        print('Outside of acceptable input, you have no more attempts')
    else: 
        lab5bmodule.fahToCel(far)
    tries = 0
    tries_left = 3
    gal = float(input('How many gallons: '))
    while gal <= 0 and tries < 3:
        tries += 1
        tries_left -= 1
        print('Please enter a positive volume, you have ', tries_left, ' tries left.')
        gal = int(input('How many gallons: '))
    if tries_left <= 0 and gal <= 0:
        print('Outside of acceptable input, you have no more attempts')
    else:
        lab5bmodule.galToLit(gal)
    tries = 0
    tries_left = 3
    pounds = float(input('How many pounds: '))
    while pounds <= 0 and tries < 3:
        tries += 1
        tries_left -= 1
        print('Please enter a measurable weight, you have ', tries_left, ' tries left.')
        pounds = int(input('What is the weight: '))
    if tries_left <= 0 and pounds <= 0:
        print('Outside of acceptable input, you have no more attempts')
    else: 
        lab5bmodule.poundsToKg(pounds)
    tries = 0
    tries_left = 3
    inches= float(input('How many inches: '))
    while inches <= 0 and tries < 3:
        tries += 1
        tries_left -= 1
        print('Please enter a measurable height, you have ', tries_left, ' tries left.')
        inches = int(input('What is the height: '))
    if tries_left <= 0 and inches <= 0:
        print('Outside of acceptable input, you have no more attempts')
    else: 
        lab5bmodule.inchesToCm(inches)

main()