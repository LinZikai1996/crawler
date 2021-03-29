import requests
import jsonpath
import json

headers = {
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.63'
}

response = requests.get('https://www.lagou.com/lbs/getAllCitySearchLabels.json', headers=headers)

dict_data = json.loads(response.content)

print(jsonpath.jsonpath(dict_data, "$..name"))
