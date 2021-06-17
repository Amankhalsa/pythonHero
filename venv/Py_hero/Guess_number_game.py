# 17-6-2021
# Generate Number from 1 -10
# Take user Input
# Tell if This User input is Equal to Random Number
# if its not Equal Print a message if number is higher or lower.

import random
rand_num = random.randint(1, 10)
guess=1
# print(f'The Random Number was {rand_num}') #if you wana won first time
print('This is a random number game  guess any number ')

while guess <=10:
# this is a try
    try:
        user_num = int(input('Please enter your desired Number: '))
        if rand_num == user_num:
            print(f'Congratulations You won {user_num} !!!!!!!')
            break;
        elif user_num > rand_num:
            print(f'Your number {user_num} is  too high!')
        elif user_num < rand_num:
            print(f'Your number {user_num} is  too small!')

        print(10-guess,"left")
        guess= guess+1
        if(guess>6):
            print("Game is Over Try Again")
            break
    except:
        print("please enter valid input")

    user_num = int(input('Please enter your desired Number: '))
    if rand_num == user_num:
        print(f'Congratulations You won {user_num} !!!!!!!')
        break;
    elif user_num > rand_num:
        print(f'Your number {user_num} is  too high!')
    elif user_num < rand_num:
        print(f'Your number {user_num} is  too small!')

    print(10-guess,"left")
    guess= guess+1
    if(guess>6):
        print("Game is Over Try Again")
        break


# 2nd example
"""
guess=1

while guess <=10:
    user_num = int(input('Please enter your desired Number: '))
    if user_num==10:
        print(f'Congratulations You won {user_num} equal to !!!!!!!')
        break;
    elif user_num >10:
        print(f'Your number {user_num} is Greater than ')

    elif user_num <10:
        print(f'YYour number {user_num} is Less than ')

    print(10-guess,"no of guess left ")
    guess=guess+1
    if(guess>9):
        print("Game Over गेम ओवर हो  गई है ")
        break

"""
# 3rd example
"""
n=18
no_of_guess=1
print("Number of guesses is limited")
while no_of_guess<=9:
    guess_number=int(input("enter number:\n"))
    if guess_number<18:
        print("you enter less number please enter grater number\n")
    elif guess_number>18:
        print("please enter less number\n")
    else:
        print("you won \n")
        print(no_of_guess,"no.of guesses he took to finish.")
        break
    print(9-no_of_guess,"no. of guesses left")
    no_of_guess = no_of_guess + 1

    if(no_of_guess>9):
        print("Game Over गेम ओवर हो  गई है ")
        break

"""