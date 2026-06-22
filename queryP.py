from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

users = []
class User(BaseModel):
    name : str
    age : int



@app.post("/users")
def create_user(user:User):
    users.append(user)
    return {
        "message" : "User Created",
        "data" : user
    }

@app.put("/users/{id}")
def update_user(id: int, user: User, notify: bool = False):
    if id < len(users):
        users[id] = user
        return {
            "message": "User Updated",
            "notify" : notify,
            "data": user
        }
    return {"message": "User not found"}

@app.get("/users")
def get_user():
    return users