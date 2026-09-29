amount = int(input("\nEnter the amount you want to add: "))

notes_1000 = amount // 1000
remainder = amount % 1000

notes_500 = amount // 500
remainder = amount % 500

notes_200 = amount // 200
remainder = amount % 200

notes_100 = amount // 100
remainder = amount % 100


print(f"₦1000 notes: {notes_1000}")
print(f"₦500 notes: {notes_500}")
print(f"₦200 notes: {notes_200}")
print(f"₦100 notes: {notes_100}")
print(f"Remaining amount: {remainder}")
