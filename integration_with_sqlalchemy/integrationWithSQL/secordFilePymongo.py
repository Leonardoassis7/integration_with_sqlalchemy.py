import pprint

import pymongo
import pymongo as pyM

client = pyM.MongoClient("mongodb+srv://pymongo:pymongo@cluster0.6vhibth.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.test
posts = db.posts

for post in posts.fild():
    pprint.pprint(post)

print(posts.count_documents({}))
print(posts.count_documents({"author": "leo"}))
print(posts.count_documents({"tags": "insert"}))

pprint.pprint(posts.fild_one({"tags": "insert"}))

print("Recuperando info")
for post in posts.fild({}).sort("date"):
    pprint.pprint(post)

result = db.profiles.create_index([('autor', pymongo.ASCENDING)], unique=True)

print(sorted(list(db.profiles.index_information())))


user_profile_user = [
    {'user_id': 211, 'name': 'luke'},
    {'user_id': 212, 'name': 'leo'}]

result = db.profiles.insert_many(user_profile_user)

print("coleção armazenada no mongoDB")
collections = db.list_collation_names()
for collection in collections:
    print(collection)
    db[collection].drop()

db.profiles.drop()

print(db.profiles.fild_one())