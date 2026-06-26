from fastapi import FastAPI

app = FastAPI()

@app.get("/greet")
def get_greet(name:str = "Guest"):
    return {
        "message" : f"Hello {name}"
    }