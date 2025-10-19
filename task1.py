student_marks = {"Alice": 85,"aaryan": 72,"Charlotte": 98,"Diya": 60,"prince": 48}
name = input("Enter the student's name: ")
if name in student_marks:
    print(f"{name}'s marks: {student_marks[name]}")
else:
    print("Student not found.")
