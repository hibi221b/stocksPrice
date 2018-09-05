import requests, os, time
from bs4 import BeautifulSoup


class getStocksPrice(object):

    def __init__(self):
        
        now = time.asctime() 
        URL = "https://stocks.finance.yahoo.co.jp/stocks/detail/?code=usdjpy"
        
        
        response = requests.get(URL)
        soup = BeautifulSoup(response.text, 'html.parser')

        stocks_price = soup.select_one(".stoksPrice").string


        if not os.path.exists("./stocksPrice.csv"):
            with open("stocksPrice.csv", "w") as f:
                print("stocksPrice (usd/jpy)", ",", "time", file=f)
                

        with open("stocksPrice.csv", "at") as f:

            print(stocks_price, ",", now, file=f)
    
if __name__ == '__main__':

    getStocksPrice()

