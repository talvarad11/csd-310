#Tim Alvarado 6-25-2022 - Pytech: Updating document

from pymongo import MongoClient 

url = "mongodb+srv://admin:admin@cluster0.it9ck.mongodb.net/?retryWrites=true&w=majority"; 

client = MongoClient(url)

students = client.pytech

print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

docs = students.students.find({})

for doc in docs:
    print("\nStudent ID: ", doc["student_id"], "\nFirst Name: ", doc["first_name"], "\nLast Name: ", doc["last_name"])

print("")

print("-- DISPLAYING UPDATED STUDENT DOCUMENT FROM find_one() Query --")

result = students.students.update_one(
    {"student_id" : 1007},
    {
    "$set": {"last_name" : "Greenleaf"},
    }
)


doc = students.students.find_one({"student_id": 1007})
print("\nStudent ID: ", doc["student_id"], "\nFirst Name: ", doc["first_name"], "\nLast Name: ", doc["last_name"])

print("")

print("\nEnd of Program, press any key to exit...")