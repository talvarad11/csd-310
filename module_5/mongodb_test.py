from pymongo import MongoClient 

url = "mongodb+srv://admin:admin@cluster0.it9ck.mongodb.net/?retryWrites=true&w=majority"; 


client = MongoClient(url)

db = client.pytech
print("--Pytech Collention List--")
print(db.list_collection_names())

print("\nEnd of Progam, press any key to exit...")











