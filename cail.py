try:
    number = int(input("Enter a number: "))
    if number > 0:
       report = ("Positive")
    elif number < 0:
       report = ("Negative")
    else:
        report = ("Zero")
    odd_even = "Even" if number % 2 == 0 else "Odd"
    print(f"classification: {odd_even}; {report} number.")

except:
    print("Integer Expected! Try again")
