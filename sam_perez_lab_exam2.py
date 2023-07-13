def main():
    name = input("What is the student's name?: ")
    try:
        tst1 = int(input("What is the student's first test score?: "))
        tst2 = int(input("What is the student's second test score?: "))
        tst3 = int(input("What is the student's third test score?: "))
        if tst1 or tst2 or tst3 < 0 or tst1 or tst2 or tst3 > 100:
            raise ValueError
    except ValueError:
        print('Please enter a test score between 0 and 100')
    calc_average(tst1, tst2, tst3)
    letter_grade = calc_average(tst1, tst2, tst3)   
    determine_grade(letter_grade)
    results = [name, tst1, tst2, tst3, letter_grade, determine_grade(letter_grade)]
    display_results(results)
    write_results(results)
    append_event()
    read_results()

def calc_average(tst1, tst2, tst3):
    avg_score = (tst1 + tst2 + tst3) / 3
    return avg_score

def determine_grade(letter_grade):
    if letter_grade >= 90:
        return 'letter grade is A'
    elif letter_grade >= 80:
        return 'letter grade is B'
    elif letter_grade >= 70:
        return 'letter grade is C'
    elif letter_grade >= 60:
        return 'letter grade is D'
    else:
        return 'letter grade is F'

def display_results(results):
    for i in results:
        print(i)

def write_results(results):
    name = results[0]
    tst1 = results[1]
    tst2 = results[2]
    tst3 = results[3]
    avg_score = results[4]
    letter_grade = results[5]
    try:
        outfile = open('results.txt', 'w')
        outfile.write('The student name is ' + name + '\n')
        outfile.write('The student first test score is ' + str(tst1) + '\n')
        outfile.write('The student second test score is ' + str(tst2) + '\n')
        outfile.write('The student third test score is ' + str(tst3) + '\n')
        outfile.write('The student average score is ' + str(avg_score) + '\n')
        outfile.write('The student ' + letter_grade + '\n')
        outfile.close()
    except FileNotFoundError:
        print('Error: file not found')

def append_event():
    try:
        outfile = open('results.txt', 'a')
        for i in range(2,50,2):
            outfile.write(str(i) + '\n')
        outfile.close()
    except FileNotFoundError:
        print('Error: file not found')

def read_results():
    try:
        outfile = open('results.txt', 'r')
        for x in outfile:
            print(x)
        outfile.close()
    except FileNotFoundError:     
        print('Error: file not found')

main()