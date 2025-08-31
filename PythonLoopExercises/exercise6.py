# In this project, We'll get a word from the user and print the letters in order with for loop.
# If the letter is a, pass it (continue). If the letter is z, break the loop (break).

word = input("Please enter a word: ")

for i in word:
    if i == 'a':
        continue
    if i == 'z':
        break
    print(i)