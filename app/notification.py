from init import *
import yaml
import sys
import tenor


def parse_yml():
    with open(SCHEDULE_PATH, 'r') as yml_file:
        try:
            notifications = yaml.safe_load(yml_file)['notifications']
        except Exception as e:
            logging.error(e)
            return []
    return notifications


def run_notification(msg_id):
    notifications = parse_yml()
    msg = notifications[msg_id]
    try:
        chat_id_storage_file = open(CHAT_ID_PATH, 'r')
        chat_id = int(chat_id_storage_file.read())
        chat_id_storage_file.close()
    except Exception as e:
        logging.error(e)
        return False
    gif_url = tenor.get_random_gif_url()
    if gif_url is not None:
        bot.send_video(chat_id, gif_url)
    markup = telebot.types.InlineKeyboardMarkup()
    url_btn = telebot.types.InlineKeyboardButton(text='Тыкай', url=msg['url'])
    markup.add(url_btn)
    bot.send_message(chat_id, msg['text'], reply_markup=markup)
    return True


msg_index = sys.argv[1]
run_notification(int(msg_index))
