def students_score():
    scores = input("Enter the scores seperated by spaces: ")

    # Convert input strings into list of integers
    scores = [int(score) for score in scores.split()]
    print(type(scores))
    return scores


def check_all(student_score):
    max_all = max(student_score)
    min_all = min(student_score)
    avg = sum(student_score) / len(student_score)

    print(f"Highest: {max_all}")
    print(f"Lowest: {min_all}")
    print(f"Average: {avg:.2f}")


scores = students_score()
check_all(scores)
