student_heights = input("Input a list of student heights\n").split()
student_heights_len = 0
student_heights_somme = 0
average_height = 0

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

for m in student_heights:
    student_heights_len += 1

for o in student_heights:
    student_heights_somme += student_heights[n]

average_height = round(student_heights_somme / student_heights_len)

print(f"Average height rounded to te nearest whole number = {average_height}")

    