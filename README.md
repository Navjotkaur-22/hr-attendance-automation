Title: HR Attendance & Salary Automation (SQL + Python)

Overview:
Automated HR attendance processing system that converts raw attendance CSVs into a monthly, decision-ready salary report using SQL aggregation and Python automation. Eliminates manual calculations and Excel formulas.

Tech Stack:

Python (Pandas, SQLite)

SQL (joins, aggregation, CASE logic)

Input:

employees.csv — employee master data

attendance.csv — daily attendance (Present/Absent)

Automation Flow:

Load CSVs → SQLite

SQL aggregation (total days, absent days)

Python business logic (per-day salary, deductions)

Auto-generate final HR report (CSV)

Business Rules:

Per-day salary = monthly_salary / 30

Salary deduction = absent_days × per-day salary

Output:

outputs/monthly_hr_report.csv (payroll-ready)

How to Run:

python scripts/load_and_report.py


Result:
A clean, payroll-ready report with final payable salary per employee.