# CryptoArbit-bot
## My first project, date of creation: September 2021


## Install dependencies

```
pip install -r requirements.txt
```

## Setup .env keys

```
QIWI_TOKEN="qiwi_token_for_pay"
QIWI_PHONE="qiwi_phone_number_for_pay"
BOT_TOKEN="token_for_tg_bot"
```
## Run

```
python3 main.py
```
## Essence of the project
The bot continuously receives prices for bundles of cryptocurrencies. By clicking on the button, the bot displays the lowest price for a certain bundle, the name of the crypto exchange and a link to purchase through the telegram bot. He does the same with the maximum price per bundle. At the end it gives the difference as a percentage.
## Features
- **Getting prices** for cryptocurrencies in real time (update rate 5 s)
- **Six crypto exchanges** (Binance, ByBit, KuCoin, Mexc, Garantex, Huobi)
- **Selecting** the maximum and minimum **prices** for cryptocurrency
- **Difference** between prices as a **percentage**
- **Buying cryptocurrency** without leaving the bot (using built-in links)
- **Sending messages** to a telegram channel
- **Subscription payment**
- **Admin panel**


## Stack
- asyncio
- aiohttp
- aiogram
- websockets
- sqlite3



## Problems I encountered
- API limits for receiving prices (solution - websocket and use proxy)
- Subscription payment (solution - pyqiwip2p)
- Checking subscription expiration date
- Asynchronous post requests (solution - aiohttp)