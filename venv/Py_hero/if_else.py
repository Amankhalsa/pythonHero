passing_marks = 35
obtained_marks = int(input('Plese enter your Obtained marks: '))

if obtained_marks > passing_marks and obtained_marks >75:
    print(f'your Marks is {obtained_marks}  and passed with first division')

elif obtained_marks > passing_marks and obtained_marks >60:
    print(f'your Marks is {obtained_marks} passed with second Division')

elif obtained_marks > passing_marks and obtained_marks >50:
    print(f'your Marks is {obtained_marks}  passedwith Third Division')

elif obtained_marks > passing_marks and  obtained_marks > 40:
    print(f'your Marks is {obtained_marks} and passed ')

elif obtained_marks > passing_marks and  obtained_marks <=40:
    print(f'your Marks is {obtained_marks} and passed ')
else:
    print('you failed')