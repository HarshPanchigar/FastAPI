from fastapi.testclient import TestClient
from pytest import app

client = TestClient(app)

#test home api
def test_home():
    respones = client.get("/")
    # stuscode check
    assert respones.status_code == 200
    #response data check
    assert respones.json() == {"message":"hello world"}

#test add api 
def test_add():
    respones = client.get("/add?a=10&b=10")
    assert respones.status_code == 200
    assert respones.json() == {"result":20}