import requests

request=requests.get('http://api.open-notify.org/')

print(request.status_code)

print(request.text)

data=requests.get("http://api.open-notify.org/iss-now.json")

print(data.text)

print(data.status_code)



