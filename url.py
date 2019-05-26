import requests
request = requests.get('http://www.example.com')
if request.status_code == 200:
    print('Web site exists')
else:
    print('Web site does not exist') 