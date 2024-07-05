import schedule
import time
import datetime
import main
import indecator

def i():
    main.data_parc()
    time.sleep(5)
    indecator.indicator()
    current_time = datetime.datetime.now().time()
    print("Hello World!", current_time)
    print('🟢', end='')

schedule.every(65).minutes.do(i)

while True:
        schedule.run_pending()
        time.sleep(1)