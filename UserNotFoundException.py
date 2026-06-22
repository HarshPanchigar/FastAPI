from fastapi import FastAPI ,HTTPException, Request
from pydantic import BaseModel
from fastapi.responses import JSONResponse

app = FastAPI()

class UserNotFoundException(Exception):
    def __init__(self, name:str):
        self.name = name

#Global erro handle
@app.exception_handler(UserNotFoundException)
def userNotFound(requset:Request,exc:UserNotFoundException):
    return JSONResponse(
        status_code=404,
        content={
            "status" : "Error",
            "message" : f"user {exc.name} not found"
        }
    )

@app.get("/user/{name}")
def get_name(name:str):
    if name != "Harsh":
        raise UserNotFoundException(name)
    return{
        "name" : name
    }



# @app.get("/users/{id}")
def get_user(id:int):
    if id != 1:
        raise HTTPException(
            status_code= 404,
            detail = "User not found"
        )
    return {
        "id" : 1,
        "name" : "Harsh"
    }