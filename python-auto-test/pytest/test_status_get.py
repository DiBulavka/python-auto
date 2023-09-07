import requests
import pytest

# проверка статус кода 200
def test_get_request_status_code():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)
    assert response.status_code == 200

# тест с проверкой json ответа
def test_get_request_json_response():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)
    assert response.status_code == 200
    data = response.json()
    assert "userId" in data
    assert "id" in data
    assert "title" in data
    assert "body" in data

# параметризованый тест
@pytest.mark.parametrize("post_id", [1, 2, 3])
def test_get_request_for_multiple_posts(post_id):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    response = requests.get(url)
    assert response.status_code == 200
