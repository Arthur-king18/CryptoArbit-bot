import asyncio
import aiohttp
import datetime
import random
import time

import aioschedule
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.utils.markdown import hlink
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types.web_app_info import WebAppInfo
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import datetime as DT
from threading import Thread
from binance.websocket.spot.websocket_stream import SpotWebsocketStreamClient

from db import DataBase
from config import TOKEN, p2p, price_dict
from websocket_my import MyThread

from bundles import BTCUSDT, SOLUSDT, ETHUSDT, BNBUSDT, ADAUSDT, XRPUSDT, ANKRUSDT, USDTRUB, BTCRUB, BTCUSDP2P, \
    BTCRUBP2P, USDTRUBP2P, USDTUSDP2P, ICXUSDT, IOTXUSDT, SOFIUSDT, ANTUSDT, BBFUSDT, CULTUSDT, BAXUSDT, CELRUSDT, \
    HOTUSDT, DATAUSDT, IRISUSDT, BNBRUBP2P, ETHRUBP2P

storage = MemoryStorage()
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot, storage=storage)
db = DataBase('database.db')

CHANNEL_ID = '@CryptoArbit_Channel'

admin_id_list = [1638270549]
super_private_list = [1638270549]

bundles_list_between = ['BTC/USDT', 'ETH/USDT', 'SOL/USDT', 'BNB/USDT', 'ADA/USDT', 'ANKR/USDT', 'ICX/USDT',
                        'IOTX/USDT', 'SOFI/USDT', 'ANT/USDT', 'BBF/USDT', 'CULT/USDT', 'BAX/USDT', 'CELR/USDT',
                        'HOT/USDT',
                        'DATA/USDT', 'IRIS/USDT', 'USDT/RUB', 'BTC/RUB']

bundles_list_p2p = ['BTC/USDP2P', 'BTC/RUBP2P', 'USDT/RUBP2P', 'USDT/USDP2P', 'BNB/RUBP2P', 'ETH/RUBP2P']

symbols = ['hotusdt', 'sntusdt', 'shibusdt', 'filusdt', 'egldusdt', '1inchusdt', 'aliceusdt', 'icpusdt', 'nmrusdt',
           'chzusdt', 'dentusdt', 'eosbtc', 'bnbbtc', 'adabtc', 'ftmusdt', 'adausdt', 'sandusdt', 'zrxusdt', 'omgusdt',
           'nearusdt', 'bttcusdt', 'imxusdt', 'dogeusdt', 'roseusdt', 'fetbtc', 'astrusdt', 'xrpusdt', 'ardrusdt',
           'xvsusdt', 'galausdt', 'enjusdt', 'cakeusdt', 'dashbtc', 'aaveusdt', 'kavausdt', 'xlmusdt', 'funusdt',
           'flowusdt', 'mtlusdt', 'bnbusdt', 'jstusdt', 'ltcusdt', 'hiveusdt', 'trxbtc', 'busdusdt', 'xlmbtc',
           'xemusdt', 'spellusdt', 'luncusdt', 'ltcbtc', 'ldousdt', 'solusdt', 'ctsiusdt', 'radusdt', 'idusdt',
           'idexusdt', 'pepeusdt', 'cfxusdt', 'btcusdt', 'xmrusdt', 'audiousdt', 'bchusdt', 'stxusdt', 'ethusdt',
           'alphausdt', 'axsusdt', 'minausdt', 'ctxcusdt', 'firousdt', 'antusdt', 'dashusdt', 'wavesusdt', 'blzusdt',
           'ethbtc', 'maticbtc', 'maskusdt', 'opusdt', 'tusdusdt', 'portousdt', 'trxusdt', 'renusdt', 'linkusdt',
           'hbarusdt', 'bandusdt', 'etcusdt', 'alcxusdt', 'eosusdt', 'multiusdt', 'dotusdt', 'apeusdt', 'wrxusdt',
           'arbusdt', 'tomousdt', 'manausdt', 'sklusdt', 'joeusdt', 'sxpusdt', 'santosusdt', 'slpusdt', 'uniusdt',
           'ontusdt', 'laziousdt', 'glmusdt', 'celousdt', 'lptusdt', 'datausdt', 'iotausdt', 'bntusdt', 'linausdt',
           'dgbusdt', 'rvnusdt', 'snxusdt', 'lskusdt', 'fetusdt', 'maticusdt', 'grtusdt', 'crvusdt', 'avaxusdt',
           'injusdt', 'twtusdt', 'achusdt', 'xtzusdt', 'thetausdt', 'zilbtc', 'batusdt', 'chrusdt', 'perlusdt',
           'iostbtc', 'cosusdt', 'cotiusdt', 'api3usdt', 'galusdt', 'yfiiusdt', 'yfiusdt', 'atomusdt', 'ensusdt',
           'xrpbtc', 'kncusdt', 'dydxusdt', 'arusdt', 'xvgusdt', 'leverusdt', 'rndrusdt', 'reqbtc', 'klayusdt',
           'ksmusdt', 'iostusdt', 'perpusdt', 'xecusdt', 'betausdt', 'dexeusdt', 'farmusdt', 'atombtc', 'paxgusdt',
           'qiusdt', 'umausdt', 'lokausdt', 'tlmusdt', 'yggusdt', 'keyusdt', 'qtumusdt', 'usdcusdt', 'oxtusdt',
           'nknusdt', 'rsrusdt', 'gmtusdt', 'zilusdt', 'pundixusdt', 'burgerusdt', 'vgxusdt', 'zecusdt', 'reefusdt',
           'rlcusdt', 'clvusdt', 'woousdt', 'celrusdt', 'darusdt', 'bnxusdt', 'duskusdt', 'gnousdt', 'phausdt',
           'atausdt', 'trbusdt', 'avausdt', 'iotxusdt', 'sushiusdt', 'oneusdt', 'superusdt', 'xmrbtc', 'glmrusdt',
           'cityusdt', 'mdxusdt', 'icxbtc', 'scrtusdt', 'chessusdt', 'algousdt', 'lqtyusdt', 'compusdt', 'highusdt',
           'agldusdt', 'kdausdt', 'celrbtc', 'neousdt', 'jasmyusdt', 'ankrusdt', 'bondusdt', 'rayusdt', 'bswusdt',
           'qntusdt', 'btsusdt', 'vetusdt', 'steemusdt', 'scusdt', 'pyrusdt', 'lrcusdt', 'runeusdt', 'rvnbtc',
           'straxusdt', 'icxusdt', 'thetabtc', 'pntusdt', 'tusdt', 'oceanusdt', 'ckbusdt', 'fluxusdt', 'stmxusdt',
           'voxelusdt', 'loomusdt', 'mboxusdt', 'acausdt', 'mdtusdt', 'dodousdt', 'adxusdt', 'waxpusdt', 'glmbtc',
           'degousdt', 'tkousdt', 'sysusdt', 'ookiusdt', 'viteusdt', 'cvcusdt', 'mkrusdt', 'bakeusdt', 'ilvusdt',
           'xnousdt', 'ognusdt', 'polyxusdt', 'winusdt', 'kmdusdt', 'nulsusdt', 'vibusdt', 'sntbtc', 'alpacausdt',
           'mcusdt', 'quickusdt', 'flokiusdt', 'storjusdt', 'acmusdt', 'dcrusdt', 'forusdt', 'batbtc', 'alpineusdt',
           'balusdt', 'dockusdt', 'qkcusdt', 'sunusdt', 'ltousdt', 'auctionusdt', 'fidausdt', 'diausdt', 'requsdt',
           'zrxbtc', 'ghstusdt', 'plausdt', 'qkcbtc', 'reiusdt', 'powrusdt', 'ampusdt', 'tfuelusdt', 'bicousdt',
           'psgusdt', 'wtcusdt', 'pondusdt', 'nulsbtc', 'frontusdt']


# ------------ Technical block ------------------------------------------------#

async def scheduler_for_update():
    print('Sebscribe!')
    result = db.get_all_user_id()

    for id in result:
        vip_status = db.get_vip_status(id[0])
        end_time = db.end_time(id[0])

        if db.change_seb_3day(vip_status, end_time) == 'ok' or db.change_seb_month(vip_status, end_time) == 'ok' or \
                db.change_seb_midle_year(vip_status, end_time) == 'ok' or db.change_seb_year(vip_status,
                                                                                             end_time) == 'ok':
            db.unviped(id[0])
            try:
                await bot.send_message(id[0], f'<b>CryptoArbit Bot</b>\n\n'
                                            f'⛔ Подписка закончена', reply_markup=kb_pro_in, parse_mode='html')
            except:
                db.set_active(id[0], 0)
                
        if db.change_seb_3day(vip_status, end_time) == 1 or db.change_seb_month(vip_status, end_time) == 1 or \
                db.change_seb_midle_year(vip_status, end_time) == 1 or db.change_seb_year(vip_status,
                                                                                         end_time) == 1:
            try:
                await bot.send_message(id[0], '❗❗❗❗ До конца подписки остался 1 день', reply_markup=kb_pro_in)
            except:
                db.set_active(id[0], 0)
            
        if db.change_seb_3day(vip_status, end_time) == 2 or db.change_seb_month(vip_status, end_time) == 2 or \
                db.change_seb_midle_year(vip_status, end_time) == 2 or db.change_seb_year(vip_status,
                                                                                          end_time) == 2:
            try:
                await bot.send_message(id[0], '❗❗ До конца подписки остался 2 дня', reply_markup=kb_pro_in)
            except:
                db.set_active(id[0], 0)

        if db.change_seb_month(vip_status, end_time) == 4 or db.change_seb_midle_year(vip_status, end_time) == 4 or \
                db.change_seb_year(vip_status, end_time) == 4:
            try:
                await bot.send_message(id[0], '❗❗ До конца подписки остался 4 дня', reply_markup=kb_pro_in)
            except:
                db.set_active(id[0], 0)


async def scheduler_for_update_bot():
    # aioschedule.every().day.at("7:00").do(scheduler_for_update)
    while True:
        await scheduler_for_update()
        await asyncio.sleep(10800)


# async def sent_message_for_tg_channel():
#     pass  #Отравлять сообщение в канал
#
# async def scheduler_for_sent_message():
#     aioschedule.every().day.at("7:00").do(sent_message_for_tg_channel)
#     while True:
#         await aioschedule.run_pending()
#         await asyncio.sleep(1)

async def gather_data_1(bundles_dict):
    while True:
        tasks = []
        async with aiohttp.ClientSession() as session:
            bun = [BTCUSDP2P, BTCRUBP2P, USDTRUBP2P, USDTUSDP2P, BNBRUBP2P, ETHRUBP2P]
            for val in bun:
                task = asyncio.create_task(val(session, bundles_dict))
                tasks.append(task)

            await asyncio.gather(*tasks)

        await asyncio.sleep(10)


async def gather_data_2(bundles_dict):
    while True:
        tasks = []
        async with aiohttp.ClientSession() as session:
            bun = [ANKRUSDT, ICXUSDT, IOTXUSDT, SOFIUSDT, ANTUSDT, BBFUSDT, HOTUSDT, DATAUSDT, USDTRUB, BTCRUB]
            for val in bun:
                task = asyncio.create_task(val(session, bundles_dict))
                tasks.append(task)

            await asyncio.gather(*tasks)


async def gather_data_3(bundles_dict):
    while True:
        tasks = []
        async with aiohttp.ClientSession() as session:
            bun = [BTCUSDT, SOLUSDT, ETHUSDT, BNBUSDT, ADAUSDT, CULTUSDT, BAXUSDT, CELRUSDT, IRISUSDT]
            for val in bun:
                task = asyncio.create_task(val(session, bundles_dict))
                tasks.append(task)

            await asyncio.gather(*tasks)


def task_1(bundles_dict):
    asyncio.run(gather_data_1(bundles_dict))


def task_2(bundles_dict):
    asyncio.run(gather_data_2(bundles_dict))


def task_3(bundles_dict):
    asyncio.run(gather_data_3(bundles_dict))


async def on_startup(_):
    print('Бот вышел в онлайн')
    asyncio.create_task(scheduler_for_update_bot())


# ------------ Button ------------ -------------------------------#

btn_start = KeyboardButton('/start')
# btn_get_number = KeyboardButton('Отправить свой контакт!', request_contact=True)
# btn_register = InlineKeyboardButton(text='Регистрация', callback_data='Регистрация')

btn_check_week = InlineKeyboardButton(text='Проверить платёж', callback_data='Проверка платежа (неделя)')
btn_check_month = InlineKeyboardButton(text='Проверить платёж', callback_data='Проверка платежа (месяц)')
btn_check_mid_year = InlineKeyboardButton(text='Проверить платёж', callback_data='Проверка платежа (полгода)')
btn_check_year = InlineKeyboardButton(text='Проверить платёж', callback_data='Проверка платежа (год)')

btn_fun = KeyboardButton('👋')

kb_get_number = ReplyKeyboardMarkup(resize_keyboard=True)
kb_fun = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_register = InlineKeyboardMarkup(row_width=1)
kb_check_week = InlineKeyboardMarkup(row_width=1)
kb_check_month = InlineKeyboardMarkup(row_width=1)
kb_check_mid_year = InlineKeyboardMarkup(row_width=1)
kb_check_year = InlineKeyboardMarkup(row_width=1)
kb_back_and_bundles = InlineKeyboardMarkup(row_width=1)

kb_fun.add(btn_fun)
# kb_get_number.row(btn_get_number)
# kb_register.row(btn_register)
kb_check_week.row(btn_check_week)
kb_check_month.row(btn_check_month)
kb_check_mid_year.row(btn_check_mid_year)
kb_check_year.row(btn_check_year)

seb_btn = InlineKeyboardButton(text='Подписаться !', url='https://t.me/CryptoArbit_Channel')
btn_i_seb = InlineKeyboardButton(text='Я подписался ✅', callback_data='Назад к меню')
seb_menu = InlineKeyboardMarkup(row_width=1)
seb_menu.row(seb_btn, btn_i_seb)

btnIN_profile = InlineKeyboardButton(text='💼 Профиль', callback_data='Профиль')
btnIN_crypto_buy = InlineKeyboardButton(text='💸 Связки', callback_data='Связки')
btnIN_support = InlineKeyboardButton(text='💬 Поддержка', callback_data='Поддержка')
btnIN_pro_version = InlineKeyboardButton(text='💰 VIP', callback_data='Pro версия')
btnIN_back_main_menu = InlineKeyboardButton(text='< Назад к меню', callback_data='Назад к меню')

btn_younger = KeyboardButton(text='Я новичок')
btn_proffesional = KeyboardButton(text='Я на опыте')
btn_the_end = KeyboardButton(text='Я закончил')

btn_p2p_arbit = InlineKeyboardButton(text='🤝💳 P2P', callback_data='p2p')
btn_between_arbit = InlineKeyboardButton(text='🔁 Межбиржевой', callback_data='between')
btn_inside_arbit = InlineKeyboardButton(text='💵 Внутрибиржевой', callback_data='inside')

kbIN_menu = InlineKeyboardMarkup(row_width=2)
kb_back_main_menu = InlineKeyboardMarkup(row_width=1)
kbIN_pro = InlineKeyboardMarkup(row_width=1)
kbIN_support = InlineKeyboardMarkup(row_width=1)
kb_pro_in = InlineKeyboardMarkup(row_width=1)
kb_professional = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_the_end = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_type_arbit = InlineKeyboardMarkup(row_width=1)

kbIN_menu.insert(btnIN_profile).insert(btnIN_crypto_buy).insert(btnIN_support).insert(btnIN_pro_version)
kb_back_main_menu.insert(btnIN_back_main_menu)
kbIN_pro.add(btnIN_pro_version).add(btnIN_back_main_menu)
kbIN_support.add(btnIN_support).add(btnIN_back_main_menu)
kb_pro_in.add(btnIN_pro_version)
kb_back_and_bundles.add(btnIN_crypto_buy).add(btnIN_back_main_menu)
kb_professional.row(btn_younger, btn_proffesional)
kb_the_end.add(btn_the_end)
kb_type_arbit.add(btn_between_arbit).add(btn_inside_arbit).add(btn_p2p_arbit).add(btnIN_back_main_menu)


# ---------------------- START ------------------------------------- #

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if not db.user_exists(message.from_user.id):
        start_command = message.text
        refer_id = str(start_command[7:])

        now = DT.datetime.now()

        now_data = now.strftime("%d-%m-%Y")

        now_3 = now + DT.timedelta(days=3)
        last_year_3 = str(now_3)[:4]
        last_month_3 = str(now_3)[5:7]
        last_day_3 = str(now_3)[8:10]

        full_last_data = last_day_3 + '-' + last_month_3 + '-' + last_year_3

        if str(refer_id) != '':
            if str(refer_id) != str(message.from_user.id):
                db.add_user(message.from_user.id, start_time=now_data, end_time=full_last_data,
                            name=message.from_user.first_name, refer_id=refer_id)
                try:
                    await bot.send_message(int(refer_id), 'По вашей ссылке зарегистрировался человек')

                    if db.get_active_status(int(refer_id)) != 1:
                        db.set_active(int(refer_id), 1)
                except:
                    db.set_active(int(refer_id), 0)

            else:
                await bot.send_message(message.from_user.id, 'Нельзя регистрироваться по собсвенной реферальной ссылке')

        else:
            db.add_user(message.from_user.id, start_time=now_data, end_time=full_last_data,
                        name=message.from_user.first_name)

        await bot.send_video(message.from_user.id, video=open('video/start.mp4', 'rb'),
                             caption='<b>Привет!</b>\n\n'
                                     'Тебя привествует команда <b>Crypto Arbit</b> и это наш бот.\n\n'
                                     'С помощью него ты можешь получать огромное количество информации'
                                     ' об арбитраже криптовалюты. \nИ да, это <b>первый телеграмм бот</b>, который'
                                     ' выдаёт информацию о <b>трёх видах</b> криптовалютного арбитража:'
                                     ' <b>Межбиржевой, Внутрибиржевой, P2P</b> и всё это за секунду.\n\n'
                                     'Выбери, кто ты.\n'
                                     '<b>Новчиок</b> или <b>Профессионал</b>\n\n'
                                     'Новичок получит <b>бесплтаный курс</b>, который поможет начать зарабатывать '
                                     'на арбитраже критовалюты.\n\n'
                                     'Опытный же получит другой подарок. Хочешь узнать какой?\n\n'
                                     'Выбирай скорее, кто ты 👇👇👇👇👇👇',
                             reply_markup=kb_professional,
                             parse_mode='html')

        user_channel_status = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)

        if user_channel_status['status'] == 'left':
            await bot.send_message(message.from_user.id, '⛔️ Вы не подписаны на наш канал.\n'
                                                         'Подпишитесь на него, чтобы получить доступ к боту.',
                                   reply_markup=seb_menu)

    else:
        await bot.send_message(message.from_user.id, 'Покупай, отправляй и обменивай\n прямо сейчас с помощью'
                                                     ' <b>CryptoArbit Bot!</b>',
                               reply_markup=kbIN_menu, parse_mode='html')

        user_channel_status = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)

        if user_channel_status['status'] == 'left':
            await bot.send_message(message.from_user.id, '⛔️ Вы не подписаны на наш канал.\n'
                                                         'Подпишитесь на него, чтобы получить доступ к боту.',
                                   reply_markup=seb_menu)


@dp.message_handler(text='Я новичок')
async def younger(message: types.Message):
    user_channel_status = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)
    if user_channel_status['status'] != 'left':
        db.set_proffessional(message.from_user.id)
        text = hlink('УРС', url='https://telegra.ph/Crypto-Arbit-kurs-06-15')
        support_link = hlink('К', f'https://jwhdkj{random.randint(1, 10000000000)}jhb.com')

        await bot.send_video(message.from_user.id, video=open('video/yong.mp4', 'rb'),
                             caption=f"Лови свой {support_link}{text},"
                                     " который поможет тебе погрузиться в мир арбитража.\n\n"
                                     "Это твоя <b>уникальная</b> возможность\n"
                                     "обучиться здесь и сейчас <b>БЕСПЛАТНО</b>\n\n"
                                     "Приступай прямо сейчас 😉\n\n\n"
                                     'P.S: Чтобы видео лучше открывались, используй компьтер или скачай приложение'
                                     ' "Googl Drive" на свой смартфон.\n'
                                     'курс не является финансовой рекомендацией',
                             reply_markup=kb_the_end, parse_mode='html')

    else:
        await bot.send_message(message.from_user.id, '⛔️ Вы не подписаны на наш канал.\n'
                                                     'Подпишитесь на него, чтобы получить доступ к боту.',
                               reply_markup=seb_menu)


@dp.message_handler(text='Я на опыте')
async def younger(message: types.Message):
    user_channel_status = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)
    if user_channel_status['status'] != 'left':
        await bot.send_video(message.from_user.id, video=open('video/old.mp4', 'rb'),
                             caption=f"Твой подарок - <b>3 ДНЯ VIP БЕСПЛАТНО</b>\n\n"
                                     f"Покупай, отправляй и обменивай\n"
                                     "прямо сейчас с помощью <b>CryptoArbit Bot!</b>",
                             reply_markup=kbIN_menu, parse_mode='html')

    else:
        await bot.send_message(message.from_user.id, '⛔️ Вы не подписаны на наш канал.\n'
                                                     'Подпишитесь на него, чтобы получить доступ к боту.',
                               reply_markup=seb_menu)


@dp.callback_query_handler(text='Назад к меню')
async def back_main_menu(message: types.Message):
    user_channel_status = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)
    if user_channel_status['status'] != 'left':
        await bot.send_message(message.from_user.id, 'Покупай, отправляй и обменивай\n'
                                                     'прямо сейчас с помощью <b>CryptoArbit Bot!</b>',
                               reply_markup=kbIN_menu,
                               parse_mode='html')
    else:
        await bot.send_message(message.from_user.id, '⛔️ Вы не подписаны на наш канал.\n'
                                                     'Подпишитесь на него, чтобы получить доступ к боту.',
                               reply_markup=seb_menu)


@dp.message_handler(text='Я закончил')
async def back_main_menu(message: types.Message):
    user_channel_status = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)
    if user_channel_status['status'] != 'left':
        db.viped_3(message.from_user.id)

        await bot.send_message(message.from_user.id, 'Покупай, отправляй и обменивай\n'
                                                     'прямо сейчас с помощью <b>CryptoArbit Bot!</b>',
                               reply_markup=kbIN_menu,
                               parse_mode='html')
    else:
        await bot.send_message(message.from_user.id, '⛔️ Вы не подписаны на наш канал.\n'
                                                     'Подпишитесь на него, чтобы получить доступ к боту.',
                               reply_markup=seb_menu)


# #------------------------ ОПЛАТА И ПРОВЕРКА НА МЕСЯЦ ---------------------------------#

@dp.callback_query_handler(text='Месяц')
async def buy_month(message: types.Message):
    user_channel_status = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)
    if user_channel_status['status'] != 'left':
        random_int1 = random.randint(1, 10)
        random_int2 = random.randint(1, 10000)
        random_int3 = random.randint(1, 10000)
        random_int4 = random.randint(1, 9924)

        bill_id = (int(message.from_user.id) * random_int1) - (random_int2 + random_int3) + (random_int2 - random_int4)
        db.add_bill_id(bill_id, message.from_user.id)

        bills = p2p.bill(bill_id=bill_id, amount=999, lifetime=15)
        btn_qiwi = InlineKeyboardButton('💳 Оплатить',
                                        web_app=WebAppInfo(url=bills.pay_url))  # в url bills.pay_url это должно быть
        qiwi_menu = InlineKeyboardMarkup(row_width=1)
        qiwi_menu.insert(btn_qiwi)

        await bot.send_message(message.from_user.id, 'Оплата услуг\nСрок: <b>месяц</b>', reply_markup=qiwi_menu,
                               parse_mode='html')
        await bot.send_message(message.from_user.id, '✅ <u>Обязательно</u> проверьте статус платежа по кнопке ниже',
                               reply_markup=kb_check_month, parse_mode='html')
    else:
        await bot.send_message(message.from_user.id, '⛔ Вы не подписаны на наш канал.\n'
                                                     'Подпишитесь на него, чтобы получить доступ к боту.',
                               reply_markup=seb_menu)


@dp.callback_query_handler(text='Проверка платежа (месяц)')
async def check_month(message: types.Message):
    user_channel_status = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)
    if user_channel_status['status'] != 'left':
        bill_id = db.get_bill_id(message.from_user.id)

        status_person = p2p.check(bill_id).status

        if status_person == 'PAID':

            db.viped_month(message.from_user.id)

            await bot.send_message(message.from_user.id,
                                   f'✅ Оплата прошла успешно!\nХорошего дня, {message.from_user.first_name}!',
                                   reply_markup=kb_back_main_menu)
        elif status_person == 'WATING':
            await bot.send_message(message.from_user.id, 'Ожидание оплаты...', reply_markup=kb_back_main_menu)

        else:
            await bot.send_message(message.from_user.id, '⛔ Оплата не прошла!\nПожайлуста, подождите 5 минут и'
                                                         ' попробуйте проверить'
                                                         ' снова', reply_markup=kb_back_main_menu)

    else:
        await bot.send_message(message.from_user.id, '⛔ Вы не подписаны на наш канал.\n'
                                                     'Подпишитесь на него, чтобы получить доступ к боту.',
                               reply_markup=seb_menu)


# ------------------------ ОПЛАТА И ПРОВЕРКА НА НЕДЕЛЮ---------------------------------#

@dp.callback_query_handler(text='Неделя')
async def buy_week(message: types.Message):
    user_channel_status = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)
    if user_channel_status['status'] != 'left':
        random_int1 = random.randint(1, 10)
        random_int2 = random.randint(1, 10000)
        random_int3 = random.randint(1, 10000)
        random_int4 = random.randint(1, 9924)

        bill_id = (int(message.from_user.id) * random_int1) - (random_int2 + random_int3) + (random_int2 - random_int4)
        db.add_bill_id(bill_id, message.from_user.id)

        bills = p2p.bill(bill_id=bill_id, amount=299, lifetime=15)
        btn_qiwi = InlineKeyboardButton('💳 Оплатить', web_app=WebAppInfo(url=bills.pay_url))
        qiwi_menu = InlineKeyboardMarkup(row_width=1)
        qiwi_menu.insert(btn_qiwi)

        await bot.send_message(message.from_user.id, 'Оплата услуг\nСрок: <b>неделя</b>', reply_markup=qiwi_menu,
                               parse_mode='html')
        await bot.send_message(message.from_user.id, '✅ <u>Обязательно</u> проверьте статус платежа по кнопке ниже',
                               reply_markup=kb_check_week, parse_mode='html')

    else:
        await bot.send_message(message.from_user.id, '⛔ Вы не подписаны на наш канал.\n'
                                                     'Подпишитесь на него, чтобы получить доступ к боту.',
                               reply_markup=seb_menu)


@dp.callback_query_handler(text='Проверка платежа (неделя)')
async def check_week(message: types.Message):
    user_channel_status = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)
    if user_channel_status['status'] != 'left':
        bill_id = db.get_bill_id(message.from_user.id)

        status_person = p2p.check(bill_id).status

        if status_person == 'PAID':
            db.viped_week(message.from_user.id)

            await bot.send_message(message.from_user.id,
                                   f'✅ Оплата прошла успешно!\nХорошего дня, {message.from_user.first_name}!',
                                   reply_markup=kb_back_main_menu)
        elif status_person == 'WATING':
            await bot.send_message(message.from_user.id, 'Ожидание оплаты...', reply_markup=kb_back_main_menu)

        else:
            await bot.send_message(message.from_user.id, '⛔ Оплата не прошла!\nПожалуйста, подождите 5 минут и '
                                                         'попробуйте проверить'
                                                         ' снова', reply_markup=kb_back_main_menu)

    else:
        await bot.send_message(message.from_user.id, '⛔ Вы не подписаны на наш канал.\n'
                                                     'Подпишитесь на него, чтобы получить доступ к боту.',
                               reply_markup=seb_menu)


# ------------------------ ОПЛАТА И ПРОВЕРКА НА ПОЛ ГОДА---------------------------------#

@dp.callback_query_handler(text='Полгода')
async def buy_midle(message: types.Message):
    user_channel_status = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)
    if user_channel_status['status'] != 'left':
        random_int1 = random.randint(1, 10)
        random_int2 = random.randint(1, 10000)
        random_int3 = random.randint(1, 10000)
        random_int4 = random.randint(1, 9924)

        bill_id = (int(message.from_user.id) * random_int1) - (random_int2 + random_int3) + (random_int2 - random_int4)
        db.add_bill_id(bill_id, message.from_user.id)

        bills = p2p.bill(bill_id=bill_id, amount=4999, lifetime=15)
        btn_qiwi = InlineKeyboardButton('💳 Оплатить', web_app=WebAppInfo(url=bills.pay_url))
        qiwi_menu = InlineKeyboardMarkup(row_width=1)
        qiwi_menu.insert(btn_qiwi)

        await bot.send_message(message.from_user.id, 'Оплата услуг\nСрок: <b>полгода</b>', reply_markup=qiwi_menu,
                               parse_mode='html')
        await bot.send_message(message.from_user.id, '✅ <u>Обязательно</u> проверьте статус платежа по кнопке ниже',
                               reply_markup=kb_check_mid_year, parse_mode='html')

    else:
        await bot.send_message(message.from_user.id, '⛔ Вы не подписаны на наш канал.\n'
                                                     'Подпишитесь на него, чтобы получить доступ к боту.',
                               reply_markup=seb_menu)


@dp.callback_query_handler(text='Проверка платежа (полгода)')
async def check_midle(message: types.Message):
    user_channel_status = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)
    if user_channel_status['status'] != 'left':
        bill_id = db.get_bill_id(message.from_user.id)

        status_person = p2p.check(bill_id).status

        if status_person == 'PAID':
            db.viped_midle_year(message.from_user.id)

            await bot.send_message(message.from_user.id,
                                   f'✅ Оплата прошла успешно!\nХорошего дня, {message.from_user.first_name}!',
                                   reply_markup=kb_back_main_menu)
        elif status_person == 'WATING':
            await bot.send_message(message.from_user.id, 'Ожидание оплаты...', reply_markup=kb_back_main_menu)

        else:
            await bot.send_message(message.from_user.id, '⛔ Оплата не прошла!\nПожайлуста, подождите 5 минут и '
                                                         'попробуйте проверить'
                                                         ' снова', reply_markup=kb_back_main_menu)

    else:
        await bot.send_message(message.from_user.id, '⛔ Вы не подписаны на наш канал.\n'
                                                     'Подпишитесь на него, чтобы получить доступ к боту.',
                               reply_markup=seb_menu)


# ------------------------ ОПЛАТА И ПРОВЕРКА НА ГОД---------------------------------#

@dp.callback_query_handler(text='Год')
async def buy_year(message: types.Message):
    user_channel_status = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)
    if user_channel_status['status'] != 'left':
        random_int1 = random.randint(1, 10)
        random_int2 = random.randint(1, 10000)
        random_int3 = random.randint(1, 10000)
        random_int4 = random.randint(1, 9924)

        bill_id = (int(message.from_user.id) * random_int1) - (random_int2 + random_int3) + (random_int2 - random_int4)
        db.add_bill_id(bill_id, message.from_user.id)

        bills = p2p.bill(bill_id=bill_id, amount=8499, lifetime=15)
        btn_qiwi = InlineKeyboardButton('💳 Оплатить', web_app=WebAppInfo(url=bills.pay_url))
        qiwi_menu = InlineKeyboardMarkup(row_width=1)
        qiwi_menu.insert(btn_qiwi)

        await bot.send_message(message.from_user.id, 'Оплата услуг\nСрок: <b>год</b>', reply_markup=qiwi_menu,
                               parse_mode='html')
        await bot.send_message(message.from_user.id, '✅ <u>Обязательно</u> проверьте статус платежа по кнопке ниже',
                               reply_markup=kb_check_year, parse_mode='html')

    else:
        await bot.send_message(message.from_user.id, '⛔ Вы не подписаны на наш канал.\n'
                                                     'Подпишитесь на него, чтобы получить доступ к боту.',
                               reply_markup=seb_menu)


@dp.callback_query_handler(text='Проверка платежа (год)')
async def check_year(message: types.Message):
    user_channel_status = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)
    if user_channel_status['status'] != 'left':
        bill_id = db.get_bill_id(message.from_user.id)

        status_person = p2p.check(bill_id).status

        if status_person == 'PAID':
            db.viped_year(message.from_user.id)

            await bot.send_message(message.from_user.id,
                                   f'✅ Оплата прошла успешно!\nХорошего дня, {message.from_user.first_name}!',
                                   reply_markup=kb_back_main_menu)
        elif status_person == 'WATING':
            await bot.send_message(message.from_user.id, 'Ожидание оплаты...', reply_markup=kb_back_main_menu)

        else:
            await bot.send_message(message.from_user.id, '⛔ Оплата не прошла!\nПожалуйста, подождите 5 минут и'
                                                         ' попробуйте проверить'
                                                         ' снова', reply_markup=kb_back_main_menu)

    else:
        await bot.send_message(message.from_user.id, '⛔ Вы не подписаны на наш канал.\n'
                                                     'Подпишитесь на него, чтобы получить доступ к боту.',
                               reply_markup=seb_menu)


def get_bundles_dict(bundles_dict):
    global bundles
    bundles = bundles_dict


@dp.callback_query_handler(text='Связки')
async def bundles(message: types.Message):
    user_channel_status = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)
    if user_channel_status['status'] != 'left':
        if db.get_vip_status(message.from_user.id) == 1:
            await bot.send_message(message.from_user.id, 'Выберите тип арбитража, на котором <b>Вы</b> '
                                                         'сейчас <b>заработаете денег</b>💵\n\n'
                                                         'P.S: Не забываем выставлять <b>лимитный ордер</b>',
                                   parse_mode='html', reply_markup=kb_type_arbit)

        else:
            await bot.send_message(message.from_user.id, 'Выберите тип арбитража, на котором <b>Вы</b>'
                                                         'сейчас <b>заработаете денег</b>💵\n\n'
                                                         'P.S: У Вас нету <b>VIP</b> подписки.\n'
                                                         'Вам доступно ограниченное количество связок',
                                   parse_mode='html', reply_markup=kb_type_arbit)

            text = hlink('VIP', url='https://telegra.ph/VIP-06-15-6')
            support_link = hlink('-', f'https://jwhdkj{random.randint(1, 10000000000)}jhb.com')
            await bot.send_message(message.from_user.id,
                                   f'{support_link}{text} версию ты можешь купить по кнопке ниже ⬇️',
                                   reply_markup=kbIN_pro, parse_mode='html')

    else:
        await bot.send_message(message.from_user.id, '⛔ Вы не подписаны на наш канал.\n'
                                                     'Подпишитесь на него, чтобы получить доступ к боту.',
                               reply_markup=seb_menu)


@dp.callback_query_handler(text='between')
async def between(message: types.Message):
    user_channel_status = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)
    if user_channel_status['status'] != 'left':
        if db.get_vip_status(message.from_user.id) == 1:
            await bot.send_message(message.from_user.id, 'Подождете, идёт загрузка связок...\n'
                                                         'Пожалуйста, не нажимайте кнопку много раз')

            for name in bundles_list_between:
                if bundles[name] != 1:
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    markup.add(types.InlineKeyboardButton(f'{name} - {bundles[name][1]}', web_app=WebAppInfo(
                        url=bundles[name][2]))).add(types.InlineKeyboardButton(f'{name} - {bundles[name][3]}',
                                                                               web_app=WebAppInfo(
                                                                                   url=bundles[name][4])))
                    print(name)
                    await bot.send_message(message.from_user.id, f'{bundles[name][0]}', reply_markup=markup,
                                           parse_mode='MarkdownV2')

            await bot.send_message(message.from_user.id, f'Нет риска - <b>лимитый ордер</b>\n'
                                                         f'Рискуешь - <b>маркет ордер</b>\n\n'
                                                         f'Связки <b>действительны</b> в течение 2-3 минут\n'
                                                         f'Не является финансовой рекомендацией',
                                   parse_mode='html', reply_markup=kb_type_arbit)

        else:
            if bundles['BTC/USDT'] != 1:
                markup = types.InlineKeyboardMarkup(row_width=1)
                markup.add(types.InlineKeyboardButton(f'BTC/USDT - {bundles["BTC/USDT"][1]}', web_app=WebAppInfo(
                    url=bundles["BTC/USDT"][2]))).add(types.InlineKeyboardButton(f'BTC/USDT - {bundles["BTC/USDT"][3]}',
                                                                                 web_app=WebAppInfo(
                                                                                     url=bundles["BTC/USDT"][4])))

                await bot.send_message(message.from_user.id, f'{bundles["BTC/USDT"][0]}', parse_mode='MarkdownV2',
                                       reply_markup=markup)

                text = hlink('VIP', url='https://telegra.ph/VIP-06-15-6')
                support_link = hlink('-', f'https://jwhdkj{random.randint(1, 10000000000)}jhb.com')
                await bot.send_message(message.from_user.id,
                                       f'{support_link}{text} версию ты можешь купить по кнопке ниже ⬇️',
                                       reply_markup=kbIN_pro, parse_mode='html')
            else:
                await bot.send_message(message.from_user.id, f'К сожалению, в данный момент <b>нет прибыльных</b> '
                                                             f'связок...\n\nПопробуйте через 5 минут',
                                       parse_mode='html')

                text = hlink('VIP', url='https://telegra.ph/VIP-06-15-6')
                support_link = hlink('-', f'https://jwhdkj{random.randint(1, 10000000000)}jhb.com')
                await bot.send_message(message.from_user.id,
                                       f'{support_link}{text} версию ты можешь купить по кнопке ниже ⬇️',
                                       reply_markup=kbIN_pro, parse_mode='html')

    else:
        await bot.send_message(message.from_user.id, '⛔ Вы не подписаны на наш канал.\n'
                                                     'Подпишитесь на него, чтобы получить доступ к боту.',
                               reply_markup=seb_menu)


@dp.callback_query_handler(text='p2p')
async def p2p_bundles(message: types.Message):
    user_channel_status = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)
    if user_channel_status['status'] != 'left':
        if db.get_vip_status(message.from_user.id) == 1:
            await bot.send_message(message.from_user.id, 'Подождете, идёт загрузка связок...\n'
                                                         'Пожалуйста, не нажимайте кнопку много раз')
            for name in bundles_list_p2p:
                if bundles[name] != 1:
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    markup.add(types.InlineKeyboardButton(f'{name} - {bundles[name][1]}', web_app=WebAppInfo(
                        url=bundles[name][2]))).add(types.InlineKeyboardButton(f'{name} - {bundles[name][3]}',
                                                                               web_app=WebAppInfo(
                                                                                   url=bundles[name][4])))

                    await bot.send_message(message.from_user.id, f'{bundles[name][0]}', reply_markup=markup,
                                           parse_mode='html')

            await bot.send_message(message.from_user.id, f'Связки <b>действительны</b> в течение 2-3 минут\n'
                                                         f'Выбирай надёжных мерчатнов\n'
                                                         f'Не является финансовой рекомендацией',
                                   parse_mode='html', reply_markup=kb_type_arbit)

        else:
            if bundles['BTC/RUBP2P'] != 1:
                markup = types.InlineKeyboardMarkup(row_width=1)
                markup.add(types.InlineKeyboardButton(f'{bundles["BTC/RUBP2P"][1]}', web_app=WebAppInfo(
                    url=bundles["BTC/RUBP2P"][2]))).add(types.InlineKeyboardButton(f'{bundles["BTC/RUBP2P"][3]}',
                                                                                   web_app=WebAppInfo(
                                                                                       url=bundles["BTC/RUBP2P"][4])))

                await bot.send_message(message.from_user.id, f'{bundles["BTC/RUBP2P"][0]}', parse_mode='html',
                                       reply_markup=markup)

                text = hlink('VIP', url='https://telegra.ph/VIP-06-15-6')
                support_link = hlink('-', f'https://jwhdkj{random.randint(1, 10000000000)}jhb.com')
                await bot.send_message(message.from_user.id,
                                       f'{support_link}{text} версию ты можешь купить по кнопке ниже ⬇️',
                                       reply_markup=kbIN_pro, parse_mode='html')
            else:
                await bot.send_message(message.from_user.id, f'К сожалению, в данный момент <b>нет прибыльных</b> '
                                                             f'связок...\n\nПопробуйте через 5 минут',
                                       parse_mode='html')

                text = hlink('VIP', url='https://telegra.ph/VIP-06-15-6')
                support_link = hlink('-', f'https://jwhdkj{random.randint(1, 10000000000)}jhb.com')
                await bot.send_message(message.from_user.id,
                                       f'{support_link}{text} версию ты можешь купить по кнопке ниже ⬇️',
                                       reply_markup=kbIN_pro, parse_mode='html')

    else:
        await bot.send_message(message.from_user.id, '⛔ Вы не подписаны на наш канал.\n'
                                                     'Подпишитесь на него, чтобы получить доступ к боту.',
                               reply_markup=seb_menu)


@dp.callback_query_handler(text='inside')
async def inside(message: types.Message):
    user_channel_status = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)
    if user_channel_status['status'] != 'left':
        if db.get_vip_status(message.from_user.id) == 1:
            await bot.send_message(message.from_user.id, 'Подождете, идёт загрузка связок...\n'
                                                         'Пожалуйста, не нажимайте кнопку много раз')

            await bot.send_message(message.from_user.id, 'В разработке...', reply_markup=kb_type_arbit)

        else:
            await bot.send_message(message.from_user.id, 'В разработке...')
            text = hlink('VIP', url='https://telegra.ph/VIP-06-15-6')
            support_link = hlink('-', f'https://jwhdkj{random.randint(1, 10000000000)}jhb.com')
            await bot.send_message(message.from_user.id,
                                   f'{support_link}{text} версию ты можешь купить по кнопке ниже ⬇️',
                                   reply_markup=kbIN_pro, parse_mode='html')

    else:
        await bot.send_message(message.from_user.id, '⛔ Вы не подписаны на наш канал.\n'
                                                     'Подпишитесь на него, чтобы получить доступ к боту.',
                               reply_markup=seb_menu)


@dp.callback_query_handler(text='free')  # Реферальная ссылка
async def buy_pro_version(message: types.Message):
    if db.count_refer(message.from_user.id) == 10:
        db.viped_month(message.from_user.id)
        await bot.send_message(message.from_user.id, 'Поздравляем, ты получил месяц VIP бесплатно',
                               reply_markup=kb_back_main_menu)

    elif db.count_refer(message.from_user.id) > 10:
        await bot.send_message(message.from_user.id, 'К сожалению, реферальная система работает только один раз',
                               reply_markup=kb_back_main_menu)

    else:
        await bot.send_message(message.from_user.id, 'Хочешь месяц подписки <b>бесплатно?</b>\n'
                                                     'Это твоя реферальная ссылка\n'
                                                     'скопируй её, пригласи 10 друзей и получи VIP даром',
                               parse_mode='html')

        await bot.send_message(message.from_user.id, f'https://t.me/CryptoArb1tBot?start={message.from_user.id}\n'
                                                     f'Количество рефералов: {db.count_refer(message.from_user.id)}/10',
                               reply_markup=kb_back_main_menu)


@dp.callback_query_handler(text='Pro версия')
async def buy_pro_version(message: types.Message):
    user_channel_status = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)
    if user_channel_status['status'] != 'left':
        btn_week = InlineKeyboardButton(text='Неделя (299 руб)', callback_data='Неделя')
        btn_month = InlineKeyboardButton(text='Месяц (999 руб) 🔥', callback_data='Месяц')
        btn_mid_year = InlineKeyboardButton(text='Полгода (4999 руб)', callback_data='Полгода')
        btn_year = InlineKeyboardButton(text='Год (8499 руб)', callback_data='Год')
        btn_free = InlineKeyboardButton(text='Месяц (Бесплатно)', callback_data='free')

        kb_buy_pro_version = InlineKeyboardMarkup(row_width=2)

        if db.count_refer(message.from_user.id) < 10:
            kb_buy_pro_version.row(btn_week, btn_month).row(btn_mid_year, btn_year).row(btn_free) \
                .row(btnIN_back_main_menu)
        else:
            kb_buy_pro_version.row(btn_week, btn_month).row(btn_mid_year, btn_year).row(btnIN_back_main_menu)

        text = hlink('VIP', url='https://telegra.ph/VIP-06-15-6')
        support_link = hlink(':', f'https://jwhdkj{random.randint(1, 10000000000)}jhb.com')

        await bot.send_message(message.from_user.id, f'<b>ПОДПИСКА</b> {support_link}{text}', parse_mode='html')
        await bot.send_message(message.from_user.id, '<b>CryptoArbit Bot</b>\n\n'
                                                     'Выберите срок длительности подписки:',
                               reply_markup=kb_buy_pro_version, parse_mode='html')

    else:
        await bot.send_message(message.from_user.id, '⛔ Вы не подписаны на наш канал.\n'
                                                     'Подпишитесь на него, чтобы получить доступ к боту.',
                               reply_markup=seb_menu)


@dp.callback_query_handler(text='Профиль')
async def profile(message: types.Message):
    id = str(message.from_user.id)
    user_channel_status = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=int(id))
    if user_channel_status['status'] != 'left':
        text = hlink('УРС', url='https://telegra.ph/Crypto-Arbit-kurs-06-15')
        support_link = hlink('К', f'https://jwhdkj{random.randint(1, 10000000000)}jhb.com')
        user = db.get_info_users(message.from_user.id)
        if user[2] == 1:
            sub = '✅'
        else:
            sub = '⛔'
        await bot.send_message(message.from_user.id,
                               f'Имя - {user[0]}\n'
                               f'ID - {id}\n'
                               f'Подписка - {sub}\n'
                               f'Начало подписки - {user[3]}\n'
                               f'Конец подписки - {user[4]}\n\n'
                               f'Твой {support_link}{text}',
                               reply_markup=kb_back_main_menu,
                               parse_mode='html')

    else:
        await bot.send_message(message.from_user.id, '⛔ Вы не подписаны на наш канал.\n'
                                                     'Подпишитесь на него, чтобы получить доступ к боту.',
                               reply_markup=seb_menu)


@dp.callback_query_handler(text='Поддержка')
async def support(message: types.Message):
    user_channel_status = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)
    if user_channel_status['status'] != 'left':
        await bot.send_message(message.from_user.id, 'Напишите свой вопрос.\nОн должен начинаться со знака "!"\n\n'
                                                     'Пример: !Не корретно работает оплата.\n\n'
                                                     'В течении дня с вами свяжется наш менеджер',
                               reply_markup=kb_back_main_menu)

    else:
        await bot.send_message(message.from_user.id, '⛔ Вы не подписаны на наш канал.\n'
                                                     'Подпишитесь на него, чтобы получить доступ к боту.',
                               reply_markup=seb_menu)


###-------------------------------- ADMIN ------------------------------------------###

btn_information = InlineKeyboardButton(text='Информация о боте', callback_data='information')
btn_send = InlineKeyboardButton(text='Рассылка', callback_data='sends')

kb_admin = InlineKeyboardMarkup(row_width=1)

kb_admin.row(btn_information, btn_send)

btn_send_text = InlineKeyboardButton(text='Текстовая рассылка', callback_data='send_text')
btn_send_photo = InlineKeyboardButton(text='Рассылка с фотографией', callback_data='send_photo')
btn_send_video = InlineKeyboardButton(text='Рассылка с видео', callback_data='send_video')

kb_sends = InlineKeyboardMarkup(row_width=3)
kb_sends.add(btn_send_text).add(btn_send_photo).add(btn_send_video)


class FSMadmin_photo(StatesGroup):
    photo = State()
    text = State()


class FSMadmin_video(StatesGroup):
    video = State()
    text = State()


@dp.message_handler(commands=['admin'])
async def admin(message: types.Message):
    if message.from_user.id in admin_id_list:
        await bot.send_message(message.from_user.id, 'Выбери то, что хочешь 👇', reply_markup=kb_admin)


# ------------------------------------------------ INFORMATION -----------------------------------#

@dp.callback_query_handler(text='information')
async def information(message: types.Message):
    if message.from_user.id in admin_id_list:
        users = db.get_users()
        count_users = 0
        count_active = 0
        for row in users:
            count_users += 1
            if row[1] == 1:
                count_active += 1

        await bot.send_message(message.from_user.id, f'Всего пользователей - {count_users}\n'
                                                     f'Из них активных - {count_active}\n'
                                                     f'И не активных - {count_users - count_active}',
                               reply_markup=kb_admin)


# ---------------------------------- SENDS ------------------------------------------------#

@dp.callback_query_handler(text='sends')
async def sends(message: types.Message):
    if message.from_user.id in admin_id_list:
        await bot.send_message(message.from_user.id, 'Выбери тип рассылки 👇', reply_markup=kb_sends)


@dp.callback_query_handler(text='send_text')
async def sends(message: types.Message):
    if message.from_user.id in admin_id_list:
        await bot.send_message(message.from_user.id, 'Пример, как запустить текстовую рассылку:\n\n'
                                                     '/sendall\n'
                                                     'Тут текст')


@dp.message_handler(commands=['sendall'])
async def send_all(message: types.Message):
    if message.from_user.id in admin_id_list:
        text = message.text[9:]
        users = db.get_users()

        for row in users:
            try:
                await bot.send_message(row[0], text, parse_mode='html')
                if int(row[1]) != 1:
                    db.set_active(row[0], 1)
            except:
                db.set_active(row[0], 0)

        await bot.send_message(message.from_user.id, 'Рассылка текста завершена', reply_markup=kb_sends)

    else:
        await bot.send_message(message.from_user.id, '⛔ Такой команды нет')


@dp.message_handler(commands=['end_photo'], state="*")
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('Заявка отменена', reply_markup=kb_sends)


@dp.callback_query_handler(text='send_photo', state='*')
async def send_photo(message: types.Message):
    if message.from_user.id in admin_id_list:
        await FSMadmin_photo.photo.set()
        await bot.send_message(message.from_user.id, 'Отправь фото')


@dp.message_handler(content_types=['photo'], state=FSMadmin_photo.photo)
async def load_photo(message: types.Message, state: FSMContext):
    await state.update_data(photo=message.photo[0].file_id)
    await FSMadmin_photo.next()
    await message.reply('Если хочешь отменить заявку нажми на \n/end_photo\n'
                        'Теперь введи текст:')


@dp.message_handler(state=FSMadmin_photo.text)
async def load_text(message: types.Message, state: FSMContext):
    await state.update_data(text=message.text)
    data = await state.get_data()
    await message.reply('Начинаю рассылку....')
    users = db.get_users()

    for row in users:
        try:
            await bot.send_photo(row[0], data['photo'], caption=data['text'], parse_mode='html')
            if int(row[1]) != 1:
                db.set_active(row[0], 1)
        except:
            db.set_active(row[0], 0)

    await bot.send_message(message.from_user.id, 'Рассылка текста и фото завершена', reply_markup=kb_admin)
    await state.finish()


@dp.message_handler(commands=['end_video'], state="*")
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('Заявка отменена', reply_markup=kb_sends)


@dp.callback_query_handler(text='send_video', state='*')
async def send_video(message: types.Message):
    if message.from_user.id in admin_id_list:
        await FSMadmin_video.video.set()
        await bot.send_message(message.from_user.id, 'Отправь видео')


@dp.message_handler(content_types=['video'], state=FSMadmin_video.video)
async def load_photo(message: types.Message, state: FSMContext):
    await state.update_data(video=message.video.file_id)
    await FSMadmin_video.next()
    await message.reply('Если хочешь отменить заявку нажми на \n/end_video\n'
                        'Теперь введи текст:')


@dp.message_handler(state=FSMadmin_video.text)
async def load_text(message: types.Message, state: FSMContext):
    await state.update_data(text=message.text)
    data = await state.get_data()
    await message.reply('Начинаю рассылку...')
    users = db.get_users()

    for row in users:
        try:
            await bot.send_video(row[0], data['video'], caption=data['text'], parse_mode='html')
            if int(row[1]) != 1:
                db.set_active(row[0], 1)
        except:
            db.set_active(row[0], 0)

    await bot.send_message(message.from_user.id, 'Рассылка текста и видео завершена', reply_markup=kb_admin)
    await state.finish()


# @dp.message_handler(commands=['id'])
# async def get_id(message: types.Message):
#     if message.from_user.id in admin_id_list:
#         global id_for_support
#         id_for_support = message.get_args()
#         await bot.send_message(message.from_user.id, f'Id {id_for_support} принято')
#
# @dp.message_handler(commands=['support'])
# async def support(message: types.Message):
#     if message.from_user.id in admin_id_list:
#         text = message.get_args()
#
#     try:
#         await bot.send_message(int(id_for_support), f'#Support\n'
#                                                     f'Это сообщение отправлено командой <b>ArbitBot</b>\n\n'
#                                                     f'{text}\n\n'
#                                                     f'Если проблема не решилась, повторно обратитесь в поддержку\n\n'
#                                                     f'Хорошего дня!', parse_mode='html', reply_markup=kbIN_support)
#
#         await bot.send_message(message.from_user.id, f'Сообщение пользователю {id_for_support} отправлено')
#
#     except:
#         await bot.send_message(message.from_user.id, f'Пользователь с {id_for_support} заблокировал бота')
# #
#
@dp.message_handler()
async def support_nonamecommands(message: types.Message):
    if message.text.startswith('!'):
        await bot.send_message('@arbitbotsupport',
                               f'#Support\n'
                               f'Name - {message.from_user.first_name}\n'
                               f'Username - {message.from_user.username}\n'
                               f'ID - {message.from_user.id}\n'
                               f'Problem - {message.text}\n'
                               f'Time - {datetime.datetime.now()}')
        await bot.send_message(message.from_user.id, 'Сообщение отправлено!\nСпасибо за отзыв',
                               reply_markup=kb_back_main_menu)

    else:
        await bot.send_message(message.from_user.id, '⛔ Такой команды нет')


# -------------------------------------- WEBSOCKET ----------------------------------------------------------------------#
def websocket_stream(symbol, price_dict):
    while True:
        def is_number(word):
            try:
                float(word)
                return True
            except ValueError:
                return False

        def message_handler(_, message):
            text = message[message.find('"b"') + 5:message.find('"B"') - 3]
            if is_number(text):
                price_dict[symbol] = text

        my_client = SpotWebsocketStreamClient(on_message=message_handler)

        my_client.book_ticker(symbol=f"{symbol}")

        time.sleep(9000)

        my_client.stop()


def start_websocket(price_dict):
    for name in symbols:
        myThread = MyThread(function=websocket_stream, name=name, price_dict=price_dict)


if __name__ == '__main__':
    bundles_dict = {}
    # price_dict = {}

    t1 = Thread(target=task_1, args=(bundles_dict,))
    t2 = Thread(target=task_2, args=(bundles_dict,))
    t3 = Thread(target=task_3, args=(bundles_dict,))
    t4 = Thread(target=start_websocket, args=(price_dict,))

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    get_bundles_dict(bundles_dict)

    executor.start_polling(dp, skip_updates=False, on_startup=on_startup, timeout=10000000)
