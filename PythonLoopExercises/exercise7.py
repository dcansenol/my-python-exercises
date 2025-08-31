# In this project, We'll do mini text analysis!

text = input("Please enter a text: ")

for i in text:
    if i == ' ':
        continue
    if i == '.':
        break
    print(i)

while True:
    word = input("Please enter a word: ")
    if len(word) < 3:
        print("The word can't be smaller than 3!")
        continue
    if word == 'quit':
        print("The program is terminating...")
        break
    if word == 'python':
        print("Congratulations!")
        break

print("The program is finished.")