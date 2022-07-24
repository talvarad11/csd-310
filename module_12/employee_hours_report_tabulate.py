# must run "pip install tabulate" in cmd line before trying this

import mysql.connector
from tabulate import tabulate
# Connect to the database
config = {
    "user" : "winery_user",
    "password": "birdbox2022!",
    "host": "127.0.0.1",
    "database": "winery",
    "raise_on_warnings": True
}
db = mysql.connector.connect(**config)
print("--DISPLAYING EMPLOYEE TABLE--")
print("Report pulled : 21 July 2022")
cursor = db.cursor()
cursor.execute("SELECT employee_id, name, department, quarterly_hours_q1, quarterly_hours_q2, quarterly_hours_q3, quarterly_hours_q4, total_hours FROM employees") 
employeelist = cursor.fetchall()
print(tabulate(employeelist, headers=['Employee ID', 'Name', 'Department', 'Quarter 1 Hours', 'Quarter 2 Hours', 'Quarter 3 Hours', 'Quarter 4 Hours','Total Hours'], tablefmt='pretty'))