import telebot
import logging
import time
import pathlib
import os

ROOT_PATH = str(pathlib.Path(__file__).parent.parent.absolute())
CHAT_ID_PATH = ROOT_PATH + '/users_data/chat_id.txt'
SCHEDULE_PATH = ROOT_PATH + '/config/message_schedule.yml'

logging.basicConfig(filename='app.log', format='%(asctime)s %(levelname)-8s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
# export TELEGRAM_API_TOKEN
bot = telebot.TeleBot(os.environ.get('TELEGRAM_API_TOKEN'))
