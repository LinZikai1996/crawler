import requests
import json


class King(object):

    def __init__(self, word):
        # url
        self.url = 'https://ifanyi.iciba.com/index.php?c=trans&m=fy&client=6&auth_user=key_ciba&sign=0f70cbecb4e597f6'
        # headers
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.57'
        }
        # data字典
        self.data = {
            'from': 'en',
            'to': 'zh',
            'q': word
        }

    def get_data(self):
        # 发送请求
        response = requests.post(self.url, headers=self.headers, data=self.data)
        return response.content.decode()

    def parse_data(self, data):
        json_data = json.loads(data)
        print(json_data['content']['out'])

    def run(self):
        # 获取响应
        response = self.get_data()
        # 数据解析
        self.parse_data(response)


if __name__ == '__main__':
    king_translation = King('China')
    king_translation.run()
