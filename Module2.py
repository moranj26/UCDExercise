import requests

request=requests.get('http://api.open-notify.org/')

print(requests.status_code)

print(request.text)