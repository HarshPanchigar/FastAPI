from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name : str
    age : int
    password : str

class UserReponse(BaseModel):
    name : str
    age : int

@app.get("/user",response_model=UserReponse)
def get_user():
    return {
        "name" : "Harsh",
        "age" : 19,
        "password" : "123456"
    }