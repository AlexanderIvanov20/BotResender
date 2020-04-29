import telebot
from telebot.types import *


bot = telebot.TeleBot(token='1077949754:AAGTCrVh6NpXWIM-R7Rez4SHcCx5mM6aXck')


def get_creds(message: Message):
    user_id = message.chat.id
    name = f'{message.chat.first_name} {message.chat.last_name}'
    username = message.chat.username
    return user_id, name, username


@bot.message_handler(content_types=['photo', 'document'])
def get_message_with_photo(message: Message):
    file_id = message.photo[1].file_id
    file = bot.get_file(file_id)
    downloaded_file = bot.download_file(file.file_path)

    user_id, name, username = get_creds(message)

    with open(f'{file_id}.png', 'wb') as new_file:
        new_file.write(downloaded_file)

    if message.caption is not None:
        caption = message.caption
        print(caption)


@bot.message_handler(content_types=['text'])
def get_mesage(message: Message):
    text = message.text

    user_id, name, username = get_creds(message)
    print(text)


bot.polling(none_stop=True)
