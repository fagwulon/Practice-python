Visitors = set()

while True:
    tab = input("Enter visitor's name (or done): ")
    if tab == "done":
        break
    Visitors.add(tab)
    print(f"\n=====VISITORS({len(Visitors)})=====\n")

    for i, tab in enumerate(Visitors, start=1):
        print(f"{i}. {tab}")
