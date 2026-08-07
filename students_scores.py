def students_score(scores):
    print(scores)
    print(type(scores))
    return scores


def check_all(student_score):
    max_all = max(student_score)
    min_all = min(student_score)
    avg = sum(student_score) / len(student_score)

    print("Highest:", max_all)
    print("Lowest:", min_all)
    print("Average:", avg)


scores = students_score([78, 56, 93])
check_all(scores)
