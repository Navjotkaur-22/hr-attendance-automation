import os
import sqlite3
import pandas as pd

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "hr_attendance.db")
DATA_DIR = os.path.join(BASE_DIR, "data")
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")

os.makedirs(OUTPUT_DIR, exist_ok=True)

# Connect SQLite
conn = sqlite3.connect(DB_PATH)

# Load CSVs
employees = pd.read_csv(os.path.join(DATA_DIR, "employees.csv"))
attendance = pd.read_csv(os.path.join(DATA_DIR, "attendance.csv"))

# Save to SQL
employees.to_sql("employees", conn, if_exists="replace", index=False)
attendance.to_sql("attendance", conn, if_exists="replace", index=False)

# Attendance summary
query = """
SELECT 
    e.employee_id,
    e.employee_name,
    e.department,
    e.monthly_salary,
    COUNT(a.date) AS total_days,
    SUM(CASE WHEN a.status = 'Absent' THEN 1 ELSE 0 END) AS absent_days
FROM employees e
LEFT JOIN attendance a ON e.employee_id = a.employee_id
GROUP BY e.employee_id;
"""

df = pd.read_sql(query, conn)

# Salary calculation
df["per_day_salary"] = df["monthly_salary"] / 30
df["salary_deduction"] = df["absent_days"] * df["per_day_salary"]
df["final_salary"] = df["monthly_salary"] - df["salary_deduction"]

# Save report
output_path = os.path.join(OUTPUT_DIR, "monthly_hr_report.csv")
df.to_csv(output_path, index=False)

conn.close()

print("✅ HR monthly report generated:", output_path)
