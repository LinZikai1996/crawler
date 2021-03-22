import requests

url = 'https://www.baidu.com/'

proxies = {
    'http': 'http://171.35.212.136:9999',
    #'https': 'https://171.35.212.136:9999'
}

response = requests.get(url, proxies=proxies)

print(response.content.decode())
