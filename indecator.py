import pandas as pd
import config
import telebot
import time
import schedule

bot = telebot.TeleBot(config.API_TOKEN)

def indicator():
    data_btc = pd.read_csv("btc_data.csv")
    i = data_btc.tail(1)['WR<-80'].iloc[0]

    if i == True:
        mess = '🟢'
        print(mess, end='')
        bot.send_message(config.CHANNEL_LOGIN, mess)
        time.sleep(1)
    else:
        mess = '🔴'
        print(mess, end='')
