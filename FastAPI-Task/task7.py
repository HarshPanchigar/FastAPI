from fastapi import FastAPI, status , Depends
from pydantic import BaseModel

app = FastAPI()

def user_name():
    return "Harsh"

@app.get("/")
def user_depend(user : str = Depends(user_name)):
    return{
        "User Name" : user
    }