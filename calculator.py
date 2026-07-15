num_1 = int(input("The first number: "))
num_2 = int(input("The second number: "))
ops = input("Enter operator: ")

if ops == "+":
    print(num_1 + num_2)
elif ops == "-":
    print(num_1 - num_2)
elif ops == "*":
    print(num_1 * num_2)
elif ops == "/":
    if num_2 != 0:
        print(num_1 / num_2)
    else:  # prints an error meesage if num_2's value is zero
        print("ERROR! Cannot divide by zero")
else:
    print("invalid")
