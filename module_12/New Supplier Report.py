#Tim Alvarado 7/21/2022 NEW SUPPLIER REPORT

import mysql.connector
import tabulate
from tabulate import tabulate

config = {
    "user" : "winery_user",
    "password": "M@stiff11",
    "host": "127.0.0.1",
    "database": "winery",
    "raise_on_warnings": True
}
db = mysql.connector.connect(**config)

print("\n--- 6 MONTH SUPPLIER DELIVERY REPORT ---                                                  (Report ran on 8/1/2022)")
cursor = db.cursor()
cursor.execute("SELECT name, expected_delivery, actual_delivery, delivery_on_time, delivery_variance FROM suppliers")
supplierList = cursor.fetchall()
print(tabulate(supplierList, headers = ['Supplier Name', 'Expected Delivery Date', 'Actual Delivery Date', 'Late Delivery (Y/N)', 'Number of days Late'], tablefmt = 'pretty'))
