#Tim Alvarado 6-25-2022 - Pytech: Deleting documents

from pymongo import MongoClient 

url = "mongodb+srv://admin:admin@cluster0.it9ck.mongodb.net/?retryWrites=true&w=majority"; 

client = MongoClient(url)

students = client.pytech

print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

docs = students.students.find({})

for doc in docs:
    print("\nStudent ID: ", doc["student_id"], "\nFirst Name: ", doc["first_name"], "\nLast Name: ", doc["last_name"])

print("")

def insert_one(student):
    return students.insert_one(student).inserted_id
newAdd = {"student_id": 1010,
    "first_name": "Peter",
    "last_name": "Jackson"
}

new_Id = students.students.insert_one(newAdd).inserted_id

print("")

print("-- INSERT STATEMENTS --")

print("")

print("Inserted student record {} {} into the students collection with document_id {}".format(newAdd["first_name"], newAdd["last_name"], new_Id))

print("")

print("-- DISPLAYING NEW STUDENT LIST DOC --")

print("")

docs = students.students.find({})
for doc in docs:
    print("\nStudent ID: ", doc["student_id"], "\nFirst Name: ", doc["first_name"], "\nLast Name: ", doc["last_name"])

print("")

students.students.delete_one({"student_id": 1010})


print("-- DELETED STUDENT ID: 1010 --")

docs = students.students.find({})
for doc in docs:
    print("\nStudent ID: ", doc["student_id"], "\nFirst Name: ", doc["first_name"], "\nLast Name: ", doc["last_name"])

print("")

print("\nEnd of Program, press any key to exit...")

print("Terminated with with code 0.")