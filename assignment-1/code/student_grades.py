students = {}

while True:
    action = input("\nChoose: add / update / print / exit: ").lower()

    if action == "add":
        name = input("Student name: ")
        grade = input("Grade: ")
        if name in students:
            print("Student already exists.")
        else:
            students[name] = grade
            print("Student added.")

    elif action == "update":
        name = input("Student name: ")
        if name in students:
            grade = input("New grade: ")
            students[name] = grade
            print("Grade updated.")
        else:
            print("Student not found.")

    elif action == "print":
        for name, grade in students.items():
            print(f"{name}: {grade}")
        if not students:
            print("No students yet.")

    elif action == "exit":
        break

    else:
        print("Invalid option.")
