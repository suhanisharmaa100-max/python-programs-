# Coaching Institute Student Record System
# Features:
# 1. Stores student details permanently in JSON
# 2. Maintains a text log
# 3. Generates an Excel-compatible CSV report
# 4. Keeps all reports inside a folder

import os
import json
import csv
from datetime import datetime

# Folder and file paths
REPORT_FOLDER = "reports"
DATA_FILE = os.path.join(REPORT_FOLDER, "students.json")
LOG_FILE = os.path.join(REPORT_FOLDER, "student_log.txt")
CSV_FILE = os.path.join(REPORT_FOLDER, "student_report.csv")

# Create reports folder if it does not exist
os.makedirs(REPORT_FOLDER, exist_ok=True)


def load_students():
    """Load existing student data from JSON file."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    return []


def save_students(students):
    """Save student data permanently in JSON format."""
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(students, file, indent=4, ensure_ascii=False)


def write_log(student):
    """Add a new student entry to the text log."""
    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(
            f"{student['joined_on']} | "
            f"ID: {student['student_id']} | "
            f"Name: {student['name']} | "
            f"Course: {student['course']} | "
            f"Phone: {student['phone']}\n"
        )


def generate_csv(students):
    """Generate an Excel-compatible CSV report."""
    with open(CSV_FILE, "w", newline="", encoding="utf-8-sig") as file:
        fieldnames = [
            "student_id",
            "name",
            "age",
            "gender",
            "phone",
            "email",
            "address",
            "course",
            "joined_on",
        ]

        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students)


def add_student():
    """Collect and save a new student's details."""
    students = load_students()

    print("\n--- Add New Student ---")

    student = {
        "student_id": input("Student ID: ").strip(),
        "name": input("Student Name: ").strip(),
        "age": input("Age: ").strip(),
        "gender": input("Gender: ").strip(),
        "phone": input("Phone Number: ").strip(),
        "email": input("Email Address: ").strip(),
        "address": input("Address: ").strip(),
        "course": input("Course Joined: ").strip(),
        "joined_on": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

    # Check for duplicate ID
    for existing_student in students:
        if existing_student["student_id"] == student["student_id"]:
            print("\nStudent ID already exists. Record not added.")
            return

    students.append(student)

    save_students(students)
    write_log(student)
    generate_csv(students)

    print("\nStudent record saved successfully.")
    print(f"JSON data: {DATA_FILE}")
    print(f"Text log: {LOG_FILE}")
    print(f"CSV report: {CSV_FILE}")


def view_students():
    """Display all stored students."""
    students = load_students()

    if not students:
        print("\nNo student records found.")
        return

    print("\n--- Student Records ---")
    for student in students:
        print(
            f"\nID: {student['student_id']}"
            f"\nName: {student['name']}"
            f"\nCourse: {student['course']}"
            f"\nPhone: {student['phone']}"
            f"\nJoined On: {student['joined_on']}"
        )


def main():
    while True:
        print("\n===== Coaching Institute Management System =====")
        print("1. Add New Student")
        print("2. View All Students")
        print("3. Generate CSV Report")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            students = load_students()
            generate_csv(students)
            print(f"\nCSV report generated successfully: {CSV_FILE}")

        elif choice == "4":
            print("\nThank you. Program closed.")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()