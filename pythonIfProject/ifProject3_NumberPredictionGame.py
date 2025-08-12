import random

number = random.randint(1,50)

UserNumber = int(input("Enter your number: "))

if UserNumber == number:
    print("Congratulations! The number you kept: ",UserNumber, "Number kept by the computer:: ",number)
else:
    print("Unfortunately... Try again!")
    print("The number you kept: ", UserNumber, "Number kept by the computer:: ", number)