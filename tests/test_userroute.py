from fastapi.testclient import TestClient
import json
from main import app


client = TestClient(app)
 
def test_user():
    data = {"username":"testuser6","email":"testuser6@gmail.com","password":"testing123","is_superuser":False}
    response = client.post("/", json.dumps(data))
    assert response.status_code == 200
    assert response.json()['username'] == "testuser6"