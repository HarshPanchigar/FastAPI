from fastapi import FastAPI ,Request

app = FastAPI()

@app.middleware("http")
async def my_middleware(request:Request,call_next):
    print("Request received")

    respond = await call_next(request)

    print("respond send")

    return respond