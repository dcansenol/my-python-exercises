# Password prediction code:

RealPassword = '83572'

while True:
    print("Please write q for exit")
    EnteredPassword = input("Please enter the password: ")

    if EnteredPassword == RealPassword:
        print("Succesfully logged in! ")
        break
    if EnteredPassword == 'q':
        print("Program is terminating...")
        break
    if len(EnteredPassword) < 3:
        print("Password can not shorter than 3 characters! Please try again.")
        continue


