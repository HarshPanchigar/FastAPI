from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def home():
    return {"Message" : "Welcome to fastapi"}

#About rout
@app.get("/about")
def about():
    return {"about" : "Hii from fastAPI"}

#users route
@app.get("/users")
def users():
    return {"users" : ["mohit", "sumit" , "rohit"]}

# @app.get("/user/{user_id}")
# def user(user_id:int):
#     return {"User" : user_id}

@app.get("/user")
def user_n(name: str | None = None):
    return {"Name" : name}

@app.get("/product")
def pruduct(limit : int = 10):
    return {"Limit" : limit}

@app.get("/items")
def items(name: str | None = None, price: int = 0):
    return {
        "name": name,
        "price": price
    }

@app.post("/get_user")
#def get_user(name : str , age : int):
    # return {
    #     "name" : name,
    #     "age" : age
    # }

@app.post("/get_users")
def get_users(user : dict):
    return {
        "message" : "User created successfully",
        "user" : user
    }

class User(BaseModel):
    fname : str
    lname : str
    age : int

@app.post("/    -user")
def create_user(user:User):
    return {"user-details" : user}

#------------------------------------------------------------------------------------
#Nested JSON
class Address(BaseModel):
    city : str
    pincode : int

class user(BaseModel):
    name :  str
    age : int
    address : Address

@app.post("/get_user")
def get_user(user:user):
    return {
        "Message" : "User created",
        "User" : user
    }