import requests

for i in requests.get('http://127.0.0.1:8000/api/employee/').json():
    print(i['username'])
