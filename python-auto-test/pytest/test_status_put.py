import pytest
import requests

# тест с put, обновление объекта
def test_put_request():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    new_data = {
        "title": "Updated Title",
        "body": "Updated body text."
    }
    response = requests.put(url, json=new_data)
    assert response.status_code == 200
    updated_data = response.json()
    assert updated_data["title"] == "Updated Title"
    assert updated_data["body"] == "Updated body text."

# обновление нескольких объектов
@pytest.mark.parametrize("post_id", [1, 2, 3])
def test_put_request_for_multiple_posts(post_id):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    new_data = {
        "title": f"Updated Title {post_id}",
        "body": f"Updated body text {post_id}."
    }
    response = requests.put(url, json=new_data)
    assert response.status_code == 200
    updated_data = response.json()
    assert updated_data["title"] == f"Updated Title {post_id}"
    assert updated_data["body"] == f"Updated body text {post_id}."
