import datetime
import pprint

import pymongo as pyM

client = pyM.MongoClient("mongodb+srv://pymongo:pymongo@cluster0.6vhibth.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db = client.test
collections = db.test_collection
print(db.test_collection)


# definição de infor para compor o doc
post = {
    "author": "mike",
    "text": "My first mongodb application based on python",
    "tags": ["mongodb","python3","pymongo"],
    "date": datetime.datetime.utcnow()
}

# preparando para submeter as infos
posts = db.posts
post_id = posts.insert_one(post).inserted_id
print(post_id)

pprint.pprint(db.posts.find_one())

new_post = [{
            "author": "Mike",
            "text": "Another post",
            "tags": ["bulk", "post", "insert"],
            "date": datetime.datetime.utcnow()},
            {
            "author": "Joao",
            "text": "Post from joao. new post available",
            "title": "mongo is fun",
            "date": datetime.datetime(2024, 11, 10, 10, 45)}]

result = posts.insert_many(new_post)
print(result.insrted_ids)

pprint.pprint(db.posts.find_one({"author": "mike"}))

print("\n Documento presente na coleção posts")
for posts in posts.fild():
    pprint.pprint(post)