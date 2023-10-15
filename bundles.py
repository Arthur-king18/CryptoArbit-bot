import random

import aiohttp
from aiogram.utils.markdown import hlink

from config import session_bybit, url, headers, client_kucion
from config import price_dict


async def BTCUSDT(session, bundles_dict):
    try:
        btc = 'BTC'
        usdt = 'USDT'
        num_dict = {}
        num_list = []
        link_dict = {}

        async with session.get(url='https://api.huobi.pro/market/detail/merged?symbol=btcusdt') as response:
            if response.status == 200:
                response = await response.json()
                price_huobi = response['tick']['bid'][0]
                num_dict['Huobi'] = price_huobi

        async with session.get(url='https://garantex.io/api/v2/trades?market=btcusdt') as garantex:
            if garantex.status == 200:
                garantex = await garantex.json()
                price_garantex = float(garantex[0]['price'])
                num_dict['Garantex'] = price_garantex

        async with session.get(url='https://www.mexc.com/open/api/v2/market/deals?symbol=BTC_USDT&limit=1') as mexc:
            if mexc.status == 200:
                mexc = await mexc.json()
                price_mexc = float(mexc['data'][0]['trade_price'])
                num_dict['Mexc'] = price_mexc

        # price_binance = float(client_binance.get_order_book(symbol='BTCUSDT')['bids'][0][0])
        price_binance = float(price_dict['btcusdt'])
        price_bybit = float(session_bybit.last_traded_price(symbol='BTCUSDT')['result']['price'])
        price_kucoin = float(client_kucion.get_ticker('BTC-USDT')['price'])

        num_dict['Binance'] = price_binance
        num_dict['ByBit'] = price_bybit
        num_dict['KuCoin'] = price_kucoin

        for i in num_dict:
            num_list.append(num_dict[i])

        x = min(num_list)
        y = max(num_list)

        sum = round(100 * (y - x) / x, 3)

        for k, v in num_dict.items():
            if v == x:
                name_birg_buy = k

            if v == y:
                name_birg_sell = k

        link_dict['Binance'] = 'https://www.binance.com/ru/trade/BTC_USDT?theme=dark&type=spot'
        link_dict['ByBit'] = 'https://www.bybit.com/ru-RU/trade/spot/BTC/USDT'
        link_dict['Huobi'] = 'https://www.huobi.com/en-us/exchange/btc_usdt'
        link_dict['Garantex'] = 'https://garantex.io/trading/btcusdt'
        link_dict['Mexc'] = 'https://www.mexc.com/ru-RU/exchange/BTC_USDT?_from=header'
        link_dict['KuCoin'] = 'https://www.kucoin.com/ru/trade/BTC-USDT'

        x = str(x).replace('.', ',')
        y = str(y).replace('.', ',')
        sum = str(sum).replace('.', ',')

        link_buy = f'[{usdt} в {btc}]({link_dict[name_birg_buy]})'
        link_sell = f'[{btc} в {usdt}]({link_dict[name_birg_sell]})'
        support_link = f'[:](https://jwhdkj{random.randint(1, 10000000000)}jhb.com)'

        final = [f'1️⃣*{name_birg_buy}*\\ {support_link} {link_buy} `{x}` \n\n'
                 f'2️⃣*{name_birg_sell}*\\ {support_link} {link_sell} `{y}`\n\n'
                 f'💎*{sum}%*\\\n', name_birg_buy, link_dict[name_birg_buy], name_birg_sell,
                 link_dict[name_birg_sell]]

        bundles_dict['BTC/USDT'] = final


    except:
        bundles_dict['BTC/USDT'] = f'Связка <b>{btc}/{usdt}</b> не отвечает, поробуйте через 5 минут'


async def SOLUSDT(session, bundles_dict):
    try:
        sol = 'SOL'
        usdt = 'USDT'
        num_dict = {}
        num_list = []
        link_dict = {}

        async with session.get(url='https://api.huobi.pro/market/detail/merged?symbol=solusdt') as response:
            if response.status == 200:
                response = await response.json()
                price_huobi = response['tick']['bid'][0]
                num_dict['Huobi'] = price_huobi

        async with session.get(url='https://www.mexc.com/open/api/v2/market/deals?symbol=SOL_USDT&limit=1') as mexc:
            if mexc.status == 200:
                mexc = await mexc.json()
                price_mexc = float(mexc['data'][0]['trade_price'])
                num_dict['Mexc'] = price_mexc

        # price_binance = float(client_binance.get_order_book(symbol='SOLUSDT')['bids'][0][0])
        price_binance = float(price_dict['solusdt'])
        price_bybit = float(session_bybit.last_traded_price(symbol='SOLUSDT')['result']['price'])
        price_kucoin = float(client_kucion.get_ticker('SOL-USDT')['price'])

        num_dict['Binance'] = price_binance
        num_dict['ByBit'] = price_bybit
        num_dict['KuCoin'] = price_kucoin

        for i in num_dict:
            num_list.append(num_dict[i])

        x = min(num_list)
        y = max(num_list)
        sum = round(100 * (y - x) / x, 3)

        for k, v in num_dict.items():
            if v == x:
                name_birg_buy = k

            if v == y:
                name_birg_sell = k

        link_dict['Binance'] = 'https://www.binance.com/ru/trade/SOL_USDT?theme=dark&type=spot'
        link_dict['ByBit'] = 'https://www.bybit.com/ru-RU/trade/spot/SOL/USDT'
        link_dict['Huobi'] = 'https://www.huobi.com/en-us/exchange/sol_usdt'
        link_dict['Garantex'] = 'https://garantex.io/trading/solusdt'
        link_dict['Mexc'] = 'https://www.mexc.com/ru-RU/exchange/SOL_USDT?_from=header'
        link_dict['KuCoin'] = 'https://www.kucoin.com/ru/trade/SOL-USDT'

        x = str(x).replace('.', ',')
        y = str(y).replace('.', ',')
        sum = str(sum).replace('.', ',')

        link_buy = f'[{usdt} в {sol}]({link_dict[name_birg_buy]})'
        link_sell = f'[{sol} в {usdt}]({link_dict[name_birg_sell]})'
        support_link = f'[:](https://jwhdkj{random.randint(1, 10000000000)}jhb.com)'

        final = [f'1️⃣*{name_birg_buy}*\\ {support_link} {link_buy} `{x}` \n\n'
                 f'2️⃣*{name_birg_sell}*\\ {support_link} {link_sell} `{y}`\n\n'
                 f'💎*{sum}%*\\\n', name_birg_buy, link_dict[name_birg_buy], name_birg_sell,
                 link_dict[name_birg_sell]]

        if float(sum.replace(',', '.')) > 0.8:
            bundles_dict['SOL/USDT'] = final
        else:
            bundles_dict['SOL/USDT'] = 1

    except:
        bundles_dict['SOL/USDT'] = f'Связка <b>{sol}/{usdt}</b> не отвечает, поробуйте через 5 минут'


async def ETHUSDT(session, bundles_dict):
    try:
        eth = 'ETH'
        usdt = 'USDT'
        num_dict = {}
        num_list = []
        link_dict = {}

        async with session.get(url='https://api.huobi.pro/market/detail/merged?symbol=ethusdt') as response:
            if response.status == 200:
                response = await response.json()
                price_huobi = response['tick']['bid'][0]
                num_dict['Huobi'] = price_huobi

        async with session.get(url='https://garantex.io/api/v2/trades?market=ethusdt') as garantex:
            if garantex.status == 200:
                garantex = await garantex.json()
                price_garantex = float(garantex[0]['price'])
                num_dict['Garantex'] = price_garantex

        # garantex = requests.get('https://garantex.io/api/v2/trades?market=btcusdt')
        async with session.get(url='https://www.mexc.com/open/api/v2/market/deals?symbol=ETH_USDT&limit=1') as mexc:
            if mexc.status == 200:
                mexc = await mexc.json()
                price_mexc = float(mexc['data'][0]['trade_price'])
                num_dict['Mexc'] = price_mexc

        # price_binance = float(client_binance.get_order_book(symbol='ETHUSDT')['bids'][0][0])
        price_binance = float(price_dict['ethusdt'])
        price_bybit = float(session_bybit.last_traded_price(symbol='ETHUSDT')['result']['price'])
        price_kucoin = float(client_kucion.get_ticker('ETH-USDT')['price'])

        num_dict['Binance'] = price_binance
        num_dict['ByBit'] = price_bybit
        num_dict['KuCoin'] = price_kucoin

        for i in num_dict:
            num_list.append(num_dict[i])

        x = min(num_list)
        y = max(num_list)

        sum = round(100 * (y - x) / x, 3)

        for k, v in num_dict.items():
            if v == x:
                name_birg_buy = k

            if v == y:
                name_birg_sell = k

        link_dict['Binance'] = 'https://www.binance.com/ru/trade/ETH_USDT?theme=dark&type=spot'
        link_dict['ByBit'] = 'https://www.bybit.com/ru-RU/trade/spot/ETH/USDT'
        link_dict['Huobi'] = 'https://www.huobi.com/en-us/exchange/eth_usdt'
        link_dict['Garantex'] = 'https://garantex.io/trading/ethusdt'
        link_dict['Mexc'] = 'https://www.mexc.com/ru-RU/exchange/ETH_USDT?_from=header'
        link_dict['KuCoin'] = 'https://www.kucoin.com/ru/trade/ETH-USDT'

        x = str(x).replace('.', ',')
        y = str(y).replace('.', ',')
        sum = str(sum).replace('.', ',')

        link_buy = f'[{usdt} в {eth}]({link_dict[name_birg_buy]})'
        link_sell = f'[{eth} в {usdt}]({link_dict[name_birg_sell]})'
        support_link = f'[:](https://jwhdkj{random.randint(1, 10000000000)}jhb.com)'

        final = [f'1️⃣*{name_birg_buy}*\\ {support_link} {link_buy} `{x}` \n\n'
                 f'2️⃣*{name_birg_sell}*\\ {support_link} {link_sell} `{y}`\n\n'
                 f'💎*{sum}%*\\\n', name_birg_buy, link_dict[name_birg_buy], name_birg_sell,
                 link_dict[name_birg_sell]]

        if float(sum.replace(',', '.')) > 0.8:
            bundles_dict['ETH/USDT'] = final
        else:
            bundles_dict['ETH/USDT'] = 1

    except:
        bundles_dict['ETH/USDT'] = f'Связка <b>{eth}/{usdt}</b> не отвечает, поробуйте через 5 минут\n'


async def BNBUSDT(session, bundles_dict):
    try:
        bnb = 'BNB'
        usdt = 'USDT'
        num_dict = {}
        num_list = []
        link_dict = {}

        async with session.get(url='https://api.huobi.pro/market/detail/merged?symbol=bnbusdt') as response:
            if response.status == 200:
                response = await response.json()
                price_huobi = response['tick']['bid'][0]
                num_dict['Huobi'] = price_huobi

        async with session.get(url='https://www.mexc.com/open/api/v2/market/deals?symbol=BNB_USDT&limit=1') as mexc:
            if mexc.status == 200:
                mexc = await mexc.json()
                price_mexc = float(mexc['data'][0]['trade_price'])
                num_dict['Mexc'] = price_mexc

        # price_binance = float(client_binance.get_order_book(symbol='BNBUSDT')['bids'][0][0])
        price_binance = float(price_dict['bnbusdt'])
        price_bybit = float(session_bybit.last_traded_price(symbol='BNBUSDT')['result']['price'])
        price_kucoin = float(client_kucion.get_ticker('BNB-USDT')['price'])

        num_dict['Binance'] = price_binance
        num_dict['ByBit'] = price_bybit
        num_dict['KuCoin'] = price_kucoin

        for i in num_dict:
            num_list.append(num_dict[i])

        x = min(num_list)
        y = max(num_list)

        sum = round(100 * (y - x) / x, 3)

        for k, v in num_dict.items():
            if v == x:
                name_birg_buy = k

            if v == y:
                name_birg_sell = k

        link_dict['Binance'] = 'https://www.binance.com/ru/trade/BNB_USDT?theme=dark&type=spot'
        link_dict['ByBit'] = 'https://www.bybit.com/ru-RU/trade/spot/BNB/USDT'
        link_dict['Huobi'] = 'https://www.huobi.com/en-us/exchange/bnb_usdt'
        link_dict['Garantex'] = 'https://garantex.io/trading/bnbusdt'
        link_dict['Mexc'] = 'https://www.mexc.com/ru-RU/exchange/BNB_USDT?_from=header'
        link_dict['KuCoin'] = 'https://www.kucoin.com/ru/trade/BNB-USDT'

        x = str(x).replace('.', ',')
        y = str(y).replace('.', ',')
        sum = str(sum).replace('.', ',')

        link_buy = f'[{usdt} в {bnb}]({link_dict[name_birg_buy]})'
        link_sell = f'[{bnb} в {usdt}]({link_dict[name_birg_sell]})'
        support_link = f'[:](https://jwhdkj{random.randint(1, 10000000000)}jhb.com)'

        final = [f'1️⃣*{name_birg_buy}*\\ {support_link} {link_buy} `{x}` \n\n'
                 f'2️⃣*{name_birg_sell}*\\ {support_link} {link_sell} `{y}`\n\n'
                 f'💎*{sum}%*\\\n', name_birg_buy, link_dict[name_birg_buy], name_birg_sell,
                 link_dict[name_birg_sell]]

        if float(sum.replace(',', '.')) > 0.8:
            bundles_dict['BNB/USDT'] = final
        else:
            bundles_dict['BNB/USDT'] = 1

    except:
        bundles_dict['BNB/USDT'] = f'Связка <b>{bnb}/{usdt}</b> не отвечает, поробуйте через 5 минут'


async def ADAUSDT(session, bundles_dict):
    try:
        ada = 'ADA'
        usdt = 'USDT'
        num_dict = {}
        num_list = []
        link_dict = {}

        async with session.get(url='https://api.huobi.pro/market/detail/merged?symbol=adausdt') as response:
            if response.status == 200:
                response = await response.json()
                price_huobi = response['tick']['bid'][0]
                num_dict['Huobi'] = price_huobi

        async with session.get(url='https://www.mexc.com/open/api/v2/market/deals?symbol=ada_USDT&limit=1') as mexc:
            if mexc.status == 200:
                mexc = await mexc.json()
                price_mexc = float(mexc['data'][0]['trade_price'])
                num_dict['Mexc'] = price_mexc

        # price_binance = float(client_binance.get_order_book(symbol='ADAUSDT')['bids'][0][0])
        price_binance = float(price_dict['adausdt'])
        price_bybit = float(session_bybit.last_traded_price(symbol='ADAUSDT')['result']['price'])
        price_kucoin = float(client_kucion.get_ticker('ADA-USDT')['price'])

        num_dict['Binance'] = price_binance
        num_dict['ByBit'] = price_bybit
        num_dict['KuCoin'] = price_kucoin

        for i in num_dict:
            num_list.append(num_dict[i])

        x = min(num_list)
        y = max(num_list)

        sum = round(100 * (y - x) / x, 3)

        for k, v in num_dict.items():
            if v == x:
                name_birg_buy = k

            if v == y:
                name_birg_sell = k

        link_dict['Binance'] = 'https://www.binance.com/ru/trade/ADA_USDT?theme=dark&type=spot'
        link_dict['ByBit'] = 'https://www.bybit.com/ru-RU/trade/spot/ADA/USDT'
        link_dict['Huobi'] = 'https://www.huobi.com/en-us/exchange/ada_usdt'
        link_dict['Garantex'] = 'https://garantex.io/trading/adausdt'
        link_dict['Mexc'] = 'https://www.mexc.com/ru-RU/exchange/ADA_USDT?_from=header'
        link_dict['KuCoin'] = 'https://www.kucoin.com/ru/trade/ADA-USDT'

        x = str(x).replace('.', ',')
        y = str(y).replace('.', ',')
        sum = str(sum).replace('.', ',')

        link_buy = f'[{usdt} в {ada}]({link_dict[name_birg_buy]})'
        link_sell = f'[{ada} в {usdt}]({link_dict[name_birg_sell]})'
        support_link = f'[:](https://jwhdkj{random.randint(1, 10000000000)}jhb.com)'

        final = [f'1️⃣*{name_birg_buy}*\\ {support_link} {link_buy} `{x}` \n\n'
                 f'2️⃣*{name_birg_sell}*\\ {support_link} {link_sell} `{y}`\n\n'
                 f'💎*{sum}%*\\\n', name_birg_buy, link_dict[name_birg_buy], name_birg_sell,
                 link_dict[name_birg_sell]]

        if float(sum.replace(',', '.')) > 0.8:
            bundles_dict['ADA/USDT'] = final
        else:
            bundles_dict['ADA/USDT'] = 1

    except:
        bundles_dict['ADA/USDT'] = f'Связка <b>{ada}/{usdt}</b> не отвечает, поробуйте через 5 минут'


async def XRPUSDT(session, bundles_dict):
    try:
        xrp = 'XRP'
        usdt = 'USDT'
        num_dict = {}
        num_list = []
        link_dict = {}

        async with session.get(url='https://api.huobi.pro/market/detail/merged?symbol=xrpusdt') as response:
            if response.status == 200:
                response = await response.json()
                price_huobi = response['tick']['bid'][0]
                num_dict['Huobi'] = price_huobi

        async with session.get(url='https://www.mexc.com/open/api/v2/market/deals?symbol=XRP_USDT&limit=1') as mexc:
            if mexc.status == 200:
                mexc = await mexc.json()
                price_mexc = float(mexc['data'][0]['trade_price'])
                num_dict['Mexc'] = price_mexc

        # price_binance = float(client_binance.get_order_book(symbol='XRPUSDT')['bids'][0][0])
        price_binance = float(price_dict['xrpusdt'])
        price_bybit = float(session_bybit.last_traded_price(symbol='XRPUSDT')['result']['price'])
        price_kucoin = float(client_kucion.get_ticker('XRP-USDT')['price'])

        num_dict['Binance'] = price_binance
        num_dict['KuCoin'] = price_kucoin
        num_dict['ByBit'] = price_bybit

        for i in num_dict:
            num_list.append(num_dict[i])

        x = min(num_list)
        y = max(num_list)

        sum = round(100 * (y - x) / x, 3)

        for k, v in num_dict.items():
            if v == x:
                name_birg_buy = k

            if v == y:
                name_birg_sell = k

        link_dict['Binance'] = 'https://www.binance.com/ru/trade/XRP_USDT?theme=dark&type=spot'
        link_dict['ByBit'] = 'https://www.bybit.com/ru-RU/trade/spot/XRP/USDT'
        link_dict['Huobi'] = 'https://www.huobi.com/en-us/exchange/xrp_usdt'
        link_dict['Garantex'] = 'https://garantex.io/trading/xrpusdt'
        link_dict['Mexc'] = 'https://www.mexc.com/ru-RU/exchange/XRP_USDT?_from=header'
        link_dict['KuCoin'] = 'https://www.kucoin.com/ru/trade/XRP-USDT'

        x = str(x).replace('.', ',')
        y = str(y).replace('.', ',')
        sum = str(sum).replace('.', ',')

        link_buy = f'[{usdt} в {xrp}]({link_dict[name_birg_buy]})'
        link_sell = f'[{xrp} в {usdt}]({link_dict[name_birg_sell]})'
        support_link = f'[:](https://jwhdkj{random.randint(1, 10000000000)}jhb.com)'

        final = [f'1️⃣*{name_birg_buy}*\\ {support_link} {link_buy} `{x}` \n\n'
                 f'2️⃣*{name_birg_sell}*\\ {support_link} {link_sell} `{y}`\n\n'
                 f'💎*{sum}%*\\\n', name_birg_buy, link_dict[name_birg_buy], name_birg_sell,
                 link_dict[name_birg_sell]]

        if float(sum.replace(',', '.')) > 0.8:
            bundles_dict['XRP/USDT'] = final
        else:
            bundles_dict['XRP/USDT'] = 1

    except:
        bundles_dict['XRP/USDT'] = f'Связка <b>{xrp}/{usdt}</b> не отвечает, поробуйте через 5 минут'


async def ANKRUSDT(session, bundles_dict):
    try:
        ankr = 'ANKR'
        usdt = 'USDT'
        num_dict = {}
        num_list = []
        link_dict = {}

        async with session.get(url='https://api.huobi.pro/market/detail/merged?symbol=ankrusdt') as response:
            if response.status == 200:
                response = await response.json()
                price_huobi = response['tick']['bid'][0]
                num_dict['Huobi'] = price_huobi

        async with session.get(url='https://www.mexc.com/open/api/v2/market/deals?symbol=ANKR_USDT&limit=1') as mexc:
            if mexc.status == 200:
                mexc = await mexc.json()
                price_mexc = float(mexc['data'][0]['trade_price'])
                num_dict['Mexc'] = price_mexc

        # price_binance = float(client_binance.get_order_book(symbol='ANKRUSDT')['bids'][0][0])
        price_binance = float(price_dict['ankrusdt'])
        price_bybit = float(session_bybit.last_traded_price(symbol='ANKRUSDT')['result']['price'])
        price_kucoin = float(client_kucion.get_ticker('ANKR-USDT')['price'])

        num_dict['Binance'] = price_binance
        num_dict['ByBit'] = price_bybit
        num_dict['KuCoin'] = price_kucoin

        for i in num_dict:
            num_list.append(num_dict[i])

        x = min(num_list)
        y = max(num_list)

        sum = round(100 * (y - x) / x, 3)

        for k, v in num_dict.items():
            if v == x:
                name_birg_buy = k

            if v == y:
                name_birg_sell = k

        link_dict['Binance'] = 'https://www.binance.com/ru/trade/ANKR_USDT?theme=dark&type=spot'
        link_dict['ByBit'] = 'https://www.bybit.com/ru-RU/trade/spot/ANKR/USDT'
        link_dict['Huobi'] = 'https://www.huobi.com/en-us/exchange/ankr_usdt'
        link_dict['Garantex'] = 'https://garantex.io/trading/ankrusdt'
        link_dict['Mexc'] = 'https://www.mexc.com/ru-RU/exchange/ANKR_USDT?_from=header'
        link_dict['KuCoin'] = 'https://www.kucoin.com/ru/trade/ANKR-USDT'

        x = str(x).replace('.', ',')
        y = str(y).replace('.', ',')
        sum = str(sum).replace('.', ',')

        link_buy = f'[{usdt} в {ankr}]({link_dict[name_birg_buy]})'
        link_sell = f'[{ankr} в {usdt}]({link_dict[name_birg_sell]})'
        support_link = f'[:](https://jwhdkj{random.randint(1, 10000000000)}jhb.com)'

        final = [f'1️⃣*{name_birg_buy}*\\ {support_link} {link_buy} `{x}` \n\n'
                 f'2️⃣*{name_birg_sell}*\\ {support_link} {link_sell} `{y}`\n\n'
                 f'💎*{sum}%*\\\n', name_birg_buy, link_dict[name_birg_buy], name_birg_sell,
                 link_dict[name_birg_sell]]

        if float(sum.replace(',', '.')) > 0.8:
            bundles_dict['ANKR/USDT'] = final
        else:
            bundles_dict['ANKR/USDT'] = 1

    except:
        bundles_dict['ANKR/USDT'] = f'Связка <b>{ankr}/{usdt}</b> не отвечает, поробуйте через 5 минут'


async def ICXUSDT(session, bundles_dict):
    try:
        icx = 'ICX'
        usdt = 'USDT'
        num_dict = {}
        num_list = []
        link_dict = {}

        async with session.get(url='https://api.huobi.pro/market/detail/merged?symbol=icxusdt') as response:
            if response.status == 200:
                response = await response.json()
                price_huobi = response['tick']['bid'][0]
                num_dict['Huobi'] = price_huobi

        # price_binance = float(client_binance.get_order_book(symbol='ICXUSDT')['bids'][0][0])
        price_binance = float(price_dict['icxusdt'])
        price_bybit = float(session_bybit.last_traded_price(symbol='ICXUSDT')['result']['price'])
        price_kucoin = float(client_kucion.get_ticker('ICX-USDT')['price'])

        num_dict['Binance'] = price_binance
        num_dict['ByBit'] = price_bybit
        num_dict['KuCoin'] = price_kucoin

        for i in num_dict:
            num_list.append(num_dict[i])

        x = min(num_list)
        y = max(num_list)

        sum = round(100 * (y - x) / x, 3)

        for k, v in num_dict.items():
            if v == x:
                name_birg_buy = k

            if v == y:
                name_birg_sell = k

        link_dict['Binance'] = 'https://www.binance.com/ru/trade/ICX_USDT?theme=dark&type=spot'
        link_dict['ByBit'] = 'https://www.bybit.com/ru-RU/trade/spot/ICX/USDT'
        link_dict['Huobi'] = 'https://www.huobi.com/en-us/exchange/icx_usdt'
        link_dict['Garantex'] = 'https://garantex.io/trading/icxusdt'
        link_dict['Mexc'] = 'https://www.mexc.com/ru-RU/exchange/ICX_USDT?_from=header'
        link_dict['KuCoin'] = 'https://www.kucoin.com/ru/trade/ICX-USDT'

        x = str(x).replace('.', ',')
        y = str(y).replace('.', ',')
        sum = str(sum).replace('.', ',')

        link_buy = f'[{usdt} в {icx}]({link_dict[name_birg_buy]})'
        link_sell = f'[{icx} в {usdt}]({link_dict[name_birg_sell]})'
        support_link = f'[:](https://jwhdkj{random.randint(1, 10000000000)}jhb.com)'

        final = [f'1️⃣*{name_birg_buy}*\\ {support_link} {link_buy} `{x}` \n\n'
                 f'2️⃣*{name_birg_sell}*\\ {support_link} {link_sell} `{y}`\n\n'
                 f'💎*{sum}%*\\\n', name_birg_buy, link_dict[name_birg_buy], name_birg_sell,
                 link_dict[name_birg_sell]]

        if float(sum.replace(',', '.')) > 0.8:
            bundles_dict['ICX/USDT'] = final
        else:
            bundles_dict['ICX/USDT'] = 1

    except:
        bundles_dict['ICX/USDT'] = f'Связка <b>{icx}/{usdt}</b> не отвечает, поробуйте через 5 минут'


async def IOTXUSDT(session, bundles_dict):
    try:
        iotx = 'IOTX'
        usdt = 'USDT'
        num_dict = {}
        num_list = []
        link_dict = {}

        async with session.get(url='https://api.huobi.pro/market/detail/merged?symbol=iotxusdt') as response:
            if response.status == 200:
                response = await response.json()
                price_huobi = response['tick']['bid'][0]
                num_dict['Huobi'] = price_huobi

        async with session.get(url='https://www.mexc.com/open/api/v2/market/deals?symbol=IOTX_USDT&limit=1') as mexc:
            if mexc.status == 200:
                mexc = await mexc.json()
                price_mexc = float(mexc['data'][0]['trade_price'])
                num_dict['Mexc'] = price_mexc

        # price_binance = float(client_binance.get_order_book(symbol='IOTXUSDT')['bids'][0][0])
        price_binance = float(price_dict['iotxusdt'])
        price_kucoin = float(client_kucion.get_ticker('IOTX-USDT')['price'])

        num_dict['Binance'] = price_binance
        num_dict['KuCoin'] = price_kucoin

        for i in num_dict:
            num_list.append(num_dict[i])

        x = min(num_list)
        y = max(num_list)

        sum = round(100 * (y - x) / x, 3)

        for k, v in num_dict.items():
            if v == x:
                name_birg_buy = k

            if v == y:
                name_birg_sell = k

        link_dict['Binance'] = 'https://www.binance.com/ru/trade/IOTX_USDT?theme=dark&type=spot'
        link_dict['ByBit'] = 'https://www.bybit.com/ru-RU/trade/spot/IOTX/USDT'
        link_dict['Huobi'] = 'https://www.huobi.com/en-us/exchange/iotx_usdt'
        link_dict['Garantex'] = 'https://garantex.io/trading/iotxusdt'
        link_dict['Mexc'] = 'https://www.mexc.com/ru-RU/exchange/IOTX_USDT?_from=header'
        link_dict['KuCoin'] = 'https://www.kucoin.com/ru/trade/IOTX-USDT'

        x = str(x).replace('.', ',')
        y = str(y).replace('.', ',')
        sum = str(sum).replace('.', ',')

        link_buy = f'[{usdt} в {iotx}]({link_dict[name_birg_buy]})'
        link_sell = f'[{iotx} в {usdt}]({link_dict[name_birg_sell]})'
        support_link = f'[:](https://jwhdkj{random.randint(1, 10000000000)}jhb.com)'

        final = [f'1️⃣*{name_birg_buy}*\\ {support_link} {link_buy} `{x}` \n\n'
                 f'2️⃣*{name_birg_sell}*\\ {support_link} {link_sell} `{y}`\n\n'
                 f'💎*{sum}%*\\\n', name_birg_buy, link_dict[name_birg_buy], name_birg_sell,
                 link_dict[name_birg_sell]]

        if float(sum.replace(',', '.')) > 0.8:
            bundles_dict['IOTX/USDT'] = final
        else:
            bundles_dict['IOTX/USDT'] = 1

    except:
        bundles_dict['IOTX/USDT'] = f'Связка <b>{iotx}/{usdt}</b> не отвечает, поробуйте через 5 минут'


async def SOFIUSDT(session, bundles_dict):
    try:
        sofi = 'SOFI'
        usdt = 'USDT'
        num_dict = {}
        num_list = []
        link_dict = {}

        async with session.get(url='https://api.huobi.pro/market/detail/merged?symbol=sofiusdt') as response:
            if response.status == 200:
                response = await response.json()
                price_huobi = response['tick']['bid'][0]
                num_dict['Huobi'] = price_huobi

        async with session.get(url='https://www.mexc.com/open/api/v2/market/deals?symbol=SOFI_USDT&limit=1') as mexc:
            if mexc.status == 200:
                mexc = await mexc.json()
                price_mexc = float(mexc['data'][0]['trade_price'])
                num_dict['Mexc'] = price_mexc

        for i in num_dict:
            num_list.append(num_dict[i])

        x = min(num_list)
        y = max(num_list)

        sum = round(100 * (y - x) / x, 3)

        for k, v in num_dict.items():
            if v == x:
                name_birg_buy = k

            if v == y:
                name_birg_sell = k

        link_dict['Binance'] = 'https://www.binance.com/ru/trade/SOFI_USDT?theme=dark&type=spot'
        link_dict['ByBit'] = 'https://www.bybit.com/ru-RU/trade/spot/SOFI/USDT'
        link_dict['Huobi'] = 'https://www.huobi.com/en-us/exchange/sofi_usdt'
        link_dict['Garantex'] = 'https://garantex.io/trading/sofiusdt'
        link_dict['Mexc'] = 'https://www.mexc.com/ru-RU/exchange/SOFI_USDT?_from=header'
        link_dict['KuCoin'] = 'https://www.kucoin.com/ru/trade/SOFI-USDT'

        x = str(x).replace('.', ',')
        y = str(y).replace('.', ',')
        sum = str(sum).replace('.', ',')

        link_buy = f'[{usdt} в {sofi}]({link_dict[name_birg_buy]})'
        link_sell = f'[{sofi} в {usdt}]({link_dict[name_birg_sell]})'
        support_link = f'[:](https://jwhdkj{random.randint(1, 10000000000)}jhb.com)'

        final = [f'1️⃣*{name_birg_buy}*\\ {support_link} {link_buy} `{x}` \n\n'
                 f'2️⃣*{name_birg_sell}*\\ {support_link} {link_sell} `{y}`\n\n'
                 f'💎*{sum}%*\\\n', name_birg_buy, link_dict[name_birg_buy], name_birg_sell,
                 link_dict[name_birg_sell]]

        if float(sum.replace(',', '.')) > 0.8:
            bundles_dict['SOFI/USDT'] = final
        else:
            bundles_dict['SOFI/USDT'] = 1

    except:
        bundles_dict['SOFI/USDT'] = f'Связка <b>{sofi}/{usdt}</b> не отвечает, поробуйте через 5 минут'


async def ANTUSDT(session, bundles_dict):
    try:
        ant = 'ANT'
        usdt = 'USDT'
        num_dict = {}
        num_list = []
        link_dict = {}

        async with session.get(url='https://api.huobi.pro/market/detail/merged?symbol=antusdt') as response:
            if response.status == 200:
                response = await response.json()
                price_huobi = response['tick']['bid'][0]
                num_dict['Huobi'] = price_huobi

        async with session.get(url='https://www.mexc.com/open/api/v2/market/deals?symbol=ANT_USDT&limit=1') as mexc:
            if mexc.status == 200:
                mexc = await mexc.json()
                price_mexc = float(mexc['data'][0]['trade_price'])
                num_dict['Mexc'] = price_mexc

        # price_binance = float(client_binance.get_order_book(symbol='ANTUSDT')['bids'][0][0])
        price_binance = float(price_dict['antusdt'])
        price_kucoin = float(client_kucion.get_ticker('ANT-USDT')['price'])

        num_dict['Binance'] = price_binance
        num_dict['KuCoin'] = price_kucoin

        for i in num_dict:
            num_list.append(num_dict[i])

        x = min(num_list)
        y = max(num_list)

        sum = round(100 * (y - x) / x, 3)

        for k, v in num_dict.items():
            if v == x:
                name_birg_buy = k

            if v == y:
                name_birg_sell = k

        link_dict['Binance'] = 'https://www.binance.com/ru/trade/ANT_USDT?theme=dark&type=spot'
        link_dict['ByBit'] = 'https://www.bybit.com/ru-RU/trade/spot/ANT/USDT'
        link_dict['Huobi'] = 'https://www.huobi.com/en-us/exchange/ant_usdt'
        link_dict['Garantex'] = 'https://garantex.io/trading/antusdt'
        link_dict['Mexc'] = 'https://www.mexc.com/ru-RU/exchange/ANT_USDT?_from=header'
        link_dict['KuCoin'] = 'https://www.kucoin.com/ru/trade/ANT-USDT'

        x = str(x).replace('.', ',')
        y = str(y).replace('.', ',')
        sum = str(sum).replace('.', ',')

        link_buy = f'[{usdt} в {ant}]({link_dict[name_birg_buy]})'
        link_sell = f'[{ant} в {usdt}]({link_dict[name_birg_sell]})'
        support_link = f'[:](https://jwhdkj{random.randint(1, 10000000000)}jhb.com)'

        final = [f'1️⃣*{name_birg_buy}*\\ {support_link} {link_buy} `{x}` \n\n'
                 f'2️⃣*{name_birg_sell}*\\ {support_link} {link_sell} `{y}`\n\n'
                 f'💎*{sum}%*\\\n', name_birg_buy, link_dict[name_birg_buy], name_birg_sell,
                 link_dict[name_birg_sell]]

        if float(sum.replace(',', '.')) > 0.8:
            bundles_dict['ANT/USDT'] = final
        else:
            bundles_dict['ANT/USDT'] = 1

    except:
        bundles_dict['ANT/USDT'] = f'Связка <b>{ant}/{usdt}</b> не отвечает, поробуйте через 5 минут'


async def BBFUSDT(session, bundles_dict):
    try:
        bbf = 'BBF'
        usdt = 'USDT'
        num_dict = {}
        num_list = []
        link_dict = {}

        async with session.get(url='https://api.huobi.pro/market/detail/merged?symbol=bbfusdt') as response:
            if response.status == 200:
                response = await response.json()
                price_huobi = response['tick']['bid'][0]
                num_dict['Huobi'] = price_huobi

        async with session.get(url='https://www.mexc.com/open/api/v2/market/deals?symbol=BBF_USDT&limit=1') as mexc:
            if mexc.status == 200:
                mexc = await mexc.json()
                price_mexc = float(mexc['data'][0]['trade_price'])
                num_dict['Mexc'] = price_mexc

        for i in num_dict:
            num_list.append(num_dict[i])

        x = min(num_list)
        y = max(num_list)

        sum = round(100 * (y - x) / x, 3)

        for k, v in num_dict.items():
            if v == x:
                name_birg_buy = k

            if v == y:
                name_birg_sell = k

        link_dict['Binance'] = 'https://www.binance.com/ru/trade/BBF_USDT?theme=dark&type=spot'
        link_dict['ByBit'] = 'https://www.bybit.com/ru-RU/trade/spot/BBF/USDT'
        link_dict['Huobi'] = 'https://www.huobi.com/en-us/exchange/bbf_usdt'
        link_dict['Garantex'] = 'https://garantex.io/trading/bbfusdt'
        link_dict['Mexc'] = 'https://www.mexc.com/ru-RU/exchange/BBF_USDT?_from=header'
        link_dict['KuCoin'] = 'https://www.kucoin.com/ru/trade/BBF-USDT'

        x = str(x).replace('.', ',')
        y = str(y).replace('.', ',')
        sum = str(sum).replace('.', ',')

        link_buy = f'[{usdt} в {bbf}]({link_dict[name_birg_buy]})'
        link_sell = f'[{bbf} в {usdt}]({link_dict[name_birg_sell]})'
        support_link = f'[:](https://jwhdkj{random.randint(1, 10000000000)}jhb.com)'

        final = [f'1️⃣*{name_birg_buy}*\\ {support_link} {link_buy} `{x}` \n\n'
                 f'2️⃣*{name_birg_sell}*\\ {support_link} {link_sell} `{y}`\n\n'
                 f'💎*{sum}%*\\\n', name_birg_buy, link_dict[name_birg_buy], name_birg_sell,
                 link_dict[name_birg_sell]]

        if float(sum.replace(',', '.')) > 0.8:
            bundles_dict['BBF/USDT'] = final
        else:
            bundles_dict['BBF/USDT'] = 1

    except:
        bundles_dict['BBF/USDT'] = 'Связка <b>{bbf}/{usdt}</b> не отвечает, поробуйте через 5 минут'


async def CULTUSDT(session, bundles_dict):
    try:
        cult = 'CULT'
        usdt = 'USDT'
        num_dict = {}
        num_list = []
        link_dict = {}

        async with session.get(url='https://www.mexc.com/open/api/v2/market/deals?symbol=CULT_USDT&limit=1') as mexc:
            if mexc.status == 200:
                mexc = await mexc.json()
                price_mexc = float(mexc['data'][0]['trade_price'])
                num_dict['Mexc'] = price_mexc

        price_bybit = float(session_bybit.last_traded_price(symbol='CULTUSDT')['result']['price'])
        price_kucoin = float(client_kucion.get_ticker('CULT-USDT')['price'])

        num_dict['ByBit'] = price_bybit
        num_dict['KuCoin'] = price_kucoin

        for i in num_dict:
            num_list.append(num_dict[i])

        x = min(num_list)
        y = max(num_list)

        sum = round(100 * (y - x) / x, 3)

        for k, v in num_dict.items():
            if v == x:
                name_birg_buy = k

            if v == y:
                name_birg_sell = k

        link_dict['Binance'] = 'https://www.binance.com/ru/trade/CULT_USDT?theme=dark&type=spot'
        link_dict['ByBit'] = 'https://www.bybit.com/ru-RU/trade/spot/CULT/USDT'
        link_dict['Huobi'] = 'https://www.huobi.com/en-us/exchange/cult_usdt'
        link_dict['Garantex'] = 'https://garantex.io/trading/cultusdt'
        link_dict['Mexc'] = 'https://www.mexc.com/ru-RU/exchange/CULT_USDT?_from=header'
        link_dict['KuCoin'] = 'https://www.kucoin.com/ru/trade/CULT-USDT'

        x = str(x).replace('.', ',')
        y = str(y).replace('.', ',')
        sum = str(sum).replace('.', ',')

        link_buy = f'[{usdt} в {cult}]({link_dict[name_birg_buy]})'
        link_sell = f'[{cult} в {usdt}]({link_dict[name_birg_sell]})'
        support_link = f'[:](https://jwhdkj{random.randint(1, 10000000000)}jhb.com)'

        final = [f'1️⃣*{name_birg_buy}*\\ {support_link} {link_buy} `{x}` \n\n'
                 f'2️⃣*{name_birg_sell}*\\ {support_link} {link_sell} `{y}`\n\n'
                 f'💎*{sum}%*\\\n', name_birg_buy, link_dict[name_birg_buy], name_birg_sell,
                 link_dict[name_birg_sell]]

        if float(sum.replace(',', '.')) > 0.8:
            bundles_dict['CULT/USDT'] = final
        else:
            bundles_dict['CULT/USDT'] = 1

    except:
        bundles_dict['CULT/USDT'] = f'Связка <b>{cult}/{usdt}</b> не отвечает, поробуйте через 5 минут'


async def BAXUSDT(session, bundles_dict):
    try:
        bax = 'BAX'
        usdt = 'USDT'
        num_dict = {}
        num_list = []
        link_dict = {}

        async with session.get(url='https://www.mexc.com/open/api/v2/market/deals?symbol=BAX_USDT&limit=1') as mexc:
            if mexc.status == 200:
                mexc = await mexc.json()
                price_mexc = float(mexc['data'][0]['trade_price'])
                num_dict['Mexc'] = price_mexc

        price_kucoin = float(client_kucion.get_ticker('BAX-USDT')['price'])

        num_dict['KuCoin'] = price_kucoin

        for i in num_dict:
            num_list.append(num_dict[i])

        x = min(num_list)
        y = max(num_list)

        sum = round(100 * (y - x) / x, 3)

        for k, v in num_dict.items():
            if v == x:
                name_birg_buy = k

            if v == y:
                name_birg_sell = k

        link_dict['Binance'] = 'https://www.binance.com/ru/trade/BAX_USDT?theme=dark&type=spot'
        link_dict['ByBit'] = 'https://www.bybit.com/ru-RU/trade/spot/BAX/USDT'
        link_dict['Huobi'] = 'https://www.huobi.com/en-us/exchange/bax_usdt'
        link_dict['Garantex'] = 'https://garantex.io/trading/baxusdt'
        link_dict['Mexc'] = 'https://www.mexc.com/ru-RU/exchange/BAX_USDT?_from=header'
        link_dict['KuCoin'] = 'https://www.kucoin.com/ru/trade/BAX-USDT'

        x = str(x).replace('.', ',')
        y = str(y).replace('.', ',')
        sum = str(sum).replace('.', ',')

        link_buy = f'[{usdt} в {bax}]({link_dict[name_birg_buy]})'
        link_sell = f'[{bax} в {usdt}]({link_dict[name_birg_sell]})'
        support_link = f'[:](https://jwhdkj{random.randint(1, 10000000000)}jhb.com)'

        final = [f'1️⃣*{name_birg_buy}*\\ {support_link} {link_buy} `{x}` \n\n'
                 f'2️⃣*{name_birg_sell}*\\ {support_link} {link_sell} `{y}`\n\n'
                 f'💎*{sum}%*\\\n', name_birg_buy, link_dict[name_birg_buy], name_birg_sell,
                 link_dict[name_birg_sell]]

        if float(sum.replace(',', '.')) > 0.8:
            bundles_dict['BAX/USDT'] = final
        else:
            bundles_dict['BAX/USDT'] = 1

    except:
        bundles_dict['BAX/USDT'] = f'Связка <b>{bax}/{usdt}</b> не отвечает, поробуйте через 5 минут'


async def CELRUSDT(session, bundles_dict):
    try:
        celr = 'CELR'
        usdt = 'USDT'
        num_dict = {}
        num_list = []
        link_dict = {}

        async with session.get(url='https://www.mexc.com/open/api/v2/market/deals?symbol=CELR_USDT&limit=1') as mexc:
            if mexc.status == 200:
                mexc = await mexc.json()
                price_mexc = float(mexc['data'][0]['trade_price'])
                num_dict['Mexc'] = price_mexc

        # price_binance = float(client_binance.get_order_book(symbol='CELRUSDT')['bids'][0][0])
        price_binance = float(price_dict['celrusdt'])
        price_kucoin = float(client_kucion.get_ticker('CELR-USDT')['price'])

        num_dict['Binance'] = price_binance
        num_dict['KuCoin'] = price_kucoin

        for i in num_dict:
            num_list.append(num_dict[i])

        x = min(num_list)
        y = max(num_list)

        sum = round(100 * (y - x) / x, 3)

        for k, v in num_dict.items():
            if v == x:
                name_birg_buy = k

            if v == y:
                name_birg_sell = k

        link_dict['Binance'] = 'https://www.binance.com/ru/trade/CELR_USDT?theme=dark&type=spot'
        link_dict['ByBit'] = 'https://www.bybit.com/ru-RU/trade/spot/CELR/USDT'
        link_dict['Huobi'] = 'https://www.huobi.com/en-us/exchange/celr_usdt'
        link_dict['Garantex'] = 'https://garantex.io/trading/celrusdt'
        link_dict['Mexc'] = 'https://www.mexc.com/ru-RU/exchange/CELR_USDT?_from=header'
        link_dict['KuCoin'] = 'https://www.kucoin.com/ru/trade/CELR-USDT'

        x = str(x).replace('.', ',')
        y = str(y).replace('.', ',')
        sum = str(sum).replace('.', ',')

        link_buy = f'[{usdt} в {celr}]({link_dict[name_birg_buy]})'
        link_sell = f'[{celr} в {usdt}]({link_dict[name_birg_sell]})'
        support_link = f'[:](https://jwhdkj{random.randint(1, 10000000000)}jhb.com)'

        final = [f'1️⃣*{name_birg_buy}*\\ {support_link} {link_buy} `{x}` \n\n'
                 f'2️⃣*{name_birg_sell}*\\ {support_link} {link_sell} `{y}`\n\n'
                 f'💎*{sum}%*\\\n', name_birg_buy, link_dict[name_birg_buy], name_birg_sell,
                 link_dict[name_birg_sell]]

        if float(sum.replace(',', '.')) > 0.8:
            bundles_dict['CELR/USDT'] = final
        else:
            bundles_dict['CELR/USDT'] = 1

    except:
        bundles_dict['CELR/USDT'] = f'Связка <b>{celr}/{usdt}</b> не отвечает, поробуйте через 5 минут'


async def HOTUSDT(session, bundles_dict):
    try:
        hot = 'HOT'
        usdt = 'USDT'
        num_dict = {}
        num_list = []
        link_dict = {}

        async with session.get(url='https://www.mexc.com/open/api/v2/market/deals?symbol=HOT_USDT&limit=1') as mexc:
            if mexc.status == 200:
                mexc = await mexc.json()
                price_mexc = float(mexc['data'][0]['trade_price'])
                num_dict['Mexc'] = price_mexc

        # price_binance = float(client_binance.get_order_book(symbol='HOTUSDT')['bids'][0][0])
        price_binance = float(price_dict['hotusdt'])
        price_bybit = float(session_bybit.last_traded_price(symbol='HOTUSDT')['result']['price'])

        num_dict['Binance'] = price_binance
        num_dict['ByBit'] = price_bybit

        for i in num_dict:
            num_list.append(num_dict[i])

        x = min(num_list)
        y = max(num_list)

        sum = round(100 * (y - x) / x, 3)

        for k, v in num_dict.items():
            if v == x:
                name_birg_buy = k

            if v == y:
                name_birg_sell = k

        link_dict['Binance'] = 'https://www.binance.com/ru/trade/HOT_USDT?theme=dark&type=spot'
        link_dict['ByBit'] = 'https://www.bybit.com/ru-RU/trade/spot/HOT/USDT'
        link_dict['Huobi'] = 'https://www.huobi.com/en-us/exchange/hot_usdt'
        link_dict['Garantex'] = 'https://garantex.io/trading/hotusdt'
        link_dict['Mexc'] = 'https://www.mexc.com/ru-RU/exchange/HOT_USDT?_from=header'
        link_dict['KuCoin'] = 'https://www.kucoin.com/ru/trade/HOT-USDT'

        x = str(x).replace('.', ',')
        y = str(y).replace('.', ',')
        sum = str(sum).replace('.', ',')

        link_buy = f'[{usdt} в {hot}]({link_dict[name_birg_buy]})'
        link_sell = f'[{hot} в {usdt}]({link_dict[name_birg_sell]})'
        support_link = f'[:](https://jwhdkj{random.randint(1, 10000000000)}jhb.com)'

        final = [f'1️⃣*{name_birg_buy}*\\ {support_link} {link_buy} `{x}` \n\n'
                 f'2️⃣*{name_birg_sell}*\\ {support_link} {link_sell} `{y}`\n\n'
                 f'💎*{sum}%*\\\n', name_birg_buy, link_dict[name_birg_buy], name_birg_sell,
                 link_dict[name_birg_sell]]

        if float(sum.replace(',', '.')) > 0.8:
            bundles_dict['HOT/USDT'] = final
        else:
            bundles_dict['HOT/USDT'] = 1

    except:
        bundles_dict['HOT/USDT'] = f'Связка <b>{hot}/{usdt}</b> не отвечает, поробуйте через 5 минут'


async def DATAUSDT(session, bundles_dict):
    try:
        data = 'DATA'
        usdt = 'USDT'
        num_dict = {}
        num_list = []
        link_dict = {}

        # price_binance = float(client_binance.get_order_book(symbol='DATAUSDT')['bids'][0][0])
        price_binance = float(price_dict['datausdt'])
        price_kucoin = float(client_kucion.get_ticker('DATA-USDT')['price'])

        num_dict['Binance'] = price_binance
        num_dict['KuCoin'] = price_kucoin

        for i in num_dict:
            num_list.append(num_dict[i])

        x = min(num_list)
        y = max(num_list)

        sum = round(100 * (y - x) / x, 3)

        for k, v in num_dict.items():
            if v == x:
                name_birg_buy = k

            if v == y:
                name_birg_sell = k

        link_dict['Binance'] = 'https://www.binance.com/ru/trade/DATA_USDT?theme=dark&type=spot'
        link_dict['ByBit'] = 'https://www.bybit.com/ru-RU/trade/spot/DATA/USDT'
        link_dict['Huobi'] = 'https://www.huobi.com/en-us/exchange/data_usdt'
        link_dict['Garantex'] = 'https://garantex.io/trading/datausdt'
        link_dict['Mexc'] = 'https://www.mexc.com/ru-RU/exchange/DATA_USDT?_from=header'
        link_dict['KuCoin'] = 'https://www.kucoin.com/ru/trade/DATA-USDT'

        x = str(x).replace('.', ',')
        y = str(y).replace('.', ',')
        sum = str(sum).replace('.', ',')

        link_buy = f'[{usdt} в {data}]({link_dict[name_birg_buy]})'
        link_sell = f'[{data} в {usdt}]({link_dict[name_birg_sell]})'
        support_link = f'[:](https://jwhdkj{random.randint(1, 10000000000)}jhb.com)'

        final = [f'1️⃣*{name_birg_buy}*\\ {support_link} {link_buy} `{x}` \n\n'
                 f'2️⃣*{name_birg_sell}*\\ {support_link} {link_sell} `{y}`\n\n'
                 f'💎*{sum}%*\\\n', name_birg_buy, link_dict[name_birg_buy], name_birg_sell,
                 link_dict[name_birg_sell]]

        if float(sum.replace(',', '.')) > 0.8:
            bundles_dict['DATA/USDT'] = final
        else:
            bundles_dict['DATA/USDT'] = 1

    except:
        bundles_dict['DATA/USDT'] = f'Связка <b>{data}/{usdt}</b> не отвечает, поробуйте через 5 минут'


async def IRISUSDT(session, bundles_dict):
    try:
        iris = 'IRIS'
        usdt = 'USDT'
        num_dict = {}
        num_list = []
        link_dict = {}

        async with session.get(url='https://www.mexc.com/open/api/v2/market/deals?symbol=IRIS_USDT&limit=1') as mexc:
            if mexc.status == 200:
                mexc = await mexc.json()
                price_mexc = float(mexc['data'][0]['trade_price'])
                num_dict['Mexc'] = price_mexc

        # price_binance = float(client_binance.get_order_book(symbol='IRISUSDT')['bids'][0][0])

        # num_dict['Binance'] = price_binance

        for i in num_dict:
            num_list.append(num_dict[i])

        x = min(num_list)
        y = max(num_list)

        sum = round(100 * (y - x) / x, 3)

        for k, v in num_dict.items():
            if v == x:
                name_birg_buy = k

            if v == y:
                name_birg_sell = k

        link_dict['Binance'] = 'https://www.binance.com/ru/trade/IRIS_USDT?theme=dark&type=spot'
        link_dict['ByBit'] = 'https://www.bybit.com/ru-RU/trade/spot/IRIS/USDT'
        link_dict['Huobi'] = 'https://www.huobi.com/en-us/exchange/iris_usdt'
        link_dict['Garantex'] = 'https://garantex.io/trading/irisusdt'
        link_dict['Mexc'] = 'https://www.mexc.com/ru-RU/exchange/IRIS_USDT?_from=header'
        link_dict['KuCoin'] = 'https://www.kucoin.com/ru/trade/IRIS-USDT'

        x = str(x).replace('.', ',')
        y = str(y).replace('.', ',')
        sum = str(sum).replace('.', ',')

        link_buy = f'[{usdt} в {iris}]({link_dict[name_birg_buy]})'
        link_sell = f'[{iris} в {usdt}]({link_dict[name_birg_sell]})'
        support_link = f'[:](https://jwhdkj{random.randint(1, 10000000000)}jhb.com)'

        final = [f'1️⃣*{name_birg_buy}*\\ {support_link} {link_buy} `{x}` \n\n'
                 f'2️⃣*{name_birg_sell}*\\ {support_link} {link_sell} `{y}`\n\n'
                 f'💎*{sum}%*\\\n', name_birg_buy, link_dict[name_birg_buy], name_birg_sell,
                 link_dict[name_birg_sell]]

        if float(sum.replace(',', '.')) > 0.8:
            bundles_dict['IRIS/USDT'] = final
        else:
            bundles_dict['IRIS/USDT'] = 1

    except:
        bundles_dict['IRIS/USDT'] = f'Связка <b>{iris}/{usdt}</b> не отвечает, поробуйте через 5 минут'


async def USDTRUB(session, bundles_dict):
    try:
        usdt = 'USDT'
        rub = 'RUB'
        num_dict = {}
        num_list = []
        link_dict = {}

        async with session.get(url='https://api.huobi.pro/market/detail/merged?symbol=usdtrub') as response:
            if response.status == 200:
                response = await response.json()
                price_huobi = response['tick']['bid'][0]
                num_dict['Huobi'] = price_huobi

        async with session.get(url='https://www.mexc.com/open/api/v2/market/deals?symbol=USDT_RUB&limit=1') as mexc:
            if mexc.status == 200:
                mexc = await mexc.json()
                price_mexc = float(mexc['data'][0]['trade_price'])
                num_dict['Mexc'] = price_mexc

        # price_binance = float(client_binance.get_order_book(symbol='USDTRUB')['bids'][0][0])

        # num_dict['Binance'] = price_binance

        for i in num_dict:
            num_list.append(num_dict[i])

        x = min(num_list)
        y = max(num_list)

        sum = round(100 * (y - x) / x, 3)

        for k, v in num_dict.items():
            if v == x:
                name_birg_buy = k

            if v == y:
                name_birg_sell = k

        link_dict['Binance'] = 'https://www.binance.com/ru/trade/USDT_RUB?theme=dark&type=spot'
        link_dict['ByBit'] = 'https://www.bybit.com/ru-RU/trade/spot/USDT/RUB'
        link_dict['Huobi'] = 'https://www.huobi.com/en-us/exchange/usdt_rub'
        link_dict['Garantex'] = 'https://garantex.io/trading/usdtrub'
        link_dict['Mexc'] = 'https://www.mexc.com/ru-RU/exchange/USDT_RUB?_from=header'
        link_dict['KuCoin'] = 'https://www.kucoin.com/ru/trade/USDT-RUB'

        x = str(x).replace('.', ',')
        y = str(y).replace('.', ',')
        sum = str(sum).replace('.', ',')

        link_buy = f'[{rub} в {usdt}]({link_dict[name_birg_buy]})'
        link_sell = f'[{usdt} в {rub}]({link_dict[name_birg_sell]})'
        support_link = f'[:](https://jwhdkj{random.randint(1, 10000000000)}jhb.com)'

        final = [f'1️⃣*{name_birg_buy}*\\ {support_link} {link_buy} `{x}` \n\n'
                 f'2️⃣*{name_birg_sell}*\\ {support_link} {link_sell} `{y}`\n\n'
                 f'💎*{sum}%*\\\n', name_birg_buy, link_dict[name_birg_buy], name_birg_sell,
                 link_dict[name_birg_sell]]

        if float(sum.replace(',', '.')) > 0.8:
            bundles_dict['USDT/RUB'] = final
        else:
            bundles_dict['USDT/RUB'] = 1

    except:
        bundles_dict['USDT/RUB'] = f'Связка <b>{usdt}/{rub}</b> не отвечает, поробуйте через 5 минут'


async def BTCRUB(session, bundles_dict):
    try:
        btc = 'BTC'
        rub = 'RUB'
        num_dict = {}
        num_list = []
        link_dict = {}

        async with session.get(url='https://api.huobi.pro/market/detail/merged?symbol=btcrub') as response:
            if response.status == 200:
                response = await response.json()
                price_huobi = response['tick']['bid'][0]
                num_dict['Huobi'] = price_huobi

        async with session.get(url='https://www.mexc.com/open/api/v2/market/deals?symbol=BTC_RUB&limit=1') as mexc:
            if mexc.status == 200:
                mexc = await mexc.json()
                price_mexc = float(mexc['data'][0]['trade_price'])
                num_dict['Mexc'] = price_mexc

        # price_binance = float(client_binance.get_order_book(symbol='BTCRUB')['bids'][0][0])

        # num_dict['Binance'] = price_binance

        for i in num_dict:
            num_list.append(num_dict[i])

        x = min(num_list)
        y = max(num_list)

        sum = round(100 * (y - x) / x, 3)

        for k, v in num_dict.items():
            if v == x:
                name_birg_buy = k

            if v == y:
                name_birg_sell = k

        link_dict['Binance'] = 'https://www.binance.com/ru/trade/BTC_RUB?theme=dark&type=spot'
        link_dict['ByBit'] = 'https://www.bybit.com/ru-RU/trade/spot/BTC/RUB'
        link_dict['Huobi'] = 'https://www.huobi.com/en-us/exchange/btc_rub'
        link_dict['Garantex'] = 'https://garantex.io/trading/btcrub'
        link_dict['Mexc'] = 'https://www.mexc.com/ru-RU/exchange/BTC_RUB?_from=header'
        link_dict['KuCoin'] = 'https://www.kucoin.com/ru/trade/BTC-RUB'

        x = str(x).replace('.', ',')
        y = str(y).replace('.', ',')
        sum = str(sum).replace('.', ',')

        link_buy = f'[{rub} в {btc}]({link_dict[name_birg_buy]})'
        link_sell = f'[{btc} в {rub}]({link_dict[name_birg_sell]})'
        support_link = f'[:](https://jwhdkj{random.randint(1, 10000000000)}jhb.com)'

        final = [f'1️⃣*{name_birg_buy}*\\ {support_link} {link_buy} `{x}` \n\n'
                 f'2️⃣*{name_birg_sell}*\\ {support_link} {link_sell} `{y}`\n\n'
                 f'💎*{sum}%*\\\n', name_birg_buy, link_dict[name_birg_buy], name_birg_sell,
                 link_dict[name_birg_sell]]

        if float(sum.replace(',', '.')) > 0.8:
            bundles_dict['BTC/RUB'] = final
        else:
            bundles_dict['BTC/RUB'] = 1

    except:
        bundles_dict['BTC/RUB'] = f'Связка <b>{btc}/{rub}</b> не отвечает, поробуйте через 5 минут'


async def BTCUSDP2P(session, bundles_dict):
    try:
        btc = 'BTC'
        usd = 'USD'

        num_dict_buy = {}
        num_list_buy = []

        num_dict_sell = {}
        num_list_sell = []

        params_all_system_buy = {
            "proMerchantAds": False,
            "page": 1,
            "rows": 10,
            "payTypes": [],
            "countries": [],
            "publisherType": "merchant",
            "transAmount": "",
            "tradeType": "BUY",
            "asset": "BTC",
            "fiat": "USD",
            "merchantCheck": True
        }

        params_all_system_sell = {
            "proMerchantAds": False,
            "page": 1,
            "rows": 10,
            "payTypes": [],
            "countries": [],
            "publisherType": "merchant",
            "tradeType": "SELL",
            "asset": "BTC",
            "fiat": "USD",
            "merchantCheck": True}

        login = 'yCfHq6'
        password = 'VdyLQt'

        proxy_auth = aiohttp.BasicAuth(login, password)
        proxies = ['http://88.218.72.54:9326',
                   'http://88.218.72.172:9044',
                   'http://91.211.113.183:9243'
                   ]

        prox = random.choice(proxies)

        async with session.post(url=url, headers=headers, json=params_all_system_buy, proxy=prox,
                                proxy_auth=proxy_auth) as response:
            responce_all_system_pay_buy = await response.json()
            price_all_system_buy = responce_all_system_pay_buy['data'][0]['adv']['price']
            pay_system_buy = responce_all_system_pay_buy['data'][0]['adv']['tradeMethods'][0]['tradeMethodName']

        async with session.post(url=url, headers=headers, json=params_all_system_sell, proxy=prox,
                                proxy_auth=proxy_auth) as response:
            responce_all_system_pay_sell = await response.json()
            price_all_system_sell = responce_all_system_pay_sell['data'][0]['adv']['price']
            pay_system_sell = responce_all_system_pay_sell['data'][0]['adv']['tradeMethods'][0]['tradeMethodName']

        num_dict_buy[f'{pay_system_buy}'] = float(price_all_system_buy)

        for i in num_dict_buy:
            num_list_buy.append(num_dict_buy[i])

        x = min(num_list_buy)

        num_dict_sell[f'{pay_system_sell}'] = float(price_all_system_sell)

        for i in num_dict_sell:
            num_list_sell.append(num_dict_sell[i])

        y = max(num_list_sell)

        sum = 100 * (y - x) / x

        for k, v in num_dict_buy.items():
            if v == x:
                name_birg_buy = k

        for k, v in num_dict_sell.items():
            if v == y:
                name_birg_sell = k

        sum = round(sum, 4)

        link_buy = hlink(f'{usd} в {btc}', 'https://p2p.binance.com/ru/trade/all-payments/BTC?fiat=USD')
        link_sell = hlink(f'{btc} в {usd}', 'https://p2p.binance.com/ru/trade/sell/BTC?fiat=USD&payment=ALL')
        support_link = hlink(':', f'https://jwhdkj{random.randint(1, 10000000000)}jhb.com')

        final = [f'1️⃣<b>{name_birg_buy}</b>{support_link} {link_buy} <u>{x}</u>\n\n'
                f'2️⃣<b>{name_birg_sell}</b>{support_link} {link_sell} <u>{y}</u>\n\n'
                f'💎<b>{sum}%</b>\n',
                f'Купить {btc} за {usd}', 'https://p2p.binance.com/ru/trade/all-payments/BTC?fiat=USD',
                f'Продать {btc} за {usd}', 'https://p2p.binance.com/ru/trade/sell/BTC?fiat=USD&payment=ALL']

        if float(sum) > 0.8:
            bundles_dict['BTC/USDP2P'] = final
        else:
            bundles_dict['BTC/USDP2P'] = 1

    except:
        bundles_dict['BTC/USDP2P'] = f'Связка <b>{btc}/{usd}</b> не отвечает, поробуйте через 5 минут'


async def BTCRUBP2P(session, bundles_dict):
    try:
        btc = 'BTC'
        rub = 'RUB'

        num_dict_buy = {}
        num_list_buy = []

        num_dict_sell = {}
        num_list_sell = []

        params_tinkoff_buy = {
            "proMerchantAds": False,
            "page": 1,
            "rows": 10,
            "payTypes": ["TinkoffNew"],
            "countries": [],
            "publisherType": None, "transAmount": "",
            "asset": "BTC",
            "fiat": "RUB",
            "tradeType": "BUY"}

        params_tinkoff_sell = {
            "proMerchantAds": False,
            "page": 1,
            "rows": 10,
            "payTypes": ["TinkoffNew"],
            "countries": [],
            "publisherType": None,
            "asset": "BTC",
            "fiat": "RUB",
            "tradeType": "SELL"}

        params_all_system_buy = {
            "proMerchantAds": False,
            "page": 1,
            "rows": 10,
            "payTypes": [],
            "countries": [],
            "publisherType": None,
            "transAmount": "",
            "asset": "BTC",
            "fiat": "RUB",
            "tradeType": "BUY"}

        params_all_system_sell = {
            "proMerchantAds": False,
            "page": 1,
            "rows": 10,
            "payTypes": [],
            "countries": [],
            "publisherType": None,
            "transAmount": "",
            "tradeType": "SELL",
            "asset": "BTC",
            "fiat": "RUB"}

        login = 'p4EhY7'
        password = 'vNS7WR'

        proxy_auth = aiohttp.BasicAuth(login, password)
        proxies = ['http://213.166.72.204:9901',
                   'http://194.67.197.38:9473',
                   'http://213.166.75.206:9049',
                   'http://194.187.120.154:9276']

        prox = random.choice(proxies)

        async with session.post(url=url, headers=headers, json=params_tinkoff_buy, proxy=prox,
                                proxy_auth=proxy_auth) as response:
            responce_tinkoff_buy = await response.json()
            price_tinkoff_buy = responce_tinkoff_buy['data'][0]['adv']['price']

        async with session.post(url=url, headers=headers, json=params_tinkoff_sell, proxy=prox,
                                proxy_auth=proxy_auth) as response:
            responce_tinkoff_sell = await response.json()
            price_tinkoff_sell = responce_tinkoff_sell['data'][0]['adv']['price']

        async with session.post(url=url, headers=headers, json=params_all_system_buy, proxy=prox,
                                proxy_auth=proxy_auth) as response:
            responce_all_system_buy = await response.json()
            price_all_system_buy = responce_all_system_buy['data'][0]['adv']['price']
            pay_system_buy = responce_all_system_buy['data'][0]['adv']['tradeMethods'][0]['tradeMethodName']

        async with session.post(url=url, headers=headers, json=params_all_system_sell, proxy=prox,
                                proxy_auth=proxy_auth) as response:
            responce_all_system_sell = await response.json()
            price_all_system_sell = responce_all_system_sell['data'][0]['adv']['price']
            pay_system_sell = responce_all_system_sell['data'][0]['adv']['tradeMethods'][0]['tradeMethodName']

        num_dict_buy['Tinkoff'] = float(price_tinkoff_buy)
        num_dict_buy[f'{pay_system_buy}'] = float(price_all_system_buy)

        for i in num_dict_buy:
            num_list_buy.append(num_dict_buy[i])

        x = min(num_list_buy)

        num_dict_sell['Tinkoff'] = float(price_tinkoff_sell)
        num_dict_sell[f'{pay_system_sell}'] = float(price_all_system_sell)

        for i in num_dict_sell:
            num_list_sell.append(num_dict_sell[i])

        y = max(num_list_sell)

        sum = 100 * (y - x) / x

        for k, v in num_dict_buy.items():
            if v == x:
                name_birg_buy = k

        for k, v in num_dict_sell.items():
            if v == y:
                name_birg_sell = k

        sum = round(sum, 4)

        link_buy = hlink(f'{rub} в {btc}', 'https://p2p.binance.com/ru/trade/all-payments/BTC?fiat=RUB')
        link_sell = hlink(f'{btc} в {rub}', 'https://p2p.binance.com/ru/trade/sell/BTC?fiat=RUB&payment=ALL')
        support_link = hlink(':', f'https://jwhdkj{random.randint(1, 10000000000)}jhb.com')

        final = [f'1️⃣<b>{name_birg_buy}</b>{support_link} {link_buy} <u>{x}</u>\n\n'
                 f'2️⃣<b>{name_birg_sell}</b>{support_link} {link_sell} <u>{y}</u>\n\n'
                 f'💎<b>{sum}%</b>\n',
                 f'Купить {btc} за {rub}', 'https://p2p.binance.com/ru/trade/all-payments/BTC?fiat=RUB',
                 f'Продать {btc} за {rub}', 'https://p2p.binance.com/ru/trade/sell/BTC?fiat=RUB&payment=ALL']

        bundles_dict['BTC/RUBP2P'] = final


    except:
        bundles_dict['BTC/RUBP2P'] = f'Связка <b>{btc}/{rub}</b> не отвечает, поробуйте через 5 минут'


async def USDTRUBP2P(session, bundles_dict):
    try:
        usdt = 'USDT'
        rub = 'RUB'

        num_dict_buy = {}
        num_list_buy = []

        num_dict_sell = {}
        num_list_sell = []

        params_all_system_sell_rus = {
            "proMerchantAds": False,
            "page": 1,
            "rows": 10,
            "payTypes": [],
            "countries": [],
            "publisherType": None,
            "fiat": "RUB",
            "tradeType": "SELL",
            "asset": "USDT",
            "merchantCheck": False}

        params_all_system_buy = {
            "proMerchantAds": False,
            "page": 1,
            "rows": 10,
            "payTypes": [],
            "countries": [],
            "publisherType": None,
            "fiat": "RUB",
            "tradeType": "BUY",
            "asset": "USDT",
            "merchantCheck": False}

        login = 'yCfHq6'
        password = 'VdyLQt'

        proxy_auth = aiohttp.BasicAuth(login, password)
        proxies = ['http://91.211.113.183:9243',
                   'http://45.153.75.131:9679',
                   'http://185.191.142.58:9019'
                   ]

        prox = random.choice(proxies)

        async with session.post(url=url, headers=headers, json=params_all_system_sell_rus, proxy=prox,
                                proxy_auth=proxy_auth) as response:
            responce_all_system_sell_rus = await response.json()
            price_all_system_sell_rus = responce_all_system_sell_rus['data'][0]['adv']['price']
            pay_all_system_sell_rus = responce_all_system_sell_rus['data'][0]['adv']['tradeMethods'][0][
                'tradeMethodName']

        async with session.post(url=url, headers=headers, json=params_all_system_buy, proxy=prox,
                                proxy_auth=proxy_auth) as response:
            responce_all_system_buy = await response.json()
            price_all_system_buy = responce_all_system_buy['data'][0]['adv']['price']
            pay_system_buy = responce_all_system_buy['data'][0]['adv']['tradeMethods'][0]['tradeMethodName']

        num_dict_buy[f'{pay_system_buy}'] = float(price_all_system_buy)

        for i in num_dict_buy:
            num_list_buy.append(num_dict_buy[i])

        x = min(num_list_buy)

        num_dict_sell[f'{pay_all_system_sell_rus}'] = float(price_all_system_sell_rus)

        for i in num_dict_sell:
            num_list_sell.append(num_dict_sell[i])

        y = max(num_list_sell)

        sum = 100 * (y - x) / x

        for k, v in num_dict_buy.items():
            if v == x:
                name_birg_buy = k

        for k, v in num_dict_sell.items():
            if v == y:
                name_birg_sell = k

        sum = round(sum, 4)

        link_buy = hlink(f'{rub} в {usdt}', 'hhttps://p2p.binance.com/ru/trade/all-payments/USDT?fiat=RUB')
        link_sell = hlink(f'{usdt} в {rub}', 'https://p2p.binance.com/ru/trade/sell/USDT?fiat=RUB&payment=ALL')
        support_link = hlink(':', f'https://jwhdkj{random.randint(1, 10000000000)}jhb.com')

        final = [f'1️⃣<b>{name_birg_buy}</b>{support_link} {link_buy} <u>{x}</u>\n\n'
                 f'2️⃣<b>{name_birg_sell}</b>{support_link} {link_sell} <u>{y}</u>\n\n'
                 f'💎<b>{sum}%</b>\n',
                 f'Купить {usdt} за {rub}', 'https://p2p.binance.com/ru/trade/all-payments/USDT?fiat=RUB',
                 f'Продать {usdt} за {rub}', 'https://p2p.binance.com/ru/trade/sell/USDT?fiat=RUB&payment=ALL']

        if float(sum) > 0.8:
            bundles_dict['USDT/RUBP2P'] = final
        else:
            bundles_dict['USDT/RUBP2P'] = 1

    except:
        bundles_dict['USDT/RUBP2P'] = f'Связка <b>{usdt}/{rub}</b> не отвечает, поробуйте через 5 минут'


async def USDTUSDP2P(session, bundles_dict):
    try:
        usdt = 'USDT'
        usd = 'USD'

        num_dict_buy = {}
        num_list_buy = []

        num_dict_sell = {}
        num_list_sell = []

        params_all_system_buy = {
            "proMerchantAds": False,
            "page": 1,
            "rows": 10,
            "payTypes": [],
            "countries": [],
            "publisherType": "merchant",
            "fiat": "USD",
            "tradeType": "BUY",
            "asset": "USDT",
            "merchantCheck": True}

        params_all_system_sell = {
            "proMerchantAds": False,
            "page": 1,
            "rows": 10,
            "payTypes": [],
            "countries": [],
            "publisherType": "merchant",
            "asset": "USDT",
            "fiat": "USD",
            "tradeType": "SELL"}

        login = 'yCfHq6'
        password = 'VdyLQt'

        proxy_auth = aiohttp.BasicAuth(login, password)
        proxies = ['http://91.211.113.183:9243',
                   'http://45.153.75.131:9679',
                   'http://185.191.142.58:9019'
                   ]

        prox = random.choice(proxies)

        async with session.post(url=url, headers=headers, json=params_all_system_buy, proxy=prox,
                                proxy_auth=proxy_auth) as response:
            responce_all_system_pay_buy = await response.json()
            price_all_system_buy = responce_all_system_pay_buy['data'][0]['adv']['price']
            pay_system_buy = responce_all_system_pay_buy['data'][0]['adv']['tradeMethods'][0]['tradeMethodName']

        async with session.post(url=url, headers=headers, json=params_all_system_sell, proxy=prox,
                                proxy_auth=proxy_auth) as response:
            responce_all_system_sell = await response.json()
            price_all_system_sell = responce_all_system_sell['data'][0]['adv']['price']
            pay_system_sell = responce_all_system_sell['data'][0]['adv']['tradeMethods'][0]['tradeMethodName']

        num_dict_buy[f'{pay_system_buy}'] = float(price_all_system_buy)

        for i in num_dict_buy:
            num_list_buy.append(num_dict_buy[i])

        x = min(num_list_buy)

        num_dict_sell[f'{pay_system_sell}'] = float(price_all_system_sell)

        for i in num_dict_sell:
            num_list_sell.append(num_dict_sell[i])

        y = max(num_list_sell)

        sum = 100 * (y - x) / x

        for k, v in num_dict_buy.items():
            if v == x:
                name_birg_buy = k

        for k, v in num_dict_sell.items():
            if v == y:
                name_birg_sell = k

        sum = round(sum, 4)

        link_buy = hlink(f'{usd} в {usdt}', 'https://p2p.binance.com/ru/trade/all-payments/USDT?fiat=USD')
        link_sell = hlink(f'{usdt} в {usd}', 'https://p2p.binance.com/ru/trade/sell/USDT?fiat=USD&payment=ALL')
        support_link = hlink(':', f'https://jwhdkj{random.randint(1, 10000000000)}jhb.com')

        final = [f'1️⃣<b>{name_birg_buy}</b>{support_link} {link_buy} <u>{x}</u>\n\n'
                 f'2️⃣<b>{name_birg_sell}</b>{support_link} {link_sell} <u>{y}</u>\n\n'
                 f'💎<b>{sum}%</b>\n',
                 f'Купить {usdt} за {usd}', 'https://p2p.binance.com/ru/trade/all-payments/USDT?fiat=USD',
                 f'Продать {usdt} за {usd}', 'https://p2p.binance.com/ru/trade/sell/USDT?fiat=USD&payment=ALL']

        if float(sum) > 0.8:
            bundles_dict['USDT/USDP2P'] = final
        else:
            bundles_dict['USDT/USDP2P'] = 1

    except:
        bundles_dict['USDT/USDP2P'] = f'Связка <b>{usdt}/{usd}</b> не отвечает, поробуйте через 5 минут'


async def BNBRUBP2P(session, bundles_dict):
    try:
        bnb = 'BNB'
        rub = 'RUB'

        num_dict_buy = {}
        num_list_buy = []

        num_dict_sell = {}
        num_list_sell = []

        params_tinkoff_buy = {
            "proMerchantAds": False,
            "page": 1,
            "rows": 10,
            "payTypes": ["TinkoffNew"],
            "countries": [],
            "publisherType": None,
            "tradeType": "BUY",
            "asset": "BNB",
            "fiat": "RUB"
        }

        params_tinkoff_sell = {
            "proMerchantAds": False,
            "page": 1,
            "rows": 10,
            "payTypes": ["TinkoffNew"],
            "countries": [],
            "publisherType": None,
            "tradeType": "SELL",
            "asset": "BNB",
            "fiat": "RUB"
        }

        params_all_system_buy = {
            "proMerchantAds": False,
            "page": 1,
            "rows": 10,
            "payTypes": [],
            "countries": [],
            "publisherType": None,
            "tradeType": "BUY",
            "asset": "BNB",
            "fiat": "RUB"
        }

        params_all_system_sell = {
            "proMerchantAds": False,
            "page": 1,
            "rows": 10,
            "payTypes": [],
            "countries": [],
            "publisherType": None,
            "tradeType": "SELL",
            "asset": "BNB",
            "fiat": "RUB"
        }

        login = 'yCfHq6'
        password = 'VdyLQt'

        proxy_auth = aiohttp.BasicAuth(login, password)
        proxies = ['http://88.218.72.54:9326',
                   'http://88.218.72.172:9044',
                   'http://185.191.142.58:9019'
                   ]

        prox = random.choice(proxies)

        async with session.post(url=url, headers=headers, json=params_tinkoff_buy, proxy=prox,
                                proxy_auth=proxy_auth) as response:
            responce_tinkoff_buy = await response.json()
            price_tinkoff_buy = responce_tinkoff_buy['data'][0]['adv']['price']

        async with session.post(url=url, headers=headers, json=params_tinkoff_sell, proxy=prox,
                                proxy_auth=proxy_auth) as response:
            responce_tinkoff_sell = await response.json()
            price_tinkoff_sell = responce_tinkoff_sell['data'][0]['adv']['price']

        async with session.post(url=url, headers=headers, json=params_all_system_buy, proxy=prox,
                                proxy_auth=proxy_auth) as response:
            responce_all_system_buy = await response.json()
            price_all_system_buy = responce_all_system_buy['data'][0]['adv']['price']
            pay_system_buy = responce_all_system_buy['data'][0]['adv']['tradeMethods'][0]['tradeMethodName']

        async with session.post(url=url, headers=headers, json=params_all_system_sell, proxy=prox,
                                proxy_auth=proxy_auth) as response:
            responce_all_system_sell = await response.json()
            price_all_system_sell = responce_all_system_sell['data'][0]['adv']['price']
            pay_system_sell = responce_all_system_sell['data'][0]['adv']['tradeMethods'][0]['tradeMethodName']

        num_dict_buy['Tinkoff'] = float(price_tinkoff_buy)
        num_dict_buy[f'{pay_system_buy}'] = float(price_all_system_buy)

        for i in num_dict_buy:
            num_list_buy.append(num_dict_buy[i])

        x = min(num_list_buy)

        num_dict_sell['Tinkoff'] = float(price_tinkoff_sell)
        num_dict_sell[f'{pay_system_sell}'] = float(price_all_system_sell)

        for i in num_dict_sell:
            num_list_sell.append(num_dict_sell[i])

        y = max(num_list_sell)

        sum = 100 * (y - x) / x

        for k, v in num_dict_buy.items():
            if v == x:
                name_birg_buy = k

        for k, v in num_dict_sell.items():
            if v == y:
                name_birg_sell = k

        sum = round(sum, 4)

        link_buy = hlink(f'{rub} в {bnb}', 'https://p2p.binance.com/ru/trade/all-payments/BNB?fiat=RUB')
        link_sell = hlink(f'{bnb} в {rub}', 'https://p2p.binance.com/ru/trade/sell/BNB?fiat=RUB&payment=ALL')
        support_link = hlink(':', f'https://jwhdkj{random.randint(1, 10000000000)}jhb.com')

        final = [f'1️⃣<b>{name_birg_buy}</b>{support_link} {link_buy} <u>{x}</u>\n\n'
                 f'2️⃣<b>{name_birg_sell}</b>{support_link} {link_sell} <u>{y}</u>\n\n'
                 f'💎<b>{sum}%</b>\n',
                 f'Купить {bnb} за {rub}', 'https://p2p.binance.com/ru/trade/all-payments/BNB?fiat=RUB',
                 f'Продать {bnb} за {rub}', 'https://p2p.binance.com/ru/trade/sell/BNB?fiat=RUB&payment=ALL']

        if float(sum) > 0.8:
            bundles_dict['BNB/RUBP2P'] = final
        else:
            bundles_dict['BNB/RUBP2P'] = 1

    except:
        bundles_dict['BNB/RUBP2P'] = f'Связка <b>{bnb}/{rub}</b> не отвечает, поробуйте через 5 минут'


async def ETHRUBP2P(session, bundles_dict):
    try:
        eth = 'ETH'
        rub = 'RUB'

        num_dict_buy = {}
        num_list_buy = []

        num_dict_sell = {}
        num_list_sell = []

        params_tinkoff_buy = {
            "proMerchantAds": False,
            "page": 1,
            "rows": 10,
            "payTypes": ["TinkoffNew"],
            "countries": [],
            "publisherType": None,
            "tradeType": "BUY",
            "asset": "ETH",
            "fiat": "RUB"
        }

        params_tinkoff_sell = {
            "proMerchantAds": False,
            "page": 1,
            "rows": 10,
            "payTypes": ["TinkoffNew"],
            "countries": [],
            "publisherType": None,
            "tradeType": "SELL",
            "asset": "ETH",
            "fiat": "RUB"
        }

        params_all_system_buy = {
            "proMerchantAds": False,
            "page": 1,
            "rows": 10,
            "payTypes": [],
            "countries": [],
            "publisherType": None,
            "tradeType": "BUY",
            "asset": "ETH",
            "fiat": "RUB"
        }

        params_all_system_sell = {
            "proMerchantAds": False,
            "page": 1,
            "rows": 10,
            "payTypes": [],
            "countries": [],
            "publisherType": None,
            "tradeType": "SELL",
            "asset": "ETH",
            "fiat": "RUB"
        }

        login = 'p4EhY7'
        password = 'vNS7WR'

        proxy_auth = aiohttp.BasicAuth(login, password)
        proxies = ['http://213.166.72.204:9901',
                   'http://194.67.197.38:9473',
                   'http://213.166.75.206:9049',
                   'http://91.188.240.158:9269']

        prox = random.choice(proxies)

        async with session.post(url=url, headers=headers, json=params_tinkoff_buy, proxy=prox,
                                proxy_auth=proxy_auth) as response:
            responce_tinkoff_buy = await response.json()
            price_tinkoff_buy = responce_tinkoff_buy['data'][0]['adv']['price']

        async with session.post(url=url, headers=headers, json=params_tinkoff_sell, proxy=prox,
                                proxy_auth=proxy_auth) as response:
            responce_tinkoff_sell = await response.json()
            price_tinkoff_sell = responce_tinkoff_sell['data'][0]['adv']['price']

        async with session.post(url=url, headers=headers, json=params_all_system_buy, proxy=prox,
                                proxy_auth=proxy_auth) as response:
            responce_all_system_buy = await response.json()
            price_all_system_buy = responce_all_system_buy['data'][0]['adv']['price']
            pay_system_buy = responce_all_system_buy['data'][0]['adv']['tradeMethods'][0]['tradeMethodName']

        async with session.post(url=url, headers=headers, json=params_all_system_sell, proxy=prox,
                                proxy_auth=proxy_auth) as response:
            responce_all_system_sell = await response.json()
            price_all_system_sell = responce_all_system_sell['data'][0]['adv']['price']
            pay_system_sell = responce_all_system_sell['data'][0]['adv']['tradeMethods'][0]['tradeMethodName']

        num_dict_buy['Tinkoff'] = float(price_tinkoff_buy)
        num_dict_buy[f'{pay_system_buy}'] = float(price_all_system_buy)

        for i in num_dict_buy:
            num_list_buy.append(num_dict_buy[i])

        x = min(num_list_buy)

        num_dict_sell['Tinkoff'] = float(price_tinkoff_sell)
        num_dict_sell[f'{pay_system_sell}'] = float(price_all_system_sell)

        for i in num_dict_sell:
            num_list_sell.append(num_dict_sell[i])

        y = max(num_list_sell)

        sum = 100 * (y - x) / x

        for k, v in num_dict_buy.items():
            if v == x:
                name_birg_buy = k

        for k, v in num_dict_sell.items():
            if v == y:
                name_birg_sell = k

        sum = round(sum, 4)

        link_buy = hlink(f'{rub} в {eth}', 'https://p2p.binance.com/ru/trade/all-payments/ETH?fiat=RUB')
        link_sell = hlink(f'{eth} в {rub}', 'https://p2p.binance.com/ru/trade/sell/ETH?fiat=RUB&payment=ALL')
        support_link = hlink(':', f'https://jwhdkj{random.randint(1, 10000000000)}jhb.com')

        final = [f'1️⃣<b>{name_birg_buy}</b>{support_link} {link_buy} <u>{x}</u>\n\n'
                 f'2️⃣<b>{name_birg_sell}</b>{support_link} {link_sell} <u>{y}</u>\n\n'
                 f'💎<b>{sum}%</b>\n',
                 f'Купить {eth} за {rub}', 'https://p2p.binance.com/ru/trade/all-payments/ETH?fiat=RUB',
                 f'Продать {eth} за {rub}', 'https://p2p.binance.com/ru/trade/sell/ETH?fiat=RUB&payment=ALL']

        if float(sum) > 0.8:
            bundles_dict['ETH/RUBP2P'] = final
        else:
            bundles_dict['ETH/RUBP2P'] = 1

    except:
        bundles_dict['ETH/RUBP2P'] = f'Связка <b>{eth}/{rub}</b> не отвечает, поробуйте через 5 минут'

