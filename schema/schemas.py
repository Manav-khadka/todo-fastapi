def individual_serializer(todo)->dict:
    return {
        "id": str(todo["_id"]),
        "title": todo["title"],
        "description": todo["description"],
        "completed": todo["completed"]
    }

def list_serial(todos)->list:
    return [individual_serializer(todo)for todo in todos]
