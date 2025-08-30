# The Program to find prime factors of a number.

def primeFactorFinder(x):
    list1 = []
    list2 = []

    i = 1

    while i < x+1:
        if x % i == 0:
            list1.append(i)
        i += 1

    for m in list1:
        if m > 1:
            prime = True
            for k in range(2, int(m**0.5) + 1): # Formula
                if m % k == 0:
                    prime = False
                    break

            if prime:
                list2.append(m)
    print(list2)

while True:
    number = int(input("Please enter a number whose prime factors you want to find :"  ))
    primeFactorFinder(number)