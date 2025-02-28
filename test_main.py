from fastapi.testclient import TestClient
from main import app  # Import FastAPI app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "Word"}  

def test_print_this():
    response = client.get("/print/print_this")
    assert response.status_code == 200
    assert response.json() == {"this": "print_this"} 