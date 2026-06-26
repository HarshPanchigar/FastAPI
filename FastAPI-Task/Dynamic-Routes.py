from fastapi import FastAPI
app = FastAPI()

@app.get("/users/{user_id}")
def get_user(user_id:int):
    return{
        "user_id" : user_id
    }

@app.get("/students/{students}")
def get_std(students:str):
    return{
        "user_id" : students
    }