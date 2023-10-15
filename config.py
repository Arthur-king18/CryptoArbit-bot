import os
from pybit import spot
from pyqiwip2p import QiwiP2P
from kucoin.client import Market
from dotenv import load_dotenv

load_dotenv()
QIWI_TOKEN = os.environ.get('QIWI_TOKEN')
QIWI_PHONE = os.environ.get('QIWI_PHONE')
BOT_TOKEN = os.environ.get('BOT_TOKEN')

TOKEN = BOT_TOKEN

url = 'https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search'
headers = {
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/112.0'
}


qiwi_token = QIWI_TOKEN
qiwi_phone = QIWI_PHONE

p2p = QiwiP2P(auth_key=qiwi_token)


session_bybit = spot.HTTP(endpoint='https://api.bybit.com')

client_kucion = Market(url='https://api.kucoin.com')

price_dict = {}
