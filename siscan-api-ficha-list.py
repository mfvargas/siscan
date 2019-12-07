import requests

url = "http://157.245.87.38/api/ficha/List"
token = "<TOKEN>"

payload = "{\n\t\n}"
headers = {
    'Content-Type': "application/json",
    'api-version': "1.0",
    'Authorization': "Bearer {0}".format(token),
    'User-Agent': "PostmanRuntime/7.17.1",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Host': "157.245.87.38",
    'Accept-Encoding': "gzip, deflate",
    'Content-Length': "16",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, data=payload, headers=headers)

with open ('siscan-api-ficha-list.json', 'w', encoding="utf-8") as f:
    f.write(response.text)
