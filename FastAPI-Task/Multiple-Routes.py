from fastapi import FastAPI
app = FastAPI()

# GET /about
# GET /contact

@app.get("/about")
def get_about():
    return{
        "name" : "Harsh",
        "age" : 19,
        "email" : "harsh@gmail.com"
    }

@app.get("/contact")
def get_contact():
    return{
        "email" : "harsh@gmail.com",
        "mobile" : 6363636363
    }
