from pathlib import Path
import sys

from fastapi.testclient import TestClient

ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_DIR))

from app.main import app  # noqa: E402

client = TestClient(app)


def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "FastAPI Auth API is running"


def test_register_login_and_me_flow():
    user_payload = {
        "email": "testuser@example.com",
        "username": "test_user",
        "password": "strongpassword123",
    }

    register_response = client.post("/register", json=user_payload)
    assert register_response.status_code in (200, 400)

    login_response = client.post(
        "/login",
        json={
            "email": user_payload["email"],
            "password": user_payload["password"],
        },
    )
    assert login_response.status_code == 200

    token = login_response.json()["access_token"]

    me_response = client.get(
        "/me",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert me_response.status_code == 200
    assert me_response.json()["email"] == user_payload["email"]


def test_wrong_password_fails():
    response = client.post(
        "/login",
        json={"email": "testuser@example.com", "password": "wrong-password"},
    )
    assert response.status_code == 401
