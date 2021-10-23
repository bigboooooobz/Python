##Generate two numbers using random.randint(MIN, MAX) between 1 to 20 that we covered in the function -1 lab.##

import random 
import math

# r1 = random.randint(1,20)
# print(random.randint(1,20))


# Define a function math_quiz(number1, number2, choice) that takes defines three parameters. number1 and number2 are random numbers between 1 to 20 passed to function as an argument (from step 1). choice is a numeric value based on 1: Addtion, 2: Subtraction, 3: Multiplication, 4: Division. You don't need to verify for wrong choice entered.

def add(num1, num2):
    return num1+num2
# print(add(10, 10))
def subtract(num1, num2):
    return num1-num2
# print(subtract(10, 10))
def divide(num1, num2):
    return num1/num2
# print(divide(10, 20))
def multiply(num1, num2):
    return num1*num2
# print(multiply(10, 20))

r1 = random.randint(1,20)
r2 = random.randint(1,20)
choice = int(input("Choose 1 - 4"))
def math_quiz(num1, num2, choice):
    if(choice == 1):
        print(num1,"+",num2)
        answer1 = int(input("Enter the correct answer"))
        if(answer1 == add(num1, num2)):
            print("Congrats you're right!!")
        else:
            print("You're wrong loser, the right answer is ",add(num1, num2))
    elif(choice == 2):
        print(num1,"-", num2)
        answer2 = int(input("Enter the correct answer"))
        if(answer2 == subtract(num1, num2)):
            print("Congrats you're right!!")
        else:
            print("You're wrong loser, the right answer is ",subtract(num1, num2))
    elif(choice == 3): 
        print(num1,"/", num2) 
        answer3 = int(input("Enter the correct answer"))
        if(answer3 == divide(num1, num2)):
            print("Congrats you're right!!")
        else:
            print("You're wrong loser, the right answer is ",divide(num1, num2))
    elif(choice == 4): 
        print(num1,"*", num2)
        answer4 = int(input("Enter the correct answe"))
        if(answer4 == multiply(num1, num2)):
            print("Congrats you're right!!")
        else:
            print("You're wrong loser, the right answer is ",multiply(num1, num2))
    elif(choice > 4 or choice >0):
        print("Invaid Choice")
math_quiz(r1, r2, choice)

# Display a prompt to the user to input their choice for operator (1 through 4) and pass it along with the random numbers to the function math_quiz(number1, number2, choice). You don't have to use a repeated menu using a while loop but you can if you want to.
# (TIP: you can put the code for generating random numbers inside the while loop so that it would generate two new random numbers for each iteration.)

# The math_quiz(number1, number2, choice) function should display the numbers on the screen along the corresponding operator (+, -, *, or, /) and ask the user to enter the correct answer.