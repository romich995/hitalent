from app import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_add_question():
    response = client.post("/questions/", json={"text": "Зачем я задал данный вопрос?"})

    assert  response.status_code == 201
    assert response.json()["text"] == "Зачем я задал данный вопрос?"