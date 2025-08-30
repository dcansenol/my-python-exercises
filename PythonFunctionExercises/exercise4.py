# In this code, We will print the numbers to the screen whose sum of digits is equal to 10.

def sumOfDigits():
    list1 = list((range(1,1001)))
    for i in list1:
        sum = 0
        for m in str(i):
            sum += int(m)
        if sum == 10:
            print(i)

sumOfDigits()
