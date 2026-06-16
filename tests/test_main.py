import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.database import SessionLocal, engine
from src import models

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Task Manager API", "status": "running"}

def test_register():
    response = client.post(
        "/register",
        json={"email": "test@example.com", "password": "testpassword123"}
    )
    assert response.status_code == 200
    assert "user_id" in response.json()

def test_register_duplicate():
    # Первая регистрация
    client.post(
        "/register",
        json={"email": "duplicate@example.com", "password": "testpassword123"}
    )
    # Вторая регистрация (дубликат)
    response = client.post(
        "/register",
        json={"email": "duplicate@example.com", "password": "testpassword123"}
    )
    assert response.status_code == 400
    assert "detail" in response.json()

def test_login():
    # Сначала регистрируем пользователя
    client.post(
        "/register",
        json={"email": "login@example.com", "password": "testpassword123"}
    )
    # Пытаемся войти
    response = client.post(
        "/token",
        data={"username": "login@example.com", "password": "testpassword123"}
    )
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"

def test_login_wrong_password():
    # Сначала регистрируем пользователя
    client.post(
        "/register",
        json={"email": "wrongpass@example.com", "password": "testpassword123"}
    )
    # Пытаемся войти с неправильным паролем
    response = client.post(
        "/token",
        data={"username": "wrongpass@example.com", "password": "wrongpassword"}
    )
    assert response.status_code == 401
