# In this code, We will get a sentence from the user and find longest word. Then, we'll print.

def longestWordFinder(x):
    list1 = x.split()

    wordLength = 0
    for i in list1:
        if len(i) > wordLength:
            wordLength = len(i)
        else:
            continue

    for m in list1:
        if len(m) == wordLength:
            print("The longest word: ",m)


while True:
    sentence = input ("Please enter a sentence: ")
    longestWordFinder(sentence)