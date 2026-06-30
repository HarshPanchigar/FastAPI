from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    username: str
    email: str


@app.post("/register", status_code=status.HTTP_201_CREATED)
def register_user(user: User):
    return {
        "message": "User registered successfully"
    }