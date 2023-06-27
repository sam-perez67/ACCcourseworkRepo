test_score = float(input('Enter your test score, if there is no test score, enter -1: '))
total = 0
count = 0
while test_score != -1:
    print(test_score)
    total += test_score
    count += 1
    test_score = float(input('Enter your test score, if there is no test score, enter -1: '))

if count == 0:
    print('No test scores to show')
else:
    print('Total of test scores: ', total)
    print('Total number of tests: ', count)
    print('Average test score: ', total/count)