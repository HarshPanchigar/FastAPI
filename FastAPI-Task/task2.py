from fastapi import FastAPI

app = FastAPI()

@app.get("/add")
def get_student(num1 : int,num2:int):
    return{
         "sum" : num1 + num2
    }

@app.get("/greet")
def get_data(name : str , age : int | None = None):
    return{
        "name" : name,
        "age" : age
    }
