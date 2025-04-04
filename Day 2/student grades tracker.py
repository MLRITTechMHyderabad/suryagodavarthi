

def calculate_the_avg_grade(grades):
    avg_grade = sum(grades)/len(grades)
    return avg_grade

student_grades = [("Alice", [85, 90, 78, 92]),
("Bob", [60, 65, 70, 75]),
("Charlie", [40, 45, 50, 55]),
("David", [95, 100, 98, 92])]

highest_avg = 0
top_student = ""
pass_count = 0
for student, grades in student_grades:
    avg = calculate_the_avg_grade(grades)
    print(f"{student}'s average grade: {avg:.2f}")

    if avg > highest_avg:
        highest_avg = avg
        top_student = student
    print(f"\n{top_student} has the highest average grade: {highest_avg:.2f}")
    if avg >= 50:
        pass_count += 1
    print(f"number of students passed: {pass_count}")





