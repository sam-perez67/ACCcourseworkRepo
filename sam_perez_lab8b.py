date = input('Enter a date in mm/dd/yy format: ')
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

def main():
    date_list = date.split('/')
    month = int(date_list[0])
    day = int(date_list[1])
    year = int(date_list[2]) 
    if month > 12 or month < 1:
        print('Please enter a valid month in mm format')
        m = input('Enter a month: ')
        date_list.insert(0, m)
        month = int(date_list[0])
    if day > 31 or day < 1:
        print('Please enter a valid day in dd format')
        d = input('Enter a day: ')
        date_list.insert(1, d)
        day = int(date_list[1])
    if year != 15:
        print('The year must be 2015')
        y = input('Enter a year: ')
        date_list.insert(2, y)
        year = int(date_list[2]) 
    print(f'{months[month-1]} {day}, 20{year}')
    

main()