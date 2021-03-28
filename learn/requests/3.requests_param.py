import requests

# url里直接带参数
url = 'https://www.baidu.com/s?wd=python'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.57'}


response = requests.get(url, headers=headers)

with open('tmp/baidu.html', 'wb') as f:
    f.write(response.content)

url = 'https://www.baidu.com/s?'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.57'}

data = {'wd': 'python'}
response = requests.get(url, headers=headers, params=data)

with open('tmp/baidu1.html', 'wb') as f:
    f.write(response.content)
