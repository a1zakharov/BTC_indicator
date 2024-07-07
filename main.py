import yfinance as yf
from ta.momentum import WilliamsRIndicator
import telebot
import config
import schedule
import time


bot = telebot.TeleBot(config.API_TOKEN)


def data_btc():
    btc = yf.Ticker("BTC-USD").history(interval='1h', period="1mo").reset_index()[['Datetime', 'Open', 'Close', 'Low', 'High', 'Volume']]
    btc['Williams'] = WilliamsRIndicator(high=btc['High'], low=btc['Low'], close=btc['Close'], lbp= 14, fillna= False).williams_r()

    return btc.tail(1)['Williams'].iloc[0]


def telegram_message():
    value_indicator = data_btc()
    if value_indicator < -80:
        bot.send_message(config.CHANNEL_LOGIN, "🟢BTC in the oversold zone")
    elif value_indicator > -80 and value_indicator < -20:
        bot.send_message(config.CHANNEL_LOGIN, "🔵BTC neutral")
    elif value_indicator  >  -20:
        bot.send_message(config.CHANNEL_LOGIN, "🟡BTC in the overbought zone")
        
schedule.every(1).minutes.do(telegram_message)

while True:
        schedule.run_pending()
        time.sleep(1)