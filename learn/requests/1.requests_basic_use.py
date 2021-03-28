import requests

url = 'https://www.baidu.com/'
response = requests.get(url)


# 手动设定编码格式
response.encoding = 'utf8'
print(response.encoding)
# 打印源码的string类型
print(response.text)

# 推荐
# response.context 是存储bytes类型的响应源码，可以进行decode操作
print(response.content.decode())

# response的其他属性和方法
print(response.url)
print(response.status_code)
print(response.request.headers)
print(response.headers)
print(response.cookies)
print()

