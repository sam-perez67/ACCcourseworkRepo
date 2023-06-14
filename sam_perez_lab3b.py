name = input('name: ')
years = input('years worked: ')
if float(years) < 1: 
    months = input('How many months has this employee been employed?: ')
vacation = input('number of vacation days: ')
unpaid_vacation = float(vacation) - 3
if unpaid_vacation >= 0:
    unpaid_vacation = float(unpaid_vacation) * 200
if float(years) > 1 or float(months) >= 3:
    revenue = input('revenue: ')
    if float(revenue) > 10000 and float(revenue) < 100000:
        bonus = float(revenue) * 0.02
    else:
        if float(revenue) > 100001 and float(revenue) < 500000:
            bonus = (float(revenue) * 0.15) + 1000
        else:
            if float(revenue) > 500001 and float(revenue) < 1000000:
                bonus = (float(revenue) * 0.28) + 5000
            else:
                if float(revenue) > 100000:
                    bonus = (float(revenue) * 0.35) + 100000
                else: bonus = 0
                months = 0

if float(years) > 4.99999 and float(revenue) > 99999:
    additional_bonus = 1,000
else:
    additional_bonus = 0

if unpaid_vacation <= 0: 
    gross = 2000 + float(bonus) + float(additional_bonus)
else: gross = (2000 + float(bonus) + float(additional_bonus)) - float(unpaid_vacation)
print('Paystub:')
print(name)
if float(years) <= 0.9999:
    print (str(months) + ' months')
else: print(str(years) + ' years')
print('base salary, $2,000')
print('Commission and Bonus: $' + str(bonus))
print('Additional Bonus: $' + str(additional_bonus))
if unpaid_vacation > 0:
    print('Deductions: $' + str(unpaid_vacation))
print('Gross Income: $' + str(gross))
