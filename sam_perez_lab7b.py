
students = []

def main():
    for i in range(12):
        students.append(input('Enter a name: '))
    sort_students(students)

def sort_students(students):
    students.sort()
    print(students)
    students.reverse()
    print(students)
    students.append(input('Enter the instructor\'s name: '))
    students.insert(0, 'Sam Perez')
    f = open('names.txt', 'r+')
    for name in students:
        f.write(name + '\n')
    print(f.readlines())
    f.close()
    tuple(students)

main()