def check(prompt) :
    while True :
        mark = input(prompt)
        try :
            mark = int(mark)
            if not(mark  <= 50 and mark > 0) :
                print('total for this subject is 50, invalid entry.')
            else :
                return mark
        except ValueError :
            print('That is not an exam score.')

def grading(per) :
    if per >= 90 and per < 100 :
        grade = 'A'
    elif per >= 80 and per < 90 :
        grade = 'B'
    elif per >= 70 and per < 80 :
        grade = 'C'
    elif per >= 60 and per < 70 :
        grade = 'D'
    elif per >= 50 and per < 60 :
        grade = 'E'
    elif per < 50 :
        grade = 'F'
    return grade

def check1(prompt) :
    while True :
        mark1 = input(prompt)
        try :
            mark1 = int(mark1)
            if not(mark1  <= 100 and mark1 > 0) :
                print('total for this subject is 100, invalid entry.')
            else :
                return mark1
        except ValueError :
            print('That is not an exam score.')    

print('-----------------------------MARKS ENTRY-----------------------------\n')
print('Enter marks ')
chem = check1('Chemistry : ')
comp = check1('Computer : ')
eng = check1('English : ')
pak = check('Pak studies : ')
islam = check('Islamic studies : ')
print('\n')
total = 100 + 100 + 100 + 50 + 50
marks_obt = chem + comp + eng + pak + islam
per_obt = marks_obt / total * 100
grade  = grading(per_obt)
print('-----------------------------R E S U L T-----------------------------\n')
print('Total Marks : ' , total , '\t\tMarks Obtained : ' , marks_obt , '\n\nGrade : ' , grade , '\t\t\tPercentage : ' , per_obt , '%')