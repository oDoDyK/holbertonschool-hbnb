import pytest
from app import create_app, db

@pytest.fixture
def app():
    app = create_app("testing")
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def token(client):
    client.post("/api/v1/auth/register", json={
        "email": "test@test.com",
        "password": "123456"
    })

    res = client.post("/api/v1/auth/login", json={
        "email": "test@test.com",
        "password": "123456"
    })

    return res.json["access_token"]
