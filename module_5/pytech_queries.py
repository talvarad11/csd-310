from pymongo import MongoClient 

url = "mongodb+srv://admin:admin@cluster0.it9ck.mongodb.net/?retryWrites=true&w=majority"; 

client = MongoClient(url)

students = client.pytech.get_collection("students")

students.find({})

print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

docs = students.find({})

for doc in docs:
    print("\nStudent ID: ", doc["student_id"], "\nFirst Name: ", doc["first_name"], "\nLast Name: ", doc["last_name"])

print("")

print("-- DISPLAYING STUDENTR DOCUMENTS FROM fine_one() QUERY --")
student_name_1 = students.find_one({"student_id": 1008})
print("\nStudent ID: ", student_name_1["student_id"], "\nFirst Name: ", student_name_1["first_name"], "\nLast Name: ", student_name_1["last_name"])

print("")




print("\nEnd of Program, press any key to exit...")

