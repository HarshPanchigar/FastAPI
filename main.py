from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# import os
# from dotenv import load_dotenv
from config import settings



app = FastAPI()

# load_dotenv()
# SECRET_KEY = os.getenv("SECRET_KEY")
# DB_URL = os.getenv("DB_URL")
origins = settings.origins

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins.split(",") if origins else [],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

@app.get("/")
def get_form():
    return{
        "message":"CORS ENABLE API"
    }

