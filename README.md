# Автоматическая публикация значения индикатора в телеграмм какнал
# Automatic publication of the indicator value in the telegram channel

Функционал даннй программы заключается в том, что он использует библиотеки telebot и yfinance для взаимодействия с Telegram-ботом и получения данных о криптовалюте Bitcoin соответственно.

Создается объект bot с использованием токена API Telegram-бота. Затем загружаются данные о Bitcoin с интервалом в 1 час. Из этих данных выбираются столбцы 'Datetime', 'Open', 'Close', 'Low', 'High', 'Volume'.

Далее вычисляется индикатор WilliamsRIndicator для столбца 'High', 'Low', 'Close' с периодом 14. Результат сохраняется в столбце 'Williams'.

Далее функция telegram_message отправляет в телеграмм сообщение 
"🟢BTC in the oversold zone", "🔵BTC neutral" или "🟡BTC in the overbought zone". 

***

The functionality of this program is that it uses the telebot and finance libraries to interact with Telegram and receive data about the Bitcoin cryptocurrency, respectively.

A bot object is created using the Telegram bot API token. Then the Bitcoin data is uploaded with an interval of 1 hour. The columns 'Datetime', 'Open', 'Close', 'Low', 'High', 'Volume' are selected from this data.

Next, the Williams R Indicator is calculated for the column 'High', 'Low', 'Close' with a period of 14. The result is saved in the 'Williams' column.

Next, the telegram_message function sends a telegram message
"🟢BTC in the oversold zone", "🔵BTC neutral" or "🟡BTC in the overbought zone".