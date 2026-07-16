num = int(input("Enter a number: "))

total = 0

for i in range(1, num + 1):
    total += i

    plus = " + ".join(str(i) for i in range(1, num + 1))

print(f"{plus} = {total}")
