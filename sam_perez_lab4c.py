test_score = float(input('Enter your test score, if there is no test score, enter -1: '))
total = 0
count = 0
while test_score != -1:
    if test_score < 0 or test_score > 100:
        print('Invalid test score, please enter a valid test score')
    elif test_score >= 90:
        print(test_score,'is an A')
    elif test_score >= 80:
        print(test_score, 'is a B')
    elif test_score >= 70:
        print(test_score, 'is a C')
    elif test_score >= 60:
        print(test_score, 'is a D')
    else:
        print(test_score, 'is an F')
    total += test_score
    count += 1
    test_score = float(input('Enter your test score, if there is no test score, enter -1: '))

if count == 0:
    print('No test scores to show')
else:
    print('Total of test scores: ', total)
    print('Total number of tests: ', count)
    print('Average test score: ', total/count)