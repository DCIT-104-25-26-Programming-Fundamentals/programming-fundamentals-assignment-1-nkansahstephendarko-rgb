# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 8
# Topic: Lists of Dictionaries, Loops, and Functions
# =============================================================================
#
# TASK: Student Record Management System
#
# (instructions as given)
#

def add_student(students):
    name = input("Student name: ")
    student_id = input("Student ID: ")

    try:
        num_scores = int(input("How many scores? "))
    except ValueError:
        print("Error: please enter a valid number.")
        return

    if num_scores <= 0:
        print("Error: number of scores must be positive.")
        return

    scores = []
    for i in range(num_scores):
        try:
            score = float(input(f"Enter score {i + 1}: "))
        except ValueError:
            print("Error: please enter a valid number for the score.")
            return
        scores.append(score)

    student = {
        "name": name,
        "id": student_id,
        "scores": scores
    }
    students.append(student)
    print(f'Student "{name}" added successfully.')


def display_students(students):
    if not students:
        print("No students have been added yet.")
        return

    print("-" * 50)
    print(f"{'Name':<15}{'ID':<12}{'Scores':<15}{'Average':<10}")
    print("-" * 50)

    for student in students:
        scores_str = ", ".join(str(int(s)) if s.is_integer() else str(s) for s in student["scores"])
        average = round(sum(student["scores"]) / len(student["scores"]), 2)
        print(f"{student['name']:<15}{student['id']:<12}{scores_str:<15}{average:<10}")

    print("-" * 50)


def calculate_average(students):
    student_id = input("Enter student ID: ")

    for student in students:
        if student["id"] == student_id:
            average = round(sum(student["scores"]) / len(student["scores"]), 2)
            print(f"{student['name']}'s average score: {average}")
            return

    print("Error: student ID not found.")


def print_menu():
    print("================================")
    print("   STUDENT RECORD SYSTEM MENU")
    print("================================")
    print("1. Add student")
    print("2. Display all students")
    print("3. Calculate average score")
    print("4. Quit")


def main():
    students = []

    while True:
        print_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            display_students(students)
        elif choice == "3":
            calculate_average(students)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Error: invalid choice. Please enter a number from 1 to 4.")

        print()


if __name__ == "__main__":
    main()