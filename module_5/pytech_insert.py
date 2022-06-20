from pymongo import MongoClient 

url = "mongodb+srv://admin:admin@cluster0.it9ck.mongodb.net/?retryWrites=true&w=majority"; 


client = MongoClient(url)

students = client.pytech.get_collection("students")

students.delete_many({})

def insert_one(student):
    return students.insert_one(student).inserted_id
print("-- Insert Statements--")

thorin = {"first_name": "Thorin",
            "last_name": "Oakenshield",
            "student_id": 1007}
thorin_student_id = insert_one(thorin)

print("Inserted student record {} {} into the students collection with document_id {}".format(thorin["first_name"], thorin["last_name"], thorin_student_id))

bilbo = {"first_name": "Bilbo",
            "last_name": "Baggins",
            "student_id": 1008}
bilbo_student_id = insert_one(bilbo)

print("Inserted student record {} {} into the students collection with document_id {}".format(bilbo["first_name"], bilbo["last_name"], bilbo_student_id))

frodo = {"first_name": "Frodo",
            "last_name": "Baggins",
            "student_id": 1009}
frodo_student_id = insert_one(frodo)

print("Inserted student record {} {} into the students collection with document_id {}".format(thorin["first_name"], thorin["last_name"], frodo_student_id))

print("\nEnd of Program, press any key to exit...")



