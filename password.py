password = "Python123"
while password == "Python123":
    passcode = password
    passcode = input("Enter the password: ")
    print(passcode)
    if passcode == password:
        print("Correct")
        break
    else:
        print("Incorrect Password")
