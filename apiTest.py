import requests

url = "https://www.tradingvalley.tw/api/stock-mining/symbol-info/NVDA"

headers = {
    "accept": "*/*",
    "accept-language": "en",
    "priority": "u=1, i",
    "sec-ch-ua": "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "Referer": "https://www.growin.tv/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
}

response = requests.get(url, headers=headers)

print(response.status_code)
print(response.json())  # Assuming the response is in JSON format

data = response.json()['data']
print("value: ", data['value'])
print("trend: ", data['trend'])