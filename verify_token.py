from fastapi import FastAPI,Depends,Header,HTTPException

app = FastAPI()

def verify_token(token:str=Header(None)):
    if token != "mytoken":
        raise HTTPException(
            status_code=404,
            detail="unauthorizedError"
            )
    return{
        "user" : "User Is Authorized"
    }

@app.get("/secure-data")
def secure_data(user = Depends(verify_token)):
    return{
        "message" : "secure data access",
        "user" : user
    }

# def comman_logic():
#     return{
#         "message" : "comman logic executed"
#     }

# @app.get("/home")
# def home(data=Depends(comman_logic)):
#     return data

def get_current_user():
    return{
        "name" : "harsh"
    }

@app.get("/profile")
def profile(user=Depends(get_current_user)):
    return user

@app.get("/dashboard")
def dashboard(user=Depends(get_current_user)):
    return user

