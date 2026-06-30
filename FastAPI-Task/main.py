from fastapi import FastAPI, status , Depends , Header , HTTPException
from pydantic import BaseModel
from jose import jwt
from datetime import datetime , timezone ,timedelta


app = FastAPI()

SECETE_KEY = "MYKEY1234"
ALGORITHM = "HS256"

#create token 
def create_token(data:dict):
    to_encode = data.copy()
    expiry = datetime.now(timezone.utc) + timedelta(minutes=30)
    to_encode.update({
        "exp" : expiry
    })
    token = jwt.encode(to_encode,SECETE_KEY,algorithm=ALGORITHM)
    return token

@app.post("/")
def login(username:str,password:str):
    if username != "admin" or password != "1234":
        raise HTTPException(
            status_code=401,
            detail="invaild input"
        )
    token = create_token({
        "sub" : username,
        "password" : password
    })

    return token

#verify_token
def verify_token(token : str = Header(None)):
    try :
        payload = jwt.decode(token,SECETE_KEY,algorithms=[ALGORITHM])
        return payload
    except:
        raise HTTPException(status_code=401,detail="token not found")
    
#protected route access
@app.get("/protected")
def protect(user = Depends(verify_token)):
    return{
        "message" : "access protected route successfully...",
        "user" : user
    }