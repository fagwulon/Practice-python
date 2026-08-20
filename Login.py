def credential():
    correct_username = "admin"
    correct_password = "1234"

    return correct_username, correct_password


def login_U_check(correct_username):
    max_attempt = 4
    attempt = 0
    while max_attempt > attempt:
        username = input("Enter username: ")

        if username == correct_username:
            return True

        attempt += 1
        print("Incorrect username!")

    return False


def login_P_check(correct_password):
    max_attempt = 4
    attempt = 0
    while max_attempt > attempt:
        password = input("Enter password: ")

        if password == correct_password:
            return True

        attempt += 1
        print("Incorrect password!")

    return False


def output():
    correct_username, correct_password = credential()
    U_check = login_U_check(correct_username)

    if not U_check:
        print("Account blocked!")
        return

    P_check = login_P_check(correct_password)

    if not P_check:
        print("Account blocked!")
        return

    print("Login Successful.")


output()
