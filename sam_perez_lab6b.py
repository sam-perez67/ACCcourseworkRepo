def main():
    for x in range(12):
        try:
            name = input("What is the student's name?: ")
            grade = int(input("What is the student's grade?: "))
            if grade < 0 or grade > 100:
                raise Exception
        except Exception:
            print('Please enter a valid grade')
            grade = int(input("What is the student's grade?: "))
            
        else:
            try:
                outfile = open('grades.txt', 'a')
                outfile.write(name + ' ' + str(grade) + '\n')
                outfile.close()
                print(name + ' has a ' + str(grade) + ' in the class')
                if __file__ != 'grades.txt':
                    raise Exception
            except Exception:
                print('Error: file not found')

main()