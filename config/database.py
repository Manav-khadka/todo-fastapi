from pymongo import MongoClient

# Define the MongoDB URI

client = MongoClient("mongodb+srv://manav:manav@todo.diluwwn.mongodb.net/?retryWrites=true&w=majority&appName=todo")

db = client.todo

# Define the collection
collection_name  = db["todo_collection"]
