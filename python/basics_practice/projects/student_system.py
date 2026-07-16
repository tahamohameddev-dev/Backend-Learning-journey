# ===== Student Management System =====

# 1. Add Student
# 2. View Students
# 3. Search Student
# 4. Delete Student
# 5. Update Student Grade
# 6. Show Average Grade
# 7. Show Top Student
# 8. Exit

# ===== Student Management System =====

print("\nStudent Management System")
print("1. Add Student")
print("2. View Students")
print("3. Search Student")
print("4. Delete Student")
print("5. Update Student Grade")
print("6. Show Average Grade")
print("7. Show Top Student")
print("8. Exit")

students = []

def add_student():
    try:
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        grade = int(input("Enter your grade: "))
        students.append({"name":name, "age":age, "grade":grade})
        print(f"Done append {name} successfully!")
    except ValueError:
        print("Enter vallid number!")

def view_student():
    if not students:
        return
    for student in (students):
        print(f"your students is\n{students}")

def serch_student():
    if not students:
        return
    serch_student = input("Enter your name for serch: ")
    for student in students:
        if student["name"] == serch_student:
            print(f"name is: {student['name']}")
            print(f"the age is: {student['age']}")
            print(f"the grade is: {student['grade']}")

def delete_student():
    view_student()
    if not students:
        return
    delete_student = input("Enter name for delete it")
    for index, student in enumerate(students):
        if student["name"] == delete_student:
            remove = students.pop(index)
            print(f"delete {remove["name"]} successfully!")

def update_grade():
    view_student()
    if not students:
        return
    try:
        update = input("Enter youre name student for update grade: ")
        for student in students:
            if update == student["name"]:
                new_grade = int(input("Enter your new grade: "))
                student["grade"] = new_grade
            print("update successfully!")
        print("Student not found!")
    except ValueError:
        print("Enter try vallid name !")

def average_grade():
    view_student()
    if not students:
        return
    try:
        total_grages = 0
        for student in students:
            total_grages += student["grade"]
        average = total_grages / len(students)
        print(f"the average is {average} !")
    except ValueError:
        print("Enter vallid number!!")

def top_student():
    if not students:
        return
    top = students[0]
    for student in students:
        if student["grade"] > top["grade"]:
            top = student
    print(top)

while True:
    choice = input("Enter choice ")