import datetime

res = -18
    
if res < -80:
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "res in the oversold zone")
elif res > -80 and res < -20:
    print(datetime.datetime.now().strftime("%Y-%m-%d  %H:%M:%S"),  "res neutral")
elif res  >  -20:
    print(datetime.datetime.now().strftime("%Y-%m-%d  %H:%M:%S"),  "res in the overbought zone")