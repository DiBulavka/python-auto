import requests

# URL веб-сервиса для создания пользователя
url = "https://jsonplaceholder.typicode.com/users"

# Данные, которые мы хотим отправить на сервер в формате JSON
new_user_data = {
    "name": "John Doe",
    "username": "johndoe",
    "email": "johndoe@example.com"
}

# Отправляем POST-запрос с данными
response = requests.post(url, json=new_user_data)

# Проверяем, что ответ имеет статус 201 Created (код для успешного создания ресурса)
if response.status_code == 201:
    created_user_data = response.json()
    print("Пользователь успешно создан:")
    print(created_user_data)
else:
    print(f"Ошибка при создании пользователя. Статус код {response.status_code}")
