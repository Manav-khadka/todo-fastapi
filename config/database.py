from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

# Define the MongoDB URI
uri = os.getenv("MONGO_URI")

client = MongoClient(uri)

db = client.todo

# Define the collection
collection_name  = db["todo_collection"]
