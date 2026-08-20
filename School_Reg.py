def Grade_checker():
    name = input("Enter name: ")
    scores = [
        int(input("English: ")),
        int(input("Math: ")),
        int(input("Physics: ")),
        int(input("Chemistry: ")),
        int(input("Biology: "))
    ]
    return name, scores


def check_it(name, scores):
    for score in scores:
        if score < 0 or score > 100:
            print(f"\nInvalid score for {name}.")
            return False

    return True


def calculate(scores):
    Total_score = sum(scores)
    Average_score = Total_score / len(scores)
    print(Total_score)
    print(Average_score)
    return Total_score, Average_score


def Grade_it(Average_score):
    Grade = ""
    Status = ""
    if Average_score >= 70:
        Grade = "A"
        Status = "PASS"
    elif Average_score >= 60:
        Grade = "B"
        Status = "PASS"
    elif Average_score >= 50:
        Grade = "C"
        Status = "PASS"
    elif Average_score >= 45:
        Grade = "D"
        Status = "FAIR PASS"
    elif Average_score >= 40:
        Grade = "E"
        Status = "TOO POOR"
    else:
        Grade = "F"
        Status = "FAILED"
    return Grade, Status


def Output():
    while True:
        name, scores = Grade_checker()
        if check_it(name, scores):
            break
            print("Please enter the scores again.")

    Total_score, Average_score = calculate(scores)

    Grade, Status = Grade_it(Average_score)

    print(f"\n=====================\n")
    print(f"\nStudent: {name}")
    print(f"\nScores: {scores}")
    print(f"\nTotal: {Total_score}")
    print(f"\nAverage: {Average_score}")
    print(f"\nGrade: {Grade}")
    print(f"\nStatus: {Status}")
    print(f"\n======================\n")


Output()
