# test_simple_post_example.py

import requests
import pytest

@pytest.fixture
def base_url():
    return "https://jsonplaceholder.typicode.com/users"

@pytest.fixture
def new_user_data():
    return {
        "name": "John Doe",
        "username": "johndoe",
        "email": "johndoe@example.com"
    }

def test_create_new_user(base_url, new_user_data):
    response = requests.post(base_url, json=new_user_data)
    assert response.status_code == 201
    created_user_data = response.json()
    
    # Проверяем, что созданный пользователь содержит ожидаемые данные
    assert created_user_data["name"] == new_user_data["name"]
    assert created_user_data["username"] == new_user_data["username"]
    assert created_user_data["email"] == new_user_data["email"]
