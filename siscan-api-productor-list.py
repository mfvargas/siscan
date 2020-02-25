import requests

url = "http://157.245.87.38/api/productor/List"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiIzOSIsInN1YiI6InNpZ2NhdGllIiwiZW1haWwiOiJtZnZhcmdhc0BnbWFpbC5jb20iLCJEZWxlZ2FjaW9uIjoiMCIsIkZpbHRlclJvdyI6IjUiLCJGaWx0ZXJWYWx1ZSI6IjAiLCJleHAiOjE2MDM5Mjk2MDAsImlzcyI6ImNhdGllLmFjLmNyIiwiYXVkIjoiY2F0aWUuYWMuY3IifQ.IP9dbnGdQLCpDJIRU-3Y7-UYYP_GsRlovplWiOJKFtU"

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

with open ('siscan-api-productor-list.json', 'w', encoding="utf-8") as f:
    f.write(response.text)