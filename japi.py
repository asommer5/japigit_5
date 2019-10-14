import json
import urllib.request

QUERY_URL = "https://www.alphavantage.co/query?function={REQUEST_TYPE}&apikey={KEY}&symbol={SYMBOL}"
API_KEY = "0D3FP8EMMVK5LJUX"

def _request(symbol, req_type):
        with urllib.request.urlopen(QUERY_URL.format(REQUEST_TYPE=req_type, KEY=API_KEY, SYMBOL=symbol)) as req:
                data = req.read().decode("UTF-8")
        return data

def getStockData(symbol):
        return json.loads(_request(symbol, 'TIME_SERIES_DAILY'))

def main():
        repeat = True
        while repeat == True:
            user_symbol = input("What is the symbol of the stock company? (Enter 'quit' to end.) ")
            if user_symbol == "quit":
                break
            else:
                z = getStockData(user_symbol)["Time Series (Daily)"]["2019-10-11"]
                print(z)
                print("The current price of ", user_symbol, "is ", z['4. close'])
            
main()
