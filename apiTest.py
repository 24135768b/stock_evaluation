import random
import requests

def get_stock_values(stock_symbol: str) -> dict: 

    url = "https://www.tradingvalley.tw/api/stock-mining/symbol-info/" + stock_symbol

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

    # print(response.status_code)
    # print(response.json())  # Assuming the response is in JSON format

    data = response.json()['data']

    if(data["isExist"]):
        keys = ['value', 'trend', 'swing', 'dividend']
        return {key: data[key] for key in keys}
    else:
        return {}


def get_all_tickets():
    # Example with Alpha Vantage (replace with your API key)
    api_key = "CWHPD0K0I6IDKJOR"
    url = f"https://www.alphavantage.co/query?function=LISTING_STATUS&apikey={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        stock_data = response.text
        # Process stock_data to extract tickers (e.g., CSV parsing)
        # Split into lines and extract the symbols
        lines = stock_data.strip().split("\n")  # Split by newline
        symbols = [line.split(",")[0] for line in lines[1:]]  # Skip header and take the first column
        
        # print(symbols) # Print
        # print("numbers: " + str(len(symbols)))
        return symbols
    else:
        print("Failed to fetch data:", response.status_code)

    
# all_tickets:list = get_all_tickets()
# random_stocks:list = random.sample(all_tickets, 5)
# print(random_stocks)  

# for stock in random_stocks:
#     stock_values: dict = get_stock_values(stock)
#     print(stock_values)
stock_values: dict = get_stock_values('NVDA')
print(stock_values)
stock_values: dict = get_stock_values('AOD')
print(stock_values)
if(stock_values):
    print("ddd")