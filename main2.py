import yfinance as yf
from ta.momentum import WilliamsRIndicator
import telebot
import config
import schedule
import time


def main():
    btc = yf.Ticker("BTC-USD").history(interval='1h', period="1y").reset_index()[['Datetime', 
                                                                                  'Open', 
                                                                                  'Close', 
                                                                                  'Low', 
                                                                                  'High', 
                                                                                  'Volume']]
    btc['WR'] = WilliamsRIndicator(high=btc['High'], low=btc['Low'], 
                                   close=btc['Close'], lbp= 14, fillna= False).williams_r()
    btc['WR<-80'] = btc['WR'] < -80
    res = btc.tail(1)['WR<-80'].iloc[0]
    
    if res == True:
        return '🟢'
    else:
        return '🔵'
       


def telegram_bot():
    bot = telebot.TeleBot(config.API_TOKEN)
    bot.send_message(config.CHANNEL_LOGIN,  main())


schedule.every(65).minutes.do(telegram_bot)

while True:
        schedule.run_pending()
        time.sleep(1)