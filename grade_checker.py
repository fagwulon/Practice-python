grade = int(input("Your grade: "))
print(grade)
if grade >= 90 and grade <= 100:
    print("A")
elif grade >= 80 and grade <= 89:
    print("B")
elif grade >= 70 and grade <= 79:
    print("C")
elif grade >= 60 and grade <= 69:
    print("D")
elif grade < 60 and grade >= 0:
    print("F")
else:       # prints if grade is in negetive and above 100
    print("Invalid score")
