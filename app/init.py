import telebot
import logging
import time
import pathlib

ROOT_PATH = str(pathlib.Path(__file__).parent.parent.absolute())
CHAT_ID_PATH = ROOT_PATH + '/users_data/chat_id.txt'
SCHEDULE_PATH = ROOT_PATH + '/config/message_schedule.yml'
TELEGRAM_TOKEN_PATH = ROOT_PATH + '/config/telegram_bot_api.key'
TENOR_API_KEY_PATH = ROOT_PATH + '/config/tenor_gif_api.key'

logging.basicConfig(filename='app.log', format='%(asctime)s %(levelname)-8s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
try:
    with open(TELEGRAM_TOKEN_PATH, 'r') as file:
        telegram_api_token = file.readline()
except Exception as e:
    logging.error(e)
    telegram_api_token = None

if telegram_api_token is not None:
    bot = telebot.TeleBot(telegram_api_token)
