from fastapi import FastAPI
app = FastAPI()

@app.get("/products")
def get_products(skip:int,limit:int):
    return{
        "skip" : skip,
        "limit" : limit
    }
