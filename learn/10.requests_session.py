import requests
import re

def log():
    # session
    session = requests.session()

    # header
    session.headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.63'
    }

    # url_1
    url_1 = 'https://github.com/login'
    # 发送请求，获取响应
    result_1 = session.get(url_1).content.decode()
    # 正则提取
    print(result_1)
    token = re.findall('name = "authenticity_token" value = "(.*?)"', result_1)

    print(token)

if __name__ == '__main__':
    log()