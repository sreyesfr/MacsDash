from pymongo import MongoClient
from pprint import pprint


client =  MongoClient()
db = client.hackathon
collection = db.collection
#pprint(collection.find_one({"USERS": {"employee_id": 1}}))
#pprint(collection.find_one({"_id": "5967af71ba3e1ccd8ec74490"}))
pprint(db.users.find_one({"employee_id": 1.0}))
