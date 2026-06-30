from fastapi import FastAPI , HTTPException
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    email: str
    password: str

class user_details(BaseModel):
    id : int
    name : str
    email : str


@app.get("/",response_model=user_details)
def get_user():
    return{
    "id": 1,
    "name": "Harsh",
    "email": "harsh@gmail.com",
    "password": "123456"
}