def Input():
    age = int(input("Enter age: "))

    # Keep asking until the user enters a non-negative age.
    # This prevents negative ages from reaching the pricing logic.

    while age < 0:
        print("Invalid age. Age cannot be negative.")
        age = int(input("Enter age: "))
    day = input("Enter the day (weekday/weekend): ").lower()

    # Keep asking until the user enters one of the two accepted values.
    # .lower() also allows inputs such as "WEEKDAY" or "WeekDay".
    # Turning them to lowercase letters.

    while day not in ("weekday", "weekend"):
        print("Invalid input. Please enter weekday or weekend.")
        day = input("Enter the day (weekday/weekend): ").lower()

    return age, day


def conditions(age, day):

    # Accept ages from 0 through 4.
    # The input validation above guarantees that age cannot be negative.

    if 0 <= age <= 4:
        print("Entry is Free")

    # Because the previous condition already handled ages 0–4,
    # this condition effectively covers ages 5–12.
    # elif conditions are evaluated only if all preceding if/elif conditions were false.
    elif age <= 12:
        if day == "weekday":
            print("Price: 1500")
        else:
            print("Price: 2000")

    # The previous conditions handled ages 0–12,
    # so this effectively covers ages 13–59.

    elif age <= 59:
        if day == "weekday":
            print("Price: 2000")
        else:
            print("Price: 2500")

    # At this point, ages 0–59 have already been handled,
    # so this condition covers ages 60 and above.

    elif age >= 60:
        if day == "weekday":
            print("Price: 1000")
        else:
            print("Price: 1200")


def output():

    # Receive the validated age and day from Input().

    age, day = Input()

    # Pass the values to the pricing logic.

    conditions(age, day)


output()
