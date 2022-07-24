import mysql.connector
# Connect to the database
config = {
    "user" : "winery_user",
    "password": "wendy1981",
    "host": "127.0.0.1",
    "database": "winery",
    "raise_on_warnings": True
}
db = mysql.connector.connect(**config)

#Create cursor to obtain information from the distributors table

cursor = db.cursor()
cursor.execute('SELECT name, wine FROM distributors')

# Create a report of distributors and which wine they sell

distributors = cursor.fetchall()
print("--- LIST OF DISTRIBUTORS AND THE WINE THEY CARRY ---")
print("--- DATE OF REPORT: JULY 2022 ---")
for distributor in distributors:
    print("\nDistributor Name: {}".format(distributor[0]), "\nWine: {}".format(distributor[1]))
print()
print("Press any key to continue...")
print()

# Create a report showing how many distributors are selling each wine

print("--- LIST OF HOW MANY DISTRIBUTORS CARRY EACH WINE ---")
print("--- DATE OF REPORT: JULY 2022 ---")
cursor.execute('SELECT wine, COUNT(wine) AS num FROM distributors GROUP BY wine HAVING COUNT(wine) > 0')
wines = cursor.fetchall()
for wine in wines:
    print("\nNumber of Distributors: {}".format(wine[1]), "\nWine: {}".format(wine[0]))
print()
print("Press any key to continue...")
    
# Create a report of how many barrels of each wine was sold

print()
print("--- EXPECTED SALES (IN BARRELS) VS ACTUAL SALES ---")
print("--- DATE OF REPORT: JULY 2022 ---")
cursor.execute('SELECT wine, SUM(expected_sales) as num, SUM(actual_sales) from distributors GROUP by wine HAVING COUNT(expected_sales) > 0')
sales = cursor.fetchall()
for sale in sales:
    print("\nWine: {}".format(sale[0]), "\nExpected Sales: {}".format(sale[1]), "\nActual Sales: {}".format(sale[2]))
print()
print("Press any key to continue...")

db.close()