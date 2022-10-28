from fastapi.testclient import TestClient
from main import app
import pytest
import json

client = TestClient(app)

def test_flat_get():
    response = client.get("/flats")
    assert response.status_code == 200

def test_flat_create():
    data = {"status":"empty", "rooms":3,"halls":2, "floor_no":7, "monthly_rent":20000, "sqft_area":200}
    response = client.post("/flats", json.dumps(data))
    assert response.status_code == 201
    assert response.json()['status'] == "empty"


