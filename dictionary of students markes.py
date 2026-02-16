students_marks={'Alice':90,'John':95,'Carol':98}
def marks(a):
    a=a.capitalize()
    if a in students_marks:
        print(f'{a}\'s marks:{students_marks[a]}')
    else:
        print('Student not found')
marks(input('enter the student\'s name:'))