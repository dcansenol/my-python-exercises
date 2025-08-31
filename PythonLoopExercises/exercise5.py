# If the number could divided by 3 and 5, write it on screen. Otherwise pass it!
# If the number is equal to 18 then break loop !

list1 = list(range(1,21))

for i in list1:

    if i % 3 == 0 and i % 5 == 0:
        print(i)

    else:
        continue
