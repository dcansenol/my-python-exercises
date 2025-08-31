# In this project, We'll print the non-even numbers from 1 to 30.
# If the numbers is equal to 25, we'll break loop.

i = 1

while i < 31:
    if i % 2 == 0:
        i += 1
        continue
    if i == 25:
        break
        
    print(i)
    i +=1

