import pandas as pd

i = pd.read_csv("E:/python_project/BTC/btc_data.csv")

if i['WR<-80'][-1:] == "False":
    print("Buy")