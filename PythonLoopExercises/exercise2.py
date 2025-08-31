# In this program, we'll want 5 numbers from the user and the entered number is negative we'll pass this number without printing;
# If the number is bigger than 100; We'll completely finish the loop with "break".
# Finally, We'll print sum all of the valid numbers.

i = 1
sum = 0

while i < 6:
    numbers = int(input("Please enter the number: "))
    if numbers < 0:
        i += 1
        print("This number won't be printed. ")
        continue
    if numbers > 100:
        print("You entered bigger than 100 so the program is terminating... ")
        break
    i += 1
    sum = sum + numbers
print("Sum of the valid numbers: ",sum)