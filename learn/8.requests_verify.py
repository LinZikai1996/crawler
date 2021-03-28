import requests

url = 'https://sam.huat.edu.cn:8443/selfervice'
response = requests.get(url, verify=False)
print(response.content.decode())