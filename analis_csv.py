import pandas as pd
import numpy as np


ef = pd.read_csv("btc_data.csv", index_col='Datetime')

print(len(ef))
print(ef[-24:])
print('-------------------------------------------------------------------------------------------------')
wr80 = ef[ef['WR<-80'] == True]
print(len(wr80))
print(wr80[-24:])
