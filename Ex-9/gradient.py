student_score = {
    "harry": 81,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62
}

student_grades = {}

for student in student_score:
    if 91 <= student_score[student] <= 100:
        student_grades[student] = "Outstanding"
    elif 81 <= student_score[student] <= 90:
        student_grades[student] = "Exceeds Expectations"
    elif 71 <= student_score[student] <= 80:
        student_grades[student] = "Acceptable"
    elif student_score[student] <= 70:
        student_grades[student] = "Fail"

print(student_grades)       