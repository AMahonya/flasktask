import requests
import json

url = 'http://127.0.0.1:5000/tasks'
urlid = 'http://127.0.0.1:5000/tasks/29'

data = {
    "title": "Новая задача4",
    "description": "Описание 2",
    "status": "incomplete",  #'completed', 'incomplete'
    "priority": "high",  #'low', 'medium', 'high'
    "deadline": "2024-03-25"  #YYYY-MM-DD
}
response = requests.post(url, json=data)
# responseput = requests.put(urlid, json=data)
# responsedel = requests.delete(urlid)

if response.status_code == 201:
    # if responseput.status_code == 200:
    print("Task created successfully:", response.content.decode('utf-8', errors='replace')), response.json()
    # print("Task deleted successfully:", responsedel.json())
    # print("Task updated successfully:", responseput.json())
# else:
#     print(f"Error: {responseput.status_code} - {responseput.text}")
else:
    print(f"Error: {response.status_code} - {response.text}")
