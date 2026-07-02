from fastapi import FastAPI ,HTTPException
import requests

app = FastAPI()

respons = requests.get("https://jsonplaceholder.typicode.com/posts")

data = respons.json()
print(data)

@app.get("/posts/{post_id}")
def get_posts(post_id:int):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"

    respons = requests.get(url)

    if respons.status_code != 200:
        raise HTTPException(
            status_code=404,
            detail="page not found"
        )
    return respons.json()

@app.get("/posts")
def get_post():
    url = "https://jsonplaceholder.typicode.com/posts"

    respons = requests.get(url)

    return respons.json()