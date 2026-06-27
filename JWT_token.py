from fastapi import FastAPI, HTTPException, Depends ,Header
from jose import jwt
from datetime import datetime ,timedelta ,timezone

app = FastAPI()

SECREATE_KEY = "MySECRET_KEY"

ALGORITHM = "HS256"

#create token
def create_token(data:dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=30)
    to_encode.update({
        "exp" : expire
    })
    token = jwt.encode(to_encode,SECREATE_KEY,algorithm=ALGORITHM)
    return token

@app.post("/")
def login(userName : str , password : str):
    if userName != "admin" or password != "1234":
        raise HTTPException(
            status_code=401,
            detail="Invaild username and password"
        )
    token = create_token({
        "sub" : userName,
        "password" : password
    })
    return{
        "access_token" : token 
    }

#token veify_token
def veify_token(token:str = Header(None)):
    try:
        payload = jwt.decode(token,SECREATE_KEY,algorithms=[ALGORITHM])
        return payload
    except:
        raise HTTPException(
            status_code=401,
            detail="Invaild or expired token"
        )
    
#protected route
@app.get("/dashboard")
def secure(user = Depends(veify_token)):
    return{
        "message" : "secure data accessed",
        "user" : user
    }