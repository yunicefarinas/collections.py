def get_letter_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


student_name = input("Enter student name: ")

grade1 = int(input("Enter grade: "))
grade2 = int(input("Enter grade: "))
grade3 = int(input("Enter grade: "))
grade4 = int(input("Enter grade: "))
grade5 = int(input("Enter grade: "))

grades = [grade1, grade2, grade3, grade4, grade5]

average = sum(grades) / len(grades)

letter_grade = get_letter_grade(average)

print()
print(student_name)
print()
print("Average:", f"{average:g}")
print()
print("Letter Grade:", letter_grade)