# The program that checks if the word is a palindrome.
# Palindrome is a word that becomes the same when read in reverse.

def PalindromeFinder(x):
    reversedWord = "".join(reversed(x))

    if x == reversedWord:
        print("This is an Polindrome word.")
    else:
        print("This is not Poindrome word.")


while True:
    word = input("Please enter a number: ")
    PalindromeFinder(word)