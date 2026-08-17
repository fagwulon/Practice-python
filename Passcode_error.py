def credential():
    Username = "Admin"
    Password = "Admin"
    Count = 5
    return Username, Password, Count


def Login_username(Username, Count):
    for count in range(1, Count, + 1):
        Username_pass = input("Enter your username: ")
        if Username_pass == Username:
            return True
        else:
            remaining_count = Count - count
            if remaining_count > 0:
                print(
                    f"Incorrect username! \n Have {remaining_count - 1} left!")
    return False


def Login_Password(Password, Count):
    for count in range(1, Count, + 1):
        Passcode = input("Enter your password: ")
        if Passcode == Password:
            return True
        else:
            remaining_count = Count - count
            if remaining_count > 0:
                print(
                    f"Incorrect password! \n Have {remaining_count - 1} left!")
    return False


def check():
    Username, Password, Count = credential()
    if Login_username(Username, Count) is False:
        print(f"No attempts left! \n Can't try again!!")
        return
    print("Username correct")

    if Login_Password(Password, Count) is False:
        print(f"No attempts left! \n Can't try again!!")
        return
    print("Login Successful")


check()
