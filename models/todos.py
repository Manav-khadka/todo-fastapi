from pydantic import BaseModel, Field

class Todo(BaseModel):
    title: str
    description: str
    completed: bool = Field(default=False)
    