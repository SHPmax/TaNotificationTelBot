from init import *


@bot.message_handler(commands=['start'])
def start_message(message):
    try:
        chat_id_storage_file = open(CHAT_ID_PATH, 'w')
        chat_id_storage_file.write(str(message.chat.id))
        chat_id_storage_file.close()
        bot.send_message(message.chat.id, 'OK')
    except Exception as e:
        logging.error(e)
        bot.send_message(message.chat.id, "Все пошло по пизде")


if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)
