
# 🎓 Student Management System (Python)

A **Python-based console application** for managing students, courses, grades, and performance.  
Includes both **Admin** and **Student** roles with features like course enrollment, grade entry, and report generation.  

---

## 📌 Features

### 👨‍🏫 Admin Features
- Login with secure credentials  
- Add, update, and delete student records  
- Enroll students in courses  
- Enter marks for students  
- Generate report cards (`report_card_ID.txt`)  
- View top performers in each course  

### 👨‍🎓 Student Features
- Login with student ID and password  
- View profile (ID, name, department, semester)  
- View enrolled courses  
- Check grades and report card  
- Logout securely  

---

## 🛠️ System Design

- **Language:** Python  
- **Data Storage:** JSON (`student_data.json`)  
- **Modules Used:**  
  - `os` → File handling  
  - `json` → Data persistence  

### File Structure
- `Student Management System.py` → Main application  
- `student_data.json` → Stores admin, students, courses, grades  
- `report_card_ID.txt` → Auto-generated report cards  

---

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/student-management-system-python.git
   cd student-management-system-python


2. Run the program:

   ```bash
   python "Student Management System.py"
   ```

3. Default admin credentials:

   ```
   Username: saad
   Password: saad123
   ```

---

## 📊 Example Flow

```
Student Management System
1. Admin Login
2. Student Login
3. Exit
```

* **Admin → Add Student → Enter Marks → Generate Report Card**
* **Student → Login → View Courses → View Grades → View Report Card**

---

## 🧩 Future Improvements

* Add GUI interface with Tkinter or PyQt
* Connect with MySQL database
* Email student report cards automatically

---

## 👥 Contributor

* **Saad Kashif** – BS Computer Science (COMSATS University Islamabad)

---

⭐ *This project enhanced my understanding of Python, file handling, JSON storage, and modular programming.*

