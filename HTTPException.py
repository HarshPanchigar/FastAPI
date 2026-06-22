from fastapi import FastAPI , status ,HTTPException
from pydantic import BaseModel

app = FastAPI()

@app.post("/create_user",status_code=status.HTTP_201_CREATED)
def create_user():
    return{
        "message" : "user created"
    }

@app.get("/user")
def get_users():
    return{
        "status" : "succsess",
        "message" : "user fetch",
        "data" : {
            "name" : "Harsh",
            "age" : 20
        }
    }

@app.get("/user/{id}")
def get_user(id:int):
    if id != 1:
        raise HTTPException(
            status_code= 404,
            detail= "user not found"
        )
    return{
        "id" : 1,
        "name" : "harsh"
    }