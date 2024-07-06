import schedule
import time
import datetime
import indecator
from ta.momentum import WilliamsRIndicator
import yfinance as yf
import telebot
import config


def main():
    bot = telebot.TeleBot(config.API_TOKEN)
    btc = yf.Ticker("BTC-USD").history(interval='1h', period="1y").reset_index()[['Datetime', 
                                                                                  'Open', 
                                                                                  'Close', 
                                                                                  'Low', 
                                                                                  'High', 
                                                                                  'Volume']]
    btc['WR'] = WilliamsRIndicator(high=btc['High'], low=btc['Low'], 
                                   close=btc['Close'], lbp= 14, fillna= False).williams_r()
    btc['WR<-80'] = btc['WR'] < -80
    res = btc.tail(1)['WR'].iloc[0] 
    if res < -80:
        bot.send_message(config.CHANNEL_LOGIN, "🟢BTC in the oversold zone")
    elif res > -80 and res < -20:
        bot.send_message(config.CHANNEL_LOGIN, "🔵BTC neutral")
    elif res  >  -20:
        bot.send_message(config.CHANNEL_LOGIN, "🟡BTC in the overbought zone")

    
schedule.every(61).minutes.do(main)

while True:
        schedule.run_pending()
        time.sleep(1)