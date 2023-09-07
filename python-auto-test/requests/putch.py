import requests

# URL ресурса, который мы хотим частично обновить
url = "https://jsonplaceholder.typicode.com/posts/1"

# Часть данных, которую мы хотим обновить
partial_update_data = {
    "title": "Updated Title"
}

# Отправляем PATCH-запрос с обновленными данными
response = requests.patch(url, json=partial_update_data)

# Проверяем, что ответ имеет статус 200 OK (или другой подходящий статус)
if response.status_code == 200:
    updated_resource_data = response.json()
    print("Ресурс успешно частично обновлен:")
    print(updated_resource_data)
else:
    print(f"Ошибка при частичном обновлении ресурса. Статус код {response.status_code}")
