# In this code, We will check if the number that get from the user is Armstrong number.
# Armstrong number is the number whose sum of the cubes of its digits is equal to itself.

def ArmstrongNumberFinder(x):
    list1 = []
    sum = 0

    for i in x:
        list1.append(i)

    for m in list1:
        sum += int(m)**3

    if sum == int(x):
        print("This is an Armstrong Number.")
    else:
        print("This is not Armstrong number.")


while True:
    number = input("Please Enter a number: ")
    ArmstrongNumberFinder(number)