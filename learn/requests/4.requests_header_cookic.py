import requests

url = 'https://github.com/LinZikai1996'

response = requests.get(url)

headers = {
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.57',
    'Cookie': '_octo=GH1.1.1114592831.1605957696; _device_id=37758880654bf20b240824ca2ff1497e; user_session=tQw8jHUG5-BIejmd44GO1x4fmpdxnp90z4aNktRqGPguGXOj; __Host-user_session_same_site=tQw8jHUG5-BIejmd44GO1x4fmpdxnp90z4aNktRqGPguGXOj; logged_in=yes; dotcom_user=LinZikai1996; has_recent_activity=1; color_mode={"color_mode":"light","light_theme":{"name":"light","color_mode":"light"},"dark_theme":{"name":"dark","color_mode":"dark"}}'
}
response_header = requests.get(url, headers=headers)

with open('tmp/github.html', 'wb') as f:
    f.write(response.content)