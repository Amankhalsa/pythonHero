print("if else ")
"""
Python Conditions and If statements
Python supports the usual logical conditions from mathematics:

Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
"""


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


# Short Hand If ... Else
a = 2
b = 330
print("A") if a > b else print("B")


# Short Hand If ... Else 2
a = 330
b = 330

print("A") if a > b else print("=") if a == b else print("B")
