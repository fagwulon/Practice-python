secret_number = 7

while True:
    guess = int(input("Guess a number: "))

    if guess == secret_number:
        print("Correct, you guessed right!")
        break

    elif guess > secret_number:
        print("Too high")

    else:
        print("Too low")
