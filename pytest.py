from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def home():
    return{
        "message" : "hello world"
    }

@app.get("/add")
def add(a : int , b : int):
    return{
        "result" : a + b
    }