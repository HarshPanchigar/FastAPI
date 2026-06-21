from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

todos = []

class Todo(BaseModel):
    id : int
    title : str
    completed : bool

@app.post("/todos")
def create_todo(todo:Todo):
    todos.append(todo)
    return{
        "message" : "Todo add",
        "Data" : todo
    }

@app.get("/todos")
def get_datas():
    return todos

@app.get("/todos/{todo_id}")
def get_data(todo_id:int):
    for i in todos:
        if i.id == todo_id:
            return i
    return {"error" : "Todo not found"}

@app.put("/todos/{todo_id}")
def update_todo(todo_id:int,updated_todo:Todo):
    for i , todo in enumerate(todos):
        if todo.id == todo_id:
            todos[i] = updated_todo
            return {
                "message" : "Data Updated",
                "data" : updated_todo
            }
    return {"Error" : "Todos Not found"}

@app.delete("/todos/{id}")
def delete_user(id:int):
    for i , todo in enumerate(todos):
        if todo.id == id:
            todos.pop(i)
    return {"info" : "Data deleted"}