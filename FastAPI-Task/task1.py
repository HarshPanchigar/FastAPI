from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_user():
    return{
         "message": "Hello FastAPI"
    }

@app.get("/about")
def get_about():
    return{
    "name": "Harsh Panchigar",
    "course": "iMSc IT"
    }

@app.get("/skills")
def get_skill():
    return{
        "skill" : ["python" , "sql" , "Fastapi"]
    }