import requests

# URL ресурса, который мы хотим обновить
url = "https://jsonplaceholder.typicode.com/posts/1"

# Новые данные, которые мы хотим использовать для обновления ресурса
updated_data = {
    "title": "Updated Title",
    "body": "Updated body text."
}

# Отправляем PUT-запрос с обновленными данными
response = requests.put(url, json=updated_data)

# Проверяем, что ответ имеет статус 200 OK (или другой подходящий статус)
if response.status_code == 200:
    updated_resource_data = response.json()
    print("Ресурс успешно обновлен:")
    print(updated_resource_data)
else:
    print(f"Ошибка при обновлении ресурса. Статус код {response.status_code}")
