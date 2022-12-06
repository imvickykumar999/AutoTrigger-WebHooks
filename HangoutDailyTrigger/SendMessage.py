import requests

from requests.structures import CaseInsensitiveDict

url = "https://chat.googleapis.com/v1/spaces/pgbmrEAAAAE/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=5HcNVyaAsxdbdEZpkWlofb__9puEFtj8fe8r7VSta4g%3D"

headers = CaseInsensitiveDict()

headers["Content-Type"] = "application/json"

data = '{ "text" : "Coffee ?", "cards": [ { "sections": [ { "widgets": [ { "image": { "imageUrl": "https://i.ytimg.com/vi/NlyXpQYBS8Y/maxresdefault.jpg", "onClick": { "openLink": { "url": "https://vickykumar999.postman.co/workspace/API-Design~79299363-cc08-4753-b965-81d16fdf0cf4/collection/21969867-93dc1a1a-ea1c-40d0-aea0-22e1121b3ed3?action=share&creator=21969867" } } } } ] } ] } ] }'

resp = requests.post(url, headers=headers, data=data)

print(resp.status_code)

