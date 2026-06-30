from fastapi import FastAPI , HTTPException
from pydantic import BaseModel

app = FastAPI()

todos = []

class Todo(BaseModel):
    id : int
    title : str
    completed : bool = False

@app.post("/todos")
def add_todos(todo : Todo):
    todos.append(todo)
    return {
        "message": "Student created successfully",
        "details" : todo
    }

@app.get("/todos")
def get_details():
    return {
        "Todos" : todos
    }

@app.put("/todos/{user_id}")
def update_user(user_id: int, updated_todo: Todo):
    for index, todo in enumerate(todos):
        if todo.id == user_id:
            todos[index] = updated_todo
            return {
                "message": "Todo updated successfully",
                "details": updated_todo
            }

    raise HTTPException(status_code=404, detail="Todo not found")

@app.delete("/todos/{user_id}")
def delete_todo(user_id: int):
    for index, todo in enumerate(todos):
        if todo.id == user_id:
            deleted_todo = todos.pop(index)
            return {
                "message": "Todo deleted successfully",
                "details": deleted_todo
            }

    raise HTTPException(status_code=404, detail="Todo not found")