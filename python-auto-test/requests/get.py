import requests

# URL веб-сервиса
url = "https://jsonplaceholder.typicode.com/users/1"

# Ожидаемые данные
expected_data = {
    "id": 1,
    "name": "Leanne Graham",
    "username": "Bret",
    "email": "Sincere@april.biz",
    # Другие ожидаемые поля...
}

# Отправляем GET-запрос
response = requests.get(url)

# Проверяем, что ответ имеет статус 200 OK
if response.status_code == 200:
    # Парсим JSON-ответ
    user_data = response.json()
    
    # Проверяем, что данные соответствуют ожиданиям
    if user_data == expected_data:
        print("Тест прошел успешно. Данные верны.")
    else:
        print("Тест не прошел. Данные не соответствуют ожиданиям.")
else:
    print(f"Тест не прошел. Получен статус код {response.status_code}")
