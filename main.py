import yfinance as yf
import pandas as pd
from ta.momentum import WilliamsRIndicator
import schedule
import time


def main():
    btc = yf.Ticker("BTC-USD").history(interval='1h', period="1y").reset_index()[['Datetime', 'Open', 'Close', 'Low', 'High', 'Volume']]
    btc['WR'] = WilliamsRIndicator(high=btc['High'], low=btc['Low'], close=btc['Close'], lbp= 14, fillna= False).williams_r()
    btc['WR<-80'] = btc['WR'] < -80
    btc.to_csv('btc_data.csv')
    print('🟢', end='')
    
    return btc

# print(main().tail(50))

schedule.every().minute.at(":46").do(main)

while True:
        schedule.run_pending()
        time.sleep(1)
    