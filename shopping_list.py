shopping = []

while True:
    item = input("Enter item(or type 'done' to finish): ")

    if item.lower() == "done":
        break

    shopping.append(item)

    print("\nYour Shopping List:")
    for i, item in enumerate(shopping, start=1):
        print(f"{i}. {item}")
