import requests
import json

url = "https://api.hh.ru/employers"

response = requests.get(url)

response_pretty = json.dumps(response.json(), indent=4, ensure_ascii=False)
print(response_pretty)                                                       
# форматирование в json

