from fastapi import APIRouter
from models.todos import Todo
from schema.schemas import list_serial
from config.database import collection_name
from bson import ObjectId 

router = APIRouter()

# test
@router.get("/test")
def test():
    return "hi"
# Get all todos
@router.get("/")
async def get_all_todos():
    todos = collection_name.find()
    return list_serial(todos)

# Get a single todo
@router.get("/{id}")
async def get_single_todo(id: str):
    todo = collection_name.find_one({id: id})
    return list_serial(todo)

# Post Request to create a todo
@router.post("/")
async def add_todo(todo:Todo):
    collection_name.insert_one(dict(todo))

