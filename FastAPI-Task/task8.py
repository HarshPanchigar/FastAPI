from fastapi import FastAPI, status , Depends , Header , HTTPException
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def get_hed(token : str = Header()):
    if token != "mysecret123":
        raise HTTPException(status_code=401,detail="invaild token")
    return{
        "message" : "Access Granted"
    }
    