from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    fname : str
    lname : str
    age : int

@app.post("/    -user")
def create_user(user:User):
    return {"user-details" : user}
