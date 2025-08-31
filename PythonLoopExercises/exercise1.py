# printing numbers from 1 to 50 skipping multiples of 7.

i = 1

while i<51:
    if i % 7 == 0:
        i += 1
        continue
    print(i)
    i += 1
