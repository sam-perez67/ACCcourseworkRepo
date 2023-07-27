milesToKilo = 1
fahToCels = 2
galToLiter = 3
poundsToKilo = 4
inToCm = 5

def main():
     name = input('What is your name?: ')
     for x in range(10):
        try:
            menu_choice = [1,2,3,4,5]

            print('Enter 1 to convert miles to kilometers')
            print('Enter 2 to convert fahrenheit to celsius')
            print('Enter 3 to convert gallons to liters')
            print('Enter 4 to convert pounds to kilograms')
            print('Enter 5 to convert inches to centimeters')

            choice = int(input('Hello ' + name + ' what would you like to convert?: '))
            while choice not in menu_choice:
                raise Exception
            
        except Exception:
            print('Please enter a valid menu choice')
            choice = int(input('Hello ' + name + ' what would you like to convert?: '))

        if choice == milesToKilo:
            milesToKm()
        elif choice == fahToCels:
            fahToCel()
        elif choice == galToLiter:
            galToLit()
        elif choice == poundsToKilo:
            poundsToKg()
        elif choice == inToCm:
            inchesToCm()
        else:
            print('Are you sure you entered a valid number?')

def milesToKm():
        try:
            miles = float(input('How many miles: '))
            if miles <= 0:
                print('Please enter a positive distance')

            if miles > 0:
                outfile = open('conversion.txt', 'a')
                outfile.write(str(miles) + ' miles is equal to ')
                mTK = miles * 1.6
                outfile.write(str(mTK) + ' kilometers\n')
                outfile.close()
                print(miles,' miles is equal to ', mTK, 'kilometers')
        except Exception as err:
            print('Error', err)
               
def fahToCel():
        try:
            temp = float(input('What is the temperature?: '))
            if temp >= 1000:
                print('Please enter a cooler temperature')

            if temp < 1000:
                outfile = open('conversion.txt', 'a')
                outfile.write(str(temp) + ' fahrenheit is equal to ')
                fTC = (temp-32)*5/9
                outfile.write(str(fTC) + ' celsius\n')
                outfile.close()
                print(temp, ' fahrenheit is equal to ', fTC, 'celsius')
        except Exception as err:
            print('Error', err)

def galToLit():
        try:
            gal = float(input('How many gallons: '))
            if gal <= 0:
                print('Please enter a positive volume')

            if gal > 0:
                outfile = open('conversion.txt', 'a')
                outfile.write(str(gal) + ' gallons is equal to ')
                liters = gal*3.9
                outfile.write(str(liters) + ' liters\n')
                outfile.close()
                print(gal,' gallons is equal to ', liters, 'liters')
        except Exception as err:
            print('Error', err)

def poundsToKg():

        try:
            pounds = float(input('How many pounds: '))
            if pounds <= 0:
                print('Please enter a positive weight')

            if pounds > 0:
                outfile = open('conversion.txt', 'a')
                outfile.write(str(pounds) + ' pounds is equal to ')
                kilograms = pounds*.45
                outfile.write(str(kilograms) + ' kilograms\n')
                outfile.close()
                print(pounds,' pounds is equal to ', kilograms, 'kilograms')
        except Exception as err:
            print('Error', err)

def inchesToCm():
        try:
            inches = float(input('How many inches: '))
            if inches <= 0:
                print('Please enter a positive distance')

            if inches > 0:
                outfile = open('conversion.txt', 'a')
                outfile.write(str(inches) + ' inches is equal to ')
                centi = inches*2.54
                outfile.write(str(centi) + ' centimeters\n')
                outfile.close()
                print(inches,' inches is equal to ', centi, 'centimeters')
        except Exception as err:
            print('Error', err)

main()