firstSide = int(input("Enter first side length: "))
secondSide = int(input("Enter second side length: "))
thirdSide = int(input("Enter third and last side length: "))

if firstSide + secondSide > thirdSide and firstSide + thirdSide > secondSide and secondSide + thirdSide > firstSide:

    if firstSide == secondSide == thirdSide:
        print("This is an equilateral triangle.")
    elif firstSide == secondSide or firstSide == thirdSide or secondSide == thirdSide:
        print("This is an isosceles triangle.")
    else:
        print("Scalene triangle.")

else:
    print("Not triangle.")