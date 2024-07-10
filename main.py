import yfinance as yf
from ta.momentum import WilliamsRIndicator
import telebot
import config
import schedule
import time
import pandas as pd

bot = telebot.TeleBot(config.API_TOKEN)


def value_williams():
    btc = yf.Ticker("BTC-USD").history(interval='1h', period="1mo").reset_index()[['Datetime', 'Open', 'Close', 'Low', 'High', 'Volume']]
    btc['Williams'] = WilliamsRIndicator(high=btc['High'], low=btc['Low'], close=btc['Close'], lbp= 14, fillna= False).williams_r()

    return btc.tail(1)['Williams'].iloc[0]


def telegram_message():
    value_indicator = value_williams()
    if value_indicator < -80:
        bot.send_message(config.CHANNEL_LOGIN, "🟢BTC in the oversold zone")
    elif value_indicator > -80 and value_indicator < -20:
        bot.send_message(config.CHANNEL_LOGIN, "🔵BTC neutral")
    elif value_indicator  >  -20:
        bot.send_message(config.CHANNEL_LOGIN, "🟡BTC in the overbought zone")
    
    bot.send_message(config.CHANNEL_LOGIN, сreating_message_SUPERT())
        
        
def supertrend():
    csv_supertrend = pd.read_csv(config.link_csv)
    SUPERT_res = csv_supertrend.tail(1)["SUPERT_7_3.0"].iloc[0]
    SUPERTd = csv_supertrend.tail(1)["SUPERTd_7_3.0"].iloc[0]
    
    return [SUPERTd, SUPERT_res]
        
        
def сreating_message_SUPERT():
    SUPERT_res = supertrend()[1].tolist()
    
    SUPERTd = supertrend()[0].tolist()
    if SUPERTd == 1:
        message = "🟢"
    elif SUPERTd == -1:
        message = "🔴"
    
    message += f" {SUPERT_res:.2f}"
    
    return message

        
schedule.every().hour.at(":06").do(telegram_message)
# schedule.every(1).minutes.do(telegram_message)
while True:
        schedule.run_pending()
        time.sleep(1)