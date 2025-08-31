# In this code, We'll print a word in reverse that we get from the user.
# If there is character 'a' in the word, we'll skip this character.
# If there is character 'z' in the word, we'll end the code.

word = input("Please enter the word that you want to be printed in reverse: ")
list1 = []

for i in word:
    list1.append(i)

l = len(list1)

for m in range(l-1, -1, -1):
    if list1[m] == 'a':
        continue
    elif list1[m] == 'z':
        break
    print(list1[m], end="")

# Alternatively, this code could be written without creating a list.
