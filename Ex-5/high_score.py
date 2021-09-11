student_score = input("Input a list of student score\n").split()

high_score = 0

for n in range(0, len(student_score)):
    student_score[n] = int(student_score[n])
print(student_score)

for score in student_score:
    if score > high_score:
        high_score = score

print(f"The highest score in the class is : {high_score}")