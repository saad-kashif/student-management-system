import json
import os

# File to store all data
DATA_FILE = "student_data.json"

# Initialize data structure if file doesn't exist
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as f:
        default_data = {
            "admin": {"username": "saad", "password": "saad123"},
            "students": {},
            "courses": ["Math", "Science", "History", "English"],
            "grades": {}
        }
        json.dump(default_data, f)

# Load data from file
def load_data():
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

# Save data to file
def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f)

# Admin functions
def admin_login():
    data = load_data()
    print("\nAdmin Login")
    username = input("Username: ")
    password = input("Password: ")
    
    if username == data["admin"]["username"] and password == data["admin"]["password"]:
        admin_menu()
    else:
        print("Invalid credentials!")

def admin_menu():
    while True:
        print("\nAdmin Menu")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Enroll Student in Course")
        print("6. Enter Marks")
        print("7. Generate Report Card")
        print("8. View Top Performers")
        print("9. Logout")
        
        choice = input("Enter choice (1-9): ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            enroll_student()
        elif choice == "6":
            enter_marks()
        elif choice == "7":
            generate_report_card()
        elif choice == "8":
            view_top_performers()
        elif choice == "9":
            break
        else:
            print("Invalid choice!")

def add_student():
    data = load_data()
    print("\nAdd New Student")
    
    student_id = input("Student ID: ")
    if student_id in data["students"]:
        print("Student ID already exists!")
        return
    
    name = input("Name: ")
    department = input("Department: ")
    semester = input("Semester: ")
    password = input("Set password: ")
    
    data["students"][student_id] = {
        "name": name,
        "department": department,
        "semester": semester,
        "password": password,
        "courses": []
    }
    
    save_data(data)
    print("Student added successfully!")

def view_students():
    data = load_data()
    print("\nStudent List")
    
    if not data["students"]:
        print("No students found!")
        return
    
    for student_id, info in data["students"].items():
        print(f"\nID: {student_id}")
        print(f"Name: {info['name']}")
        print(f"Department: {info['department']}")
        print(f"Semester: {info['semester']}")
        print(f"Courses: {', '.join(info['courses']) if info['courses'] else 'None'}")

def update_student():
    data = load_data()
    print("\nUpdate Student Record")
    
    student_id = input("Enter student ID to update: ")
    if student_id not in data["students"]:
        print("Student not found!")
        return
    
    print("\nCurrent Information:")
    print(f"1. Name: {data['students'][student_id]['name']}")
    print(f"2. Department: {data['students'][student_id]['department']}")
    print(f"3. Semester: {data['students'][student_id]['semester']}")
    print(f"4. Password: {data['students'][student_id]['password']}")
    
    field = input("\nEnter field number to update (1-4): ")
    
    if field == "1":
        new_name = input("Enter new name: ")
        data["students"][student_id]["name"] = new_name
    elif field == "2":
        new_dept = input("Enter new department: ")
        data["students"][student_id]["department"] = new_dept
    elif field == "3":
        new_sem = input("Enter new semester: ")
        data["students"][student_id]["semester"] = new_sem
    elif field == "4":
        new_pass = input("Enter new password: ")
        data["students"][student_id]["password"] = new_pass
    else:
        print("Invalid field number!")
        return
    
    save_data(data)
    print("Student record updated successfully!")

def delete_student():
    data = load_data()
    print("\nDelete Student Record")
    
    student_id = input("Enter student ID to delete: ")
    if student_id not in data["students"]:
        print("Student not found!")
        return
    
    confirm = input(f"Are you sure you want to delete {data['students'][student_id]['name']}? (y/n): ")
    if confirm.lower() == 'y':
        del data["students"][student_id]
        
        # Also remove any grades for this student
        if student_id in data["grades"]:
            del data["grades"][student_id]
        
        save_data(data)
        print("Student deleted successfully!")
    else:
        print("Deletion cancelled.")

def enroll_student():
    data = load_data()
    print("\nEnroll Student in Course")
    
    student_id = input("Enter student ID: ")
    if student_id not in data["students"]:
        print("Student not found!")
        return
    
    print("\nAvailable Courses:")
    for i, course in enumerate(data["courses"], 1):
        print(f"{i}. {course}")
    
    try:
        choice = int(input("Select course number: ")) - 1
        if 0 <= choice < len(data["courses"]):
            course = data["courses"][choice]
            if course not in data["students"][student_id]["courses"]:
                data["students"][student_id]["courses"].append(course)
                save_data(data)
                print(f"Enrolled in {course} successfully!")
            else:
                print("Already enrolled in this course!")
        else:
            print("Invalid course number!")
    except ValueError:
        print("Please enter a number!")

def enter_marks():
    data = load_data()
    print("\nEnter Marks")
    
    student_id = input("Enter student ID: ")
    if student_id not in data["students"]:
        print("Student not found!")
        return
    
    if not data["students"][student_id]["courses"]:
        print("Student is not enrolled in any courses!")
        return
    
    print("\nSelect Course:")
    for i, course in enumerate(data["students"][student_id]["courses"], 1):
        print(f"{i}. {course}")
    
    try:
        choice = int(input("Select course number: ")) - 1
        if 0 <= choice < len(data["students"][student_id]["courses"]):
            course = data["students"][student_id]["courses"][choice]
            marks = float(input(f"Enter marks for {course} (0-100): "))
            
            if student_id not in data["grades"]:
                data["grades"][student_id] = {}
            
            data["grades"][student_id][course] = marks
            save_data(data)
            print("Marks entered successfully!")
        else:
            print("Invalid course number!")
    except ValueError:
        print("Please enter valid numbers!")

def generate_report_card():
    data = load_data()
    print("\nGenerate Report Card")
    
    student_id = input("Enter student ID: ")
    if student_id not in data["students"]:
        print("Student not found!")
        return
    
    if student_id not in data["grades"] or not data["grades"][student_id]:
        print("No grades available for this student!")
        return
    
    filename = f"report_card_{student_id}.txt"
    with open(filename, 'w') as f:
        f.write(f"Report Card for {data['students'][student_id]['name']}\n")
        f.write(f"ID: {student_id}\n")
        f.write(f"Department: {data['students'][student_id]['department']}\n")
        f.write(f"Semester: {data['students'][student_id]['semester']}\n\n")
        f.write("Course\t\tMarks\tGrade\n")
        f.write("-------------------------\n")
        
        total = 0
        courses = 0
        
        for course, marks in data["grades"][student_id].items():
            total += marks
            courses += 1
            
            if marks >= 90:
                grade = "A"
            elif marks >= 80:
                grade = "B"
            elif marks >= 70:
                grade = "C"
            elif marks >= 60:
                grade = "D"
            else:
                grade = "F"
                
            f.write(f"{course}\t\t{marks}\t{grade}\n")
        
        percentage = total / courses if courses > 0 else 0
        f.write(f"\nTotal Percentage: {percentage:.2f}%\n")
    
    print(f"Report card generated as {filename}")

def view_top_performers():
    data = load_data()
    print("\nTop Performers")
    
    if not data["grades"]:
        print("No grade data available!")
        return
    
    # Get all courses that have grades
    courses_with_grades = set()
    for student_grades in data["grades"].values():
        courses_with_grades.update(student_grades.keys())
    
    if not courses_with_grades:
        print("No courses with grades available!")
        return
    
    print("\nSelect Course:")
    for i, course in enumerate(courses_with_grades, 1):
        print(f"{i}. {course}")
    
    try:
        choice = int(input("Select course number: ")) - 1
        selected_course = list(courses_with_grades)[choice]
        
        # Collect all grades for this course
        course_grades = []
        for student_id, grades in data["grades"].items():
            if selected_course in grades:
                course_grades.append((student_id, grades[selected_course]))
        
        if not course_grades:
            print("No grades for this course!")
            return
        
        # Sort by marks (descending)
        course_grades.sort(key=lambda x: x[1], reverse=True)
        
        print(f"\nTop Performers in {selected_course}:")
        print("Rank\tID\tName\t\tMarks")
        for rank, (student_id, marks) in enumerate(course_grades[:5], 1):  # Show top 5
            print(f"{rank}\t{student_id}\t{data['students'][student_id]['name']}\t\t{marks}")
            
    except (ValueError, IndexError):
        print("Invalid selection!")

# Student functions
def student_login():
    data = load_data()
    print("\nStudent Login")
    student_id = input("Student ID: ")
    password = input("Password: ")
    
    if student_id in data["students"] and data["students"][student_id]["password"] == password:
        student_menu(student_id)
    else:
        print("Invalid credentials!")

def student_menu(student_id):
    while True:
        print("\nStudent Menu")
        print("1. View Profile")
        print("2. View Courses")
        print("3. View Grades")
        print("4. View Report Card")
        print("5. Logout")
        
        choice = input("Enter choice (1-5): ")
        
        if choice == "1":
            view_profile(student_id)
        elif choice == "2":
            view_courses(student_id)
        elif choice == "3":
            view_grades(student_id)
        elif choice == "4":
            view_report_card(student_id)
        elif choice == "5":
            break
        else:
            print("Invalid choice!")

def view_profile(student_id):
    data = load_data()
    student = data["students"][student_id]
    
    print("\nStudent Profile")
    print(f"ID: {student_id}")
    print(f"Name: {student['name']}")
    print(f"Department: {student['department']}")
    print(f"Semester: {student['semester']}")

def view_courses(student_id):
    data = load_data()
    courses = data["students"][student_id]["courses"]
    
    print("\nEnrolled Courses")
    if courses:
        for course in courses:
            print(f"- {course}")
    else:
        print("Not enrolled in any courses yet.")

def view_grades(student_id):
    data = load_data()
    
    if student_id not in data["grades"] or not data["grades"][student_id]:
        print("\nNo grades available yet.")
        return
    
    print("\nYour Grades")
    print("Course\t\tMarks\tGrade")
    print("-------------------------")
    
    for course, marks in data["grades"][student_id].items():
        if marks >= 90:
            grade = "A"
        elif marks >= 80:
            grade = "B"
        elif marks >= 70:
            grade = "C"
        elif marks >= 60:
            grade = "D"
        else:
            grade = "F"
        
        print(f"{course}\t\t{marks}\t{grade}")

def view_report_card(student_id):
    data = load_data()
    
    if student_id not in data["grades"] or not data["grades"][student_id]:
        print("\nNo grades available to generate report card.")
        return
    
    print("\nReport Card")
    print(f"Name: {data['students'][student_id]['name']}")
    print(f"ID: {student_id}")
    print(f"Department: {data['students'][student_id]['department']}")
    print(f"Semester: {data['students'][student_id]['semester']}")
    print("\nCourse\t\tMarks\tGrade")
    print("-------------------------")
    
    total = 0
    courses = 0
    
    for course, marks in data["grades"][student_id].items():
        total += marks
        courses += 1
        
        if marks >= 90:
            grade = "A"
        elif marks >= 80:
            grade = "B"
        elif marks >= 70:
            grade = "C"
        elif marks >= 60:
            grade = "D"
        else:
            grade = "F"
            
        print(f"{course}\t\t{marks}\t{grade}")
    
    percentage = total / courses if courses > 0 else 0
    print(f"\nTotal Percentage: {percentage:.2f}%")

# Main menu
def main():
    while True:
        print("\nStudent Management System")
        print("1. Admin Login")
        print("2. Student Login")
        print("3. Exit")
        
        choice = input("Enter choice (1-3): ")
        
        if choice == "1":
            admin_login()
        elif choice == "2":
            student_login()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "_main_":
    main() 