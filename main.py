import yfinance as yf
import pandas as pd
from ta.momentum import WilliamsRIndicator



def main():
    btc = yf.Ticker("BTC-USD").history(interval='1h', period="1y").reset_index()[['Datetime', 'Open', 'Close', 'Low', 'High', 'Volume']]
    btc['WR'] = WilliamsRIndicator(high=btc['High'], low=btc['Low'], close=btc['Close'], lbp= 14, fillna= False).williams_r()
    btc['WR<-80'] = btc['WR'] < -80
    btc.to_csv('btc_data.csv')
    print('🟢', end='')
    
    return btc

# print(main().tail(50))


if __name__ == '__main__':
    main()