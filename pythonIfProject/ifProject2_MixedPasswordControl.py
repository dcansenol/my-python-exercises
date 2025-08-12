print("""Neccessary rules to be valid of password
***********************************
1. Minimum 8 characters
2. Minimum one big character
3. Minimum one small character
4. It should include minimum one number
***********************************
""")

validPassword = input("Please enter valid password: ")

if (len(validPassword) >= 8) and (any(char.isupper() for char in validPassword)) and (any(char.islower() for char in validPassword)) and (any(char.isdigit() for char in validPassword)):
    print("Your password is valid !")
else:
    print("Your password is invalid !")