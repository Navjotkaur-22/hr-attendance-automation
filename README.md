# HR Attendance & Salary Automation (SQL + Python)

## 📌 Project Overview
This project automates monthly HR attendance processing and salary calculation using SQL and Python. It converts raw attendance data into a clean, payroll-ready salary report, eliminating manual calculations and Excel-based errors.

## 🛠️ Tech Stack
Python (Pandas, SQLite)  
SQL (Joins, Aggregations, CASE logic)

## 📂 Input Data
employees.csv – Employee master data including ID, name, department, and monthly salary  
attendance.csv – Daily attendance records with fixed status values (Present, Absent)

## ⚙️ Automation Workflow
1. Load CSV files into a lightweight SQLite database  
2. Aggregate attendance data using SQL  
3. Apply salary deduction logic using Python  
4. Automatically generate a monthly HR salary report

## 💼 Business Logic
Per-day salary = Monthly Salary / 30  
Salary deduction = Absent Days × Per-day Salary  
Final salary = Monthly Salary − Salary Deduction

## 📊 Output
monthly_hr_report.csv – A payroll-ready report containing total working days, absent days, salary deduction, and final payable salary.  
The file is automatically generated inside the `outputs` folder.

## ▶️ How to Run
Run the automation script using:
python scripts/load_and_report.py

## 🚀 Use Case
HR teams  
Payroll processing  
Small companies and startups  
Freelance automation projects

## ⭐ Key Highlights
End-to-end automation (CSV → SQL → Report)  
Clean and scalable business logic  
No manual intervention required  
Real-world HR use case

## 👩‍💻 Author
Navjot Kaur  
Data Science | SQL & Python Automation  

GitHub: https://github.com/Navjotkaur-22  
LinkedIn: https://www.linkedin.com/in/navjot-kaur-b61aab299  
Upwork: https://www.upwork.com/freelancers/~01b30aa09d478b524c
