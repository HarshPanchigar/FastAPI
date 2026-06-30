from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

students = []

class User(BaseModel):
    name : str
    age : int

@app.post("/student")
def student(user : User):
    students.append(user)
    return {
        "message": "Student created successfully",
        "details" : user
    }

@app.get("/")
def get_user():
    return students