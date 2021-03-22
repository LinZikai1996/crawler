import requests

url = 'http://www.baidu.com'

response = requests.get(url)
print(len(response.content.decode()))
print(response.content.decode())


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.57'}
# 发送带请求头的请求
response_header = requests.get(url, headers=headers)
print(len(response_header.content.decode()))
print(response_header.content.decode())
